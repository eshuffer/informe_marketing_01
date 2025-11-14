"""
Marketing Analytics Configuration
Settings for analytics processing and AI insights generation
"""

import os
from pathlib import Path

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")  # Set via environment variable or update here
OPENAI_MODEL = "gpt-4o"  # Using GPT-4 for best analysis quality
OPENAI_TEMPERATURE = 0.3  # Lower temperature for more focused, analytical responses

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "metricool_data_fetcher" / "data"
REPORTS_DIR = PROJECT_ROOT / "marketing_analytics" / "reports"

# Brand Information
BRAND_NAME = "Sattvica"
START_DATE = "2025-08-13"
END_DATE = "2025-11-13"

# Analytics Settings
ENABLED_PLATFORMS = ['instagram', 'facebook']

# Report Settings
REPORT_FORMAT = "markdown"  # Options: markdown, html, json
INCLUDE_AI_INSIGHTS = True
INCLUDE_VISUALIZATIONS = True

# Insight Generation Settings
INSIGHT_CATEGORIES = [
    'content_performance',
    'engagement_trends',
    'audience_demographics',
    'posting_strategy',
    'platform_comparison',
    'growth_analysis',
    'hashtag_effectiveness',
]

# Thresholds for highlighting
HIGH_ENGAGEMENT_THRESHOLD = 5.0  # percentage
LOW_ENGAGEMENT_THRESHOLD = 1.0   # percentage
SIGNIFICANT_GROWTH_THRESHOLD = 10.0  # percentage change

# AI Prompt Templates
AI_CONTEXT_TEMPLATE = """
You are a expert marketing analyst specializing in social media analytics.
You have access to {days} days of data from {brand_name}'s social media presence on {platforms}.

Your role is to:
1. Analyze performance data objectively
2. Identify trends, patterns, and anomalies
3. Provide actionable recommendations
4. Highlight both successes and areas for improvement
5. Use specific metrics and numbers to support your insights
"""

AI_INSIGHT_PROMPT_TEMPLATE = """
Based on the following social media analytics data for {brand_name}, provide strategic marketing insights:

DATA:
{data_summary}

Please provide:
1. **Key Findings**: 3-5 most important observations
2. **Performance Highlights**: What's working well
3. **Areas for Improvement**: What needs attention
4. **Actionable Recommendations**: Specific next steps to improve performance
5. **Trend Analysis**: Patterns or trends you observe in the data

Be specific, use numbers, and make recommendations actionable.
"""
