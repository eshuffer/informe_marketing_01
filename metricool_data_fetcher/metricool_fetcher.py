"""
Main Metricool Data Fetcher
Retrieves all available data for Sattvica brand from Metricool API
"""

import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional
from tqdm import tqdm

from config.config import (
    METRICOOL_USER_ID, CLIENT_NAME, START_DATE, END_DATE
)
from utils import make_api_request, save_json, get_date_range_params

# Setup logging
logger = logging.getLogger(__name__)

# Data directory
DATA_DIR = Path(__file__).parent / 'data'


class MetricoolDataFetcher:
    """Fetches and stores Metricool data for a specific brand"""

    def __init__(self):
        self.blog_id = None
        self.brand_name = CLIENT_NAME
        self.start_date = START_DATE
        self.end_date = END_DATE
        self.fetched_data = {
            'brand_info': {},
            'analytics': {},
            'stats': {},
            'posts': {},
            'media': {},
            'reports': {}
        }

    def get_blog_id(self) -> Optional[str]:
        """Retrieve the blog ID for the Sattvica brand"""
        logger.info("Fetching brand profiles to get blog ID...")

        response = make_api_request('/admin/simpleProfiles')

        if response:
            # API returns profiles directly as a list
            profiles = response if isinstance(response, list) else response.get('data', [])
            logger.info(f"Found {len(profiles)} brand profiles")

            # Save all profiles for reference
            save_json(
                profiles,
                DATA_DIR / 'brand_info' / 'all_profiles.json'
            )

            # Find Sattvica brand (check 'label' and 'title' fields)
            for profile in profiles:
                name = profile.get('label', '') or profile.get('title', '') or profile.get('name', '')
                if self.brand_name.lower() in name.lower():
                    self.blog_id = str(profile.get('id') or profile.get('blogId'))
                    logger.info(f"Found {self.brand_name} brand with ID: {self.blog_id}")
                    logger.info(f"  Instagram: {profile.get('instagram', 'N/A')}")
                    logger.info(f"  Facebook: {profile.get('facebook', 'N/A')}")
                    save_json(
                        profile,
                        DATA_DIR / 'brand_info' / f'{self.brand_name}_profile.json'
                    )
                    return self.blog_id

            # If not found by name, use first profile
            if profiles:
                self.blog_id = str(profiles[0].get('id') or profiles[0].get('blogId'))
                first_name = profiles[0].get('label', '') or profiles[0].get('title', 'Unknown')
                logger.warning(f"Brand '{self.brand_name}' not found by name. Using first profile: {first_name} (ID: {self.blog_id})")
                return self.blog_id

        logger.error("Failed to retrieve blog ID")
        return None

    def fetch_brand_info(self):
        """Fetch brand information and settings"""
        logger.info("Fetching brand information...")

        endpoints = [
            ('/admin/blog/profiles', 'connected_profiles.json'),
            ('/profile/subscription', 'subscription.json'),
            ('/v2/settings/brands', 'brand_settings.json'),
        ]

        for endpoint, filename in tqdm(endpoints, desc="Brand Info"):
            data = make_api_request(endpoint, blog_id=self.blog_id)
            if data:
                save_json(data, DATA_DIR / 'brand_info' / filename)
                self.fetched_data['brand_info'][filename] = data

    def fetch_analytics_timelines(self):
        """Fetch timeline analytics - SKIPPED due to complex requirements"""
        logger.info("Skipping timeline analytics (requires network-specific queries)")
        # Timeline endpoint requires specific network and metric combinations
        # This can be added later with proper parameter mapping
        pass

    def fetch_analytics_aggregation(self):
        """Fetch aggregated analytics - SKIPPED due to API requirements"""
        logger.info("Skipping aggregation analytics (use platform-specific endpoints instead)")
        # Aggregation endpoint has complex requirements
        # Using platform-specific endpoints provides better data
        pass

    def fetch_instagram_analytics(self):
        """Fetch Instagram-specific analytics"""
        logger.info("Fetching Instagram analytics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        # Only use working v2 endpoints
        endpoints = [
            ('/v2/analytics/posts/instagram', 'instagram_posts.json'),
            ('/v2/analytics/reels/instagram', 'instagram_reels.json'),
            ('/v2/analytics/stories/instagram', 'instagram_stories.json'),
            ('/v2/analytics/posts/instagram/hashtags', 'instagram_hashtags.json'),
        ]

        for endpoint, filename in tqdm(endpoints, desc="Instagram Analytics"):
            data = make_api_request(
                endpoint,
                params=date_params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'analytics' / 'instagram' / filename
                )

    def fetch_facebook_analytics(self):
        """Fetch Facebook-specific analytics"""
        logger.info("Fetching Facebook analytics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        # Only use working v2 endpoints
        endpoints = [
            ('/v2/analytics/posts/facebook', 'facebook_posts.json'),
            ('/v2/analytics/reels/facebook', 'facebook_reels.json'),
            ('/v2/analytics/stories/facebook', 'facebook_stories.json'),
        ]

        for endpoint, filename in tqdm(endpoints, desc="Facebook Analytics"):
            data = make_api_request(
                endpoint,
                params=date_params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'analytics' / 'facebook' / filename
                )

    def fetch_linkedin_analytics(self):
        """Fetch LinkedIn-specific analytics - SKIPPED (not connected)"""
        logger.info("Skipping LinkedIn analytics (platform not connected)")
        pass

    def fetch_twitter_analytics(self):
        """Fetch Twitter/X-specific analytics - SKIPPED (not connected)"""
        logger.info("Skipping Twitter analytics (platform not connected)")
        pass

    def fetch_tiktok_analytics(self):
        """Fetch TikTok-specific analytics - SKIPPED (not connected)"""
        logger.info("Skipping TikTok analytics (platform not connected)")
        pass

    def fetch_youtube_analytics(self):
        """Fetch YouTube-specific analytics - SKIPPED (not connected)"""
        logger.info("Skipping YouTube analytics (platform not connected)")
        pass

    def fetch_pinterest_analytics(self):
        """Fetch Pinterest-specific analytics - SKIPPED (not connected)"""
        logger.info("Skipping Pinterest analytics (platform not connected)")
        pass

    def fetch_threads_analytics(self):
        """Fetch Threads-specific analytics - SKIPPED (not connected)"""
        logger.info("Skipping Threads analytics (platform not connected)")
        pass

    def fetch_bluesky_analytics(self):
        """Fetch Bluesky-specific analytics - SKIPPED (not connected)"""
        logger.info("Skipping Bluesky analytics (platform not connected)")
        pass

    def fetch_general_stats(self):
        """Fetch general statistics"""
        logger.info("Fetching general statistics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        # Only fetch brand summary (distribution endpoint has issues)
        data = make_api_request(
            '/v2/analytics/brand-summary/posts',
            params=date_params,
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'stats' / 'brand_summary_posts.json'
            )

    def fetch_demographic_data(self):
        """Fetch demographic data (age, gender, location) - Only connected platforms"""
        logger.info("Fetching demographic data...")

        # Only fetch for connected platforms (Instagram and Facebook)
        providers = ['instagram', 'facebook']
        date_params = get_date_range_params(self.start_date, self.end_date)

        for provider in tqdm(providers, desc="Demographics"):
            # Gender data
            data = make_api_request(
                f'/stats/gender/{provider}',
                params=date_params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'stats' / f'{provider}_gender.json'
                )

            # Age data
            data = make_api_request(
                f'/stats/age/{provider}',
                params=date_params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'stats' / f'{provider}_age.json'
                )

            # Gender-Age combined
            data = make_api_request(
                f'/stats/gender-age/{provider}',
                params=date_params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'stats' / f'{provider}_gender_age.json'
                )

            # Country data
            data = make_api_request(
                f'/stats/country/{provider}',
                params=date_params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'stats' / f'{provider}_country.json'
                )

            # City data
            data = make_api_request(
                f'/stats/city/{provider}',
                params=date_params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'stats' / f'{provider}_city.json'
                )

    def fetch_scheduled_posts(self):
        """Fetch scheduled and library posts"""
        logger.info("Fetching scheduled posts...")

        # Get scheduled posts
        data = make_api_request(
            '/v2/scheduler/posts',
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'posts' / 'scheduled_posts.json'
            )

        # Get library posts
        data = make_api_request(
            '/v2/scheduler/library/posts',
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'posts' / 'library_posts.json'
            )

    def fetch_media_library(self):
        """Fetch media library items"""
        logger.info("Fetching media library...")

        # Get images
        data = make_api_request(
            '/v2/media/images',
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'media' / 'images.json'
            )

        # Get videos
        data = make_api_request(
            '/v2/media/videos',
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'media' / 'videos.json'
            )

    def fetch_hashtag_data(self):
        """Fetch hashtag tracking data"""
        logger.info("Fetching hashtag data...")

        # Get hashtag tracking sessions
        data = make_api_request(
            '/v2/hashtags-tracker/tracking-sessions',
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'analytics' / 'hashtag_tracking_sessions.json'
            )

    def fetch_smart_links(self):
        """Fetch smart links data"""
        logger.info("Fetching smart links...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        # Get all smart links
        data = make_api_request(
            '/v2/smart-links/links',
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'analytics' / 'smart_links.json'
            )

            # Get analytics for each link
            if 'data' in data and isinstance(data['data'], list):
                for link in data['data']:
                    link_id = link.get('id')
                    if link_id:
                        # Timeline analytics
                        analytics = make_api_request(
                            f'/v2/smart-links/links/{link_id}/analytics/timeline',
                            params=date_params,
                            blog_id=self.blog_id
                        )
                        if analytics:
                            save_json(
                                analytics,
                                DATA_DIR / 'analytics' / f'smart_link_{link_id}_timeline.json'
                            )

    def fetch_all_data(self):
        """Fetch all available data from Metricool API"""
        logger.info("=" * 60)
        logger.info(f"Starting data fetch for {self.brand_name}")
        logger.info(f"Date range: {self.start_date} to {self.end_date}")
        logger.info("=" * 60)

        # First, get the blog ID
        if not self.get_blog_id():
            logger.error("Cannot proceed without blog ID")
            return False

        try:
            # Fetch all data categories
            self.fetch_brand_info()
            self.fetch_analytics_timelines()
            self.fetch_analytics_aggregation()
            self.fetch_instagram_analytics()
            self.fetch_facebook_analytics()
            self.fetch_linkedin_analytics()
            self.fetch_twitter_analytics()
            self.fetch_tiktok_analytics()
            self.fetch_youtube_analytics()
            self.fetch_pinterest_analytics()
            self.fetch_threads_analytics()
            self.fetch_bluesky_analytics()
            self.fetch_general_stats()
            self.fetch_demographic_data()
            self.fetch_scheduled_posts()
            self.fetch_media_library()
            self.fetch_hashtag_data()
            self.fetch_smart_links()

            logger.info("=" * 60)
            logger.info("Data fetch completed successfully!")
            logger.info(f"All data saved in: {DATA_DIR}")
            logger.info("=" * 60)

            # Create summary
            self.create_summary()

            return True

        except Exception as e:
            logger.error(f"Error during data fetch: {str(e)}", exc_info=True)
            return False

    def create_summary(self):
        """Create a summary of fetched data"""
        summary = {
            'brand_name': self.brand_name,
            'blog_id': self.blog_id,
            'date_range': {
                'start': self.start_date,
                'end': self.end_date
            },
            'fetch_timestamp': datetime.now().isoformat(),
            'data_directory': str(DATA_DIR),
            'files_created': []
        }

        # Count files in each directory
        for category in ['brand_info', 'analytics', 'stats', 'posts', 'media', 'reports']:
            category_dir = DATA_DIR / category
            if category_dir.exists():
                files = list(category_dir.rglob('*.json'))
                summary['files_created'].extend([str(f.relative_to(DATA_DIR)) for f in files])

        summary['total_files'] = len(summary['files_created'])

        save_json(summary, DATA_DIR / 'fetch_summary.json')
        logger.info(f"Created summary with {summary['total_files']} files")


def main():
    """Main execution function"""
    fetcher = MetricoolDataFetcher()
    success = fetcher.fetch_all_data()

    if success:
        print("\n✅ Data fetch completed successfully!")
        print(f"📁 Data saved in: {DATA_DIR}")
        print(f"📊 Check fetch_summary.json for details")
    else:
        print("\n❌ Data fetch failed. Check logs for details.")


if __name__ == '__main__':
    main()
