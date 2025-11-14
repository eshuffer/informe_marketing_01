"""
AI-Powered Insights Generator
Uses OpenAI to generate strategic marketing insights from analytics data
"""

import logging
import json
from typing import Dict, Any, List
from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPENAI_TEMPERATURE,
    AI_CONTEXT_TEMPLATE,
    AI_INSIGHT_PROMPT_TEMPLATE,
    BRAND_NAME,
    START_DATE,
    END_DATE
)

logger = logging.getLogger(__name__)


class AIInsightGenerator:
    """Generate AI-powered marketing insights"""

    def __init__(self, api_key: str = OPENAI_API_KEY):
        if not api_key:
            logger.warning("OpenAI API key not set. AI insights will be disabled.")
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)

    def generate_comprehensive_insights(self, analytics_data: Dict[str, Any]) -> Dict[str, str]:
        """Generate comprehensive marketing insights from all analytics data"""
        if not self.client:
            return {
                'error': 'OpenAI API key not configured',
                'message': 'Set OPENAI_API_KEY environment variable to enable AI insights'
            }

        try:
            # Prepare data summary
            data_summary = self._prepare_data_summary(analytics_data)

            # Calculate date range
            from datetime import datetime
            start = datetime.fromisoformat(START_DATE)
            end = datetime.fromisoformat(END_DATE)
            days = (end - start).days

            platforms = analytics_data.get('summary', {}).get('platforms', ['instagram', 'facebook'])
            platforms_str = ', '.join(platforms)

            # Create context
            context = AI_CONTEXT_TEMPLATE.format(
                days=days,
                brand_name=BRAND_NAME,
                platforms=platforms_str
            )

            # Create prompt
            prompt = AI_INSIGHT_PROMPT_TEMPLATE.format(
                brand_name=BRAND_NAME,
                data_summary=data_summary
            )

            # Generate insights
            logger.info("Generating AI insights with OpenAI...")
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": prompt}
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=2000
            )

            insights_text = response.choices[0].message.content

            return {
                'status': 'success',
                'insights': insights_text,
                'model': OPENAI_MODEL,
                'prompt_tokens': response.usage.prompt_tokens,
                'completion_tokens': response.usage.completion_tokens,
            }

        except Exception as e:
            logger.error(f"Error generating AI insights: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def generate_specific_insights(self, topic: str, data: Dict[str, Any]) -> str:
        """Generate insights for a specific topic"""
        if not self.client:
            return "AI insights disabled - OpenAI API key not configured"

        try:
            prompt = f"""
As a social media marketing expert, analyze the following {topic} data for {BRAND_NAME}:

{json.dumps(data, indent=2, default=str)}

Provide:
1. Key observations (3-5 bullet points)
2. Strategic recommendations (2-3 actionable items)

Be specific and use the actual numbers from the data.
"""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You are an expert social media marketing analyst."},
                    {"role": "user", "content": prompt}
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=800
            )

            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"Error generating specific insights for {topic}: {e}")
            return f"Error generating insights: {str(e)}"

    def _prepare_data_summary(self, analytics_data: Dict[str, Any]) -> str:
        """Prepare a concise summary of analytics data for the AI"""
        summary_parts = []

        # Overall summary
        if 'summary' in analytics_data:
            summary_parts.append("=== OVERALL SUMMARY ===")
            summary_parts.append(json.dumps(analytics_data['summary'], indent=2, default=str))

        # Platform comparisons
        if 'platform_comparison' in analytics_data:
            summary_parts.append("\n=== PLATFORM COMPARISON ===")
            summary_parts.append(json.dumps(analytics_data['platform_comparison'], indent=2, default=str))

        # Engagement analysis
        if 'engagement' in analytics_data:
            summary_parts.append("\n=== ENGAGEMENT ANALYSIS ===")
            for platform, data in analytics_data['engagement'].items():
                summary_parts.append(f"\n{platform.upper()}:")
                summary_parts.append(json.dumps(data, indent=2, default=str))

        # Content performance
        if 'content_performance' in analytics_data:
            summary_parts.append("\n=== CONTENT PERFORMANCE ===")
            summary_parts.append(json.dumps(analytics_data['content_performance'], indent=2, default=str))

        # Trends
        if 'trends' in analytics_data:
            summary_parts.append("\n=== KEY TRENDS ===")
            # Include only top trends to avoid token limits
            top_trends = dict(list(analytics_data['trends'].items())[:5])
            summary_parts.append(json.dumps(top_trends, indent=2, default=str))

        # Demographics
        if 'demographics' in analytics_data:
            summary_parts.append("\n=== AUDIENCE DEMOGRAPHICS ===")
            summary_parts.append(json.dumps(analytics_data['demographics'], indent=2, default=str))

        # Best times
        if 'best_times' in analytics_data:
            summary_parts.append("\n=== OPTIMAL POSTING TIMES ===")
            summary_parts.append(json.dumps(analytics_data['best_times'], indent=2, default=str))

        summary_text = '\n'.join(summary_parts)

        # Truncate if too long (to stay within token limits)
        max_chars = 15000
        if len(summary_text) > max_chars:
            summary_text = summary_text[:max_chars] + "\n\n[Data truncated for brevity...]"

        return summary_text

    def generate_executive_summary(self, analytics_data: Dict[str, Any]) -> str:
        """Generate a brief executive summary"""
        if not self.client:
            return "Executive Summary: AI insights disabled - configure OpenAI API key to enable"

        try:
            # Extract key metrics
            key_metrics = self._extract_key_metrics(analytics_data)

            prompt = f"""
Create a brief executive summary (3-4 paragraphs) for {BRAND_NAME}'s social media performance
from {START_DATE} to {END_DATE}.

Key Metrics:
{json.dumps(key_metrics, indent=2, default=str)}

The summary should:
1. Highlight overall performance
2. Mention 2-3 key achievements
3. Note 1-2 areas for improvement
4. Be written for C-level executives (concise, strategic)
"""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You are a marketing analytics executive."},
                    {"role": "user", "content": prompt}
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=500
            )

            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"Error generating executive summary: {e}")
            return f"Error generating executive summary: {str(e)}"

    def _extract_key_metrics(self, analytics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract the most important metrics for executive summary"""
        key_metrics = {}

        # Total posts
        if 'summary' in analytics_data:
            key_metrics['data_overview'] = analytics_data['summary']

        # Average engagement rates
        if 'engagement' in analytics_data:
            engagement_summary = {}
            for platform, data in analytics_data['engagement'].items():
                if 'avg_engagement_rate' in data:
                    engagement_summary[platform] = {
                        'avg_engagement_rate': round(data['avg_engagement_rate'], 2),
                        'total_posts': data.get('total_posts', 0)
                    }
            if engagement_summary:
                key_metrics['engagement_rates'] = engagement_summary

        # Top performing content type
        if 'content_performance' in analytics_data:
            content_comp = analytics_data['content_performance'].get('content_type_comparison', {})
            if content_comp:
                key_metrics['content_comparison'] = content_comp

        # Growth trends
        if 'trends' in analytics_data:
            growth_metrics = {}
            for metric_name, trend_data in analytics_data['trends'].items():
                if 'growth_rate_pct' in trend_data:
                    growth_metrics[metric_name] = {
                        'growth_rate': round(trend_data['growth_rate_pct'], 1),
                        'trend': trend_data.get('trend', 'stable')
                    }
            if growth_metrics:
                key_metrics['growth_trends'] = dict(list(growth_metrics.items())[:3])

        return key_metrics
