"""
Metricool API Configuration
Contains credentials and settings for API access
"""

# Metricool API Credentials
METRICOOL_TOKEN = "OJROWJGDDYOVADGDGKNJFZJFRLZPKRQKHPYZAEYBVPWWGNMKMDQFRJMROWRAKLOO"
METRICOOL_USER_ID = "4226571"
CLIENT_NAME = "sattvica"

# Date Range for Data Retrieval
START_DATE = "2025-08-13"
END_DATE = "2025-11-13"

# API Configuration
BASE_URL = "https://app.metricool.com/api"
HEADERS = {
    "X-Mc-Auth": METRICOOL_TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Request timeout (seconds)
REQUEST_TIMEOUT = 30

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Rate limiting (requests per second)
RATE_LIMIT = 2  # Conservative to avoid API limits

# Platform Configuration
# Set to True to fetch data from that platform, False to skip
PLATFORMS_ENABLED = {
    'instagram': True,
    'facebook': True,
    'linkedin': True,
    'twitter': False,     # Disabled by default (usually not connected)
    'tiktok': True,
    'youtube': False,     # Disabled by default (usually not connected)
    'pinterest': True,
    'threads': True,
    'bluesky': False,     # Disabled by default (usually not connected)
}

# Features Configuration
FETCH_TIMELINES = True           # Fetch timeline analytics (time-series data)
FETCH_AGGREGATIONS = True        # Fetch aggregated metrics
FETCH_DEMOGRAPHICS = True        # Fetch age/gender/location data
FETCH_TRAFFIC_SOURCES = True     # Fetch traffic source data
FETCH_BEST_TIMES = True          # Fetch optimal posting times
FETCH_SMART_LINKS = True         # Fetch smart links analytics
FETCH_HASHTAG_TRACKER = True     # Fetch hashtag tracking data
