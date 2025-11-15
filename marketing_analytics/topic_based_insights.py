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
    END_DATE,
    REPORT_LANGUAGE
)

logger = logging.getLogger(__name__)


class TopicBasedInsightsGenerator:
    """Generate deep insights by analyzing data topics separately"""

    def __init__(self, api_key: str = OPENAI_API_KEY, language: str = REPORT_LANGUAGE):
        if not api_key:
            logger.warning("OpenAI API key not set. AI insights will be disabled.")
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)

        self.language = language

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

    def _get_system_prompt(self) -> str:
        """Get system prompt with language support"""
        base_prompt = """You are an elite social media marketing strategist with 15+ years experience.
You've managed accounts with millions of followers and consistently achieve 3-5x industry average engagement.
You understand platform algorithms deeply and provide insights that directly impact business growth.

CRITICAL: Your recommendations are ALWAYS:
1. Backed by specific numbers from the client's data (cite exact metrics)
2. Supported by credible industry research (cite sources like "According to Hootsuite 2024...")
3. Show calculations for impact estimates (e.g., "7.12% × 1.20 = 8.54%")
4. Verifiable - another analyst should be able to check your sources

You NEVER give vague or generic advice. Every insight must be evidence-based."""

        if self.language == 'es':
            base_prompt += """

LANGUAGE REQUIREMENT: You MUST respond COMPLETELY in Spanish (Español).
- Translate ALL text, titles, and headers to Spanish
- Keep numbers, percentages, and metrics exactly as provided
- Use Spanish marketing terminology (engagement, alcance, interacciones, likes, comentarios, compartidos)
- Keep Markdown formatting
- Cite sources in English but explain in Spanish"""

        return base_prompt

    def _prepare_prompt(self, prompt: str) -> str:
        """
        Prepare prompt with language-specific instructions

        Args:
            prompt: The original English prompt

        Returns:
            Prompt with language wrapper if needed
        """
        if self.language == 'es':
            spanish_instruction = """INSTRUCCIONES IMPORTANTES - LEE CUIDADOSAMENTE:
- Responde TODO el análisis en ESPAÑOL
- Traduce TODOS los títulos, encabezados y textos al español
- Mantén todos los números, porcentajes y métricas EXACTAMENTE como se proporcionan
- Usa terminología de marketing en español (engagement, alcance, interacciones, etc.)
- Mantén el formato Markdown
- Cita las fuentes en inglés pero EXPLICA en español

"""
            return spanish_instruction + prompt
        return prompt

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
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": self._prepare_prompt(prompt)
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
