"""
Utility functions for Metricool API interactions
"""

import requests
import time
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
from config.config import (
    BASE_URL, HEADERS, METRICOOL_USER_ID, METRICOOL_TOKEN,
    REQUEST_TIMEOUT, MAX_RETRIES, RETRY_DELAY, RATE_LIMIT
)

# Create logs directory if it doesn't exist
logs_dir = Path(__file__).parent / 'logs'
logs_dir.mkdir(parents=True, exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(logs_dir / 'metricool_fetcher.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Rate limiting
last_request_time = 0


def rate_limit_wait():
    """Implement rate limiting between requests"""
    global last_request_time
    current_time = time.time()
    time_since_last_request = current_time - last_request_time
    min_interval = 1.0 / RATE_LIMIT

    if time_since_last_request < min_interval:
        sleep_time = min_interval - time_since_last_request
        time.sleep(sleep_time)

    last_request_time = time.time()


def make_api_request(
    endpoint: str,
    method: str = "GET",
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    blog_id: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Make an API request to Metricool with retry logic

    Args:
        endpoint: API endpoint (e.g., '/admin/simpleProfiles')
        method: HTTP method (GET, POST, etc.)
        params: Query parameters
        data: Request body data
        blog_id: Blog ID if required for this endpoint

    Returns:
        Response data as dictionary or None if failed
    """
    if params is None:
        params = {}

    # Add required authentication parameters
    params['userId'] = METRICOOL_USER_ID
    params['userToken'] = METRICOOL_TOKEN

    if blog_id:
        params['blogId'] = blog_id

    url = f"{BASE_URL}{endpoint}"

    for attempt in range(MAX_RETRIES):
        try:
            rate_limit_wait()

            logger.debug(f"Request to {endpoint} (attempt {attempt + 1}/{MAX_RETRIES})")
            logger.debug(f"Full URL: {url} with params: {params}")

            if method.upper() == "GET":
                response = requests.get(
                    url,
                    params=params,
                    headers=HEADERS,
                    timeout=REQUEST_TIMEOUT
                )
            elif method.upper() == "POST":
                response = requests.post(
                    url,
                    params=params,
                    json=data,
                    headers=HEADERS,
                    timeout=REQUEST_TIMEOUT
                )
            else:
                logger.error(f"Unsupported HTTP method: {method}")
                return None

            # Check if request was successful
            if response.status_code == 200:
                try:
                    return response.json()
                except json.JSONDecodeError:
                    logger.warning(f"Response is not JSON for {endpoint}")
                    return {"raw_response": response.text}
            elif response.status_code == 404:
                logger.warning(f"Endpoint not found: {endpoint}")
                return None
            elif response.status_code == 401:
                logger.error(f"Authentication failed for {endpoint}")
                return None
            elif response.status_code == 429:
                logger.warning(f"Rate limit hit, waiting longer...")
                time.sleep(RETRY_DELAY * (attempt + 1) * 2)
                continue
            else:
                logger.warning(
                    f"Request failed with status {response.status_code}: {response.text[:200]}"
                )

        except requests.exceptions.Timeout:
            logger.warning(f"Request timeout for {endpoint} (attempt {attempt + 1})")
        except requests.exceptions.ConnectionError:
            logger.warning(f"Connection error for {endpoint} (attempt {attempt + 1})")
        except Exception as e:
            logger.error(f"Unexpected error for {endpoint}: {str(e)}")

        # Wait before retry
        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY * (attempt + 1))

    logger.error(f"Failed to fetch data from {endpoint} after {MAX_RETRIES} attempts")
    return None


def save_json(data: Any, filepath: Path, indent: int = 2):
    """
    Save data as JSON file

    Args:
        data: Data to save
        filepath: Path to save file
        indent: JSON indentation level
    """
    try:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False, default=str)
        logger.info(f"Saved data to {filepath}")
    except Exception as e:
        logger.error(f"Failed to save data to {filepath}: {str(e)}")


def load_json(filepath: Path) -> Optional[Dict[str, Any]]:
    """
    Load data from JSON file

    Args:
        filepath: Path to JSON file

    Returns:
        Loaded data or None if failed
    """
    try:
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load data from {filepath}: {str(e)}")
    return None


def get_date_range_params(start_date: str, end_date: str) -> Dict[str, Any]:
    """
    Create date range parameters for API requests

    Args:
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)

    Returns:
        Dictionary with date parameters in YYYYMMDD integer format
    """
    # Convert YYYY-MM-DD to YYYYMMDD integer format (as required by Metricool API)
    start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')

    start_int = int(start_dt.strftime('%Y%m%d'))
    end_int = int(end_dt.strftime('%Y%m%d'))

    return {
        'start': start_int,
        'end': end_int
    }


def get_timeline_date_params(start_date: str, end_date: str) -> Dict[str, Any]:
    """
    Create date range parameters for timeline/aggregation endpoints
    These endpoints use 'from' and 'to' with ISO 8601 format

    Args:
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)

    Returns:
        Dictionary with date parameters in ISO 8601 format
    """
    # Convert to ISO 8601 datetime format (YYYY-MM-DDTHH:MM:SS)
    start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')

    # Format as ISO 8601 with time component
    start_iso = start_dt.strftime('%Y-%m-%dT00:00:00')
    end_iso = end_dt.strftime('%Y-%m-%dT23:59:59')

    return {
        'from': start_iso,
        'to': end_iso
    }
