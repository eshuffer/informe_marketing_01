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

            # Hashtag Performance (only if data exists)
            if self._has_hashtag_data(analytics_data):
                f.write(self._generate_hashtag_performance(analytics_data))

            # Top Performers vs Average
            f.write(self._generate_top_performers(analytics_data))

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

                # AI Strategic Recommendations (separate from data-based recommendations)
                if ai_insights.get('strategic_recommendations'):
                    f.write("\n---\n\n")
                    f.write("## 🎯 AI Strategic Action Plan\n\n")
                    f.write(ai_insights.get('strategic_recommendations'))
                    f.write("\n\n")

                # Show token usage and cost
                if 'tokens' in ai_insights:
                    tokens = ai_insights['tokens']
                    cost = ai_insights.get('cost_estimate', 0)
                    f.write("\n---\n\n")
                    f.write("### 💡 AI Analysis Metrics\n\n")
                    f.write(f"- **Total tokens used:** {tokens.get('prompt', 0) + tokens.get('completion', 0):,}\n")
                    f.write(f"- **Input tokens:** {tokens.get('prompt', 0):,}\n")
                    f.write(f"- **Output tokens:** {tokens.get('completion', 0):,}\n")
                    f.write(f"- **Estimated cost:** ${cost:.4f}\n\n")

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

1. [Executive Summary](#executive-summary)
2. [Overview](#overview)
3. [Platform Performance](#platform-performance-comparison)
4. [Engagement Analysis](#engagement-analysis)
5. [Content Performance](#content-performance)
6. [Hashtag Performance](#hashtag-performance)
7. [Top Performers vs Average](#top-performers-vs-average)
8. [Detailed Content Insights](#detailed-content-insights)
9. [Trends Analysis](#trends-analysis)
10. [Audience Demographics](#audience-demographics)
11. [Best Posting Times](#optimal-posting-times)
12. [AI Strategic Insights](#ai-powered-strategic-insights)
13. [AI Strategic Action Plan](#ai-strategic-action-plan)
14. [Recommendations](#recommendations)
15. [Appendix](#appendix)

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

    def _generate_hashtag_performance(self, data: Dict[str, Any]) -> str:
        """Generate hashtag performance section"""
        output = "\n---\n\n## #️⃣ Hashtag Performance\n\n"
        output += "*Analysis of hashtag usage and effectiveness*\n\n"

        content_perf = data.get('content_performance', {})
        hashtag_analysis = content_perf.get('hashtag_analysis', {})

        if not hashtag_analysis:
            return ""

        # Process each platform/content type
        for platform, hashtag_data in hashtag_analysis.items():
            if 'error' in hashtag_data:
                continue

            # Extract platform name and type (e.g., "Instagram_Posts" -> "Instagram", "Posts")
            platform_parts = platform.split('_')
            platform_name = platform_parts[0] if len(platform_parts) > 0 else platform
            content_type = platform_parts[1] if len(platform_parts) > 1 else "Content"

            output += f"### {platform_name.title()} {content_type}\n\n"

            # Overall statistics
            total_hashtags = hashtag_data.get('total_unique_hashtags', 0)
            posts_with = hashtag_data.get('posts_with_hashtags', 0)
            posts_without = hashtag_data.get('posts_without_hashtags', 0)
            avg_eng_with = hashtag_data.get('avg_engagement_with_hashtags', 0)
            avg_eng_without = hashtag_data.get('avg_engagement_without_hashtags', 0)
            hashtag_lift = hashtag_data.get('hashtag_lift', 0)

            output += "**📊 Overall Hashtag Impact:**\n\n"
            output += f"- **Total Unique Hashtags:** {total_hashtags}\n"
            output += f"- **Posts with Hashtags:** {posts_with} ({posts_with / (posts_with + posts_without) * 100:.1f}%)\n" if (posts_with + posts_without) > 0 else "- **Posts with Hashtags:** 0\n"
            output += f"- **Posts without Hashtags:** {posts_without}\n"
            output += f"- **Avg Engagement with Hashtags:** {avg_eng_with:.2f}%\n"
            output += f"- **Avg Engagement without Hashtags:** {avg_eng_without:.2f}%\n"

            # Hashtag lift indicator
            if hashtag_lift > 0:
                output += f"- **Hashtag Lift:** 🔺 +{hashtag_lift:.1f}% (hashtags boost engagement)\n\n"
            elif hashtag_lift < 0:
                output += f"- **Hashtag Lift:** 🔻 {hashtag_lift:.1f}% (hashtags reduce engagement)\n\n"
            else:
                output += f"- **Hashtag Lift:** ➡️ No significant impact\n\n"

            # Top performing hashtags
            hashtag_performance = hashtag_data.get('hashtag_performance', [])
            if hashtag_performance and len(hashtag_performance) > 0:
                output += "**🏆 Top 10 Hashtags by Engagement:**\n\n"
                output += "| Rank | Hashtag | Uses | Avg Engagement | Avg Reach | Avg Interactions |\n"
                output += "|------|---------|------|----------------|-----------|------------------|\n"

                for i, hashtag in enumerate(hashtag_performance[:10], 1):
                    medal = ""
                    if i == 1:
                        medal = "🥇 "
                    elif i == 2:
                        medal = "🥈 "
                    elif i == 3:
                        medal = "🥉 "

                    tag_name = hashtag.get('hashtag', '')
                    usage = hashtag.get('usage_count', 0)
                    avg_eng = hashtag.get('avg_engagement_rate', 0)
                    avg_reach = hashtag.get('avg_reach', 0)
                    avg_int = hashtag.get('avg_interactions', 0)

                    output += f"| {medal}#{i} | {tag_name} | {usage} | {avg_eng:.2f}% | {avg_reach:,.0f} | {avg_int:,.1f} |\n"

                output += "\n"

                # Key insights
                if len(hashtag_performance) >= 3:
                    top_3_avg_eng = sum(h.get('avg_engagement_rate', 0) for h in hashtag_performance[:3]) / 3
                    most_used = max(hashtag_performance, key=lambda x: x.get('usage_count', 0))

                    output += "**💡 Key Insights:**\n\n"
                    output += f"- Top 3 hashtags average {top_3_avg_eng:.2f}% engagement\n"
                    output += f"- Most used hashtag: {most_used.get('hashtag', 'N/A')} ({most_used.get('usage_count', 0)} times)\n"

                    if avg_eng_with > avg_eng_without:
                        output += f"- ✅ **Recommendation:** Continue using hashtags - they improve engagement by {hashtag_lift:.1f}%\n"
                    elif avg_eng_without > avg_eng_with:
                        output += f"- ⚠️ **Recommendation:** Review hashtag strategy - posts without hashtags perform {abs(hashtag_lift):.1f}% better\n"

                    output += "\n"

            output += "---\n\n"

        return output

    def _generate_top_performers(self, data: Dict[str, Any]) -> str:
        """Generate top performers vs average comparison section"""
        output = "\n---\n\n## 🏅 Top Performers vs Average\n\n"
        output += "*Detailed comparison of best-performing content against period averages*\n\n"

        engagement = data.get('engagement', {})
        content_perf = data.get('content_performance', {})

        # Extract averages from content type comparison
        content_type_comp = content_perf.get('content_type_comparison', {})
        posts_avg_engagement = content_type_comp.get('posts', {}).get('avg_engagement', 0)
        posts_avg_reach = content_type_comp.get('posts', {}).get('avg_reach', 0)
        reels_avg_engagement = content_type_comp.get('reels', {}).get('avg_engagement', 0)
        reels_avg_reach = content_type_comp.get('reels', {}).get('avg_reach', 0)

        # Get top content from content_performance
        top_content = content_perf.get('top_content', {})

        # Process each platform
        for platform, top_posts in top_content.items():
            if not top_posts or len(top_posts) == 0:
                continue

            # Extract platform name and content type (e.g., "Instagram_Posts" -> "Instagram", "Posts")
            platform_parts = platform.split('_')
            platform_name = platform_parts[0] if len(platform_parts) > 0 else platform

            output += f"### {platform_name.title()}\n\n"

            # Separate posts and reels based on platform naming or type
            # Assuming platform names like "Instagram_Posts" and "Instagram_Reels"
            is_posts = 'posts' in platform.lower() or 'post' in platform.lower()
            is_reels = 'reels' in platform.lower() or 'reel' in platform.lower()

            # Get engagement data for this platform to calculate total interactions average
            platform_eng = engagement.get(platform, {})
            avg_interactions = 0
            if 'total_interactions' in platform_eng and 'total_posts' in platform_eng:
                if platform_eng['total_posts'] > 0:
                    avg_interactions = platform_eng['total_interactions'] / platform_eng['total_posts']

            # Determine which averages to use
            if is_posts:
                comparison_avg_engagement = posts_avg_engagement
                comparison_avg_reach = posts_avg_reach
                content_type_name = "Posts"
            elif is_reels:
                comparison_avg_engagement = reels_avg_engagement
                comparison_avg_reach = reels_avg_reach
                content_type_name = "Reels"
            else:
                # Use platform-specific averages if available
                comparison_avg_engagement = platform_eng.get('avg_engagement_rate', 0)
                comparison_avg_reach = platform_eng.get('total_reach', 0) / platform_eng.get('total_posts', 1) if platform_eng.get('total_posts', 0) > 0 else 0
                content_type_name = "Content"

            # Show top 3
            output += f"#### 🥇 Top 3 {content_type_name}\n\n"
            output += "| Rank | Title | Date | Type | Engagement | Reach | Interactions | vs Avg Eng | Link |\n"
            output += "|------|-------|------|------|------------|-------|--------------|------------|------|\n"

            for i, post in enumerate(top_posts[:3], 1):
                eng_rate = post.get('metric_value', 0)
                reach = post.get('reach', 0) if isinstance(post.get('reach'), (int, float)) else 0
                interactions = post.get('interactions', 0) if isinstance(post.get('interactions'), (int, float)) else 0

                # Get title (truncate if too long)
                title = post.get('title', 'Untitled')
                if len(title) > 50:
                    title = title[:47] + "..."

                # Get date (format nicely)
                date_str = post.get('date', 'N/A')
                if date_str != 'N/A' and len(date_str) > 10:
                    # Try to format date nicely (YYYY-MM-DD HH:MM -> MM/DD)
                    try:
                        date_str = date_str[:10]  # Get just YYYY-MM-DD part
                        parts = date_str.split('-')
                        if len(parts) == 3:
                            date_str = f"{parts[1]}/{parts[2]}"  # MM/DD
                    except:
                        pass

                # Get content type
                content_type_display = post.get('content_type', content_type_name)

                # Calculate differences
                eng_diff = ((eng_rate - comparison_avg_engagement) / comparison_avg_engagement * 100) if comparison_avg_engagement > 0 else 0

                # Format differences with + or -
                eng_diff_str = f"+{eng_diff:.1f}%" if eng_diff >= 0 else f"{eng_diff:.1f}%"

                # Medal emojis
                medal = "🥇" if i == 1 else ("🥈" if i == 2 else "🥉")

                # Create anchor ID for this post
                anchor_id = f"post-{platform.lower().replace('_', '-')}-{i}"

                # Create link - use external URL if available, otherwise link to detail section
                if 'url' in post and post['url'] != 'N/A':
                    link_md = f"[🔗]({post['url']})"
                elif 'shortcode' in post and 'instagram' in platform.lower():
                    # Construct Instagram URL from shortcode
                    link_md = f"[🔗](https://www.instagram.com/p/{post['shortcode']}/)"
                else:
                    # Link to detail section within report
                    link_md = f"[📝](#{anchor_id})"

                output += f"| {medal} #{i} | {title} | {date_str} | {content_type_display} | {eng_rate:.2f}% | {reach:,} | {interactions:,} | {eng_diff_str} | {link_md} |\n"

            output += "\n"

            # Show detailed information for top 3
            has_content = any('preview' in post or 'full_text' in post for post in top_posts[:3])
            if has_content:
                output += "**📋 Detailed Content Information:**\n\n"
                for i, post in enumerate(top_posts[:3], 1):
                    medal = "🥇" if i == 1 else ("🥈" if i == 2 else "🥉")
                    anchor_id = f"post-{platform.lower().replace('_', '-')}-{i}"

                    # Add anchor for internal linking
                    output += f'<a id="{anchor_id}"></a>\n\n'

                    # Title with content type indicator
                    content_type_display = post.get('content_type', content_type_name)
                    title = post.get('title', f'Post #{i}')
                    output += f"{medal} **{title}** ({content_type_display})\n\n"

                    # Add date if available
                    if 'date' in post:
                        output += f"- **Posted:** {post['date']}\n"

                    # Add title if separate from above
                    if 'title' in post and post.get('title') != title:
                        output += f"- **Title:** {post['title']}\n"

                    # Add comprehensive metrics
                    eng_rate = post.get('metric_value', 0)
                    reach = post.get('reach', 'N/A')
                    interactions = post.get('interactions', 'N/A')
                    likes = post.get('likes', 'N/A')
                    comments = post.get('comments', 'N/A')
                    shares = post.get('shares', 'N/A')
                    saves = post.get('saves', 'N/A')

                    output += f"- **Engagement Rate:** {eng_rate:.2f}%\n"
                    if isinstance(reach, (int, float)) and reach != 'N/A':
                        output += f"- **Reach:** {reach:,}\n"
                    if isinstance(interactions, (int, float)) and interactions != 'N/A':
                        output += f"- **Total Interactions:** {interactions:,}\n"

                    # Detailed metrics breakdown
                    metrics_line = []
                    if isinstance(likes, (int, float)) and likes != 'N/A' and likes > 0:
                        metrics_line.append(f"❤️ {likes:,} likes")
                    if isinstance(comments, (int, float)) and comments != 'N/A' and comments > 0:
                        metrics_line.append(f"💬 {comments:,} comments")
                    if isinstance(shares, (int, float)) and shares != 'N/A' and shares > 0:
                        metrics_line.append(f"🔄 {shares:,} shares")
                    if isinstance(saves, (int, float)) and saves != 'N/A' and saves > 0:
                        metrics_line.append(f"🔖 {saves:,} saves")

                    if metrics_line:
                        output += f"- **Details:** {' | '.join(metrics_line)}\n"

                    # Add link if available
                    if 'url' in post and post['url'] != 'N/A':
                        output += f"- **Link:** [View Post]({post['url']})\n"
                    elif 'shortcode' in post and 'instagram' in platform.lower():
                        ig_url = f"https://www.instagram.com/p/{post['shortcode']}/"
                        output += f"- **Link:** [View on Instagram]({ig_url})\n"

                    # Add content
                    if 'full_text' in post:
                        full_text = post['full_text']
                        output += f"\n**Caption:**\n\n> {full_text[:500]}\n\n"
                        if len(full_text) > 500:
                            output += f"*[Caption truncated - {len(full_text)} characters total]*\n\n"
                    elif 'preview' in post:
                        output += f"\n**Caption Preview:**\n\n> {post['preview']}\n\n"

                    output += "---\n\n"

            # Add period averages for reference
            output += f"**Period Averages for {content_type_name}:**\n"
            output += f"- Average Engagement Rate: {comparison_avg_engagement:.2f}%\n"
            output += f"- Average Reach: {comparison_avg_reach:,.0f}\n"
            if avg_interactions > 0:
                output += f"- Average Interactions: {avg_interactions:,.0f}\n"
            output += "\n"

            # Add key insights
            if len(top_posts) >= 3:
                top_3_avg_eng = sum(post.get('metric_value', 0) for post in top_posts[:3]) / 3
                performance_multiplier = top_3_avg_eng / comparison_avg_engagement if comparison_avg_engagement > 0 else 0

                output += f"**Key Insight:** Top 3 {content_type_name.lower()} average {top_3_avg_eng:.2f}% engagement, "
                output += f"performing **{performance_multiplier:.1f}x** better than the period average.\n\n"

        if not top_content:
            output += "*No top performer data available for this period.*\n\n"

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

    def _has_hashtag_data(self, data: Dict[str, Any]) -> bool:
        """Check if hashtag data exists"""
        content_perf = data.get('content_performance', {})
        hashtag_analysis = content_perf.get('hashtag_analysis', {})
        return bool(hashtag_analysis and any('error' not in v for v in hashtag_analysis.values()))

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
