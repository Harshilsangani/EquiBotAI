import os
import requests
import datetime
import tweepy

# API keys from environment
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GEMINI_KEY = os.getenv("GEMINI_KEY")
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")


# 1️⃣ Fetch Indian stock market news with variety
def fetch_indian_stock_news():
    """Fetch Indian stock market and business news with time-based variety"""
    if not NEWSAPI_KEY:
        raise ValueError("NEWSAPI_KEY not found in environment variables")
    
    current_hour = datetime.datetime.now().hour
    
    # Vary search queries based on time of day for diverse content
    if 6 <= current_hour < 10:
        # Morning: Focus on opening, overnight news, Asian markets
        primary_queries = [
            "indian+stock+market+opening+OR+market+opens+OR+pre-market",
            "Sensex+Nifty+opening+OR+morning+trade",
            "BSE+NSE+early+trade+OR+market+sentiment"
        ]
    elif 10 <= current_hour < 14:
        # Mid-day: Focus on trading activity, sector movements
        primary_queries = [
            "indian+stocks+mid-day+OR+intraday+trading",
            "sectoral+indices+OR+banking+stocks+OR+IT+stocks",
            "Sensex+Nifty+trading+OR+stock+movers"
        ]
    elif 14 <= current_hour < 18:
        # Afternoon: Focus on trends, investor activity
        primary_queries = [
            "FII+DII+activity+OR+institutional+investors+india",
            "stock+recommendations+OR+analyst+ratings+india",
            "market+outlook+OR+trading+strategy+india"
        ]
    elif 18 <= current_hour < 22:
        # Evening: Focus on closing, summaries, results
        primary_queries = [
            "sensex+closes+OR+nifty+ends+OR+market+close",
            "top+gainers+losers+OR+stock+performance+india",
            "earnings+results+OR+quarterly+results+india"
        ]
    else:
        # Night: Focus on analysis, global impact, next day prep
        primary_queries = [
            "global+markets+impact+india+OR+us+markets+asian",
            "stock+market+analysis+india+OR+technical+analysis",
            "market+preview+OR+tomorrow+outlook+india"
        ]
    
    # Multiple strategies for Indian stock market news
    news_sources = []
    
    # Add time-specific queries
    for query in primary_queries:
        news_sources.append({
            "url": f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&from={datetime.date.today()}&apiKey={NEWSAPI_KEY}",
            "description": f"Time-specific: {query.replace('+', ' ')}"
        })
    
    # Add general fallbacks
    news_sources.extend([
        {
            "url": f"https://newsapi.org/v2/everything?q=BSE+OR+NSE+OR+sensex+OR+nifty&language=en&sortBy=publishedAt&from={datetime.date.today()}&apiKey={NEWSAPI_KEY}",
            "description": "General Indian indices"
        },
        {
            "url": f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={NEWSAPI_KEY}",
            "description": "Indian business headlines"
        },
        {
            "url": f"https://newsapi.org/v2/everything?q=indian+companies+stock+OR+share+price&language=en&sortBy=publishedAt&apiKey={NEWSAPI_KEY}",
            "description": "Indian company stocks"
        }
    ])
    
    for i, source in enumerate(news_sources):
        try:
            print(f"Trying source {i+1}: {source['description']}")
            print(f"URL: {source['url']}")
            
            resp = requests.get(source['url'])
            resp.raise_for_status()
            data = resp.json()
            
            print(f"Response status: {data.get('status')}")
            print(f"Total results: {data.get('totalResults', 0)}")
            
            if data.get("status") == "ok" and data.get("articles"):
                articles = data.get("articles", [])[:5]  # Get top 5
                
                # Filter for stock market relevance
                relevant_articles = []
                stock_keywords = ['stock', 'share', 'market', 'BSE', 'NSE', 'sensex', 'nifty', 'equity', 'trading', 'investor', 'rupee', 'economy']
                
                for article in articles:
                    title = article.get("title", "").lower()
                    description = article.get("description", "").lower()
                    
                    # Check if article is stock market related
                    if any(keyword in title or keyword in description for keyword in stock_keywords):
                        relevant_articles.append({
                            "title": article.get("title"),
                            "description": article.get("description"),
                            "url": article.get("url"),
                            "source": article.get("source", {}).get("name"),
                            "publishedAt": article.get("publishedAt")
                        })
                
                if relevant_articles:
                    print(f"Found {len(relevant_articles)} relevant articles")
                    return relevant_articles
                else:
                    print("No relevant stock market articles found")
                    
        except Exception as e:
            print(f"Source {i+1} failed: {e}")
            continue
    
    return []


# 2️⃣ Enhanced summarize with better formatting for Indian stock market
def summarize_indian_stock_news(articles):
    """Create formatted summary of Indian stock market news"""
    if not GEMINI_KEY:
        raise ValueError("GEMINI_KEY not found in environment variables")
    
    if not articles:
        return "No stock market news to summarize"
    
    # Prepare article text with sources
    articles_text = "\n\n".join([
        f"HEADLINE: {article['title']}\n"
        f"DESCRIPTION: {article['description'] or 'No description'}\n"
        f"SOURCE: {article['source']}\n"
        f"URL: {article['url']}"
        for article in articles[:3]  # Limit to top 3 articles
    ])
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={GEMINI_KEY}"
    
    # Get current hour to determine posting style
    current_hour = datetime.datetime.now().hour
    
    # Different tones for different times of day
    if 6 <= current_hour < 10:
        time_context = "Morning Market Opening"
        tone = "energetic and optimistic"
        emojis = "☀️📈💹"
    elif 10 <= current_hour < 14:
        time_context = "Mid-Day Market Update"
        tone = "informative and analytical"
        emojis = "📊💼🔍"
    elif 14 <= current_hour < 18:
        time_context = "Afternoon Trading Session"
        tone = "balanced and insightful"
        emojis = "⏰📉📈"
    elif 18 <= current_hour < 22:
        time_context = "Market Closing Update"
        tone = "reflective and summary-focused"
        emojis = "🌙📊✅"
    else:
        time_context = "Late Night Market Insights"
        tone = "calm and forward-looking"
        emojis = "🌃💭📰"
    
    # Enhanced prompt with time-aware context
    prompt = f"""
Create an engaging Twitter post about Indian stock market news for {time_context}. 

CRITICAL REQUIREMENTS:
1. Focus ONLY on INDIAN companies, BSE, NSE, Sensex, Nifty, Indian economy
2. Use {tone} tone appropriate for this time of day
3. Include relevant emojis: {emojis} and others
4. Add Indian stock symbols with $ prefix (e.g., $RELIANCE $TCS $INFY $HDFC $TATAMOTORS)
5. Use 2-3 bullet points (•) with proper spacing
6. Keep TOTAL length under 260 characters (very important!)
7. Add 3-4 relevant hashtags from: #IndianStockMarket #BSE #NSE #Sensex #Nifty #StockMarket #India #Trading #Investment
8. Make it HIGHLY engaging - use power words and create urgency
9. Include brief market sentiment (bullish/bearish/neutral)
10. DO NOT include URLs in the summary (I'll add them separately)

News articles to summarize:
{articles_text}

Format examples:

For Morning:
{emojis} Indian Markets Open Strong!

• Sensex jumps 300pts on global cues
• IT stocks lead rally
• FII buying boosts sentiment

$RELIANCE $TCS #Sensex #NSE #IndianStockMarket

For Afternoon:
{emojis} Mid-Day Market Check

• Banking stocks under pressure
• Nifty holds 18,500 support
• Mixed signals from sectors

$HDFCBANK $ICICIBANK #BSE #StockMarket #India

For Evening:
{emojis} Market Wrap-Up

• Sensex closes 150pts higher
• Auto & pharma outperform
• Positive breadth across board

$TATAMOTORS $SUNPHARMA #Sensex #IndianStockMarket

Create a unique, engaging post that stands out and encourages engagement!
"""
    
    payload = {
        "contents": [{"parts":[{"text": prompt}]}]
    }
    
    try:
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        
        print("Gemini API response:", data)
        
        if "candidates" not in data:
            if "error" in data:
                raise ValueError(f"Gemini API error: {data['error'].get('message', 'Unknown error')}")
            else:
                raise ValueError(f"Unexpected Gemini API response: {data}")
        
        if not data["candidates"]:
            raise ValueError("No candidates returned by Gemini API")
        
        candidate = data["candidates"][0]
        if "content" not in candidate:
            raise ValueError("No content in Gemini API response")
        
        parts = candidate["content"].get("parts", [])
        if not parts:
            raise ValueError("No parts in Gemini API response")
        
        summary = parts[0]["text"]
        
        # Add the most relevant news URL to the summary
        if articles and not any(url in summary for article in articles for url in [article['url']]):
            # Add the first article URL if no URL is present
            most_relevant_url = articles[0]['url']
            # Shorten the summary slightly to make room for URL
            if len(summary) > 230:
                summary = summary[:230] + "..."
            summary += f"\n\n🔗 {most_relevant_url}"
        
        return summary
        
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error calling Gemini API: {e}")


# 3️⃣ Post to Twitter/X (same as before)
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
        print("🇮🇳 Indian Stock Market News Bot Starting...")
        print(f"⏰ Current time: {datetime.datetime.now()}")
        
        print("📈 Fetching Indian stock market news...")
        articles = fetch_indian_stock_news()
        
        if articles:
            print(f"✅ Found {len(articles)} relevant articles:")
            for i, article in enumerate(articles[:3], 1):
                print(f"{i}. {article['title'][:60]}...")
                print(f"   Source: {article['source']}")
                print(f"   URL: {article['url']}")
                print()
            
            print("🤖 Generating Indian stock market summary...")
            summary_text = summarize_indian_stock_news(articles)
            print("\nGenerated summary:\n", summary_text)
            print(f"📏 Character count: {len(summary_text)}")
            
            # Truncate if still too long
            if len(summary_text) > 280:
                print(f"⚠️  Summary too long ({len(summary_text)} chars), truncating...")
                # Find a good breaking point
                truncated = summary_text[:270]
                last_newline = truncated.rfind('\n')
                last_space = truncated.rfind(' ')
                
                if last_newline > 200:  # Prefer line breaks
                    summary_text = truncated[:last_newline]
                elif last_space > 200:  # Then word boundaries
                    summary_text = truncated[:last_space] + "..."
                else:  # Last resort
                    summary_text = truncated + "..."
                
                print(f"✂️ Truncated to: {len(summary_text)} characters")
            
            print("\n🐦 Posting to Twitter...")
            response = post_to_twitter(summary_text)
            print(f"\n✅ Posted successfully! Tweet ID: {response.data['id']}")
            print(f"🎉 Indian stock market bot completed at {datetime.datetime.now()}")
            
        else:
            print("❌ No relevant Indian stock market news found")
            print("📰 Trying to post general business update...")
            
            # Fallback message
            fallback_message = f"""🇮🇳 Indian Stock Market Bot 📈

Market monitoring active! 
Check back for latest updates.

#{datetime.date.today().strftime('%d%b%Y')} #IndianStockMarket #BSE #NSE #StockMarket #India

Stay tuned for market insights! 💹"""
            
            response = post_to_twitter(fallback_message)
            print(f"✅ Fallback message posted! Tweet ID: {response.data['id']}")

    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"💥 Bot failed at {datetime.datetime.now()}")
        
        # Try to post an error status (optional)
        try:
            error_message = f"""🤖 Indian Stock Market Bot Status

Temporary service interruption. 
Will resume shortly with market updates.

#{datetime.date.today().strftime('%d%b%Y')} #IndianStockMarket #TechUpdate"""
            
            post_to_twitter(error_message)
            print("📤 Error status posted to Twitter")
        except:
            print("❌ Could not post error status")
