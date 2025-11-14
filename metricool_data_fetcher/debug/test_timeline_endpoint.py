"""
Debug script to test /v2/analytics/timelines endpoint
Tests a single timeline request with correct parameters
"""

import sys
import json
from pathlib import Path

# Add parent directory to path to import config and utils
sys.path.insert(0, str(Path(__file__).parent.parent))

import requests
from datetime import datetime
from config.config import (
    BASE_URL,
    METRICOOL_TOKEN,
    METRICOOL_USER_ID,
    START_DATE,
    END_DATE
)

# Sattvica brand ID
BLOG_ID = "3991897"

def test_timeline_endpoint():
    """Test the timeline endpoint with correct parameters"""

    print("=" * 80)
    print("TESTING /v2/analytics/timelines ENDPOINT")
    print("=" * 80)
    print()

    # Convert dates to ISO 8601 format (what timeline endpoint needs)
    start_dt = datetime.strptime(START_DATE, '%Y-%m-%d')
    end_dt = datetime.strptime(END_DATE, '%Y-%m-%d')

    from_date = start_dt.strftime('%Y-%m-%dT00:00:00')
    to_date = end_dt.strftime('%Y-%m-%dT23:59:59')

    # Build URL
    url = f"{BASE_URL}/v2/analytics/timelines"

    # Build parameters
    params = {
        'userId': METRICOOL_USER_ID,
        'userToken': METRICOOL_TOKEN,
        'blogId': BLOG_ID,
        'network': 'instagram',
        'metric': 'impressions',
        'subject': 'posts',
        'from': from_date,
        'to': to_date
    }

    # Headers
    headers = {
        'X-Mc-Auth': METRICOOL_TOKEN,
        'Content-Type': 'application/json'
    }

    # Display what we're sending
    print("📍 URL:")
    print(f"   {url}")
    print()

    print("📊 PARAMETERS:")
    for key, value in params.items():
        if key == 'userToken':
            print(f"   {key}: {value[:20]}... (hidden)")
        else:
            print(f"   {key}: {value}")
    print()

    print("🔑 HEADERS:")
    for key, value in headers.items():
        if key == 'X-Mc-Auth':
            print(f"   {key}: {value[:20]}... (hidden)")
        else:
            print(f"   {key}: {value}")
    print()

    print("🚀 SENDING REQUEST...")
    print()

    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)

        print(f"📥 RESPONSE STATUS: {response.status_code}")
        print()

        if response.status_code == 200:
            print("✅ SUCCESS!")
            print()
            data = response.json()

            # Pretty print the response
            print("📄 RESPONSE DATA:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            print()

            # Save to file
            output_file = Path(__file__).parent / 'timeline_test_response.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"💾 Response saved to: {output_file}")

        else:
            print("❌ REQUEST FAILED")
            print()
            print("📄 ERROR RESPONSE:")
            try:
                error_data = response.json()
                print(json.dumps(error_data, indent=2, ensure_ascii=False))
            except:
                print(response.text)

        print()
        print("=" * 80)

    except Exception as e:
        print(f"❌ EXCEPTION: {str(e)}")
        print()
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    test_timeline_endpoint()
