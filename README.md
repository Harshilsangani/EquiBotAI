# 🇮🇳 Indian Stock Market News Bot

An intelligent Twitter bot that automatically posts Indian stock market updates 4 times daily using AI-powered news summarization.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 📊 Features

- 🤖 **Automated Posting** - Posts 4 times daily at optimal times
- 🇮🇳 **Indian Market Focus** - BSE, NSE, Sensex, Nifty updates
- 🧠 **AI-Powered** - Uses Google Gemini for intelligent summaries
- ⏰ **Time-Aware** - Different content and tone based on time of day
- 📈 **Real-Time News** - Fetches latest stock market news via NewsAPI
- 🎯 **High Engagement** - Optimized formatting with emojis, hashtags, and stock symbols
- 🔗 **Media Links** - Includes relevant news source URLs
- 🛡️ **Error Handling** - Robust fallback mechanisms

## 📅 Posting Schedule

| Time (IST) | Focus Area | Tone |
|------------|------------|------|
| 8:00 AM | Market Opening | Energetic & Optimistic ☀️ |
| 12:00 PM | Mid-Day Update | Informative & Analytical 📊 |
| 4:00 PM | Afternoon Session | Balanced & Insightful ⏰ |
| 8:00 PM | Market Closing | Reflective & Summary 🌙 |

## 🚀 Quick Start

### Prerequisites

- GitHub account
- Twitter Developer account with API access
- NewsAPI key (free tier available)
- Google Gemini API key (free tier available)

### 1. Get API Keys

#### Twitter/X API Keys
1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new app or select existing one
3. Set **App permissions** to "Read and Write"
4. Set **Type of App** to "Web App, Automated App or Bot"
5. Fill in required URLs (can use placeholders):
   - Callback URI: `https://example.com/callback`
   - Website URL: `https://example.com`
   - Terms of service: `https://example.com/terms`
   - Privacy policy: `https://example.com/privacy`
6. Save settings
7. Go to "Keys and tokens" tab
8. **Regenerate** Access Token and Secret (important!)
9. Save these keys:
   - API Key (Consumer Key)
   - API Secret (Consumer Secret)
   - Access Token
   - Access Token Secret

#### NewsAPI Key
1. Go to [NewsAPI.org](https://newsapi.org/)
2. Sign up for free account
3. Get your API key from dashboard
4. Free tier: 100 requests/day (sufficient for this bot)

#### Google Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with Google account
3. Click "Create API Key"
4. Copy your API key
5. Free tier: 60 requests/minute

### 2. Setup GitHub Repository

1. **Create New Repository**
   ```
   Go to GitHub → New Repository
   Name: indian-stock-market-bot
   Visibility: Public or Private
   Initialize with README: No
   ```

2. **Clone Repository** (or upload files via web interface)
   ```bash
   git clone https://github.com/YOUR_USERNAME/indian-stock-market-bot.git
   cd indian-stock-market-bot
   ```

3. **Create Required Files**

   Create these 3 files in your repository:

   **File 1: `agent.py`**
   - Copy the complete Python code from the artifact
   
   **File 2: `requirements.txt`**
   ```txt
   requests
   tweepy
   ```

   **File 3: `.github/workflows/daily-news.yml`**
   - Copy the workflow YAML from the artifact
   - Create the folder structure: `.github/workflows/`

4. **Upload to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit: Indian stock market bot"
   git push origin main
   ```

### 3. Configure GitHub Secrets

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these 6 secrets one by one:

| Secret Name | Description | Example Value |
|-------------|-------------|---------------|
| `NEWSAPI_KEY` | Your NewsAPI key | `abc123def456...` |
| `GEMINI_KEY` | Your Google Gemini API key | `AIzaSy...` |
| `X_API_KEY` | Twitter API Key (Consumer Key) | `KjMnHO...` |
| `X_API_SECRET` | Twitter API Secret | `lzfSgP...` |
| `X_ACCESS_TOKEN` | Twitter Access Token | `197218...` |
| `X_ACCESS_SECRET` | Twitter Access Token Secret | `9rtcG6...` |

⚠️ **Important**: Never commit API keys to your code or README!

### 4. Test the Bot

1. Go to **Actions** tab in your GitHub repository
2. Click on **Daily News Bot** workflow
3. Click **Run workflow** → **Run workflow** (green button)
4. Watch the execution in real-time
5. Check your Twitter account for the posted tweet!

### 5. Enable Automated Posting

Once tested successfully:
- The bot will automatically run at scheduled times (8 AM, 12 PM, 4 PM, 8 PM IST)
- GitHub Actions will execute the workflow
- No further action needed!

## 📖 How It Works

```
┌─────────────────┐
│  GitHub Actions │  (Triggers every 4 hours)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Fetch News     │  (NewsAPI - Indian stock market)
│  • Time-based   │
│  • Relevant     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI Summary     │  (Google Gemini)
│  • Format       │
│  • Optimize     │
│  • Add context  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Post to X      │  (Twitter API)
│  • With links   │
│  • With hashtags│
└─────────────────┘
```

## 🎨 Sample Output

### Morning Post (8 AM)
```
☀️📈💹 Indian Markets Open Strong!

• Sensex jumps 300pts on global cues
• IT stocks lead morning rally
• FII buying boosts sentiment

$RELIANCE $TCS $INFY #Sensex #NSE #IndianStockMarket

🔗 https://economictimes.com/...
```

### Evening Post (8 PM)
```
🌙📊✅ Market Wrap-Up

• Sensex closes 150pts higher
• Pharma leads gainers list
• Positive breadth: 2:1 ratio

$SUNPHARMA $DRREDDY #Sensex #NSE #StockMarket

🔗 https://moneycontrol.com/...
```

## 📈 Growth & Engagement Tips

### Content Optimization
- ✅ Focus on trending Indian stocks ($RELIANCE, $TCS, $INFY, $HDFC)
- ✅ Use power words: "surges", "plunges", "breakout", "rally"
- ✅ Add urgency: "breaking", "just in", "alert"
- ✅ Include numbers: specific points, percentages
- ✅ Mix positive and realistic sentiment

### Hashtag Strategy
**Primary (always use):**
- `#IndianStockMarket`
- `#BSE` or `#NSE`
- `#Sensex` or `#Nifty`

**Secondary (rotate):**
- `#StockMarket` `#India` `#Trading` `#Investment`
- `#Stocks` `#Finance` `#Markets` `#Economy`
- `#DalalStreet` `#MumbaiMarket`

**Trending (when relevant):**
- `#Budget2024` `#MonetaryPolicy` `#RBI`
- `#Earnings` `#Q1Results` `#IPO`

### Best Practices
1. **Consistency** - Post at exact times daily
2. **Quality** - Ensure accurate, relevant information
3. **Engagement** - Reply to comments and questions
4. **Variety** - Mix market updates with insights
5. **Visuals** - Consider adding charts/graphs (manual)
6. **Timing** - Post when market is active (9:15 AM - 3:30 PM IST)

### Growing Your Audience
- 🔄 Retweet relevant market news from major sources
- 💬 Engage with finance influencers
- 📊 Share weekend market analysis (manual)
- 🎯 Use trending finance hashtags
- 🤝 Follow back engaged users
- 📱 Cross-promote on other platforms
- 🏆 Join finance Twitter communities

## 🔧 Customization

### Change Posting Times
Edit `.github/workflows/daily-news.yml`:
```yaml
schedule:
  - cron: '30 2 * * *'   # 8:00 AM IST
  - cron: '30 6 * * *'   # 12:00 PM IST
  - cron: '30 10 * * *'  # 4:00 PM IST
  - cron: '30 14 * * *'  # 8:00 PM IST
```

**Cron Time Converter:**
- IST = UTC + 5:30
- Use [Crontab.guru](https://crontab.guru/) for calculations

### Customize Content Focus
Edit `agent.py` - modify search queries:
```python
primary_queries = [
    "your+custom+query",
    "another+topic",
]
```

### Adjust Post Length
Edit `agent.py` - find this line:
```python
if len(summary_text) > 280:  # Change this number
```

### Change Tone/Style
Edit the prompt in `summarize_indian_stock_news()` function:
```python
tone = "your desired tone"
emojis = "your preferred emojis"
```

## 🐛 Troubleshooting

### Common Issues

**1. Bot not posting**
- ✅ Check GitHub Actions logs (Actions tab)
- ✅ Verify all 6 secrets are added correctly
- ✅ Ensure Twitter app has "Read and Write" permissions
- ✅ Confirm access tokens were regenerated after permission change

**2. "No news found" errors**
- ✅ NewsAPI free tier has daily limits (100 requests)
- ✅ Check if NewsAPI key is valid
- ✅ Try different search queries
- ✅ Verify internet connectivity in GitHub Actions

**3. "Gemini API error"**
- ✅ Check Gemini API key is correct
- ✅ Verify you haven't exceeded rate limits (60/min)
- ✅ Ensure API is enabled in Google Cloud Console

**4. "Twitter 403 Forbidden"**
- ✅ App permissions must be "Read and Write"
- ✅ Regenerate tokens AFTER changing permissions
- ✅ Update secrets with new tokens
- ✅ Wait 5-10 minutes for Twitter to update permissions

**5. Posts are too long**
- ✅ Reduce character limit in prompt
- ✅ Check truncation logic is working
- ✅ Simplify Gemini instructions

### Debug Mode

Add debug logging to `agent.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Manual Testing Locally

```bash
# Set environment variables
export NEWSAPI_KEY="your_key"
export GEMINI_KEY="your_key"
export X_API_KEY="your_key"
export X_API_SECRET="your_key"
export X_ACCESS_TOKEN="your_key"
export X_ACCESS_SECRET="your_key"

# Run the bot
python agent.py
```

## 📊 Monitoring & Analytics

### Track Performance
1. **Twitter Analytics** - Check impressions, engagements, profile visits
2. **GitHub Actions** - Monitor workflow success/failure rates
3. **Engagement Rate** - Likes, retweets, replies per post
4. **Follower Growth** - Track daily/weekly growth

### Key Metrics to Monitor
- **Post frequency**: 4 times/day = 28 posts/week
- **Engagement rate**: Target 2-5% of impressions
- **Follower growth**: Target 50-100 new followers/week initially
- **Click-through rate**: Track link clicks from posts

### Optimization Loop
1. Post content → 2. Monitor metrics → 3. Analyze what works → 4. Adjust prompts/timing → Repeat

## 🔐 Security Best Practices

- ✅ Never commit API keys to repository
- ✅ Use GitHub Secrets for all credentials
- ✅ Enable 2FA on all accounts (GitHub, Twitter, Google)
- ✅ Regularly rotate API keys (every 3-6 months)
- ✅ Monitor API usage for unusual activity
- ✅ Keep repository private if handling sensitive data
- ✅ Review GitHub Actions logs for exposed secrets

## 📝 Cost Breakdown

| Service | Free Tier | Paid Option |
|---------|-----------|-------------|
| **GitHub Actions** | 2,000 min/month | $0.008/min after |
| **NewsAPI** | 100 requests/day | $449/month for more |
| **Google Gemini** | 60 requests/min | Pay-as-you-go |
| **Twitter API** | Free tier available | $100-$5,000/month |

**Total Cost: $0/month** (within free tiers)

**Monthly Usage:**
- GitHub Actions: ~120 minutes/month (well within free tier)
- NewsAPI: ~120 requests/month (within 100/day limit)
- Gemini: ~120 requests/month (within 60/min limit)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Ideas for Enhancement
- [ ] Add chart/graph generation
- [ ] Sentiment analysis of news
- [ ] Historical market data tracking
- [ ] Weekly market summary thread
- [ ] Support for multiple languages
- [ ] Integration with Telegram/Discord
- [ ] Custom stock watchlist
- [ ] Technical analysis integration

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This bot is for informational and educational purposes only. It does not provide financial advice. Always do your own research and consult with a qualified financial advisor before making investment decisions.

The creator is not responsible for any trading losses or decisions made based on information from this bot.

## 🙏 Acknowledgments

- [NewsAPI](https://newsapi.org/) - News aggregation
- [Google Gemini](https://ai.google.dev/) - AI summarization
- [Twitter API](https://developer.twitter.com/) - Social media platform
- [Tweepy](https://www.tweepy.org/) - Python Twitter library
- [GitHub Actions](https://github.com/features/actions) - Automation platform

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/indian-stock-market-bot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/indian-stock-market-bot/discussions)
- **Twitter**: [@YourBotHandle](https://twitter.com/YourBotHandle)

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐️ on GitHub!

---

**Made with ❤️ for Indian Stock Market Enthusiasts**

*Last Updated: September 2025*
