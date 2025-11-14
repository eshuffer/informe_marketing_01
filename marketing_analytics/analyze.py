"""
Main Analytics Runner
Orchestrates data loading, analysis, AI insights generation, and reporting
"""

import logging
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from data_loader import MetricoolDataLoader
from analytics_processors import (
    EngagementAnalyzer,
    TrendAnalyzer,
    DemographicAnalyzer,
    ContentPerformanceAnalyzer
)
from ai_insights import AIInsightGenerator
from report_generator import MarkdownReportGenerator
from config import BRAND_NAME, ENABLED_PLATFORMS, REPORTS_DIR

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(REPORTS_DIR / 'analytics.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class MarketingAnalytics:
    """Main analytics orchestrator"""

    def __init__(self):
        self.loader = MetricoolDataLoader()
        self.engagement_analyzer = EngagementAnalyzer()
        self.trend_analyzer = TrendAnalyzer()
        self.demo_analyzer = DemographicAnalyzer()
        self.content_analyzer = ContentPerformanceAnalyzer()
        self.ai_generator = AIInsightGenerator()
        self.report_generator = MarkdownReportGenerator()

        self.raw_data = {}
        self.analytics_results = {}

    def run_full_analysis(self):
        """Run complete analytics pipeline"""
        logger.info("="*80)
        logger.info(f"Starting Marketing Analytics for {BRAND_NAME}")
        logger.info("="*80)

        # Step 1: Load data
        logger.info("\n📁 Step 1: Loading data...")
        self.raw_data = self.loader.load_all_data()
        summary = self.loader.get_summary_stats()
        self.analytics_results['summary'] = summary
        logger.info(f"✅ Loaded {summary['data_counts']} files")

        # Step 2: Analyze engagement
        logger.info("\n💬 Step 2: Analyzing engagement...")
        self.analyze_engagement()

        # Step 3: Analyze trends
        logger.info("\n📈 Step 3: Analyzing trends...")
        self.analyze_trends()

        # Step 4: Analyze content performance
        logger.info("\n🎨 Step 4: Analyzing content performance...")
        self.analyze_content_performance()

        # Step 5: Analyze demographics
        logger.info("\n👥 Step 5: Analyzing demographics...")
        self.analyze_demographics()

        # Step 6: Process best times
        logger.info("\n⏰ Step 6: Processing optimal posting times...")
        self.process_best_times()

        # Step 7: Create platform comparison
        logger.info("\n🏆 Step 7: Creating platform comparison...")
        self.create_platform_comparison()

        # Step 8: Generate AI insights
        logger.info("\n🤖 Step 8: Generating AI insights...")
        ai_insights = self.generate_ai_insights()

        # Step 9: Generate report
        logger.info("\n📊 Step 9: Generating report...")
        report_path = self.report_generator.generate_comprehensive_report(
            self.analytics_results,
            ai_insights
        )

        logger.info("\n" + "="*80)
        logger.info("✅ Analysis Complete!")
        logger.info(f"📄 Report saved to: {report_path}")
        logger.info("="*80)

        return report_path

    def analyze_engagement(self):
        """Analyze engagement metrics for all platforms"""
        engagement_results = {}

        for platform in ENABLED_PLATFORMS:
            logger.info(f"  Analyzing {platform} engagement...")

            # Posts
            posts_df = self.loader.get_posts_dataframe(platform, 'posts')
            if posts_df is not None:
                engagement_results[f'{platform}_posts'] = \
                    self.engagement_analyzer.analyze_platform_engagement(posts_df, platform)

            # Reels (if available)
            reels_df = self.loader.get_posts_dataframe(platform, 'reels')
            if reels_df is not None:
                engagement_results[f'{platform}_reels'] = \
                    self.engagement_analyzer.analyze_platform_engagement(reels_df, f"{platform}_reels")

        self.analytics_results['engagement'] = engagement_results

    def analyze_trends(self):
        """Analyze timeline trends"""
        trends_results = {}

        # Key metrics to analyze
        metrics_to_analyze = {
            'instagram': ['posts_count', 'posts_engagement', 'posts_reach', 'reels_count'],
            'facebook': ['posts_count', 'posts_engagement', 'page_likes']
        }

        for platform in ENABLED_PLATFORMS:
            if platform in metrics_to_analyze:
                for metric in metrics_to_analyze[platform]:
                    timeline_df = self.loader.get_timeline_dataframe(platform, metric)
                    if timeline_df is not None and not timeline_df.empty:
                        key = f"{platform}_{metric}"
                        logger.info(f"  Analyzing trend: {key}")
                        trends_results[key] = self.trend_analyzer.analyze_timeline_trend(
                            timeline_df, key
                        )

        self.analytics_results['trends'] = trends_results

    def analyze_content_performance(self):
        """Analyze content performance"""
        content_results = {}

        # Compare content types (Posts vs Reels)
        if 'instagram' in ENABLED_PLATFORMS:
            posts_df = self.loader.get_posts_dataframe('instagram', 'posts')
            reels_df = self.loader.get_posts_dataframe('instagram', 'reels')

            if posts_df is not None or reels_df is not None:
                content_results['content_type_comparison'] = \
                    self.engagement_analyzer.compare_content_types(posts_df, reels_df)

        # Top performing content
        top_content = {}
        for platform in ENABLED_PLATFORMS:
            posts_df = self.loader.get_posts_dataframe(platform, 'posts')
            if posts_df is not None:
                top_posts = self.content_analyzer.find_top_performing_content(
                    posts_df, metric='engagement_rate', top_n=10
                )
                if top_posts:
                    top_content[platform] = top_posts

        if top_content:
            content_results['top_content'] = top_content

        self.analytics_results['content_performance'] = content_results

    def analyze_demographics(self):
        """Analyze audience demographics"""
        demo_results = {}

        demo_types = ['gender', 'age', 'country', 'city']

        for platform in ENABLED_PLATFORMS:
            for demo_type in demo_types:
                key = f"{platform}_{demo_type}"
                demo_data = self.raw_data.get('stats', {}).get(key)

                if demo_data:
                    logger.info(f"  Analyzing {key}...")
                    demo_results[key] = self.demo_analyzer.analyze_demographics(
                        demo_data, demo_type
                    )

        self.analytics_results['demographics'] = demo_results

    def process_best_times(self):
        """Process optimal posting times"""
        best_times_results = {}

        for platform in ENABLED_PLATFORMS:
            times_data = self.raw_data.get('best_times', {}).get(platform)
            if times_data:
                best_times_results[platform] = times_data

        self.analytics_results['best_times'] = best_times_results

    def create_platform_comparison(self):
        """Create cross-platform comparison"""
        comparison = {}

        engagement = self.analytics_results.get('engagement', {})

        # Compare average engagement rates
        avg_engagement = {}
        total_posts = {}
        total_reach = {}

        for key, data in engagement.items():
            if isinstance(data, dict) and 'platform' in data:
                platform = data['platform']
                if platform in ENABLED_PLATFORMS:
                    avg_engagement[platform] = data.get('avg_engagement_rate', 0)
                    total_posts[platform] = data.get('total_posts', 0)
                    total_reach[platform] = data.get('total_reach', 0)

        if avg_engagement:
            comparison['avg_engagement_rate'] = avg_engagement
        if total_posts:
            comparison['total_posts'] = total_posts
        if total_reach:
            comparison['total_reach'] = total_reach

        self.analytics_results['platform_comparison'] = comparison

    def generate_ai_insights(self):
        """Generate AI-powered insights"""
        insights = {}

        # Generate comprehensive insights
        comprehensive = self.ai_generator.generate_comprehensive_insights(
            self.analytics_results
        )
        insights.update(comprehensive)

        # Generate executive summary
        exec_summary = self.ai_generator.generate_executive_summary(
            self.analytics_results
        )
        insights['executive_summary'] = exec_summary

        return insights


def main():
    """Main entry point"""
    try:
        # Create reports directory
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)

        # Run analysis
        analytics = MarketingAnalytics()
        report_path = analytics.run_full_analysis()

        print("\n" + "="*80)
        print(f"✅ SUCCESS!")
        print(f"📄 Report available at: {report_path}")
        print("="*80)

    except Exception as e:
        logger.error(f"Error during analysis: {e}", exc_info=True)
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
