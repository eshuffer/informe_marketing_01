"""
Data Loader Module
Loads and organizes JSON data from Metricool fetcher for analysis
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd

from config import DATA_DIR, BRAND_NAME

logger = logging.getLogger(__name__)


class MetricoolDataLoader:
    """Load and organize Metricool data for analytics"""

    def __init__(self, data_dir: Path = DATA_DIR):
        self.data_dir = Path(data_dir)
        self.raw_data = {}
        self.processed_data = {}

    def load_json(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Load a single JSON file"""
        try:
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                logger.warning(f"File not found: {file_path}")
                return None
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error in {file_path}: {e}")
            return None
        except Exception as e:
            logger.error(f"Error loading {file_path}: {e}")
            return None

    def load_all_data(self) -> Dict[str, Any]:
        """Load all JSON data files"""
        logger.info("Loading all data files...")

        # Brand info
        self.raw_data['brand_info'] = {
            'profile': self.load_json(self.data_dir / 'brand_info' / 'sattvica_profile.json'),
            'all_profiles': self.load_json(self.data_dir / 'brand_info' / 'all_profiles.json'),
            'subscription': self.load_json(self.data_dir / 'brand_info' / 'subscription.json'),
            'settings': self.load_json(self.data_dir / 'brand_info' / 'brand_settings.json'),
            'platform_status': self.load_json(self.data_dir / 'brand_info' / 'platform_status.json'),
            'last_syncs': self.load_json(self.data_dir / 'brand_info' / 'last_syncs.json'),
        }

        # Timelines
        self.raw_data['timelines'] = self._load_directory(
            self.data_dir / 'analytics' / 'timelines'
        )

        # Aggregations
        self.raw_data['aggregations'] = self._load_directory(
            self.data_dir / 'analytics' / 'aggregations'
        )

        # Platform analytics
        self.raw_data['instagram'] = self._load_directory(
            self.data_dir / 'analytics' / 'instagram'
        )
        self.raw_data['facebook'] = self._load_directory(
            self.data_dir / 'analytics' / 'facebook'
        )

        # Stats
        self.raw_data['stats'] = self._load_directory(
            self.data_dir / 'stats'
        )

        # Posts
        self.raw_data['posts'] = {
            'scheduled': self.load_json(self.data_dir / 'posts' / 'scheduled_posts.json'),
            'library': self.load_json(self.data_dir / 'posts' / 'library_posts.json'),
        }

        # Media
        self.raw_data['media'] = {
            'images': self.load_json(self.data_dir / 'media' / 'images.json'),
            'videos': self.load_json(self.data_dir / 'media' / 'videos.json'),
        }

        # Other analytics
        self.raw_data['hashtags'] = self.load_json(
            self.data_dir / 'analytics' / 'hashtag_tracking_sessions.json'
        )
        self.raw_data['smart_links'] = self.load_json(
            self.data_dir / 'analytics' / 'smart_links.json'
        )
        self.raw_data['best_times'] = {
            'instagram': self.load_json(self.data_dir / 'analytics' / 'instagram_best_times.json'),
            'facebook': self.load_json(self.data_dir / 'analytics' / 'facebook_best_times.json'),
        }

        logger.info("All data loaded successfully")
        return self.raw_data

    def _load_directory(self, dir_path: Path) -> Dict[str, Any]:
        """Load all JSON files from a directory"""
        data = {}
        if not dir_path.exists():
            logger.warning(f"Directory not found: {dir_path}")
            return data

        for json_file in dir_path.glob('*.json'):
            key = json_file.stem  # filename without extension
            data[key] = self.load_json(json_file)

        return data

    def get_timeline_dataframe(self, platform: str, metric: str) -> Optional[pd.DataFrame]:
        """Convert timeline data to pandas DataFrame"""
        key = f"{platform}_{metric}_timeline"
        timeline_data = self.raw_data.get('timelines', {}).get(key)

        if not timeline_data or 'data' not in timeline_data:
            logger.warning(f"No timeline data found for {key}")
            return None

        try:
            df = pd.DataFrame(timeline_data['data'])
            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                df = df.sort_values('date')
            return df
        except Exception as e:
            logger.error(f"Error creating DataFrame for {key}: {e}")
            return None

    def get_posts_dataframe(self, platform: str, post_type: str = 'posts') -> Optional[pd.DataFrame]:
        """Convert posts data to pandas DataFrame"""
        key = f"{platform}_{post_type}"
        posts_data = self.raw_data.get(platform, {}).get(key)

        if not posts_data or 'data' not in posts_data:
            logger.warning(f"No posts data found for {key}")
            return None

        try:
            df = pd.DataFrame(posts_data['data'])
            # Convert date fields if present
            date_fields = ['publishDate', 'createdAt', 'date', 'timestamp']
            for field in date_fields:
                if field in df.columns:
                    df[field] = pd.to_datetime(df[field], errors='coerce')
            return df
        except Exception as e:
            logger.error(f"Error creating DataFrame for {key}: {e}")
            return None

    def get_summary_stats(self) -> Dict[str, Any]:
        """Get summary statistics from loaded data"""
        summary = {
            'brand': BRAND_NAME,
            'data_loaded': True,
            'platforms': [],
            'date_range': {},
            'data_counts': {}
        }

        # Platform status
        platform_status = self.raw_data.get('brand_info', {}).get('platform_status', {})
        if platform_status:
            summary['platforms'] = platform_status.get('enabled_in_config', [])

        # Count data files
        summary['data_counts'] = {
            'timelines': len(self.raw_data.get('timelines', {})),
            'aggregations': len(self.raw_data.get('aggregations', {})),
            'instagram_files': len(self.raw_data.get('instagram', {})),
            'facebook_files': len(self.raw_data.get('facebook', {})),
            'stats_files': len(self.raw_data.get('stats', {})),
        }

        # Get date range from fetch summary
        fetch_summary_path = self.data_dir / 'fetch_summary.json'
        if fetch_summary_path.exists():
            fetch_summary = self.load_json(fetch_summary_path)
            if fetch_summary:
                start_date = fetch_summary.get('start_date')
                end_date = fetch_summary.get('end_date')

                summary['date_range'] = {
                    'start': start_date,
                    'end': end_date,
                }

                # Calculate days if both dates are valid strings
                if isinstance(start_date, str) and isinstance(end_date, str):
                    try:
                        summary['date_range']['days'] = (
                            datetime.fromisoformat(end_date) -
                            datetime.fromisoformat(start_date)
                        ).days
                    except (ValueError, TypeError) as e:
                        logger.warning(f"Could not parse dates: {e}")

        return summary
