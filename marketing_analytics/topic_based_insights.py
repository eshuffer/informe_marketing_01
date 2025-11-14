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

        # Define analysis phases and topics
        self.enable_data_consolidation = True  # Phase 1: Data consolidation
        self.enable_validation = True  # Phase 4: Validation

        # Define topic groups (Phase 2)
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
        """Generate insights for all topics using 12-request enhanced architecture"""
        if not self.client:
            return {
                'error': 'OpenAI API key not configured',
                'message': 'Set OPENAI_API_KEY environment variable to enable AI insights'
            }

        logger.info("Generating enhanced AI insights (12-request architecture)...")

        all_insights = {
            'topics': {},
            'executive_summary': '',
            'strategic_recommendations': '',
            'status': 'success',
            'data_consolidation': {},
            'validation': {}
        }

        total_tokens = {'prompt': 0, 'completion': 0}

        # === PHASE 1: DATA CONSOLIDATION (2 requests) ===
        logger.info("\n[Phase 1/4] Data Consolidation")

        if self.enable_data_consolidation:
            # Request 1: Data Synthesis & Key Metrics Extraction
            logger.info("  [1/12] Extracting key metrics dictionary...")
            metrics_dict = self._generate_metrics_dictionary(analytics_data)
            if metrics_dict.get('status') == 'success':
                all_insights['data_consolidation']['metrics_dictionary'] = metrics_dict['content']
                total_tokens['prompt'] += metrics_dict.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += metrics_dict.get('tokens', {}).get('completion', 0)

            # Request 2: Cross-Metric Pattern Detection
            logger.info("  [2/12] Detecting cross-metric patterns...")
            patterns = self._detect_cross_metric_patterns(analytics_data, metrics_dict.get('content', ''))
            if patterns.get('status') == 'success':
                all_insights['data_consolidation']['patterns'] = patterns['content']
                total_tokens['prompt'] += patterns.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += patterns.get('tokens', {}).get('completion', 0)

        # === PHASE 2: TOPIC ANALYSIS (5 requests) ===
        logger.info("\n[Phase 2/4] Topic-Based Analysis")

        request_num = 3
        for topic_id, topic_config in self.topics.items():
            logger.info(f"  [{request_num}/12] Analyzing: {topic_config['name']}")

            topic_data = self._extract_topic_data(analytics_data, topic_config['data_keys'])

            if topic_data:
                insights = self._generate_topic_insights(
                    topic_id,
                    topic_config['name'],
                    topic_config['description'],
                    topic_data,
                    metrics_dict=all_insights['data_consolidation'].get('metrics_dictionary', ''),
                    patterns=all_insights['data_consolidation'].get('patterns', '')
                )

                if insights.get('status') == 'success':
                    all_insights['topics'][topic_id] = {
                        'name': topic_config['name'],
                        'insights': insights['content'],
                        'tokens': insights.get('tokens', {})
                    }
                    total_tokens['prompt'] += insights.get('tokens', {}).get('prompt', 0)
                    total_tokens['completion'] += insights.get('tokens', {}).get('completion', 0)

            request_num += 1

        # === PHASE 3: SYNTHESIS (2 requests) ===
        logger.info("\n[Phase 3/4] Executive Synthesis")

        if all_insights['topics']:
            # Request 8: Executive Summary
            logger.info("  [8/12] Generating executive summary...")
            exec_summary = self._generate_executive_summary(all_insights['topics'], analytics_data)
            if exec_summary.get('status') == 'success':
                all_insights['executive_summary'] = exec_summary['content']
                total_tokens['prompt'] += exec_summary.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += exec_summary.get('tokens', {}).get('completion', 0)

            # Request 9: Strategic Action Plan
            logger.info("  [9/12] Generating strategic action plan...")
            recommendations = self._generate_strategic_recommendations(all_insights['topics'], analytics_data)
            if recommendations.get('status') == 'success':
                all_insights['strategic_recommendations'] = recommendations['content']
                total_tokens['prompt'] += recommendations.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += recommendations.get('tokens', {}).get('completion', 0)

        # === PHASE 4: VALIDATION (3 requests) ===
        logger.info("\n[Phase 4/4] Quality Validation")

        if self.enable_validation:
            # Request 10: Data Citation Validation
            logger.info("  [10/12] Validating data citations...")
            citation_check = self._validate_data_citations(
                all_insights['strategic_recommendations'],
                all_insights['data_consolidation'].get('metrics_dictionary', '')
            )
            if citation_check.get('status') == 'success':
                all_insights['validation']['citation_validation'] = citation_check['content']
                total_tokens['prompt'] += citation_check.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += citation_check.get('tokens', {}).get('completion', 0)

            # Request 11: Research Source Quality Review
            logger.info("  [11/12] Reviewing research source quality...")
            source_review = self._review_research_sources(all_insights['strategic_recommendations'])
            if source_review.get('status') == 'success':
                all_insights['validation']['source_quality'] = source_review['content']
                total_tokens['prompt'] += source_review.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += source_review.get('tokens', {}).get('completion', 0)

            # Request 12: Final Enhancement & Integration
            logger.info("  [12/12] Final enhancement & integration...")
            final_enhanced = self._enhance_recommendations(
                all_insights['strategic_recommendations'],
                citation_check.get('content', ''),
                source_review.get('content', '')
            )
            if final_enhanced.get('status') == 'success':
                all_insights['strategic_recommendations'] = final_enhanced['content']
                total_tokens['prompt'] += final_enhanced.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += final_enhanced.get('tokens', {}).get('completion', 0)

        all_insights['total_tokens'] = total_tokens
        all_insights['total_cost_estimate'] = self._estimate_cost(total_tokens)

        logger.info(f"\n✓ Completed 12-request enhanced analysis")
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
                                 description: str, data: Dict[str, Any],
                                 metrics_dict: str = '', patterns: str = '') -> Dict[str, Any]:
        """Generate AI insights for a specific topic with consolidated metrics"""
        try:
            # Prepare focused prompt for this topic
            data_summary = json.dumps(data, indent=2, default=str)

            # Truncate if too long
            max_chars = 12000
            if len(data_summary) > max_chars:
                data_summary = data_summary[:max_chars] + "\n\n[Data truncated...]"

            # Add consolidated metrics context if available
            consolidated_context = ""
            if metrics_dict:
                consolidated_context += f"\n\n**CONSOLIDATED METRICS REFERENCE:**\n{metrics_dict[:3000]}\n"
            if patterns:
                consolidated_context += f"\n**KEY PATTERNS DETECTED:**\n{patterns[:2000]}\n"

            prompt = f"""You are a world-class social media marketing strategist and growth expert for {BRAND_NAME}.
You have deep expertise in social media algorithms, content strategy, audience psychology, and data-driven optimization.

Analyze this {topic_name.upper()} data from {START_DATE} to {END_DATE}:

{data_summary}
{consolidated_context}

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

    # === PHASE 1: DATA CONSOLIDATION METHODS ===

    def _generate_metrics_dictionary(self, analytics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and consolidate all key metrics into a structured dictionary"""
        try:
            data_json = json.dumps(analytics_data, indent=2, default=str)[:15000]

            prompt = f"""You are a data analyst creating a comprehensive metrics dictionary for {BRAND_NAME}.

RAW ANALYTICS DATA:
{data_json}

Create a STRUCTURED METRICS DICTIONARY extracting EVERY important number:

## KEY PERFORMANCE INDICATORS
List ALL metrics with exact numbers:
- Instagram Posts: Engagement rate X%, total reach Y, total interactions Z, post count N
- Instagram Reels: Engagement rate X%, total reach Y, total interactions Z, post count N
- Facebook: [same format]
- Best performing post: X% engagement, Y reach
- Worst performing post: X% engagement, Y reach
- etc.

## CONTENT METRICS
- Average caption length: X characters
- Posts with hashtags: X (Y%)
- Average hashtags per post: X
- Most used hashtags: [list with counts]
- etc.

## TIMING METRICS
- Most active posting hours: [list with counts]
- Most active posting days: [list with counts]
- Best performing hours: [list with avg engagement]
- Best performing days: [list with avg engagement]
- etc.

## TREND METRICS
- Weekly performance changes: Week X: Y posts, Z% avg engagement
- Growth rates: +X% engagement, +Y% reach
- etc.

## PLATFORM COMPARISON
- Instagram vs Facebook: X% vs Y% engagement, A reach vs B reach
- Posts vs Reels: X% vs Y% engagement
- Performance gap: +Z%
- etc.

**FORMAT REQUIREMENTS:**
- Every metric must have an EXACT number
- Use format: "Metric name: X (specific value with units)"
- Include percentage breakdowns where relevant
- Note any missing data as "N/A"

Create a comprehensive reference that subsequent analysis can cite."""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a meticulous data analyst who extracts every relevant metric from raw data. You create structured, comprehensive dictionaries that serve as authoritative references."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1,  # Lower for factual extraction
                max_tokens=2000
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
            logger.error(f"Error generating metrics dictionary: {e}")
            return {'status': 'error', 'error': str(e)}

    def _detect_cross_metric_patterns(self, analytics_data: Dict[str, Any],
                                     metrics_dict: str) -> Dict[str, Any]:
        """Detect correlations and patterns across different metrics"""
        try:
            # Extract enhanced content data for pattern detection
            enhanced_data = analytics_data.get('enhanced_content', {})
            enhanced_json = json.dumps(enhanced_data, indent=2, default=str)[:10000]

            prompt = f"""You are a data scientist detecting patterns and correlations for {BRAND_NAME}.

METRICS REFERENCE:
{metrics_dict[:4000]}

DETAILED PERFORMANCE DATA:
{enhanced_json}

Identify CROSS-METRIC PATTERNS and CORRELATIONS:

## PERFORMANCE CORRELATIONS
What metrics move together?
- "When X increases, Y tends to [increase/decrease] by Z%"
- "Posts with X hashtags get Y% more engagement than posts with Z hashtags"
- "Content posted at X hour gets Y% better reach than content at Z hour"
- etc.

## CONTENT ATTRIBUTE PATTERNS
What content characteristics correlate with success?
- "Posts with caption length X-Y characters get Z% higher engagement"
- "Content including [specific elements] performs X% better"
- etc.

## TIME-BASED PATTERNS
- "Posting frequency of X per week correlates with Y% engagement"
- "Day of week Z shows X% higher engagement than average"
- etc.

## FORMAT PERFORMANCE PATTERNS
- "Reels with X characteristic get Y% more reach than those without"
- etc.

## HIDDEN INSIGHTS
Find non-obvious connections:
- Surprising correlations
- Counter-intuitive findings
- Underutilized opportunities

**REQUIREMENTS:**
- Every pattern must cite SPECIFIC numbers
- Show correlation strength (strong/moderate/weak)
- Identify causation vs correlation
- Note sample sizes

This will be used to strengthen recommendations with data-backed connections."""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a data scientist specialized in finding meaningful patterns and correlations in social media data. You identify both obvious and non-obvious relationships between metrics."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
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
            logger.error(f"Error detecting patterns: {e}")
            return {'status': 'error', 'error': str(e)}

    # === PHASE 4: VALIDATION METHODS ===

    def _validate_data_citations(self, recommendations: str,
                                metrics_dict: str) -> Dict[str, Any]:
        """Validate that every recommendation cites specific data"""
        try:
            prompt = f"""You are a quality auditor reviewing strategic recommendations for {BRAND_NAME}.

METRICS DICTIONARY (Source of Truth):
{metrics_dict[:5000]}

RECOMMENDATIONS TO VALIDATE:
{recommendations[:8000]}

AUDIT TASK: Check if EVERY recommendation properly cites data.

For each recommendation/action in the document:

## COMPLIANT EXAMPLES ✓
- "Your Instagram posts (7.12% engagement) outperform Reels (5.94%)..." [CITES SPECIFIC METRICS]
- "With only 17 posts generating 17,981 reach..." [CITES ACTUAL NUMBERS]

## NON-COMPLIANT EXAMPLES ✗
- "Optimize posting schedule" [NO DATA CITED]
- "Engagement is low" [VAGUE, NO NUMBERS]
- "Post more frequently" [NO BASELINE REFERENCED]

PROVIDE:

### 1. VALIDATION SCORE
- X out of Y recommendations properly cite data (Z%)

### 2. MISSING DATA CITATIONS
List recommendations that lack specific data citations:
- "Recommendation: [quote]" → Missing: Should cite [specific metric from dictionary]

### 3. IMPROVEMENT SUGGESTIONS
For each flagged item, suggest the correction:
- Original: "[vague statement]"
- Improved: "[statement with specific metric citation]"

Be strict - every action/recommendation MUST reference specific numbers from the data."""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a strict quality auditor. Your job is to ensure every recommendation is backed by specific data citations. You flag any vague or generic advice."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1,
                max_tokens=2000
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
            logger.error(f"Error validating citations: {e}")
            return {'status': 'error', 'error': str(e)}

    def _review_research_sources(self, recommendations: str) -> Dict[str, Any]:
        """Review the quality and plausibility of research citations"""
        try:
            prompt = f"""You are a research librarian reviewing citations in marketing recommendations for {BRAND_NAME}.

RECOMMENDATIONS WITH RESEARCH CITATIONS:
{recommendations[:10000]}

REVIEW TASK: Assess the quality and plausibility of research citations.

## EVALUATE EACH CITATION:

### 1. PLAUSIBILITY CHECK
Identify citations and assess if they're realistic:
- ✓ PLAUSIBLE: "According to Hootsuite's 2024 Social Media Report..." [Known publisher, reasonable]
- ✓ PLAUSIBLE: "Meta's 2024 Algorithm Update states..." [Official platform source]
- ✗ SUSPICIOUS: "According to XYZ's 2024 study..." [Unknown publisher]
- ✗ SUSPICIOUS: "Research shows..." [No source provided]

### 2. CITATION QUALITY SCORE
Rate overall citation quality: X/10
- Percentage with named sources: Y%
- Percentage with year: Z%
- Percentage from credible publishers: W%

### 3. MISSING SOURCES
List recommendations that should cite research but don't:
- "Claim: [quote]" → Should cite: [type of research that would support this]

### 4. SUGGESTED ALTERNATIVES
For weak/missing citations, suggest credible sources:
- Original: "Studies show..."
- Suggested: "According to [credible source] like Sprout Social/Hootsuite/Buffer/Later..."

### 5. CREDIBLE SOURCE RECOMMENDATIONS
List 10-15 credible social media research publishers the analyst should reference:
- Hootsuite (annual reports)
- Sprout Social (quarterly benchmarks)
- Meta Business (algorithm updates)
- etc.

Be helpful - suggest realistic improvements while maintaining rigor."""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a research librarian who evaluates citation quality. You know credible social media research publishers and can spot vague or missing sources. You're helpful and suggest realistic alternatives."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
                max_tokens=1800
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
            logger.error(f"Error reviewing sources: {e}")
            return {'status': 'error', 'error': str(e)}

    def _enhance_recommendations(self, recommendations: str,
                                citation_validation: str,
                                source_review: str) -> Dict[str, Any]:
        """Final enhancement pass incorporating validation feedback"""
        try:
            prompt = f"""You are refining strategic recommendations for {BRAND_NAME} based on quality review feedback.

ORIGINAL RECOMMENDATIONS:
{recommendations[:7000]}

CITATION VALIDATION FEEDBACK:
{citation_validation[:2500]}

RESEARCH SOURCE REVIEW:
{source_review[:2500]}

TASK: Produce FINAL ENHANCED RECOMMENDATIONS incorporating all feedback.

## ENHANCEMENT REQUIREMENTS:

1. **Fix Missing Data Citations**
   - Add specific metrics to any vague statements
   - Replace generic advice with data-backed specifics

2. **Strengthen Research Sources**
   - Replace weak citations with credible sources
   - Add sources where missing
   - Use suggested alternatives from review

3. **Maintain Structure**
   - Keep the same sections and organization
   - Preserve all good content that already had proper citations
   - Only enhance weak areas

4. **Quality Standards**
   - Every action: Data citation + Research citation + Calculation
   - Every claim: Verifiable and specific
   - No generic advice

OUTPUT the COMPLETE enhanced version of the strategic action plan with all improvements integrated.

Make this publication-ready - every recommendation should withstand scrutiny."""

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a senior editor finalizing a strategic document. You integrate feedback seamlessly while maintaining the document's value and readability. You're meticulous about data citations and research sources."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=3500
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
            logger.error(f"Error enhancing recommendations: {e}")
            return {'status': 'error', 'error': str(e)}

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
