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
