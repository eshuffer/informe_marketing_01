"""
Report Generator
Creates comprehensive marketing analytics reports in various formats
"""

import logging
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime
import json

from config import BRAND_NAME, START_DATE, END_DATE, REPORTS_DIR

logger = logging.getLogger(__name__)


class MarkdownReportGenerator:
    """Generate markdown format reports"""

    def __init__(self, output_dir: Path = REPORTS_DIR):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_comprehensive_report(self, analytics_data: Dict[str, Any],
                                     ai_insights: Dict[str, Any]) -> Path:
        """Generate a comprehensive marketing analytics report"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = self.output_dir / f'{BRAND_NAME.lower()}_marketing_report_{timestamp}.md'

        with open(report_path, 'w', encoding='utf-8') as f:
            # Header
            f.write(self._generate_header())

            # Executive Summary (AI-generated)
            if ai_insights.get('status') == 'success':
                f.write("\n## 📊 Executive Summary\n\n")
                f.write(ai_insights.get('executive_summary', 'N/A'))
                f.write("\n\n")

            # Table of Contents
            f.write(self._generate_toc())

            # Overview
            f.write(self._generate_overview(analytics_data))

            # Platform Performance
            f.write(self._generate_platform_performance(analytics_data))

            # Engagement Analysis
            f.write(self._generate_engagement_section(analytics_data))

            # Content Performance
            f.write(self._generate_content_performance(analytics_data))

            # Enhanced Content Insights
            f.write(self._generate_enhanced_insights(analytics_data))

            # Trends Analysis (only if data exists)
            if self._has_trends_data(analytics_data):
                f.write(self._generate_trends_section(analytics_data))

            # Audience Demographics (only if data exists)
            if self._has_demographics_data(analytics_data):
                f.write(self._generate_demographics_section(analytics_data))

            # Best Posting Times (only if data exists)
            if self._has_best_times_data(analytics_data):
                f.write(self._generate_best_times_section(analytics_data))

            # AI Strategic Insights
            if ai_insights.get('status') == 'success':
                f.write("\n---\n\n")
                f.write("## 🤖 AI-Powered Strategic Insights\n\n")
                f.write(ai_insights.get('insights', 'No insights generated'))
                f.write("\n\n")

            # Recommendations
            f.write(self._generate_recommendations(analytics_data))

            # Appendix
            f.write(self._generate_appendix(analytics_data))

        logger.info(f"Report generated: {report_path}")
        return report_path

    def _generate_header(self) -> str:
        """Generate report header"""
        return f"""# {BRAND_NAME} - Social Media Marketing Analytics Report

**Report Generated:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
**Analysis Period:** {START_DATE} to {END_DATE}
**Platforms Analyzed:** Instagram, Facebook

---

"""

    def _generate_toc(self) -> str:
        """Generate table of contents"""
        return """## 📑 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [Overview](#-overview)
3. [Platform Performance](#-platform-performance-comparison)
4. [Engagement Analysis](#-engagement-analysis)
5. [Content Performance](#-content-performance)
6. [Trends Analysis](#-trends-analysis)
7. [Audience Demographics](#-audience-demographics)
8. [Best Posting Times](#-optimal-posting-times)
9. [AI Strategic Insights](#-ai-powered-strategic-insights)
10. [Recommendations](#-recommendations)
11. [Appendix](#-appendix)

---

"""

    def _generate_overview(self, data: Dict[str, Any]) -> str:
        """Generate overview section"""
        summary = data.get('summary', {})

        output = "## 📈 Overview\n\n"

        if summary:
            output += "### Key Metrics Summary\n\n"
            output += f"- **Data Files Analyzed:** {summary.get('data_counts', {}).get('timelines', 0) + summary.get('data_counts', {}).get('aggregations', 0)}\n"
            output += f"- **Platforms:** {', '.join(summary.get('platforms', []))}\n"

            if 'date_range' in summary:
                output += f"- **Period:** {summary['date_range'].get('days', 'N/A')} days\n"

            output += "\n"

        return output

    def _generate_platform_performance(self, data: Dict[str, Any]) -> str:
        """Generate platform comparison section"""
        output = "## 🏆 Platform Performance Comparison\n\n"

        comparison = data.get('platform_comparison', {})

        if comparison:
            output += "### Instagram vs Facebook\n\n"
            output += "| Metric | Instagram | Facebook |\n"
            output += "|--------|-----------|----------|\n"

            for metric, values in comparison.items():
                if isinstance(values, dict):
                    ig_val = values.get('instagram', 'N/A')
                    fb_val = values.get('facebook', 'N/A')

                    # Format numbers
                    if isinstance(ig_val, (int, float)):
                        ig_val = f"{ig_val:,.2f}" if isinstance(ig_val, float) else f"{ig_val:,}"
                    if isinstance(fb_val, (int, float)):
                        fb_val = f"{fb_val:,.2f}" if isinstance(fb_val, float) else f"{fb_val:,}"

                    output += f"| {metric.replace('_', ' ').title()} | {ig_val} | {fb_val} |\n"
        else:
            output += "*Platform comparison data not available*\n"

        output += "\n"
        return output

    def _generate_engagement_section(self, data: Dict[str, Any]) -> str:
        """Generate engagement analysis section"""
        output = "## 💬 Engagement Analysis\n\n"

        engagement = data.get('engagement', {})

        for platform, eng_data in engagement.items():
            if eng_data and 'error' not in eng_data:
                output += f"### {platform.title()}\n\n"

                output += f"- **Total Posts:** {eng_data.get('total_posts', 'N/A')}\n"
                output += f"- **Average Engagement Rate:** {eng_data.get('avg_engagement_rate', 0):.2f}%\n"
                output += f"- **Median Engagement Rate:** {eng_data.get('median_engagement_rate', 0):.2f}%\n"

                if 'total_interactions' in eng_data:
                    output += f"- **Total Interactions:** {eng_data['total_interactions']:,.0f}\n"
                if 'total_reach' in eng_data:
                    output += f"- **Total Reach:** {eng_data['total_reach']:,.0f}\n"

                # Best post
                if 'best_post' in eng_data:
                    bp = eng_data['best_post']
                    output += f"\n**Best Performing Post:**\n"
                    output += f"- Engagement Rate: {bp.get('engagement_rate', 0):.2f}%\n"
                    output += f"- Reach: {bp.get('reach', 'N/A'):,}\n" if isinstance(bp.get('reach'), (int, float)) else f"- Reach: {bp.get('reach', 'N/A')}\n"
                    if 'preview' in bp:
                        output += f"- Preview: *{bp['preview']}*\n"

                output += "\n"

        return output

    def _generate_content_performance(self, data: Dict[str, Any]) -> str:
        """Generate content performance section"""
        output = "## 🎨 Content Performance\n\n"

        content_perf = data.get('content_performance', {})

        # Content type comparison
        if 'content_type_comparison' in content_perf:
            comp = content_perf['content_type_comparison']
            output += "### Posts vs Reels Comparison\n\n"

            if 'posts' in comp:
                output += f"**Regular Posts:**\n"
                output += f"- Count: {comp['posts'].get('count', 'N/A')}\n"
                output += f"- Avg Engagement: {comp['posts'].get('avg_engagement', 0):.2f}%\n"
                output += f"- Avg Reach: {comp['posts'].get('avg_reach', 0):,.0f}\n\n"

            if 'reels' in comp:
                output += f"**Reels:**\n"
                output += f"- Count: {comp['reels'].get('count', 'N/A')}\n"
                output += f"- Avg Engagement: {comp['reels'].get('avg_engagement', 0):.2f}%\n"
                output += f"- Avg Reach: {comp['reels'].get('avg_reach', 0):,.0f}\n\n"

            if 'winner' in comp:
                output += f"**Winner:** {comp['winner'].title()} "
                output += f"(+{comp.get('performance_difference_pct', 0):.1f}% better engagement)\n\n"

        # Top performing content
        if 'top_content' in content_perf:
            output += "### Top Performing Content\n\n"
            for platform, top_posts in content_perf['top_content'].items():
                if top_posts and len(top_posts) > 0:
                    output += f"**{platform.title()} Top Posts:**\n\n"
                    for i, post in enumerate(top_posts[:5], 1):
                        output += f"{i}. **Engagement Rate:** {post.get('metric_value', 0):.2f}% | "
                        output += f"**Reach:** {post.get('reach', 'N/A')} | "
                        output += f"**Interactions:** {post.get('interactions', 'N/A')}\n"
                        if 'preview' in post:
                            output += f"   *{post['preview']}*\n"
                        output += "\n"

        return output

    def _generate_trends_section(self, data: Dict[str, Any]) -> str:
        """Generate trends analysis section"""
        output = "## 📉 Trends Analysis\n\n"

        trends = data.get('trends', {})

        if trends:
            # Show key growth trends
            output += "### Key Metrics Growth Trends\n\n"
            output += "| Metric | Total | Average | Growth Rate | Trend |\n"
            output += "|--------|-------|---------|-------------|-------|\n"

            for metric_name, trend_data in trends.items():
                if 'error' not in trend_data:
                    metric_display = metric_name.replace('_', ' ').title()
                    total = f"{trend_data.get('total', 0):,.0f}"
                    avg = f"{trend_data.get('average', 0):,.2f}"
                    growth = f"{trend_data.get('growth_rate_pct', 0):+.1f}%" if 'growth_rate_pct' in trend_data else 'N/A'
                    trend = trend_data.get('trend', 'N/A')

                    # Emoji for trend
                    trend_emoji = '📈' if trend == 'increasing' else ('📉' if trend == 'decreasing' else '➡️')

                    output += f"| {metric_display} | {total} | {avg} | {growth} | {trend_emoji} {trend} |\n"

            output += "\n"

        return output

    def _generate_demographics_section(self, data: Dict[str, Any]) -> str:
        """Generate demographics section"""
        output = "## 👥 Audience Demographics\n\n"

        demographics = data.get('demographics', {})

        for demo_type, demo_data in demographics.items():
            if demo_data and 'error' not in demo_data:
                output += f"### {demo_type.replace('_', ' ').title()}\n\n"

                if 'top_3_segments' in demo_data:
                    output += "**Top 3 Segments:**\n\n"
                    for segment in demo_data['top_3_segments']:
                        output += f"- **{segment['name']}:** {segment['percentage']:.1f}% ({segment['value']:,} users)\n"
                    output += "\n"

        return output

    def _generate_best_times_section(self, data: Dict[str, Any]) -> str:
        """Generate best posting times section"""
        output = "## ⏰ Optimal Posting Times\n\n"

        best_times = data.get('best_times', {})

        if best_times:
            for platform, times_data in best_times.items():
                if times_data:
                    output += f"### {platform.title()}\n\n"
                    output += "*Based on historical engagement patterns*\n\n"
                    output += json.dumps(times_data, indent=2)
                    output += "\n\n"

        return output

    def _generate_recommendations(self, data: Dict[str, Any]) -> str:
        """Generate recommendations section"""
        output = "## 💡 Recommendations\n\n"

        # Based on data analysis, generate recommendations
        engagement = data.get('engagement', {})
        content_perf = data.get('content_performance', {})

        output += "### Content Strategy\n\n"

        # Content type recommendation
        if 'content_type_comparison' in content_perf:
            comp = content_perf['content_type_comparison']
            if 'winner' in comp:
                winner = comp['winner']
                diff = comp.get('performance_difference_pct', 0)
                output += f"- **Focus on {winner.title()}:** They perform {diff:.1f}% better in engagement\n"

        # Engagement recommendations
        for platform, eng_data in engagement.items():
            if eng_data and 'avg_engagement_rate' in eng_data:
                avg_eng = eng_data['avg_engagement_rate']
                if avg_eng < 1.0:
                    output += f"- **{platform.title()}:** Low engagement rate ({avg_eng:.2f}%) - consider more interactive content\n"
                elif avg_eng > 5.0:
                    output += f"- **{platform.title()}:** Strong engagement rate ({avg_eng:.2f}%) - maintain current strategy\n"

        output += "\n### Posting Strategy\n\n"
        output += "- Review optimal posting times section above\n"
        output += "- Maintain consistent posting schedule\n"
        output += "- Test different content formats\n\n"

        return output

    def _has_trends_data(self, data: Dict[str, Any]) -> bool:
        """Check if trends data exists"""
        trends = data.get('trends', {})
        return bool(trends and any('error' not in v for v in trends.values()))

    def _has_demographics_data(self, data: Dict[str, Any]) -> bool:
        """Check if demographics data exists"""
        demographics = data.get('demographics', {})
        return bool(demographics and any('error' not in v for v in demographics.values()))

    def _has_best_times_data(self, data: Dict[str, Any]) -> bool:
        """Check if best times data exists and is not empty"""
        best_times = data.get('best_times', {})
        if not best_times:
            return False
        # Check if any platform has actual data (not just {"data": []})
        for platform_data in best_times.values():
            if isinstance(platform_data, dict):
                data_array = platform_data.get('data', [])
                if data_array and len(data_array) > 0:
                    return True
        return False

    def _generate_enhanced_insights(self, data: Dict[str, Any]) -> str:
        """Generate enhanced content insights section"""
        enhanced_data = data.get('enhanced_content', {})

        if not enhanced_data:
            return ""

        output = "\n---\n\n## 📊 Detailed Content Insights\n\n"

        for platform, platform_data in enhanced_data.items():
            output += f"### {platform.title()}\n\n"

            # Posting Patterns
            if 'posting_patterns' in platform_data:
                patterns = platform_data['posting_patterns']
                output += "#### 📅 Posting Patterns\n\n"

                if 'posting_frequency' in patterns:
                    freq = patterns['posting_frequency']
                    output += f"- **Posts per week:** {freq.get('posts_per_week', 0):.1f}\n"
                    output += f"- **Posts per day:** {freq.get('posts_per_day', 0):.2f}\n\n"

                if 'most_active_hours' in patterns:
                    output += "**Most Active Posting Hours:**\n"
                    for hour, count in list(patterns['most_active_hours'].items())[:3]:
                        output += f"- {hour}:00 - {count} posts\n"
                    output += "\n"

                if 'day_distribution' in patterns:
                    output += "**Posts by Day of Week:**\n"
                    days_sorted = sorted(patterns['day_distribution'].items(), key=lambda x: x[1], reverse=True)
                    for day, count in days_sorted[:5]:
                        output += f"- {day}: {count} posts\n"
                    output += "\n"

            # Engagement by Time
            if 'engagement_by_time' in platform_data:
                time_eng = platform_data['engagement_by_time']
                output += "#### ⏰ Best Times to Post (Based on Actual Performance)\n\n"

                if 'best_posting_hours' in time_eng:
                    output += "**Top Performing Hours:**\n\n"
                    output += "| Hour | Avg Engagement Rate | Avg Reach | Total Interactions |\n"
                    output += "|------|-------------------|-----------|--------------------|\n"
                    for hour, metrics in sorted(time_eng['best_posting_hours'].items())[:5]:
                        output += f"| {hour}:00 | {metrics['avg_engagement']:.2f}% | {metrics['avg_reach']:,.0f} | {metrics['total_interactions']:,} |\n"
                    output += "\n"

                if 'best_posting_days' in time_eng:
                    output += "**Top Performing Days:**\n\n"
                    output += "| Day | Avg Engagement Rate | Avg Reach |\n"
                    output += "|-----|-------------------|-----------||\n"
                    for day, metrics in time_eng['best_posting_days'].items():
                        output += f"| {day} | {metrics['avg_engagement']:.2f}% | {metrics['avg_reach']:,.0f} |\n"
                    output += "\n"

            # Content Length Analysis
            if 'content_length' in platform_data:
                length_data = platform_data['content_length']
                output += "#### 📝 Content Length Analysis\n\n"

                output += f"- **Average caption length:** {length_data.get('avg_text_length', 0):.0f} characters\n"
                output += f"- **Median caption length:** {length_data.get('median_text_length', 0):.0f} characters\n\n"

                if 'length_vs_engagement' in length_data:
                    output += "**Engagement by Content Length:**\n\n"
                    output += "| Length Category | Avg Engagement | Post Count |\n"
                    output += "|----------------|----------------|------------|\n"
                    for category, metrics in length_data['length_vs_engagement'].items():
                        output += f"| {category} | {metrics['avg_engagement']:.2f}% | {metrics['post_count']} |\n"
                    output += "\n"

            # Hashtag Analysis
            if 'hashtag_analysis' in platform_data:
                hashtag_data = platform_data['hashtag_analysis']
                output += "#### #️⃣ Hashtag Analysis\n\n"

                total_posts = hashtag_data.get('posts_with_hashtags', 0) + hashtag_data.get('posts_without_hashtags', 0)
                if total_posts > 0:
                    hashtag_pct = (hashtag_data.get('posts_with_hashtags', 0) / total_posts) * 100
                    output += f"- **Posts with hashtags:** {hashtag_data.get('posts_with_hashtags', 0)} ({hashtag_pct:.1f}%)\n"
                    output += f"- **Average hashtags per post:** {hashtag_data.get('avg_hashtags_per_post', 0):.1f}\n\n"

                if 'most_used_hashtags' in hashtag_data and hashtag_data['most_used_hashtags']:
                    output += "**Most Used Hashtags:**\n\n"
                    for i, tag_info in enumerate(hashtag_data['most_used_hashtags'][:10], 1):
                        output += f"{i}. {tag_info['hashtag']} ({tag_info['count']} times)\n"
                    output += "\n"

                if 'hashtag_count_vs_engagement' in hashtag_data:
                    output += "**Hashtag Count vs Engagement:**\n\n"
                    output += "| Number of Hashtags | Avg Engagement | Post Count |\n"
                    output += "|-------------------|----------------|------------|\n"
                    for count, metrics in sorted(hashtag_data['hashtag_count_vs_engagement'].items()):
                        output += f"| {count} | {metrics['avg_engagement']:.2f}% | {metrics['post_count']} |\n"
                    output += "\n"

            # Performance Trends
            if 'performance_trends' in platform_data:
                trends = platform_data['performance_trends']
                output += "#### 📈 Performance Trends Over Time\n\n"

                if 'growth_metrics' in trends:
                    growth = trends['growth_metrics']
                    eng_change = growth.get('engagement_rate_change', 0)
                    reach_change = growth.get('reach_change', 0)

                    trend_icon = '📈' if eng_change > 0 else '📉'
                    output += f"{trend_icon} **Engagement Trend:** {trends.get('trend', 'stable').title()}\n"
                    output += f"- Engagement rate change: {eng_change:+.1f}%\n"
                    output += f"- Reach change: {reach_change:+.1f}%\n\n"

                if 'weekly_performance' in trends:
                    output += "**Weekly Performance:**\n\n"
                    output += "| Week | Posts | Avg Engagement | Total Interactions |\n"
                    output += "|------|-------|----------------|--------------------|\n"
                    for week, metrics in list(trends['weekly_performance'].items())[-4:]:
                        output += f"| {week} | {metrics['posts']} | {metrics['avg_engagement']:.2f}% | {metrics['total_interactions']:,} |\n"
                    output += "\n"

            # Reels Patterns (if available)
            if 'reels_posting_patterns' in platform_data:
                reels_patterns = platform_data['reels_posting_patterns']
                output += "#### 🎥 Reels Posting Patterns\n\n"

                if 'posting_frequency' in reels_patterns:
                    freq = reels_patterns['posting_frequency']
                    output += f"- **Reels per week:** {freq.get('posts_per_week', 0):.1f}\n\n"

            output += "\n"

        return output

    def _generate_appendix(self, data: Dict[str, Any]) -> str:
        """Generate appendix with methodology"""
        output = "## 📋 Appendix\n\n"

        output += "### Methodology\n\n"
        output += "This report analyzes data from Metricool API covering all available metrics for the specified period.\n\n"

        output += "**Engagement Rate Calculation:**\n"
        output += "```\n"
        output += "Engagement Rate = (Total Interactions / Reach) × 100\n"
        output += "```\n\n"

        output += "**Data Sources:**\n"
        output += "- Timeline metrics (daily granularity)\n"
        output += "- Aggregated metrics\n"
        output += "- Post-level analytics\n"
        output += "- Audience demographics\n"
        output += "- Platform-specific metrics\n\n"

        output += "---\n\n"
        output += f"*Report generated by {BRAND_NAME} Marketing Analytics System*\n"

        return output
