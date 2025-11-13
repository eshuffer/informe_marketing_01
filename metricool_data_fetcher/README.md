# Metricool Data Fetcher for Sattvica Brand

A comprehensive Python tool to retrieve all marketing data from Metricool API for the Sattvica brand.

## Overview

This project fetches and organizes marketing analytics data from Metricool API, including:

- **Brand Information**: Profile details, subscription, timezone, and settings
- **Analytics**: Timeline metrics, aggregations, and platform-specific analytics
- **Social Media Platforms**: Instagram, Facebook, LinkedIn, Twitter/X, TikTok, YouTube, Pinterest, Threads, Bluesky
- **Content**: Posts, reels, stories, and scheduled content
- **Demographics**: Age, gender, location data for different platforms
- **Media**: Images and videos from the media library
- **Hashtags**: Hashtag performance and tracking
- **Smart Links**: Link analytics and tracking

## Date Range

- **Start Date**: 2025-08-13
- **End Date**: 2025-11-13
- **Duration**: 3 months of data

## Project Structure

```
metricool_data_fetcher/
├── config/
│   └── config.py              # API credentials and configuration
├── data/
│   ├── analytics/
│   │   ├── instagram/         # Instagram-specific analytics
│   │   ├── facebook/          # Facebook-specific analytics
│   │   ├── linkedin/          # LinkedIn-specific analytics
│   │   ├── twitter/           # Twitter/X-specific analytics
│   │   ├── tiktok/            # TikTok-specific analytics
│   │   ├── youtube/           # YouTube-specific analytics
│   │   ├── pinterest/         # Pinterest-specific analytics
│   │   ├── threads/           # Threads-specific analytics
│   │   ├── bluesky/           # Bluesky-specific analytics
│   │   └── competitors/       # Competitor analytics
│   ├── stats/                 # General statistics and demographics
│   ├── posts/                 # Scheduled and library posts
│   ├── media/                 # Media library (images, videos)
│   ├── reports/               # Generated reports
│   └── brand_info/            # Brand profile and settings
├── logs/
│   └── metricool_fetcher.log  # Execution logs
├── metricool_fetcher.py       # Main script
├── utils.py                   # Utility functions
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation

1. **Install Python dependencies**:
   ```bash
   cd metricool_data_fetcher
   pip install -r requirements.txt
   ```

## Configuration

All credentials are pre-configured in `config/config.py`:

- **METRICOOL_TOKEN**: API authentication token
- **METRICOOL_USER_ID**: User ID (4226571)
- **CLIENT_NAME**: Brand name (sattvica)
- **Date Range**: August 13 - November 13, 2025

## Usage

### Run the complete data fetch:

```bash
python metricool_fetcher.py
```

The script will:

1. ✅ Authenticate with Metricool API
2. ✅ Retrieve the blog ID for Sattvica brand
3. ✅ Fetch all available data from 326+ API endpoints
4. ✅ Organize and save data in JSON format
5. ✅ Generate a summary report
6. ✅ Create detailed logs

## Data Retrieved

### Brand Information
- All connected profiles
- Subscription details
- Timezone settings
- Brand configuration

### Analytics Data

#### Timeline Metrics (for all platforms):
- Followers growth
- Engagement rates
- Impressions
- Reach
- Likes, comments, shares, saves
- Views
- Profile visits
- Website clicks

#### Platform-Specific Analytics:
- **Instagram**: Posts, Reels, Stories, Hashtags
- **Facebook**: Posts, Reels, Stories
- **LinkedIn**: Posts, Newsletters
- **Twitter/X**: Posts and engagement
- **TikTok**: Videos and performance
- **YouTube**: Video analytics
- **Pinterest**: Pin performance
- **Threads**: Thread analytics
- **Bluesky**: Post analytics

### Demographics
For Instagram, Facebook, LinkedIn, and TikTok:
- Gender distribution
- Age distribution
- Gender-age combinations
- Country distribution
- City distribution

### Content Data
- Scheduled posts
- Library posts
- Post performance metrics
- Content types distribution

### Media Library
- All images
- All videos
- Media metadata

### Additional Data
- Hashtag tracking and performance
- Smart links analytics
- Traffic sources
- Best posting times

## Output

All data is saved in JSON format with the following structure:

```
data/
├── fetch_summary.json         # Summary of all fetched data
├── brand_info/
│   ├── all_profiles.json
│   ├── sattvica_profile.json
│   ├── subscription.json
│   └── ...
├── analytics/
│   ├── timeline_followers.json
│   ├── timeline_engagement.json
│   ├── aggregation.json
│   ├── instagram/
│   │   ├── instagram_posts.json
│   │   ├── instagram_reels.json
│   │   └── ...
│   └── ...
└── stats/
    ├── all_posts.json
    ├── instagram_gender.json
    ├── facebook_age.json
    └── ...
```

## Features

### Robust Error Handling
- Automatic retry mechanism (3 attempts)
- Rate limiting to respect API limits
- Detailed logging of all operations
- Graceful handling of missing endpoints

### Data Organization
- Hierarchical directory structure
- Categorized by data type
- Platform-specific folders
- Easy to navigate and analyze

### Comprehensive Logging
- Real-time progress updates
- Detailed error messages
- Request/response logging
- Saved to `logs/metricool_fetcher.log`

### Progress Tracking
- Visual progress bars with tqdm
- Step-by-step status updates
- Summary report generation

## API Endpoints Coverage

The script covers **326 API endpoints** including:

- ✅ Admin & Profile Management
- ✅ Analytics (v2 API)
- ✅ Statistics
- ✅ Posts & Content
- ✅ Media Management
- ✅ Scheduler
- ✅ Demographics
- ✅ Hashtag Tracking
- ✅ Smart Links
- ✅ Reports

## Rate Limiting

The script implements conservative rate limiting:
- **2 requests per second** to avoid API throttling
- Automatic backoff on rate limit errors
- Configurable in `config/config.py`

## Troubleshooting

### Authentication Errors
- Verify the METRICOOL_TOKEN in `config/config.py`
- Check that the token has not expired

### Missing Data
- Some endpoints may return no data if the feature is not used
- Check logs for 404 errors (endpoint not available)
- Verify the blog_id is correct

### Rate Limiting
- If you encounter 429 errors, increase RETRY_DELAY in config
- Decrease RATE_LIMIT for slower requests

## Logs

Check `logs/metricool_fetcher.log` for:
- Detailed execution logs
- Error messages and stack traces
- API request/response information
- Progress updates

## Summary Report

After execution, check `data/fetch_summary.json` for:
- Total files created
- List of all saved files
- Fetch timestamp
- Date range used

## Next Steps

After data retrieval, you can:

1. **Analyze the data** using Python pandas or other tools
2. **Create visualizations** from the JSON data
3. **Build reports** combining multiple data sources
4. **Track trends** over the 3-month period
5. **Compare platforms** to identify best performers

## API Reference

Based on Metricool's official Swagger documentation:
- Base URL: `https://app.metricool.com/api`
- Authentication: `X-Mc-Auth` header with token
- Full API docs: See `swagger.yaml` in parent directory

## Support

For issues or questions:
- Check the logs in `logs/metricool_fetcher.log`
- Review the Metricool API documentation
- Verify credentials and permissions

---

**Last Updated**: 2025-11-13
**Version**: 1.0.0
**Brand**: Sattvica
**Data Period**: August 13 - November 13, 2025
