# Marketing Analytics Module

AI-powered social media marketing analytics system for analyzing Metricool data and generating strategic insights.

## 🎯 Features

- **Comprehensive Data Analysis**
  - Engagement metrics across platforms (Instagram, Facebook)
  - Timeline trends analysis with growth rates
  - Content performance comparison (Posts vs Reels)
  - Audience demographics breakdown
  - Platform performance comparison

- **AI-Powered Marketing Guru Insights** 🔥
  - **Topic-Based Deep Analysis**: 5 separate focused AI analyses per report
  - **Guru-Level Strategic Recommendations**: 20-30 pages of expert insights
  - **Reach Optimization Playbook**: 8-10 tactics to increase reach 30-50%
  - **Experimentation Roadmap**: 5-7 A/B tests with detailed protocols
  - **Implementation-Ready Action Plans**: Immediate/short/long-term strategies
  - **Root Cause Analysis**: WHY things work (psychology + algorithms)
  - **Executive-Level Summaries**: 6-paragraph C-suite briefings
  - **Risk Mitigation Strategies**: What could go wrong + how to prevent it
  - **Resource Requirements**: Team time, tools, budget recommendations
  - **Success Milestones**: 30/60/90 day targets with metrics

- **Professional Reports**
  - Markdown format reports
  - Executive summaries
  - Data visualizations
  - Detailed appendices

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key (for AI insights)
- Metricool data (from the data fetcher module)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd marketing_analytics
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key

Set your OpenAI API key as an environment variable:

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-api-key-here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

Alternatively, edit `config.py` and set the API key directly:
```python
OPENAI_API_KEY = "your-api-key-here"
```

### 3. Run Analytics

```bash
python analyze.py
```

The system will:
1. Load all JSON data from the Metricool fetcher
2. Perform comprehensive analytics
3. Generate AI-powered insights
4. Create a detailed markdown report

## 📁 Project Structure

```
marketing_analytics/
├── analyze.py              # Main analytics runner
├── config.py               # Configuration settings
├── data_loader.py          # JSON data loading utilities
├── analytics_processors.py # Core analytics functions
├── ai_insights.py          # OpenAI integration for insights
├── report_generator.py     # Report generation
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── reports/               # Generated reports (created automatically)
```

## 📊 Analytics Components

### 1. Engagement Analysis
- Calculates engagement rates for all posts
- Identifies best performing content
- Compares platform performance
- Analyzes interaction patterns

### 2. Trend Analysis
- Timeline metric trends
- Growth rate calculations
- Weekly pattern detection
- Peak performance identification

### 3. Content Performance
- Posts vs Reels comparison
- Top performing content identification
- Content type recommendations
- Hashtag effectiveness (if available)

### 4. Demographics Analysis
- Age distribution
- Gender breakdown
- Geographic insights (country, city)
- Audience segmentation

### 5. AI Strategic Insights
- Executive summaries
- Key findings and observations
- Performance highlights
- Actionable recommendations
- Trend interpretations

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# OpenAI Settings
OPENAI_MODEL = "gpt-4o"        # AI model to use
OPENAI_TEMPERATURE = 0.3       # Response creativity (0.0-1.0)

# Analysis Settings
ENABLED_PLATFORMS = ['instagram', 'facebook']

# Report Settings
REPORT_FORMAT = "markdown"     # Options: markdown, html, json
INCLUDE_AI_INSIGHTS = True     # Enable/disable AI insights
```

## 📈 Output

The analysis generates:

1. **Markdown Report** (`reports/sattvica_marketing_report_YYYYMMDD_HHMMSS.md`)
   - Executive summary
   - Platform performance comparison
   - Engagement analysis
   - Content performance breakdown
   - Trends analysis
   - Demographics insights
   - AI-powered strategic recommendations

2. **Log File** (`reports/analytics.log`)
   - Detailed processing logs
   - Error tracking
   - Performance metrics

## 🔍 Example Report Sections

### Executive Summary
AI-generated strategic overview of the analysis period with key achievements and areas for improvement.

### Platform Performance
```
| Metric              | Instagram | Facebook |
|---------------------|-----------|----------|
| Avg Engagement Rate | 3.45%     | 2.12%    |
| Total Posts         | 45        | 32       |
| Total Reach         | 125,430   | 89,234   |
```

### Top Performing Content
Lists the best-performing posts with:
- Engagement rate
- Reach and impressions
- Interaction counts
- Content preview

### AI Strategic Insights
- Key findings based on data
- Performance highlights
- Areas for improvement
- Specific, actionable recommendations
- Trend analysis and predictions

## 💡 Usage Tips

1. **Run After Data Fetch**: Always run the analytics after fetching fresh data with the Metricool fetcher

2. **Regular Analysis**: Run weekly or monthly to track performance trends over time

3. **Compare Reports**: Save reports with timestamps to compare performance across periods

4. **Review AI Insights**: The AI-generated recommendations are based on your actual data and provide strategic value

5. **Customize Thresholds**: Adjust engagement thresholds in `config.py` to match your industry standards

## 🛠️ Advanced Usage

### Analyze Specific Time Periods

Edit the date range in `config.py`:
```python
START_DATE = "2025-08-13"
END_DATE = "2025-11-13"
```

### Disable AI Insights

If you don't have an OpenAI API key:
```python
INCLUDE_AI_INSIGHTS = False
```

The system will still generate comprehensive analytics, just without AI-powered strategic insights.

### Custom Analytics

You can import the modules and create custom analyses:

```python
from data_loader import MetricoolDataLoader
from analytics_processors import EngagementAnalyzer

# Load data
loader = MetricoolDataLoader()
data = loader.load_all_data()

# Custom analysis
analyzer = EngagementAnalyzer()
posts_df = loader.get_posts_dataframe('instagram', 'posts')
engagement = analyzer.analyze_platform_engagement(posts_df, 'instagram')
```

## 🔐 Security Notes

- Never commit your OpenAI API key to version control
- Use environment variables for sensitive credentials
- The `.gitignore` should exclude `config.py` if it contains keys
- Review generated reports before sharing (they may contain sensitive data)

## 📞 Troubleshooting

### "No module named 'openai'"
```bash
pip install openai
```

### "OpenAI API key not configured"
Set the environment variable or update `config.py` with your API key

### "No data available"
Ensure you've run the Metricool data fetcher first to populate the `data/` directory

### Import errors
Make sure you're running from the `marketing_analytics` directory:
```bash
cd marketing_analytics
python analyze.py
```

## 📄 License

Part of the Sattvica Marketing Analytics System

## 🤝 Contributing

This is a custom analytics solution for Sattvica. Modifications should be tested thoroughly before production use.

---

**Last Updated:** 2025-11-14
**Version:** 1.0.0
