# Getting Started with Metricool Data Fetcher

## Quick Start (3 Simple Steps)

### Step 1: Navigate to the project directory
```bash
cd /home/user/informe_marketing_01/metricool_data_fetcher
```

### Step 2: Run the automated script
```bash
./run.sh
```

This single command will:
- ✅ Install all required dependencies
- ✅ Fetch all Sattvica brand data from Metricool
- ✅ Organize data in structured folders
- ✅ Generate analysis reports
- ✅ Create summary documents

### Step 3: Explore your data
```bash
# View the summary
cat data/fetch_summary.json

# View the analysis
cat data/analysis_report.txt

# Browse the data
ls -la data/
```

## What Data Will Be Retrieved?

The script will automatically fetch:

### 📊 **Brand Analytics** (3 months: Aug 13 - Nov 13, 2025)
- Timeline metrics (followers, engagement, impressions, reach)
- Aggregated statistics
- Platform-specific performance data

### 📱 **Social Media Platforms**
- **Instagram**: Posts, Reels, Stories, Hashtags
- **Facebook**: Posts, Reels, Stories, Page metrics
- **LinkedIn**: Posts (if connected)
- **Twitter/X**: Tweets and engagement
- **TikTok**: Videos (if connected)
- **YouTube**: Videos (if connected)
- **Pinterest**: Pins (if connected)
- **Threads**: Posts (if connected)
- **Bluesky**: Posts (if connected)

### 👥 **Audience Demographics**
- Gender distribution
- Age groups
- Geographic location (countries & cities)
- Combined demographic data

### 📝 **Content Management**
- Scheduled posts
- Content library
- Post performance metrics

### 🎨 **Media Assets**
- Image library
- Video library
- Media metadata

### 🔗 **Advanced Features**
- Hashtag tracking
- Smart links analytics
- Traffic sources
- Best posting times

## Folder Structure After Running

```
data/
├── fetch_summary.json          # Overview of fetch results
├── analysis_report.txt         # Detailed analysis
│
├── brand_info/                 # Brand details
│   ├── all_profiles.json
│   ├── sattvica_profile.json
│   ├── subscription.json
│   └── brand_settings.json
│
├── analytics/                  # Platform analytics
│   ├── timeline_*.json        # Time-series data
│   ├── aggregation.json       # Summary stats
│   ├── hashtags.json          # Hashtag data
│   ├── instagram/             # Instagram data
│   ├── facebook/              # Facebook data
│   └── ...                    # Other platforms
│
├── stats/                      # Statistics
│   ├── all_posts.json
│   ├── *_gender.json
│   ├── *_age.json
│   ├── *_country.json
│   └── ...
│
├── posts/                      # Content
│   ├── scheduled_posts.json
│   └── library_posts.json
│
└── media/                      # Media library
    ├── images.json
    ├── videos.json
    └── all_media.json
```

## Manual Execution (Alternative Method)

If you prefer to run commands manually:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the data fetcher
python metricool_fetcher.py

# 3. Run the analyzer
python analyze_data.py
```

## Viewing Results

### Summary File
```bash
# View JSON summary with formatting
python -m json.tool data/fetch_summary.json
```

### Analysis Report
```bash
# View full analysis
less data/analysis_report.txt

# Or use cat for quick view
cat data/analysis_report.txt
```

### Explore Specific Data
```bash
# Instagram posts
python -m json.tool data/analytics/instagram/instagram_posts.json | less

# Timeline metrics
python -m json.tool data/analytics/timeline_followers.json | less

# Demographics
python -m json.tool data/stats/instagram_gender.json | less
```

## Execution Time

Expected execution time: **15-30 minutes**
- Depends on amount of data available
- Network speed
- API response times

The script implements:
- ✅ Rate limiting (2 requests/second)
- ✅ Automatic retries (3 attempts per endpoint)
- ✅ Progress bars showing current status
- ✅ Detailed logging

## Checking Progress

While the script runs, you can:

1. **Watch the console output** - Real-time progress bars
2. **Check the log file** - `tail -f logs/metricool_fetcher.log`
3. **Browse partial results** - Data is saved as it's fetched

## Troubleshooting

### If the script fails to start:
```bash
# Check Python version (needs 3.8+)
python3 --version

# Install dependencies manually
pip3 install requests python-dateutil pyyaml tqdm
```

### If API authentication fails:
- Check that credentials in `config/config.py` are correct
- Verify the Metricool token hasn't expired

### If some data is missing:
- This is normal! Not all platforms may be connected
- Check `logs/metricool_fetcher.log` for details
- Some endpoints may not have data for the date range

### To re-run data fetch:
```bash
# The script is safe to re-run
# It will overwrite existing data
./run.sh
```

## Next Steps After Data Retrieval

### 1. Data Analysis
```python
import json
import pandas as pd

# Load Instagram posts
with open('data/analytics/instagram/instagram_posts.json') as f:
    posts = json.load(f)

# Convert to DataFrame for analysis
df = pd.DataFrame(posts.get('data', []))
print(df.head())
```

### 2. Create Visualizations
```python
import matplotlib.pyplot as plt

# Load followers timeline
with open('data/analytics/timeline_followers.json') as f:
    followers = json.load(f)

# Plot growth over time
# Your visualization code here
```

### 3. Generate Reports
- Use the JSON data with your preferred reporting tool
- Export to Excel/CSV for stakeholders
- Create custom dashboards

## Configuration

All settings are in `config/config.py`:

```python
METRICOOL_TOKEN = "..."        # Your API token
METRICOOL_USER_ID = "4226571"  # Your user ID
CLIENT_NAME = "sattvica"       # Brand name
START_DATE = "2025-08-13"      # Data start
END_DATE = "2025-11-13"        # Data end
```

To change the date range, edit these values and re-run.

## Support

- **Documentation**: See README.md and PROJECT_OVERVIEW.md
- **Logs**: Check `logs/metricool_fetcher.log`
- **API Docs**: See `swagger.yaml` in parent directory

---

**Ready to start?** Just run: `./run.sh`
