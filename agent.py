import os
import requests
import datetime
import tweepy

# API keys from environment - GitHub Actions will provide these
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GEMINI_KEY = os.getenv("GEMINI_KEY")
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")


# 1️⃣ Fetch news
def fetch_news():
    if not NEWSAPI_KEY:
        raise ValueError("NEWSAPI_KEY not found in environment variables")
    
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWSAPI_KEY}"
    try:
        print(f"Making request to: {url}")
        resp = requests.get(url)
        print(f"Response status code: {resp.status_code}")
        
        resp.raise_for_status()  # Raises an HTTPError for bad responses
        data = resp.json()
        
        print(f"API Response: {data}")  # Debug: Print full response
        
        if data.get("status") != "ok":
            raise ValueError(f"NewsAPI error: {data.get('message', 'Unknown error')}")
        
        articles = data.get("articles", [])
        print(f"Number of articles found: {len(articles)}")
        
        if not articles:
            # Try alternative endpoints if no articles found
            print("No articles found with country=in, trying general top headlines...")
            return fetch_news_alternative()
        
        headlines = [a["title"] for a in articles[:5] if a.get("title")]
        return "\n".join(headlines)
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching news: {e}")

def fetch_news_alternative():
    """Alternative news fetching methods if the first one fails"""
    alternatives = [
        f"https://newsapi.org/v2/top-headlines?apiKey={NEWSAPI_KEY}",  # Global headlines
        f"https://newsapi.org/v2/everything?q=technology&sortBy=publishedAt&apiKey={NEWSAPI_KEY}",  # Tech news
        f"https://newsapi.org/v2/everything?q=business&sortBy=publishedAt&apiKey={NEWSAPI_KEY}",  # Business news
    ]
    
    for i, url in enumerate(alternatives):
        try:
            print(f"Trying alternative {i+1}: {url}")
            resp = requests.get(url)
            resp.raise_for_status()
            data = resp.json()
            
            if data.get("status") == "ok" and data.get("articles"):
                articles = data.get("articles", [])[:5]
                headlines = [a["title"] for a in articles if a.get("title")]
                if headlines:
                    return "\n".join(headlines)
        except Exception as e:
            print(f"Alternative {i+1} failed: {e}")
            continue
    
    return "No news articles found from any source"


# 2️⃣ Summarize with Gemini
def summarize_with_gemini(text):
    if not GEMINI_KEY:
        raise ValueError("GEMINI_KEY not found in environment variables")
    
    if not text.strip():
        return "No content to summarize"
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={GEMINI_KEY}"
    payload = {
        "contents": [{"parts":[{"text": f"Create a concise Twitter post (under 250 characters) summarizing these news headlines. Include relevant hashtags and stock symbols where appropriate:\n{text}"}]}]
    }
    
    try:
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        
        # Debug: Print the response to see what we're getting
        print("Gemini API response:", data)
        
        # Check if the response has the expected structure
        if "candidates" not in data:
            if "error" in data:
                raise ValueError(f"Gemini API error: {data['error'].get('message', 'Unknown error')}")
            else:
                raise ValueError(f"Unexpected Gemini API response structure: {data}")
        
        if not data["candidates"]:
            raise ValueError("No candidates returned by Gemini API")
        
        candidate = data["candidates"][0]
        if "content" not in candidate:
            raise ValueError("No content in Gemini API response")
        
        parts = candidate["content"].get("parts", [])
        if not parts:
            raise ValueError("No parts in Gemini API response")
        
        return parts[0]["text"]
        
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error calling Gemini API: {e}")


# 3️⃣ Post to Twitter/X
def post_to_twitter(text):
    if not all([X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET]):
        raise ValueError("Twitter API credentials not found in environment variables")
    
    try:
        client = tweepy.Client(
            consumer_key=X_API_KEY,
            consumer_secret=X_API_SECRET,
            access_token=X_ACCESS_TOKEN,
            access_token_secret=X_ACCESS_SECRET
        )
        resp = client.create_tweet(text=text)
        return resp
    except Exception as e:
        raise ValueError(f"Error posting to Twitter: {e}")


# 4️⃣ Main flow
if __name__ == "__main__":
    try:
        print("🤖 Daily News Bot Starting...")
        print(f"⏰ Current time: {datetime.datetime.now()}")
        
        print("📰 Fetching news...")
        news_text = fetch_news()
        print("Fetched news:\n", news_text)

        if news_text and news_text != "No news articles found" and news_text != "No news articles found from any source":
            print("\n🤖 Generating summary...")
            summary_text = summarize_with_gemini(news_text)
            print("\nGenerated summary:\n", summary_text)
            
            # Truncate if still too long
            if len(summary_text) > 280:
                print(f"⚠️  Summary too long ({len(summary_text)} chars), truncating...")
                # Find a good breaking point (end of sentence or word)
                truncated = summary_text[:270]
                last_period = truncated.rfind('.')
                last_space = truncated.rfind(' ')
                
                if last_period > 200:  # If there's a sentence ending point
                    summary_text = truncated[:last_period + 1]
                elif last_space > 200:  # If there's a word boundary
                    summary_text = truncated[:last_space] + "..."
                else:  # Just cut it off
                    summary_text = truncated + "..."
                
                print(f"Truncated to: {len(summary_text)} characters")
                print(f"New summary: {summary_text}")

            print("\n🐦 Posting to Twitter...")
            response = post_to_twitter(summary_text)
            print(f"\n✅ Posted successfully! Tweet ID: {response.data['id']}")
            print(f"🎉 Daily news bot completed at {datetime.datetime.now()}")
            
        else:
            print("❌ No news content to process")

    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"💥 Bot failed at {datetime.datetime.now()}")