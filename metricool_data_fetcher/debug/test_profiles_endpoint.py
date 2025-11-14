"""
Test the /admin/blog/profiles endpoint to debug platform detection
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import requests
import json
from config.config import (
    BASE_URL,
    METRICOOL_TOKEN,
    METRICOOL_USER_ID,
)

BLOG_ID = "3991897"

def test_profiles_endpoint():
    """Test the /admin/blog/profiles endpoint"""
    print("="*80)
    print("TESTING /admin/blog/profiles ENDPOINT")
    print("="*80)

    url = f"{BASE_URL}/admin/blog/profiles"

    params = {
        'userId': METRICOOL_USER_ID,
        'userToken': METRICOOL_TOKEN,
        'blogId': BLOG_ID,
    }

    print(f"\n📍 URL: {url}")
    print(f"📦 Params: {json.dumps(params, indent=2)}")

    try:
        print("\n🔄 Making request...")
        response = requests.get(url, params=params, timeout=30)

        print(f"\n✅ Status Code: {response.status_code}")
        print(f"📄 Content-Type: {response.headers.get('Content-Type', 'Unknown')}")

        # Try to parse as JSON
        try:
            data = response.json()
            print(f"\n✅ Response is valid JSON")
            print(f"\n📊 JSON Response:")
            print(json.dumps(data, indent=2))

            # Analyze the structure
            print(f"\n🔍 Analysis:")
            if isinstance(data, list):
                print(f"   • Response is a list with {len(data)} items")
                if data:
                    print(f"   • First item keys: {list(data[0].keys())}")
                    print(f"   • First item sample: {json.dumps(data[0], indent=6)}")
            elif isinstance(data, dict):
                print(f"   • Response is a dict with keys: {list(data.keys())}")
                if 'data' in data:
                    print(f"   • Has 'data' field (type: {type(data['data'])})")
                    if isinstance(data['data'], list) and data['data']:
                        print(f"   • data[0] keys: {list(data['data'][0].keys())}")
                        print(f"   • data[0] sample: {json.dumps(data['data'][0], indent=6)}")

        except ValueError as e:
            print(f"\n❌ Response is NOT valid JSON")
            print(f"   Error: {e}")
            print(f"\n📄 Raw response (first 500 chars):")
            print(response.text[:500])

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request failed: {e}")

    print("\n" + "="*80)

if __name__ == "__main__":
    test_profiles_endpoint()
