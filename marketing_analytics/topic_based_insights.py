"""
Topic-Based AI Insights Generator
Groups data by topic and generates focused, deep insights for each area
"""

import logging
from typing import Dict, Any, List
from openai import OpenAI
import json

from config import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPENAI_TEMPERATURE,
    BRAND_NAME,
    START_DATE,
    END_DATE
)

logger = logging.getLogger(__name__)


class TopicBasedInsightsGenerator:
    """Generate deep insights by analyzing data topics separately"""

    def __init__(self, api_key: str = OPENAI_API_KEY):
        if not api_key:
            logger.warning("OpenAI API key not set. AI insights will be disabled.")
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)

        # Define topic groups
        self.topics = {
            'engagement_performance': {
                'name': 'Engagement & Performance Analysis',
                'description': 'Post performance, engagement rates, reach, and interactions',
                'data_keys': ['engagement', 'content_performance', 'platform_comparison']
            },
            'content_strategy': {
                'name': 'Content Strategy Insights',
                'description': 'Hashtags, content length, posting patterns, and format analysis',
                'data_keys': ['enhanced_content']
            },
            'audience_behavior': {
                'name': 'Audience Behavior & Timing',
                'description': 'Best posting times, audience activity patterns, demographics',
                'data_keys': ['enhanced_content', 'demographics', 'best_times']
            },
            'growth_trends': {
                'name': 'Growth & Trend Analysis',
                'description': 'Performance over time, weekly trends, growth metrics',
                'data_keys': ['trends', 'enhanced_content']
            },
            'platform_optimization': {
                'name': 'Platform-Specific Optimization',
                'description': 'Instagram vs Facebook performance, platform-specific strategies',
                'data_keys': ['platform_comparison', 'engagement', 'enhanced_content']
            }
        }

    def generate_all_topic_insights(self, analytics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate insights for all topics"""
        if not self.client:
            return {
                'error': 'OpenAI API key not configured',
                'message': 'Set OPENAI_API_KEY environment variable to enable AI insights'
            }

        logger.info("Generating topic-based AI insights...")

        all_insights = {
            'topics': {},
            'executive_summary': '',
            'strategic_recommendations': '',
            'status': 'success'
        }

        total_tokens = {'prompt': 0, 'completion': 0}

        # Generate insights for each topic
        for topic_id, topic_config in self.topics.items():
            logger.info(f"  Analyzing: {topic_config['name']}")

            topic_data = self._extract_topic_data(analytics_data, topic_config['data_keys'])

            if topic_data:
                insights = self._generate_topic_insights(
                    topic_id,
                    topic_config['name'],
                    topic_config['description'],
                    topic_data
                )

                if insights.get('status') == 'success':
                    all_insights['topics'][topic_id] = {
                        'name': topic_config['name'],
                        'insights': insights['content'],
                        'tokens': insights.get('tokens', {})
                    }
                    total_tokens['prompt'] += insights.get('tokens', {}).get('prompt', 0)
                    total_tokens['completion'] += insights.get('tokens', {}).get('completion', 0)

        # Generate executive summary based on all topic insights
        if all_insights['topics']:
            logger.info("  Generating executive summary...")
            exec_summary = self._generate_executive_summary(all_insights['topics'], analytics_data)
            if exec_summary.get('status') == 'success':
                all_insights['executive_summary'] = exec_summary['content']
                total_tokens['prompt'] += exec_summary.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += exec_summary.get('tokens', {}).get('completion', 0)

            # Generate strategic recommendations
            logger.info("  Generating strategic recommendations...")
            recommendations = self._generate_strategic_recommendations(all_insights['topics'], analytics_data)
            if recommendations.get('status') == 'success':
                all_insights['strategic_recommendations'] = recommendations['content']
                total_tokens['prompt'] += recommendations.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += recommendations.get('tokens', {}).get('completion', 0)

        all_insights['total_tokens'] = total_tokens
        all_insights['total_cost_estimate'] = self._estimate_cost(total_tokens)

        logger.info(f"✓ Generated insights for {len(all_insights['topics'])} topics")
        logger.info(f"  Total tokens: {total_tokens['prompt'] + total_tokens['completion']:,}")
        logger.info(f"  Estimated cost: ${all_insights['total_cost_estimate']:.4f}")

        return all_insights

    def _extract_topic_data(self, analytics_data: Dict[str, Any], data_keys: List[str]) -> Dict[str, Any]:
        """Extract relevant data for a specific topic"""
        topic_data = {}

        for key in data_keys:
            if key in analytics_data and analytics_data[key]:
                # Filter out empty or error data
                if isinstance(analytics_data[key], dict):
                    filtered = {k: v for k, v in analytics_data[key].items()
                               if v and not isinstance(v, dict) or 'error' not in v}
                    if filtered:
                        topic_data[key] = filtered
                else:
                    topic_data[key] = analytics_data[key]

        return topic_data

    def _generate_topic_insights(self, topic_id: str, topic_name: str,
                                 description: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate AI insights for a specific topic"""
        try:
            # Prepare focused prompt for this topic
            data_summary = json.dumps(data, indent=2, default=str)

            # Truncate if too long
            max_chars = 12000
            if len(data_summary) > max_chars:
                data_summary = data_summary[:max_chars] + "\n\n[Data truncated...]"

            prompt = f"""You are an expert social media marketing analyst for {BRAND_NAME}.

Analyze the following {topic_name.upper()} data from {START_DATE} to {END_DATE}:

{data_summary}

Provide a detailed, actionable analysis covering:

1. **Key Findings** (3-5 specific observations with numbers)
2. **What's Working Well** (2-3 highlights with evidence)
3. **Areas for Improvement** (2-3 specific issues with data)
4. **Actionable Recommendations** (3-5 specific, implementable actions)
5. **Quick Wins** (1-2 things to do immediately)

Be specific, use actual numbers from the data, and make recommendations actionable and concrete.
Focus ONLY on {description}.
"""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert social media marketing analyst who provides specific, data-driven insights."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=1500
            )

            return {
                'status': 'success',
                'content': response.choices[0].message.content,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error generating insights for {topic_name}: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def _generate_executive_summary(self, topic_insights: Dict[str, Any],
                                   full_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate executive summary based on all topic insights"""
        try:
            # Compile key points from all topics
            all_insights = []
            for topic_id, topic_data in topic_insights.items():
                all_insights.append(f"## {topic_data['name']}\n{topic_data['insights']}\n")

            insights_text = "\n".join(all_insights)

            # Truncate if needed
            max_chars = 15000
            if len(insights_text) > max_chars:
                insights_text = insights_text[:max_chars] + "\n\n[Insights truncated...]"

            # Get overview stats
            summary_stats = full_data.get('summary', {})
            platform_comparison = full_data.get('platform_comparison', {})

            prompt = f"""You are a marketing executive creating a brief for C-level leadership.

Based on the following detailed topic analyses for {BRAND_NAME} ({START_DATE} to {END_DATE}):

{insights_text}

OVERVIEW STATS:
{json.dumps(summary_stats, indent=2, default=str)}

PLATFORM COMPARISON:
{json.dumps(platform_comparison, indent=2, default=str)}

Write a compelling 3-4 paragraph executive summary that:

1. Opens with the overall performance state (great/good/needs attention)
2. Highlights 2-3 biggest wins or achievements (with specific numbers)
3. Identifies 1-2 critical areas needing attention
4. Ends with the strategic direction forward

Write for busy executives - be concise, impactful, and focus on business outcomes.
Use specific numbers and avoid generic statements.
"""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a senior marketing executive who communicates clearly and strategically to C-level leadership."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=800
            )

            return {
                'status': 'success',
                'content': response.choices[0].message.content,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error generating executive summary: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def _generate_strategic_recommendations(self, topic_insights: Dict[str, Any],
                                          full_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate prioritized strategic recommendations"""
        try:
            # Extract recommendations from all topics
            recommendations_context = []
            for topic_id, topic_data in topic_insights.items():
                recommendations_context.append(f"{topic_data['name']}:\n{topic_data['insights']}\n")

            context_text = "\n".join(recommendations_context)

            # Truncate if needed
            max_chars = 12000
            if len(context_text) > max_chars:
                context_text = context_text[:max_chars] + "\n\n[Context truncated...]"

            prompt = f"""Based on all the analyses for {BRAND_NAME}, create a prioritized action plan.

CONTEXT FROM ALL ANALYSES:
{context_text}

Create a strategic action plan with:

**IMMEDIATE ACTIONS (This Week)**
- List 2-3 quick wins that can be implemented immediately
- Each with expected impact

**SHORT-TERM PRIORITIES (This Month)**
- List 3-4 high-impact actions for the next 30 days
- Each with clear success metrics

**LONG-TERM STRATEGY (Next Quarter)**
- List 2-3 strategic initiatives for sustained growth
- Each with business justification

For each recommendation:
- Be specific and actionable
- Include WHY it matters (with data)
- Suggest HOW to measure success

Prioritize by impact and feasibility.
"""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a strategic marketing consultant who creates clear, prioritized action plans."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=1200
            )

            return {
                'status': 'success',
                'content': response.choices[0].message.content,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error generating strategic recommendations: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def _estimate_cost(self, tokens: Dict[str, int]) -> float:
        """Estimate OpenAI API cost"""
        # GPT-4o pricing (as of 2024)
        # Input: $2.50 per 1M tokens
        # Output: $10.00 per 1M tokens

        input_cost = (tokens.get('prompt', 0) / 1_000_000) * 2.50
        output_cost = (tokens.get('completion', 0) / 1_000_000) * 10.00

        return input_cost + output_cost
