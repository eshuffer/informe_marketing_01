# Metricool Data Fetcher - Project Overview

## 🎯 Project Goal

Retrieve comprehensive marketing analytics data from Metricool API for the **Sattvica** brand, covering a 3-month period from **August 13, 2025** to **November 13, 2025**.

## 📋 What Data Is Retrieved

### 1. Brand Information
- All connected social media profiles
- Subscription plan and status
- Timezone and regional settings
- Brand configuration and preferences

### 2. Analytics Data (Per Platform)

#### **Instagram**
- Posts analytics (likes, comments, shares, saves)
- Reels performance
- Stories insights
- Hashtag performance
- Profile metrics (followers, reach, impressions)

#### **Facebook**
- Page posts analytics
- Reels performance
- Stories insights
- Page engagement metrics

#### **LinkedIn**
- Post analytics
- Newsletter performance
- Company page metrics

#### **Twitter/X**
- Tweet analytics
- Engagement metrics
- Follower growth

#### **TikTok**
- Video performance
- Engagement metrics
- Follower statistics

#### **YouTube**
- Video analytics
- Channel statistics

#### **Pinterest**
- Pin performance
- Board statistics

#### **Threads**
- Post analytics
- Thread engagement

#### **Bluesky**
- Post analytics
- Platform metrics

### 3. Demographic Data (Where Available)
- **Gender distribution**
- **Age groups**
- **Geographic location** (countries and cities)
- **Combined gender-age data**

Platforms with demographic data: Instagram, Facebook, LinkedIn, TikTok

### 4. Content Management
- **Scheduled Posts**: All posts scheduled for publication
- **Library Posts**: Posts saved in the content library
- **Post Events**: Scheduling and publication events

### 5. Media Library
- **Images**: All uploaded images
- **Videos**: All uploaded videos
- **Media metadata**: Upload dates, sizes, usage

### 6. Advanced Features
- **Hashtag Tracking**: Performance of tracked hashtags
- **Smart Links**: Link analytics and click tracking
- **Traffic Sources**: Where your audience comes from
- **Best Times**: Optimal posting times analysis

### 7. Performance Metrics
- **Timeline Metrics**: Day-by-day performance
  - Followers growth
  - Engagement rates
  - Impressions
  - Reach
  - Profile visits
  - Website clicks

- **Aggregated Metrics**: Summary statistics for the period
- **Distribution Analysis**: Content type performance
- **Engagement Metrics**: Detailed interaction data

## 🗂️ Data Organization

All data is organized in a clear hierarchy:

```
data/
├── fetch_summary.json          # Overview of all fetched data
├── analysis_report.txt         # Detailed analysis report
│
├── brand_info/                 # Brand configuration
│   ├── all_profiles.json      # All connected profiles
│   ├── sattvica_profile.json  # Sattvica-specific data
│   ├── subscription.json      # Plan details
│   └── timezone.json          # Time settings
│
├── analytics/                  # Platform-specific analytics
│   ├── timeline_*.json        # Time-series metrics
│   ├── aggregation.json       # Summary statistics
│   ├── hashtags.json          # Hashtag performance
│   ├── smart_links.json       # Link tracking
│   │
│   ├── instagram/             # Instagram data
│   │   ├── instagram_posts.json
│   │   ├── instagram_reels.json
│   │   ├── instagram_stories.json
│   │   └── instagram_hashtags.json
│   │
│   ├── facebook/              # Facebook data
│   ├── linkedin/              # LinkedIn data
│   ├── twitter/               # Twitter data
│   ├── tiktok/                # TikTok data
│   ├── youtube/               # YouTube data
│   ├── pinterest/             # Pinterest data
│   ├── threads/               # Threads data
│   └── bluesky/               # Bluesky data
│
├── stats/                      # General statistics
│   ├── all_posts.json         # All posts overview
│   ├── distribution.json      # Content distribution
│   ├── *_gender.json          # Gender demographics
│   ├── *_age.json             # Age demographics
│   ├── *_country.json         # Country data
│   └── *_city.json            # City data
│
├── posts/                      # Content management
│   ├── scheduled_posts.json   # Scheduled content
│   └── library_posts.json     # Content library
│
└── media/                      # Media library
    ├── images.json            # All images
    ├── videos.json            # All videos
    └── all_media.json         # Complete media inventory
```

## 🚀 How to Use

### Quick Start (Recommended)

```bash
cd metricool_data_fetcher
./run.sh
```

This will:
1. ✅ Install required Python packages
2. ✅ Fetch all data from Metricool API
3. ✅ Organize data in structured folders
4. ✅ Generate analysis report
5. ✅ Create summary document

### Manual Execution

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the data fetcher
python metricool_fetcher.py

# 3. Analyze the results
python analyze_data.py
```

## 📊 Output Files

After execution, you'll have:

1. **fetch_summary.json**
   - Overview of all fetched data
   - Total files created
   - Timestamp of fetch
   - Date range used

2. **analysis_report.txt**
   - Detailed breakdown of all data
   - File inventory with sizes
   - Data availability by platform

3. **metricool_fetcher.log** (in logs/)
   - Detailed execution log
   - API request/response info
   - Error messages (if any)

4. **200+ JSON files**
   - Raw data from Metricool API
   - Ready for analysis and visualization

## 🔧 Configuration

All settings are in `config/config.py`:

```python
METRICOOL_TOKEN = "OJROWJGDDYOVADGDGKNJFZJFRLZPKRQKHPYZAEYBVPWWGNMKMDQFRJMROWRAKLOO"
METRICOOL_USER_ID = "4226571"
CLIENT_NAME = "sattvica"
START_DATE = "2025-08-13"
END_DATE = "2025-11-13"
```

## 📈 Data Analysis Capabilities

The fetched data enables you to:

1. **Track Growth**
   - Follower growth over time
   - Engagement rate trends
   - Platform-specific performance

2. **Content Performance**
   - Best performing posts
   - Optimal posting times
   - Content type comparison (posts vs reels vs stories)

3. **Audience Insights**
   - Demographic breakdown
   - Geographic distribution
   - Engagement patterns

4. **Platform Comparison**
   - Cross-platform performance
   - Channel effectiveness
   - Resource allocation optimization

5. **Hashtag Strategy**
   - Hashtag performance tracking
   - Trending hashtags
   - Hashtag reach and engagement

6. **Link Performance**
   - Click-through rates
   - Traffic sources
   - Conversion tracking

## 🔒 Security Notes

- API token is stored in `config/config.py`
- Token provides read-only access to Metricool data
- No sensitive data is logged
- All data stored locally

## 📝 API Coverage

The script queries **326 Metricool API endpoints**, including:

- ✅ 50+ Analytics endpoints
- ✅ 40+ Statistics endpoints
- ✅ 30+ Post management endpoints
- ✅ 20+ Media endpoints
- ✅ 15+ Demographic endpoints
- ✅ 10+ Hashtag endpoints
- ✅ And many more...

## 💡 Next Steps After Data Retrieval

1. **Data Analysis**
   - Use Python pandas for data manipulation
   - Create visualizations with matplotlib/seaborn
   - Build dashboards with Plotly or Streamlit

2. **Reporting**
   - Generate automated reports
   - Create executive summaries
   - Track KPIs over time

3. **Optimization**
   - Identify best-performing content
   - Optimize posting schedule
   - Refine content strategy

4. **Export & Integration**
   - Export to Excel/CSV for stakeholders
   - Import into BI tools
   - Integrate with other analytics platforms

## 🛠️ Technical Details

- **Language**: Python 3.8+
- **Key Libraries**: requests, pandas, tqdm
- **API**: Metricool REST API v2
- **Data Format**: JSON
- **Rate Limiting**: 2 requests/second
- **Retry Logic**: 3 attempts per endpoint
- **Logging**: Comprehensive file and console logging

## 📞 Support & Troubleshooting

Check the README.md for:
- Detailed installation instructions
- Troubleshooting guide
- API endpoint reference
- Common issues and solutions

---

**Project Created**: November 13, 2025
**Data Period**: August 13 - November 13, 2025 (3 months)
**Brand**: Sattvica
**API Version**: Metricool API v2
