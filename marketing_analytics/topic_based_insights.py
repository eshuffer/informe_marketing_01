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

**CRITICAL REQUIREMENTS:**
1. EVERY recommendation MUST cite specific numbers from the data above (e.g., "Your data shows posts average 7.12% engagement vs reels at 5.94%...")
2. EVERY general claim MUST cite industry research/studies (e.g., "According to Meta's 2024 Algorithm Report...", "HubSpot's 2024 Social Media Study found...")
3. NO GENERIC ADVICE - Every insight must be grounded in either YOUR data or CITED research
4. When suggesting best practices, cite the source (e.g., "Hootsuite's 2024 research shows...", "Sprout Social's analysis of 10M posts found...")

**GOOD EXAMPLE:** "Your Instagram posts (avg 7.12% engagement, 17,981 total reach) significantly outperform Reels (5.94% engagement). According to Later's 2024 Instagram Analysis of 5M posts, carousel posts achieve 1.4x higher engagement than Reels for accounts under 50K followers, suggesting you should increase carousel post frequency by 40%."

**BAD EXAMPLE:** "Content relevance is important. Post at optimal times to increase engagement." [TOO GENERIC, NO DATA]

Provide an EXTENSIVE, GURU-LEVEL strategic analysis:

## 1. DEEP DATA ANALYSIS (Be exhaustive)
- Identify 5-7 key patterns citing SPECIFIC NUMBERS from the data
- What does this data reveal about audience behavior? (Reference actual metrics)
- What hidden opportunities exist? (Compare specific data points)
- Compare performance across different dimensions (use exact percentages/numbers)

## 2. STRATEGIC ASSESSMENT
- What's working exceptionally well? (Cite 3-4 examples with EXACT metrics from your data)
- What's underperforming? (Identify 3-4 specific issues with ACTUAL numbers showing the gap)
- What trends are emerging? (Reference SPECIFIC time-based changes in the data)
- How does this compare to industry benchmarks? (Cite research: "According to [Source Year], industry average is X% vs your Y%")

## 3. ROOT CAUSE ANALYSIS
- WHY are certain things performing well/poorly? (Cite platform algorithm documentation or research)
- What psychological/algorithmic factors are at play? (Reference studies, e.g., "Meta's 2024 Engagement Study shows...")
- What patterns connect high-performing content? (Use SPECIFIC examples from the data with numbers)
- What mistakes are being repeated? (Identify with data evidence)

## 4. REACH OPTIMIZATION STRATEGIES
- Specific tactics to increase reach (Each backed by: YOUR data showing gap + Research showing solution works)
- Algorithm-friendly best practices (Cite official platform documentation or credible studies)
- Content format optimization (Reference YOUR format performance data + industry research)
- Timing strategies (Base on YOUR actual posting time performance data if available)

## 5. COMPREHENSIVE ACTION PLAN
Provide 8-10 specific, prioritized actions where EACH includes:
- ✓ Data justification: "Your data shows [specific metric]..."
- ✓ Research backing: "According to [Source Year], this tactic delivers..."
- ✓ Exact implementation steps
- ✓ Expected impact with reasoning (+X% based on [your gap] × [research multiplier])
- ✓ Timeline and success metrics
- ✓ Effort level

## 6. QUICK WINS (Implement This Week)
- 3-4 changes backed by YOUR data showing the opportunity
- Each citing research supporting why it will work
- Specific numbers and expected lift with calculation shown

## 7. EXPERIMENTATION ROADMAP
- 3-5 A/B tests based on gaps/questions in YOUR data
- Each with hypothesis supported by data observation
- Variables and success criteria tied to YOUR current metrics

## 8. RISK FACTORS & WARNINGS
- What could go wrong? (Show with data trends)
- What opportunities are being missed? (Quantify with your numbers)
- What should be monitored? (Reference specific metrics from your data)

**REMEMBER:**
- Zero generic advice - every sentence needs data or research citation
- Format citations like: "According to Hootsuite's 2024 report..." or "Your data shows engagement dropped from X to Y..."
- Calculate impact estimates: Don't just say "+20% engagement" - show "Your current 7.12% × 1.20 = 8.54% target"

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

CRITICAL: Your recommendations are ALWAYS:
1. Backed by specific numbers from the client's data (cite exact metrics)
2. Supported by credible industry research (cite sources like "According to Hootsuite 2024...")
3. Show calculations for impact estimates (e.g., "7.12% × 1.20 = 8.54%")
4. Verifiable - another analyst should be able to check your sources

You NEVER give vague or generic advice. Every insight must be evidence-based."""
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

**CRITICAL REQUIREMENTS:**
1. EVERY claim MUST cite specific metrics from the data above (exact numbers, percentages)
2. Industry comparisons MUST cite sources (e.g., "According to Rival IQ's 2024 Benchmark Report, industry average is X% vs our Y%")
3. Growth projections MUST show the math (e.g., "Current 7.12% × projected 1.15 improvement = 8.19% target")
4. NO generic statements - every sentence backed by data or research

**GOOD EXAMPLE:** "Instagram engagement rate of 7.12% significantly exceeds Hootsuite's 2024 industry benchmark of 2.3% for similar-sized accounts, positioning us in the top 15% of performers."

**BAD EXAMPLE:** "Performance has increased year-over-year" [NO NUMBERS, NO SOURCE]

Create a COMPELLING, DATA-RICH executive summary (4-6 paragraphs):

**Paragraph 1: Performance State & Context**
- Overall performance with SPECIFIC metrics from your data
- Benchmark against industry (cite source: "According to [Research] industry average is X%, we achieved Y%")
- Key metric highlights with EXACT numbers from the data

**Paragraph 2: Strategic Wins & Successes**
- 3-4 achievements with SPECIFIC metrics (cite exact numbers from data)
- Why they're working (cite research/platform documentation if making claims)
- Quantified competitive advantages

**Paragraph 3: Critical Challenges & Gaps**
- 2-3 underperforming areas with EXACT metrics showing the gap
- Root causes backed by data patterns or cited research
- Quantified risk (e.g., "missing X% of potential reach based on...")

**Paragraph 4: Growth Trajectory & Trends**
- Direction with SPECIFIC trend data (from X to Y over period)
- Patterns citing actual metrics from the data
- Forecast with calculation shown (current metric × expected change)

**Paragraph 5: Strategic Imperatives**
- Top 3 priorities backed by data gaps identified above
- Resource recommendations with expected ROI (cite similar case studies if available)
- Expected outcomes with specific targets

**Paragraph 6: Bottom Line**
- Go/no-go based on specific performance thresholds
- Investment recommendations tied to data-backed opportunities
- Success metrics with specific targets (not vague)

**REMEMBER:**
- Every number must come from the data provided
- Every industry comparison needs a cited source
- Show your math for projections
- Zero generic business speak without data backing

Use executive language - strategic, outcome-focused, and financially aware.
"""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a seasoned Chief Marketing Officer with 20+ years experience.
You've presented to hundreds of boards and know how to communicate marketing performance in business terms.
You connect social media metrics to revenue, brand value, and competitive advantage.

CRITICAL: Boards expect evidence-based reporting. Every statement must:
1. Cite specific metrics from the data (exact numbers, not ranges)
2. Benchmark against industry with sources (e.g., "vs Rival IQ's 2024 benchmark of X%")
3. Show calculations for projections (current × expected change = target)
4. Be fact-checkable - no unsupported claims

Generic business language without data backing will be questioned. Be precise and cite sources."""
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

**CRITICAL REQUIREMENTS - READ CAREFULLY:**
1. EVERY action MUST be justified by SPECIFIC data from the analysis (e.g., "Your data shows posts get 7.12% vs reels 5.94%, so...")
2. EVERY tactic MUST cite credible research (e.g., "According to Buffer's 2024 Study of 50K posts...", "Meta's 2024 Algorithm Update states...")
3. EVERY impact estimate MUST show the calculation (e.g., "Current 7.12% × 1.20 improvement = 8.54% target")
4. NO GENERIC TACTICS - Each must be tied to a specific gap/opportunity in THEIR data
5. When recommending posting times, tools, or strategies - cite the source of that recommendation

**GOOD EXAMPLE:** "Your data shows Reels underperform posts by 16.5% (5.94% vs 7.12%). According to Later's 2024 analysis of 5M Reels, adding captions increases engagement by 23%. Implement captions on all Reels → Expected: 5.94% × 1.23 = 7.31% target."

**BAD EXAMPLE:** "Optimize posting schedule. Post during peak times for better reach." [NO DATA REFERENCE, NO SOURCE, NO CALCULATION]

Create an EXTENSIVE, IMPLEMENTATION-READY strategic action plan:

## IMMEDIATE ACTIONS (This Week - Days 1-7)
Provide 4-6 quick wins where EACH includes:
- ✓ Data justification: "Your data shows [specific metric/gap]..."
- ✓ Research backing: "According to [Source Year], this delivers [specific result]..."
- ✓ Exact action steps (numbered, specific)
- ✓ Who should do it (role)
- ✓ Expected impact with calculation shown
- ✓ Time required
- ✓ Resources needed
- ✓ Success metric (specific number to hit)
- ✓ Risk level

## SHORT-TERM PRIORITIES (This Month - Weeks 2-4)
Provide 6-8 high-impact initiatives where EACH includes:
- ✓ Data-backed rationale (cite specific metrics from their analysis)
- ✓ Research support (cite studies showing this works)
- ✓ Detailed implementation roadmap
- ✓ Week-by-week timeline
- ✓ Content requirements
- ✓ Team resources needed
- ✓ Budget estimate with ROI calculation
- ✓ Success criteria (specific numbers based on current metrics)
- ✓ Contingency plans

## MEDIUM-TERM STRATEGY (Next Quarter - Months 2-3)
Provide 4-6 strategic initiatives where EACH includes:
- ✓ Strategic rationale citing gaps in THEIR data
- ✓ Industry precedent (cite case studies/research)
- ✓ Implementation phases
- ✓ Resource allocation
- ✓ Dependencies
- ✓ Risk mitigation
- ✓ Expected ROI with calculation
- ✓ Key milestones with target metrics

## REACH AMPLIFICATION PLAYBOOK
Provide 8-10 specific tactics where EACH includes:
- ✓ Current state from their data (e.g., "Your reach is X...")
- ✓ Research backing (e.g., "According to Hootsuite 2024...")
- ✓ Implementation specifics
- ✓ Expected impact with math shown
- ✓ Source citation

Categories to cover:
- Algorithm optimization (cite platform documentation)
- Viral content frameworks (cite research)
- Cross-promotion tactics (cite case studies)
- Paid amplification (cite benchmark data)
- Influencer strategies (cite ROI studies)
- Platform-specific hacks (cite source)
- Content repurposing (cite efficiency gains)
- Audience expansion (cite growth data)

## CONTENT OPTIMIZATION FRAMEWORK
Based on THEIR content performance data:
- Content pillars (backed by their top-performing content data)
- Posting calendar (based on their actual timing data if available, or cite research)
- Content format mix (based on their performance: X% posts vs Y% reels)
- Caption formulas (cite copywriting research or case studies)
- Visual guidelines (based on their best performers)
- Hashtag strategy (based on their data + cite research like "RiteTag's 2024 study...")
- CTA frameworks (cite conversion research)

## EXPERIMENTATION PROGRAM (30-Day Test Plan)
For each experiment (provide 5-7), include:
1. **Data Observation**: What gap/question in THEIR data sparked this
2. **Hypothesis**: Specific claim backed by research (cite source)
3. **Test Design**: Control vs variant (specific to their content)
4. **Variables**: What changes
5. **Sample Size**: How many (based on their posting frequency)
6. **Success Metrics**: Tied to their current baseline
7. **Decision Criteria**: Specific threshold (e.g., "If >8% engagement vs current 7.12%")
8. **Research Basis**: Why we expect this to work (cite source)

## PERFORMANCE MONITORING DASHBOARD
Based on THEIR key metrics:
- Daily metrics (specific to their important KPIs)
- Weekly review (based on their data patterns)
- Monthly indicators (tied to their goals)
- Red flags (specific thresholds based on their data)
- Course correction triggers (quantified)

## RESOURCE REQUIREMENTS
Justified by scope of their opportunities:
- Team time (estimated based on action plan above)
- Tools (specific recommendations with why - cite reviews/comparisons)
- Content needs (based on their posting frequency)
- Budget (with ROI calc based on their current performance)
- Training (specific skills needed, cite courses/resources)

## RISK MITIGATION & CONTINGENCIES
Based on THEIR specific situation:
- Risks from their data trends (cite specific metrics)
- Prevention (backed by research)
- Backup plans (alternative tactics with sources)
- Crisis protocols (industry best practices, cite source)
- Competitive threats (based on their market position)

## SUCCESS MILESTONES (30/60/90 Days)
Based on THEIR current metrics:
- Week 4 targets (current X → target Y with calculation)
- Week 8 targets (progressive improvement shown)
- Week 12 targets (ambitious but data-backed)
- Celebration criteria (specific achievements)
- Pivot triggers (specific underperformance thresholds)

**REMEMBER - ABSOLUTE REQUIREMENTS:**
- Every recommendation needs: Their data + Research citation + Math
- No generic advice that could apply to any brand
- Every number must be calculated from their baseline
- Every tactic must cite why it works (research/case study)

Make this worth $10,000 in consulting value - deeply customized to THEIR data.
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
You've personally managed $50M+ in social media budgets and know what actually works.

CRITICAL: You NEVER give generic advice. Every single recommendation must be:
1. Grounded in the client's specific data (cite exact metrics)
2. Backed by credible research (cite source and year)
3. Show your math for impact estimates
4. So specific that another marketer could verify your sources

You are known for recommendations that stand up to scrutiny because everything is evidence-based."""
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
