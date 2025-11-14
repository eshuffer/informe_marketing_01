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

            prompt = f"""You are a world-class social media marketing strategist and growth expert for {BRAND_NAME}.
You have deep expertise in social media algorithms, content strategy, audience psychology, and data-driven optimization.

Analyze this {topic_name.upper()} data from {START_DATE} to {END_DATE}:

{data_summary}

Provide an EXTENSIVE, GURU-LEVEL strategic analysis:

## 1. DEEP DATA ANALYSIS (Be exhaustive)
- Identify 5-7 key patterns and insights from the numbers
- What does this data reveal about audience behavior?
- What hidden opportunities exist in the data?
- Compare performance across different dimensions

## 2. STRATEGIC ASSESSMENT
- What's working exceptionally well? (Provide 3-4 examples with evidence)
- What's underperforming? (Identify 3-4 specific issues with root causes)
- What trends are emerging over the time period?
- How does this compare to industry benchmarks?

## 3. ROOT CAUSE ANALYSIS
- WHY are certain things performing well/poorly?
- What psychological/algorithmic factors are at play?
- What patterns connect high-performing content?
- What mistakes are being repeated?

## 4. REACH OPTIMIZATION STRATEGIES
- Specific tactics to increase reach by 20-50%
- Algorithm-friendly best practices for this platform
- Content format optimization for maximum distribution
- Timing and frequency strategies for reach

## 5. COMPREHENSIVE ACTION PLAN
Provide 8-10 specific, prioritized actions:

For each action include:
- ✓ Exact implementation steps (be specific!)
- ✓ Expected impact (quantify: +X% reach, +Y% engagement)
- ✓ Timeline (when to implement, how long to test)
- ✓ Success metrics (how to measure)
- ✓ Effort level (low/medium/high)

## 6. QUICK WINS (Implement This Week)
- 3-4 changes that can be made immediately
- Each with specific numbers and expected lift

## 7. EXPERIMENTATION ROADMAP
- 3-5 A/B tests to run in next 30 days
- Each test with hypothesis, variables, and success criteria

## 8. RISK FACTORS & WARNINGS
- What could go wrong if current trends continue?
- What opportunities are being missed?
- What competitor strategies should be monitored?

Be extremely specific with numbers, percentages, and concrete examples.
Think like a $500/hour marketing consultant - provide insights worth paying for.
Focus EXCLUSIVELY on {description}.
"""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": """You are an elite social media marketing strategist with 15+ years experience.
You've managed accounts with millions of followers and consistently achieve 3-5x industry average engagement.
You understand platform algorithms deeply and provide insights that directly impact business growth.
Your recommendations are specific, actionable, and backed by data and psychology."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=3000  # Increased for more detailed responses
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

            prompt = f"""You are a CMO presenting to the CEO and board about {BRAND_NAME}'s social media performance.

COMPREHENSIVE ANALYSIS INSIGHTS:
{insights_text}

OVERVIEW METRICS:
{json.dumps(summary_stats, indent=2, default=str)}

PLATFORM COMPARISON:
{json.dumps(platform_comparison, indent=2, default=str)}

Period: {START_DATE} to {END_DATE}

Create a COMPELLING, DATA-RICH executive summary (4-6 paragraphs):

**Paragraph 1: Performance State & Context**
- Overall performance assessment with year-over-year comparison
- Market context and competitive positioning
- Key metric highlights (reach, engagement, growth rate)

**Paragraph 2: Strategic Wins & Successes**
- 3-4 major achievements with specific ROI/impact numbers
- What strategies are working and why
- Competitive advantages gained

**Paragraph 3: Critical Challenges & Gaps**
- 2-3 underperforming areas with business impact
- Root causes and missed opportunities
- Risk factors if unaddressed

**Paragraph 4: Growth Trajectory & Trends**
- Where performance is heading (up/down/stable)
- Emerging patterns and their implications
- Forecast for next quarter

**Paragraph 5: Strategic Imperatives**
- Top 3 priorities for leadership focus
- Resource allocation recommendations
- Expected business outcomes

**Paragraph 6: Bottom Line**
- Clear go/no-go on current strategy
- Investment recommendations
- Success metrics to track

Use executive language - strategic, outcome-focused, and financially aware.
Include specific percentages, growth rates, and ROI implications.
"""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a seasoned Chief Marketing Officer with 20+ years experience.
You've presented to hundreds of boards and know how to communicate marketing performance in business terms.
You connect social media metrics to revenue, brand value, and competitive advantage."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=1500  # Increased for longer executive summary
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

            prompt = f"""You are an elite growth marketing consultant hired by {BRAND_NAME} to create a comprehensive growth roadmap.

COMPLETE PERFORMANCE ANALYSIS:
{context_text}

Create an EXTENSIVE, IMPLEMENTATION-READY strategic action plan:

## IMMEDIATE ACTIONS (This Week - Days 1-7)
Provide 4-6 quick wins with:
- ✓ Exact action steps (numbered, specific)
- ✓ Who should do it (role/person)
- ✓ Expected impact (+X% reach/engagement)
- ✓ Time required (hours/days)
- ✓ Resources needed
- ✓ Success metric (how to measure)
- ✓ Risk level (low/medium/high)

## SHORT-TERM PRIORITIES (This Month - Weeks 2-4)
Provide 6-8 high-impact initiatives with:
- ✓ Detailed implementation roadmap
- ✓ Week-by-week timeline
- ✓ Content requirements
- ✓ Team resources needed
- ✓ Budget estimate (if applicable)
- ✓ Success criteria (specific numbers)
- ✓ Contingency plans

## MEDIUM-TERM STRATEGY (Next Quarter - Months 2-3)
Provide 4-6 strategic initiatives with:
- ✓ Strategic rationale (WHY this matters)
- ✓ Implementation phases
- ✓ Resource allocation
- ✓ Dependencies and prerequisites
- ✓ Risk mitigation strategies
- ✓ Expected ROI/impact
- ✓ Key milestones

## REACH AMPLIFICATION PLAYBOOK
Provide 8-10 specific tactics to increase reach by 30-50%:
- Algorithm optimization strategies
- Viral content frameworks
- Cross-promotion tactics
- Paid amplification opportunities
- Influencer/partnership strategies
- Platform-specific growth hacks
- Content repurposing strategies
- Audience expansion tactics

## CONTENT OPTIMIZATION FRAMEWORK
- Content pillars and themes (with rationale)
- Posting calendar structure
- Content format mix (percentage breakdown)
- Caption formulas that convert
- Visual style guidelines
- Hashtag strategy per content type
- Call-to-action frameworks

## EXPERIMENTATION PROGRAM (30-Day Test Plan)
For each experiment (provide 5-7):
1. **Hypothesis**: What we're testing and why
2. **Test Design**: Control vs variant
3. **Variables**: What changes
4. **Sample Size**: How many posts/days
5. **Success Metrics**: What we measure
6. **Decision Criteria**: When to scale/stop
7. **Expected Learning**: What we'll discover

## PERFORMANCE MONITORING DASHBOARD
- Daily metrics to track
- Weekly review checklist
- Monthly performance indicators
- Red flags and warning signs
- Course correction triggers

## RESOURCE REQUIREMENTS
- Team time allocation
- Tool/software needs
- Content creation requirements
- Budget recommendations
- Training/upskilling needs

## RISK MITIGATION & CONTINGENCIES
- What could go wrong
- Prevention strategies
- Backup plans
- Crisis response protocols
- Competitive threats to monitor

## SUCCESS MILESTONES (30/60/90 Days)
- Week 4 targets (with numbers)
- Week 8 targets (with numbers)
- Week 12 targets (with numbers)
- How to celebrate wins
- When to pivot strategies

Be EXTREMELY specific - provide actual numbers, exact steps, and detailed implementation guidance.
Think like you're creating a playbook someone could execute without asking clarification questions.
Make this worth $10,000 in consulting value.
"""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a legendary growth marketing consultant who has 10x'd dozens of brands.
Your action plans are so detailed and effective that clients call them "growth bibles."
You think in systems, frameworks, and repeatable processes.
You provide implementation-level detail that eliminates guesswork.
You've personally managed $50M+ in social media budgets and know what actually works."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=3500  # Maximum allowed for detailed recommendations
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

        total_cost = input_cost + output_cost

        # Log detailed breakdown
        logger.info(f"  Cost breakdown:")
        logger.info(f"    Input: {tokens.get('prompt', 0):,} tokens = ${input_cost:.4f}")
        logger.info(f"    Output: {tokens.get('completion', 0):,} tokens = ${output_cost:.4f}")
        logger.info(f"    Total: ${total_cost:.4f}")

        return total_cost
