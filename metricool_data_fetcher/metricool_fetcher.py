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
        """Fetch timeline analytics for Instagram and Facebook"""
        logger.info("Fetching timeline analytics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        # Define metrics for Instagram
        instagram_metrics = {
            'posts_count': ('instagram', 'count', 'posts'),
            'posts_interactions': ('instagram', 'interactions', 'posts'),
            'posts_engagement': ('instagram', 'engagement', 'posts'),
            'posts_reach': ('instagram', 'reach', 'posts'),
            'posts_impressions': ('instagram', 'impressions', 'posts'),
            'posts_likes': ('instagram', 'likes', 'posts'),
            'posts_comments': ('instagram', 'comments', 'posts'),
            'posts_saves': ('instagram', 'saves', 'posts'),
            'reels_count': ('instagram', 'count', 'reels'),
            'reels_likes': ('instagram', 'likes', 'reels'),
            'reels_comments': ('instagram', 'comments', 'reels'),
            'reels_engagement': ('instagram', 'engagement', 'reels'),
            'reels_reach': ('instagram', 'reach', 'reels'),
            'reels_videoviews': ('instagram', 'videoviews', 'reels'),
        }

        # Define metrics for Facebook
        facebook_metrics = {
            'posts_count': ('facebook', 'count', 'posts'),
            'posts_interactions': ('facebook', 'interactions', 'posts'),
            'posts_engagement': ('facebook', 'engagement', 'posts'),
            'posts_impressions': ('facebook', 'impressions', 'posts'),
            'posts_clicks': ('facebook', 'clicks', 'posts'),
            'posts_comments': ('facebook', 'comments', 'posts'),
            'posts_shares': ('facebook', 'shares', 'posts'),
            'posts_reactions': ('facebook', 'reactions', 'posts'),
            'reels_count': ('facebook', 'count', 'reels'),
            'reels_engagement': ('facebook', 'engagement', 'reels'),
            'page_likes': ('facebook', 'likes', 'account'),
            'page_follows': ('facebook', 'pageFollows', 'account'),
            'page_impressions': ('facebook', 'pageImpressions', 'account'),
        }

        # Fetch Instagram timelines
        for metric_name, (network, metric, subject) in tqdm(instagram_metrics.items(), desc="Instagram Timelines"):
            params = date_params.copy()
            params['network'] = network
            params['metric'] = metric
            params['subject'] = subject

            data = make_api_request(
                '/v2/analytics/timelines',
                params=params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'analytics' / 'timelines' / f'instagram_{metric_name}_timeline.json'
                )

        # Fetch Facebook timelines
        for metric_name, (network, metric, subject) in tqdm(facebook_metrics.items(), desc="Facebook Timelines"):
            params = date_params.copy()
            params['network'] = network
            params['metric'] = metric
            params['subject'] = subject

            data = make_api_request(
                '/v2/analytics/timelines',
                params=params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'analytics' / 'timelines' / f'facebook_{metric_name}_timeline.json'
                )

    def fetch_analytics_aggregation(self):
        """Fetch aggregated analytics for Instagram and Facebook"""
        logger.info("Fetching aggregation analytics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        # Define metrics for aggregation (total counts/sums for the period)
        aggregation_metrics = {
            # Instagram
            'instagram_posts_interactions': ('instagram', 'interactions', 'posts'),
            'instagram_posts_engagement': ('instagram', 'engagement', 'posts'),
            'instagram_posts_reach': ('instagram', 'reach', 'posts'),
            'instagram_reels_engagement': ('instagram', 'engagement', 'reels'),
            'instagram_reels_reach': ('instagram', 'reach', 'reels'),
            # Facebook
            'facebook_posts_interactions': ('facebook', 'interactions', 'posts'),
            'facebook_posts_engagement': ('facebook', 'engagement', 'posts'),
            'facebook_posts_impressions': ('facebook', 'impressions', 'posts'),
            'facebook_reels_engagement': ('facebook', 'engagement', 'reels'),
        }

        for metric_name, (network, metric, subject) in tqdm(aggregation_metrics.items(), desc="Aggregations"):
            params = date_params.copy()
            params['network'] = network
            params['metric'] = metric
            params['subject'] = subject

            data = make_api_request(
                '/v2/analytics/aggregation',
                params=params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'analytics' / 'aggregations' / f'{metric_name}_aggregation.json'
                )

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
        """Fetch LinkedIn-specific analytics"""
        logger.info("Fetching LinkedIn analytics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        endpoints = [
            ('/v2/analytics/posts/linkedin', 'linkedin_posts.json'),
            ('/v2/analytics/newsletters/linkedin', 'linkedin_newsletters.json'),
        ]

        for endpoint, filename in tqdm(endpoints, desc="LinkedIn Analytics"):
            data = make_api_request(
                endpoint,
                params=date_params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'analytics' / 'linkedin' / filename
                )

    def fetch_twitter_analytics(self):
        """Fetch Twitter/X-specific analytics - SKIPPED (not connected)"""
        logger.info("Skipping Twitter analytics (platform not connected)")
        pass

    def fetch_tiktok_analytics(self):
        """Fetch TikTok-specific analytics"""
        logger.info("Fetching TikTok analytics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        data = make_api_request(
            '/v2/analytics/posts/tiktok',
            params=date_params,
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'analytics' / 'tiktok' / 'tiktok_posts.json'
            )

    def fetch_youtube_analytics(self):
        """Fetch YouTube-specific analytics - SKIPPED (not connected)"""
        logger.info("Skipping YouTube analytics (platform not connected)")
        pass

    def fetch_pinterest_analytics(self):
        """Fetch Pinterest-specific analytics"""
        logger.info("Fetching Pinterest analytics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        data = make_api_request(
            '/v2/analytics/posts/pinterest',
            params=date_params,
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'analytics' / 'pinterest' / 'pinterest_posts.json'
            )

    def fetch_threads_analytics(self):
        """Fetch Threads-specific analytics"""
        logger.info("Fetching Threads analytics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        data = make_api_request(
            '/v2/analytics/posts/threads',
            params=date_params,
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'analytics' / 'threads' / 'threads_posts.json'
            )

    def fetch_bluesky_analytics(self):
        """Fetch Bluesky-specific analytics"""
        logger.info("Fetching Bluesky analytics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        data = make_api_request(
            '/v2/analytics/posts/bluesky',
            params=date_params,
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'analytics' / 'bluesky' / 'bluesky_posts.json'
            )

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

    def fetch_best_posting_times(self):
        """Fetch best posting times for each platform"""
        logger.info("Fetching best posting times...")

        providers = ['instagram', 'facebook', 'linkedin', 'twitter', 'tiktok', 'pinterest', 'threads']

        for provider in tqdm(providers, desc="Best Times"):
            data = make_api_request(
                f'/v2/scheduler/besttimes/{provider}',
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'analytics' / f'{provider}_best_times.json'
                )

    def fetch_traffic_sources(self):
        """Fetch traffic source data for connected platforms"""
        logger.info("Fetching traffic sources...")

        date_params = get_date_range_params(self.start_date, self.end_date)
        providers = ['instagram', 'facebook']

        for provider in tqdm(providers, desc="Traffic Sources"):
            data = make_api_request(
                f'/stats/trafficsource/{provider}',
                params=date_params,
                blog_id=self.blog_id
            )
            if data:
                save_json(
                    data,
                    DATA_DIR / 'stats' / f'{provider}_traffic_source.json'
                )

    def fetch_general_posts_stats(self):
        """Fetch general posts statistics across all platforms"""
        logger.info("Fetching general posts statistics...")

        date_params = get_date_range_params(self.start_date, self.end_date)

        data = make_api_request(
            '/stats/posts',
            params=date_params,
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'stats' / 'all_posts_stats.json'
            )

    def fetch_profile_sync_info(self):
        """Fetch profile last sync information"""
        logger.info("Fetching profile sync information...")

        data = make_api_request(
            '/profile/lastsyncs',
            blog_id=self.blog_id
        )
        if data:
            save_json(
                data,
                DATA_DIR / 'brand_info' / 'last_syncs.json'
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
        sessions_data = make_api_request(
            '/v2/hashtags-tracker/tracking-sessions',
            blog_id=self.blog_id
        )
        if sessions_data:
            save_json(
                sessions_data,
                DATA_DIR / 'analytics' / 'hashtag_tracking_sessions.json'
            )

            # For each tracking session, get detailed data
            if 'data' in sessions_data and isinstance(sessions_data['data'], list):
                for session in tqdm(sessions_data['data'], desc="Hashtag Sessions"):
                    session_id = session.get('id')
                    if session_id:
                        # Get consolidation data
                        consolidation = make_api_request(
                            f'/v2/hashtags-tracker/tracking-sessions/{session_id}/consolidations',
                            blog_id=self.blog_id
                        )
                        if consolidation:
                            save_json(
                                consolidation,
                                DATA_DIR / 'analytics' / 'hashtags' / f'session_{session_id}_consolidation.json'
                            )

                        # Get distribution data
                        distribution = make_api_request(
                            f'/v2/hashtags-tracker/tracking-sessions/{session_id}/distribution',
                            blog_id=self.blog_id
                        )
                        if distribution:
                            save_json(
                                distribution,
                                DATA_DIR / 'analytics' / 'hashtags' / f'session_{session_id}_distribution.json'
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
                for link in tqdm(data['data'], desc="Smart Links Analytics"):
                    link_id = link.get('id')
                    if link_id:
                        # Timeline analytics
                        timeline_analytics = make_api_request(
                            f'/v2/smart-links/links/{link_id}/analytics/timeline',
                            params=date_params,
                            blog_id=self.blog_id
                        )
                        if timeline_analytics:
                            save_json(
                                timeline_analytics,
                                DATA_DIR / 'analytics' / 'smart_links' / f'link_{link_id}_timeline.json'
                            )

                        # Buttons analytics
                        buttons_analytics = make_api_request(
                            f'/v2/smart-links/links/{link_id}/analytics/buttons',
                            params=date_params,
                            blog_id=self.blog_id
                        )
                        if buttons_analytics:
                            save_json(
                                buttons_analytics,
                                DATA_DIR / 'analytics' / 'smart_links' / f'link_{link_id}_buttons.json'
                            )

                        # Images analytics
                        images_analytics = make_api_request(
                            f'/v2/smart-links/links/{link_id}/analytics/images',
                            params=date_params,
                            blog_id=self.blog_id
                        )
                        if images_analytics:
                            save_json(
                                images_analytics,
                                DATA_DIR / 'analytics' / 'smart_links' / f'link_{link_id}_images.json'
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
            self.fetch_profile_sync_info()
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
            self.fetch_general_posts_stats()
            self.fetch_demographic_data()
            self.fetch_traffic_sources()
            self.fetch_best_posting_times()
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
