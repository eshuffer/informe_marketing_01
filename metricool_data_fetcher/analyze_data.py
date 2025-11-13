"""
Data Analysis Helper
Analyzes and summarizes the fetched Metricool data
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime


class MetricoolDataAnalyzer:
    """Analyzes fetched Metricool data and generates insights"""

    def __init__(self, data_dir: Path = None):
        if data_dir is None:
            data_dir = Path(__file__).parent / 'data'
        self.data_dir = data_dir

    def analyze_all(self):
        """Generate comprehensive analysis of all fetched data"""
        print("=" * 70)
        print("METRICOOL DATA ANALYSIS - SATTVICA BRAND")
        print("=" * 70)
        print()

        # Check if data directory exists
        if not self.data_dir.exists():
            print("❌ No data directory found. Please run the fetcher first.")
            return

        # Load summary
        summary_file = self.data_dir / 'fetch_summary.json'
        if summary_file.exists():
            with open(summary_file, 'r') as f:
                summary = json.load(f)
            self.print_summary(summary)

        # Analyze each category
        self.analyze_brand_info()
        self.analyze_analytics()
        self.analyze_posts()
        self.analyze_media()
        self.analyze_demographics()

    def print_summary(self, summary: dict):
        """Print fetch summary"""
        print("📊 FETCH SUMMARY")
        print("-" * 70)
        print(f"Brand: {summary.get('brand_name', 'N/A')}")
        print(f"Blog ID: {summary.get('blog_id', 'N/A')}")
        print(f"Date Range: {summary.get('date_range', {}).get('start')} to {summary.get('date_range', {}).get('end')}")
        print(f"Fetch Time: {summary.get('fetch_timestamp', 'N/A')}")
        print(f"Total Files: {summary.get('total_files', 0)}")
        print()

    def analyze_brand_info(self):
        """Analyze brand information"""
        print("🏢 BRAND INFORMATION")
        print("-" * 70)

        brand_dir = self.data_dir / 'brand_info'
        if not brand_dir.exists():
            print("No brand info found.")
            print()
            return

        # Check profiles
        profiles_file = brand_dir / 'all_profiles.json'
        if profiles_file.exists():
            with open(profiles_file, 'r') as f:
                profiles_data = json.load(f)

            # Handle both list and dict with 'data' key
            profiles = profiles_data if isinstance(profiles_data, list) else profiles_data.get('data', [])

            if profiles:
                print(f"Total Profiles/Brands: {len(profiles)}")

                # List all connected platforms
                platforms = set()
                for profile in profiles:
                    # Check various platform fields
                    for platform_key in ['instagram', 'facebook', 'linkedin', 'twitter',
                                        'tiktok', 'youtube', 'pinterest', 'threads', 'bluesky']:
                        if profile.get(platform_key):
                            platforms.add(platform_key)

                if platforms:
                    print(f"Connected Platforms: {', '.join(sorted(platforms))}")

        # Check subscription
        subscription_file = brand_dir / 'subscription.json'
        if subscription_file.exists():
            with open(subscription_file, 'r') as f:
                subscription = json.load(f)
            if 'data' in subscription and 'plan' in subscription['data']:
                print(f"Subscription Plan: {subscription['data']['plan']}")

        print()

    def analyze_analytics(self):
        """Analyze analytics data"""
        print("📈 ANALYTICS DATA")
        print("-" * 70)

        analytics_dir = self.data_dir / 'analytics'
        if not analytics_dir.exists():
            print("No analytics data found.")
            print()
            return

        # Count files per platform
        platforms = ['instagram', 'facebook', 'linkedin', 'twitter', 'tiktok',
                    'youtube', 'pinterest', 'threads', 'bluesky']

        for platform in platforms:
            platform_dir = analytics_dir / platform
            if platform_dir.exists():
                files = list(platform_dir.glob('*.json'))
                if files:
                    print(f"{platform.capitalize()}: {len(files)} data files")

                    # Try to show post count if available
                    posts_file = platform_dir / f'{platform}_posts.json'
                    if posts_file.exists():
                        try:
                            with open(posts_file, 'r') as f:
                                posts_data = json.load(f)
                            if 'data' in posts_data:
                                if isinstance(posts_data['data'], list):
                                    print(f"  └─ {len(posts_data['data'])} posts found")
                                elif isinstance(posts_data['data'], dict) and 'posts' in posts_data['data']:
                                    print(f"  └─ {len(posts_data['data']['posts'])} posts found")
                        except:
                            pass

        # Check timeline files
        timeline_files = list(analytics_dir.glob('timeline_*.json'))
        if timeline_files:
            print(f"\nTimeline Metrics: {len(timeline_files)} metrics tracked")

        print()

    def analyze_posts(self):
        """Analyze posts data"""
        print("📝 POSTS & CONTENT")
        print("-" * 70)

        posts_dir = self.data_dir / 'posts'
        if not posts_dir.exists():
            print("No posts data found.")
            print()
            return

        # Check scheduled posts
        scheduled_file = posts_dir / 'scheduled_posts.json'
        if scheduled_file.exists():
            with open(scheduled_file, 'r') as f:
                scheduled = json.load(f)
            if 'data' in scheduled and isinstance(scheduled['data'], list):
                print(f"Scheduled Posts: {len(scheduled['data'])}")

        # Check library posts
        library_file = posts_dir / 'library_posts.json'
        if library_file.exists():
            with open(library_file, 'r') as f:
                library = json.load(f)
            if 'data' in library and isinstance(library['data'], list):
                print(f"Library Posts: {len(library['data'])}")

        print()

    def analyze_media(self):
        """Analyze media library"""
        print("🎨 MEDIA LIBRARY")
        print("-" * 70)

        media_dir = self.data_dir / 'media'
        if not media_dir.exists():
            print("No media data found.")
            print()
            return

        # Check images
        images_file = media_dir / 'images.json'
        if images_file.exists():
            with open(images_file, 'r') as f:
                images = json.load(f)
            if 'data' in images and isinstance(images['data'], list):
                print(f"Images: {len(images['data'])}")

        # Check videos
        videos_file = media_dir / 'videos.json'
        if videos_file.exists():
            with open(videos_file, 'r') as f:
                videos = json.load(f)
            if 'data' in videos and isinstance(videos['data'], list):
                print(f"Videos: {len(videos['data'])}")

        print()

    def analyze_demographics(self):
        """Analyze demographic data"""
        print("👥 DEMOGRAPHICS")
        print("-" * 70)

        stats_dir = self.data_dir / 'stats'
        if not stats_dir.exists():
            print("No statistics data found.")
            print()
            return

        platforms = ['instagram', 'facebook', 'linkedin', 'tiktok']
        demographic_types = ['gender', 'age', 'country', 'city']

        available_demographics = defaultdict(list)

        for platform in platforms:
            for demo_type in demographic_types:
                demo_file = stats_dir / f'{platform}_{demo_type}.json'
                if demo_file.exists():
                    available_demographics[platform].append(demo_type)

        if available_demographics:
            for platform, demo_types in available_demographics.items():
                print(f"{platform.capitalize()}: {', '.join(demo_types)}")
        else:
            print("No demographic data found.")

        print()

    def generate_report(self):
        """Generate a detailed text report"""
        print("=" * 70)
        print("Generating detailed report...")
        print("=" * 70)

        report_lines = []
        report_lines.append("METRICOOL DATA REPORT - SATTVICA BRAND")
        report_lines.append("=" * 70)
        report_lines.append("")
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("")

        # Add file inventory
        report_lines.append("FILE INVENTORY")
        report_lines.append("-" * 70)

        for category in ['brand_info', 'analytics', 'stats', 'posts', 'media', 'reports']:
            category_dir = self.data_dir / category
            if category_dir.exists():
                files = list(category_dir.rglob('*.json'))
                report_lines.append(f"\n{category.upper().replace('_', ' ')}: {len(files)} files")
                for file in sorted(files):
                    rel_path = file.relative_to(self.data_dir)
                    size_kb = file.stat().st_size / 1024
                    report_lines.append(f"  - {rel_path} ({size_kb:.1f} KB)")

        # Save report
        report_file = self.data_dir / 'analysis_report.txt'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))

        print(f"\n✅ Detailed report saved to: {report_file}")


def main():
    """Main execution"""
    analyzer = MetricoolDataAnalyzer()
    analyzer.analyze_all()
    analyzer.generate_report()


if __name__ == '__main__':
    main()
