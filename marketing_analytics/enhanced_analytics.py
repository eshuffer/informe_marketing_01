"""
Enhanced Analytics Processors
Additional detailed analysis to extract maximum value from available data
"""

import logging
from typing import Dict, List, Any, Optional
import pandas as pd
import numpy as np
from datetime import datetime
from collections import Counter

logger = logging.getLogger(__name__)


class EnhancedContentAnalyzer:
    """Extract deeper insights from post-level data"""

    @staticmethod
    def analyze_posting_patterns(posts_df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze when content is being posted"""
        if posts_df is None or posts_df.empty:
            return {'error': 'No data available'}

        # Find date column
        date_col = None
        for col in ['publishDate', 'date', 'createdAt', 'timestamp']:
            if col in posts_df.columns:
                date_col = col
                break

        if not date_col:
            return {'error': 'No date column found'}

        posts_df[date_col] = pd.to_datetime(posts_df[date_col], errors='coerce')
        posts_df = posts_df.dropna(subset=[date_col])

        if posts_df.empty:
            return {'error': 'No valid dates'}

        # Extract time components
        posts_df['hour'] = posts_df[date_col].dt.hour
        posts_df['day_of_week'] = posts_df[date_col].dt.day_name()
        posts_df['date_only'] = posts_df[date_col].dt.date

        # Posting frequency by hour
        hour_distribution = posts_df['hour'].value_counts().sort_index().to_dict()

        # Posting frequency by day of week
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_distribution = posts_df['day_of_week'].value_counts().reindex(day_order, fill_value=0).to_dict()

        # Most active posting times
        most_active_hours = posts_df['hour'].value_counts().head(3).to_dict()

        # Posts per week/month
        posts_df['week'] = posts_df[date_col].dt.isocalendar().week
        posts_df['month'] = posts_df[date_col].dt.to_period('M').astype(str)

        weekly_posts = posts_df.groupby('week').size().to_dict()
        monthly_posts = posts_df.groupby('month').size().to_dict()

        # Posting consistency
        date_counts = posts_df.groupby('date_only').size()
        avg_posts_per_day = date_counts.mean()
        posting_frequency = len(posts_df) / max((posts_df[date_col].max() - posts_df[date_col].min()).days, 1)

        return {
            'total_posts': len(posts_df),
            'date_range': {
                'start': posts_df[date_col].min().strftime('%Y-%m-%d'),
                'end': posts_df[date_col].max().strftime('%Y-%m-%d'),
                'days': (posts_df[date_col].max() - posts_df[date_col].min()).days
            },
            'posting_frequency': {
                'posts_per_week': posting_frequency * 7,
                'posts_per_day': posting_frequency,
                'avg_posts_per_active_day': avg_posts_per_day
            },
            'hour_distribution': hour_distribution,
            'day_distribution': day_distribution,
            'most_active_hours': most_active_hours,
            'weekly_breakdown': weekly_posts,
            'monthly_breakdown': monthly_posts,
        }

    @staticmethod
    def analyze_engagement_by_time(posts_df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze which posting times get best engagement"""
        if posts_df is None or posts_df.empty:
            return {'error': 'No data available'}

        # Find date column
        date_col = None
        for col in ['publishDate', 'date', 'createdAt', 'timestamp']:
            if col in posts_df.columns:
                date_col = col
                break

        if not date_col or 'reach' not in posts_df.columns:
            return {'error': 'Missing required columns'}

        posts_df[date_col] = pd.to_datetime(posts_df[date_col], errors='coerce')
        posts_df = posts_df.dropna(subset=[date_col])

        # Calculate engagement rate
        posts_df['engagement_rate'] = posts_df.apply(
            lambda row: (row.get('interactions', 0) / row.get('reach', 1) * 100) if row.get('reach', 0) > 0 else 0,
            axis=1
        )

        # Extract time components
        posts_df['hour'] = posts_df[date_col].dt.hour
        posts_df['day_of_week'] = posts_df[date_col].dt.day_name()

        # Best performing hours
        hour_performance = posts_df.groupby('hour').agg({
            'engagement_rate': 'mean',
            'reach': 'mean',
            'interactions': 'sum'
        }).round(2)

        best_hours = hour_performance.nlargest(5, 'engagement_rate')

        # Best performing days
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_performance = posts_df.groupby('day_of_week').agg({
            'engagement_rate': 'mean',
            'reach': 'mean',
            'interactions': 'sum'
        }).reindex(day_order)

        best_days = day_performance.nlargest(3, 'engagement_rate')

        return {
            'best_posting_hours': {
                int(hour): {
                    'avg_engagement': float(row['engagement_rate']),
                    'avg_reach': float(row['reach']),
                    'total_interactions': int(row['interactions'])
                }
                for hour, row in best_hours.iterrows()
            },
            'best_posting_days': {
                day: {
                    'avg_engagement': float(row['engagement_rate']),
                    'avg_reach': float(row['reach']),
                    'total_interactions': int(row['interactions'])
                }
                for day, row in best_days.iterrows()
            },
            'hour_performance_all': {
                int(hour): float(row['engagement_rate'])
                for hour, row in hour_performance.iterrows()
            }
        }

    @staticmethod
    def analyze_content_length(posts_df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze if content length affects engagement"""
        if posts_df is None or posts_df.empty:
            return {'error': 'No data available'}

        # Find text column
        text_col = None
        for col in ['text', 'caption', 'description', 'message']:
            if col in posts_df.columns:
                text_col = col
                break

        if not text_col:
            return {'info': 'No text content available'}

        # Calculate text length
        posts_df['text_length'] = posts_df[text_col].fillna('').astype(str).str.len()

        # Calculate engagement rate
        posts_df['engagement_rate'] = posts_df.apply(
            lambda row: (row.get('interactions', 0) / row.get('reach', 1) * 100) if row.get('reach', 0) > 0 else 0,
            axis=1
        )

        # Categorize by length
        posts_df['length_category'] = pd.cut(
            posts_df['text_length'],
            bins=[0, 50, 150, 300, 1000],
            labels=['Very Short (0-50)', 'Short (50-150)', 'Medium (150-300)', 'Long (300+)']
        )

        length_performance = posts_df.groupby('length_category', observed=True).agg({
            'engagement_rate': 'mean',
            'reach': 'mean',
            'text_length': 'count'
        }).round(2)

        return {
            'avg_text_length': float(posts_df['text_length'].mean()),
            'median_text_length': float(posts_df['text_length'].median()),
            'length_vs_engagement': {
                str(cat): {
                    'avg_engagement': float(row['engagement_rate']),
                    'avg_reach': float(row['reach']),
                    'post_count': int(row['text_length'])
                }
                for cat, row in length_performance.iterrows()
            }
        }

    @staticmethod
    def analyze_hashtag_usage(posts_df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze hashtag patterns and effectiveness"""
        if posts_df is None or posts_df.empty:
            return {'error': 'No data available'}

        # Find text column
        text_col = None
        for col in ['text', 'caption', 'description', 'message']:
            if col in posts_df.columns:
                text_col = col
                break

        if not text_col:
            return {'info': 'No text content available'}

        # Extract hashtags
        posts_df['hashtags'] = posts_df[text_col].fillna('').astype(str).str.findall(r'#\w+')
        posts_df['hashtag_count'] = posts_df['hashtags'].str.len()

        # Calculate engagement rate
        posts_df['engagement_rate'] = posts_df.apply(
            lambda row: (row.get('interactions', 0) / row.get('reach', 1) * 100) if row.get('reach', 0) > 0 else 0,
            axis=1
        )

        # Overall hashtag stats
        total_posts_with_hashtags = (posts_df['hashtag_count'] > 0).sum()
        avg_hashtags_per_post = posts_df['hashtag_count'].mean()

        # Hashtag count vs engagement
        hashtag_performance = posts_df.groupby('hashtag_count').agg({
            'engagement_rate': 'mean',
            'reach': 'mean',
            'hashtag_count': 'count'
        }).round(2)

        # Most used hashtags
        all_hashtags = []
        for tags in posts_df['hashtags']:
            all_hashtags.extend(tags)

        hashtag_frequency = Counter(all_hashtags).most_common(20)

        return {
            'posts_with_hashtags': int(total_posts_with_hashtags),
            'posts_without_hashtags': int(len(posts_df) - total_posts_with_hashtags),
            'avg_hashtags_per_post': float(avg_hashtags_per_post),
            'hashtag_count_vs_engagement': {
                int(count): {
                    'avg_engagement': float(row['engagement_rate']),
                    'post_count': int(row['hashtag_count'])
                }
                for count, row in hashtag_performance.iterrows() if count <= 10
            },
            'most_used_hashtags': [
                {'hashtag': tag, 'count': count}
                for tag, count in hashtag_frequency[:15]
            ]
        }

    @staticmethod
    def analyze_performance_trends(posts_df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze how performance changes over time"""
        if posts_df is None or posts_df.empty:
            return {'error': 'No data available'}

        # Find date column
        date_col = None
        for col in ['publishDate', 'date', 'createdAt', 'timestamp']:
            if col in posts_df.columns:
                date_col = col
                break

        if not date_col:
            return {'error': 'No date column found'}

        posts_df[date_col] = pd.to_datetime(posts_df[date_col], errors='coerce')
        posts_df = posts_df.dropna(subset=[date_col])
        posts_df = posts_df.sort_values(date_col)

        # Calculate engagement rate
        posts_df['engagement_rate'] = posts_df.apply(
            lambda row: (row.get('interactions', 0) / row.get('reach', 1) * 100) if row.get('reach', 0) > 0 else 0,
            axis=1
        )

        # Weekly trends
        posts_df['week'] = posts_df[date_col].dt.to_period('W')
        weekly_metrics = posts_df.groupby('week').agg({
            'engagement_rate': 'mean',
            'reach': 'mean',
            'interactions': 'sum',
            date_col: 'count'
        }).round(2)

        weekly_metrics = weekly_metrics.rename(columns={date_col: 'post_count'})

        # Calculate growth
        if len(weekly_metrics) >= 2:
            first_week = weekly_metrics.iloc[0]
            last_week = weekly_metrics.iloc[-1]

            engagement_growth = ((last_week['engagement_rate'] - first_week['engagement_rate']) /
                               first_week['engagement_rate'] * 100) if first_week['engagement_rate'] > 0 else 0
            reach_growth = ((last_week['reach'] - first_week['reach']) /
                          first_week['reach'] * 100) if first_week['reach'] > 0 else 0
        else:
            engagement_growth = 0
            reach_growth = 0

        return {
            'weekly_performance': {
                str(week): {
                    'avg_engagement': float(row['engagement_rate']),
                    'avg_reach': float(row['reach']),
                    'total_interactions': int(row['interactions']),
                    'posts': int(row['post_count'])
                }
                for week, row in weekly_metrics.iterrows()
            },
            'growth_metrics': {
                'engagement_rate_change': round(engagement_growth, 2),
                'reach_change': round(reach_growth, 2),
            },
            'trend': 'improving' if engagement_growth > 5 else ('declining' if engagement_growth < -5 else 'stable')
        }
