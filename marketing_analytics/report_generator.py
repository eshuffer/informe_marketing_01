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

            # Trends Analysis
            f.write(self._generate_trends_section(analytics_data))

            # Audience Demographics
            f.write(self._generate_demographics_section(analytics_data))

            # Best Posting Times
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
