"""
Debug script to test multiple timeline metrics
Tests different network/metric/subject combinations
"""

import sys
import json
from pathlib import Path

# Add parent directory to path
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

def test_timeline_metric(network, metric, subject, description):
    """Test a specific timeline metric"""

    # Convert dates to ISO 8601 format
    start_dt = datetime.strptime(START_DATE, '%Y-%m-%d')
    end_dt = datetime.strptime(END_DATE, '%Y-%m-%d')

    from_date = start_dt.strftime('%Y-%m-%dT00:00:00')
    to_date = end_dt.strftime('%Y-%m-%dT23:59:59')

    # Build URL and params
    url = f"{BASE_URL}/v2/analytics/timelines"

    params = {
        'userId': METRICOOL_USER_ID,
        'userToken': METRICOOL_TOKEN,
        'blogId': BLOG_ID,
        'network': network,
        'metric': metric,
        'subject': subject,
        'from': from_date,
        'to': to_date
    }

    headers = {
        'X-Mc-Auth': METRICOOL_TOKEN,
        'Content-Type': 'application/json'
    }

    print(f"\n{'='*80}")
    print(f"Testing: {description}")
    print(f"  Network: {network} | Metric: {metric} | Subject: {subject}")
    print(f"{'='*80}")

    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)

        if response.status_code == 200:
            print(f"✅ SUCCESS (Status: {response.status_code})")
            data = response.json()

            # Show data summary
            if isinstance(data, dict):
                if 'data' in data:
                    if isinstance(data['data'], list):
                        print(f"   Data points: {len(data['data'])}")
                        if len(data['data']) > 0:
                            print(f"   First entry: {data['data'][0]}")
                    else:
                        print(f"   Data type: {type(data['data'])}")
                        print(f"   Data: {data['data']}")
                else:
                    print(f"   Keys: {list(data.keys())}")

            # Save successful response
            output_file = Path(__file__).parent / f'timeline_{network}_{metric}_{subject}.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"   Saved to: {output_file.name}")

            return True

        else:
            print(f"❌ FAILED (Status: {response.status_code})")
            try:
                error_data = response.json()
                print(f"   Error: {json.dumps(error_data, indent=2)}")
            except:
                print(f"   Error: {response.text[:200]}")

            return False

    except Exception as e:
        print(f"❌ EXCEPTION: {str(e)}")
        return False


def main():
    """Test multiple timeline metrics"""

    print("\n" + "="*80)
    print("TESTING MULTIPLE TIMELINE METRICS")
    print("="*80)
    print(f"\nDate Range: {START_DATE} to {END_DATE}")
    print(f"Blog ID: {BLOG_ID}")
    print(f"User ID: {METRICOOL_USER_ID}")
    print(f"Token: {METRICOOL_TOKEN[:20]}... (hidden)")

    # Test cases: (network, metric, subject, description)
    test_cases = [
        # Instagram Posts
        ('instagram', 'count', 'posts', 'Instagram Posts Count'),
        ('instagram', 'impressions', 'posts', 'Instagram Posts Impressions'),
        ('instagram', 'engagement', 'posts', 'Instagram Posts Engagement'),
        ('instagram', 'reach', 'posts', 'Instagram Posts Reach'),
        ('instagram', 'likes', 'posts', 'Instagram Posts Likes'),

        # Instagram Reels
        ('instagram', 'count', 'reels', 'Instagram Reels Count'),
        ('instagram', 'engagement', 'reels', 'Instagram Reels Engagement'),
        ('instagram', 'videoviews', 'reels', 'Instagram Reels Video Views'),

        # Facebook Posts
        ('facebook', 'count', 'posts', 'Facebook Posts Count'),
        ('facebook', 'impressions', 'posts', 'Facebook Posts Impressions'),
        ('facebook', 'engagement', 'posts', 'Facebook Posts Engagement'),

        # Facebook Account
        ('facebook', 'likes', 'account', 'Facebook Page Likes'),
        ('facebook', 'pageFollows', 'account', 'Facebook Page Follows'),
    ]

    results = {
        'success': [],
        'failed': []
    }

    for network, metric, subject, description in test_cases:
        success = test_timeline_metric(network, metric, subject, description)

        if success:
            results['success'].append(description)
        else:
            results['failed'].append(description)

    # Summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    print(f"\n✅ Successful: {len(results['success'])}/{len(test_cases)}")
    for item in results['success']:
        print(f"   • {item}")

    if results['failed']:
        print(f"\n❌ Failed: {len(results['failed'])}/{len(test_cases)}")
        for item in results['failed']:
            print(f"   • {item}")

    print("\n" + "="*80)


if __name__ == '__main__':
    main()
