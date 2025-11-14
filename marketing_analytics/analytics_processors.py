"""
Analytics Processors
Functions to analyze different aspects of social media data
"""

import logging
from typing import Dict, List, Any, Optional
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import re
from collections import defaultdict

logger = logging.getLogger(__name__)


class EngagementAnalyzer:
    """Analyze engagement metrics across platforms"""

    @staticmethod
    def calculate_engagement_rate(row: pd.Series) -> float:
        """Calculate engagement rate for a post"""
        try:
            interactions = row.get('interactions', 0) or 0
            reach = row.get('reach', 0) or 0
            impressions = row.get('impressions', 0) or 0

            # Use reach if available, otherwise impressions
            denominator = reach if reach > 0 else impressions
            if denominator == 0:
                return 0.0

            return (interactions / denominator) * 100
        except Exception as e:
            logger.error(f"Error calculating engagement rate: {e}")
            return 0.0

    @staticmethod
    def analyze_platform_engagement(posts_df: pd.DataFrame, platform: str) -> Dict[str, Any]:
        """Analyze engagement for a platform"""
        if posts_df is None or posts_df.empty:
            return {'platform': platform, 'error': 'No data available'}

        # Calculate engagement rates
        posts_df['engagement_rate'] = posts_df.apply(
            EngagementAnalyzer.calculate_engagement_rate, axis=1
        )

        analysis = {
            'platform': platform,
            'total_posts': len(posts_df),
            'avg_engagement_rate': posts_df['engagement_rate'].mean(),
            'median_engagement_rate': posts_df['engagement_rate'].median(),
            'max_engagement_rate': posts_df['engagement_rate'].max(),
            'min_engagement_rate': posts_df['engagement_rate'].min(),
        }

        # Aggregate metrics
        numeric_cols = ['interactions', 'reach', 'impressions', 'likes', 'comments', 'shares']
        for col in numeric_cols:
            if col in posts_df.columns:
                analysis[f'total_{col}'] = posts_df[col].sum()
                analysis[f'avg_{col}'] = posts_df[col].mean()

        # Best performing post
        if not posts_df.empty:
            best_post = posts_df.loc[posts_df['engagement_rate'].idxmax()]
            analysis['best_post'] = {
                'engagement_rate': best_post['engagement_rate'],
                'reach': best_post.get('reach', 'N/A'),
                'interactions': best_post.get('interactions', 'N/A'),
            }
            if 'text' in best_post:
                analysis['best_post']['preview'] = str(best_post['text'])[:100]

        return analysis

    @staticmethod
    def compare_content_types(instagram_posts_df: pd.DataFrame,
                             instagram_reels_df: pd.DataFrame) -> Dict[str, Any]:
        """Compare performance of posts vs reels"""
        comparison = {}

        if instagram_posts_df is not None and not instagram_posts_df.empty:
            instagram_posts_df['engagement_rate'] = instagram_posts_df.apply(
                EngagementAnalyzer.calculate_engagement_rate, axis=1
            )
            comparison['posts'] = {
                'count': len(instagram_posts_df),
                'avg_engagement': instagram_posts_df['engagement_rate'].mean(),
                'avg_reach': instagram_posts_df.get('reach', pd.Series([0])).mean(),
            }

        if instagram_reels_df is not None and not instagram_reels_df.empty:
            instagram_reels_df['engagement_rate'] = instagram_reels_df.apply(
                EngagementAnalyzer.calculate_engagement_rate, axis=1
            )
            comparison['reels'] = {
                'count': len(instagram_reels_df),
                'avg_engagement': instagram_reels_df['engagement_rate'].mean(),
                'avg_reach': instagram_reels_df.get('reach', pd.Series([0])).mean(),
            }

        # Performance comparison
        if 'posts' in comparison and 'reels' in comparison:
            posts_eng = comparison['posts']['avg_engagement']
            reels_eng = comparison['reels']['avg_engagement']

            if posts_eng > 0:
                comparison['winner'] = 'reels' if reels_eng > posts_eng else 'posts'
                comparison['performance_difference_pct'] = (
                    abs(reels_eng - posts_eng) / posts_eng * 100
                )

        return comparison


class TrendAnalyzer:
    """Analyze trends over time"""

    @staticmethod
    def analyze_timeline_trend(timeline_df: pd.DataFrame, metric_name: str) -> Dict[str, Any]:
        """Analyze trend for a timeline metric"""
        if timeline_df is None or timeline_df.empty or 'date' not in timeline_df.columns:
            return {'metric': metric_name, 'error': 'No data available'}

        timeline_df = timeline_df.sort_values('date')

        # Get value column (usually 'value' or metric name)
        value_col = 'value' if 'value' in timeline_df.columns else timeline_df.columns[-1]

        analysis = {
            'metric': metric_name,
            'data_points': len(timeline_df),
            'date_range': {
                'start': timeline_df['date'].min().strftime('%Y-%m-%d'),
                'end': timeline_df['date'].max().strftime('%Y-%m-%d'),
            },
            'total': timeline_df[value_col].sum(),
            'average': timeline_df[value_col].mean(),
            'peak': timeline_df[value_col].max(),
            'lowest': timeline_df[value_col].min(),
        }

        # Calculate growth rate
        if len(timeline_df) >= 2:
            first_value = timeline_df[value_col].iloc[0]
            last_value = timeline_df[value_col].iloc[-1]

            if first_value > 0:
                growth_rate = ((last_value - first_value) / first_value) * 100
                analysis['growth_rate_pct'] = growth_rate
                analysis['trend'] = 'increasing' if growth_rate > 5 else ('decreasing' if growth_rate < -5 else 'stable')

        # Find peak date
        peak_idx = timeline_df[value_col].idxmax()
        analysis['peak_date'] = timeline_df.loc[peak_idx, 'date'].strftime('%Y-%m-%d')

        return analysis

    @staticmethod
    def weekly_pattern_analysis(timeline_df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze weekly patterns in timeline data"""
        if timeline_df is None or timeline_df.empty or 'date' not in timeline_df.columns:
            return {'error': 'No data available'}

        timeline_df = timeline_df.copy()
        timeline_df['weekday'] = timeline_df['date'].dt.day_name()
        timeline_df['week'] = timeline_df['date'].dt.isocalendar().week

        value_col = 'value' if 'value' in timeline_df.columns else timeline_df.columns[-1]

        # Average by day of week
        weekday_avg = timeline_df.groupby('weekday')[value_col].mean().to_dict()

        # Best and worst days
        best_day = max(weekday_avg, key=weekday_avg.get)
        worst_day = min(weekday_avg, key=weekday_avg.get)

        return {
            'weekday_averages': weekday_avg,
            'best_day': best_day,
            'worst_day': worst_day,
        }


class DemographicAnalyzer:
    """Analyze audience demographics"""

    @staticmethod
    def analyze_demographics(demo_data: Dict[str, Any], demo_type: str) -> Dict[str, Any]:
        """Analyze demographic data (age, gender, location)"""
        if not demo_data or 'data' not in demo_data:
            return {'type': demo_type, 'error': 'No data available'}

        data = demo_data['data']

        if isinstance(data, list):
            # Convert to dict format
            total = sum(item.get('value', 0) for item in data)
            distribution = {
                item.get('name', item.get('label', 'Unknown')): {
                    'value': item.get('value', 0),
                    'percentage': (item.get('value', 0) / total * 100) if total > 0 else 0
                }
                for item in data
            }
        elif isinstance(data, dict):
            total = sum(data.values())
            distribution = {
                key: {
                    'value': value,
                    'percentage': (value / total * 100) if total > 0 else 0
                }
                for key, value in data.items()
            }
        else:
            return {'type': demo_type, 'error': 'Unsupported data format'}

        # Find top segments
        sorted_segments = sorted(
            distribution.items(),
            key=lambda x: x[1]['value'],
            reverse=True
        )

        analysis = {
            'type': demo_type,
            'total_audience': total,
            'distribution': distribution,
            'top_3_segments': [
                {
                    'name': seg[0],
                    'value': seg[1]['value'],
                    'percentage': seg[1]['percentage']
                }
                for seg in sorted_segments[:3]
            ]
        }

        return analysis


class ContentPerformanceAnalyzer:
    """Analyze content performance"""

    @staticmethod
    def find_top_performing_content(posts_df: pd.DataFrame, metric: str = 'engagement_rate',
                                   top_n: int = 10) -> List[Dict[str, Any]]:
        """Find top performing content by metric"""
        if posts_df is None or posts_df.empty:
            return []

        # Calculate engagement rate if needed
        if metric == 'engagement_rate' and metric not in posts_df.columns:
            posts_df['engagement_rate'] = posts_df.apply(
                EngagementAnalyzer.calculate_engagement_rate, axis=1
            )

        # Sort by metric
        if metric not in posts_df.columns:
            logger.warning(f"Metric {metric} not found in DataFrame")
            return []

        top_posts = posts_df.nlargest(top_n, metric)

        results = []
        for idx, post in top_posts.iterrows():
            result = {
                'metric_value': post[metric],
                'reach': post.get('reach', 'N/A'),
                'interactions': post.get('interactions', 'N/A'),
                'likes': post.get('likes', 'N/A'),
                'comments': post.get('comments', 'N/A'),
            }

            # Add post ID/permalink/URL if available
            id_fields = ['id', 'postId', 'post_id', 'shortcode', 'permalink', 'url', 'link']
            for field in id_fields:
                if field in post and pd.notna(post[field]):
                    result['post_id'] = str(post[field])
                    break

            # Add shortcode if available (for Instagram URL construction)
            if 'shortcode' in post and pd.notna(post['shortcode']):
                result['shortcode'] = str(post['shortcode'])

            # Add permalink/URL if available
            url_fields = ['permalink', 'url', 'link', 'postUrl']
            for field in url_fields:
                if field in post and pd.notna(post[field]):
                    result['url'] = str(post[field])
                    break

            # Add text preview if available
            text_fields = ['text', 'caption', 'description', 'message']
            for field in text_fields:
                if field in post and pd.notna(post[field]):
                    result['preview'] = str(post[field])[:150] + '...'
                    result['full_text'] = str(post[field])  # Keep full text for detailed view
                    break

            # Add date if available
            date_fields = ['publishDate', 'date', 'createdAt']
            for field in date_fields:
                if field in post and pd.notna(post[field]):
                    result['date'] = str(post[field])
                    break

            results.append(result)

        return results

    @staticmethod
    def analyze_hashtag_performance(hashtag_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze hashtag tracking data"""
        if not hashtag_data or 'data' not in hashtag_data:
            return {'error': 'No hashtag data available'}

        sessions = hashtag_data['data']

        analysis = {
            'total_tracked_sessions': len(sessions),
            'sessions': []
        }

        for session in sessions:
            session_info = {
                'id': session.get('id'),
                'hashtag': session.get('hashtag', session.get('name', 'Unknown')),
                'status': session.get('status', 'Unknown'),
            }

            # Extract metrics if available
            if 'metrics' in session:
                session_info['metrics'] = session['metrics']

            analysis['sessions'].append(session_info)

        return analysis


class HashtagAnalyzer:
    """Analyze hashtag performance from post content"""

    @staticmethod
    def extract_hashtags(text: str) -> List[str]:
        """Extract hashtags from text"""
        if not text or not isinstance(text, str):
            return []

        # Find all hashtags (# followed by word characters, allowing underscores and numbers)
        hashtags = re.findall(r'#(\w+)', text)

        # Return lowercase versions for consistency
        return [tag.lower() for tag in hashtags]

    @staticmethod
    def analyze_hashtag_performance(posts_df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze hashtag performance from posts"""
        if posts_df is None or posts_df.empty:
            return {'error': 'No post data available'}

        # Calculate engagement rate if not present
        if 'engagement_rate' not in posts_df.columns:
            posts_df['engagement_rate'] = posts_df.apply(
                EngagementAnalyzer.calculate_engagement_rate, axis=1
            )

        # Extract hashtags from all available text fields
        hashtag_stats = defaultdict(lambda: {
            'count': 0,
            'total_engagement': 0,
            'total_reach': 0,
            'total_interactions': 0,
            'post_ids': []
        })

        text_fields = ['text', 'caption', 'description', 'content', 'message', 'full_text', 'preview']

        for idx, post in posts_df.iterrows():
            # Get post text from available fields
            post_text = ''
            for field in text_fields:
                if field in post and pd.notna(post[field]):
                    post_text = str(post[field])
                    break

            if not post_text:
                continue

            # Extract hashtags
            hashtags = HashtagAnalyzer.extract_hashtags(post_text)

            if not hashtags:
                continue

            # Get post metrics
            engagement_rate = post.get('engagement_rate', 0)
            reach = post.get('reach', 0) if pd.notna(post.get('reach')) else 0
            interactions = post.get('interactions', 0) if pd.notna(post.get('interactions')) else 0

            # Update stats for each hashtag
            for hashtag in hashtags:
                hashtag_stats[hashtag]['count'] += 1
                hashtag_stats[hashtag]['total_engagement'] += engagement_rate
                hashtag_stats[hashtag]['total_reach'] += reach
                hashtag_stats[hashtag]['total_interactions'] += interactions

                # Store post ID if available
                post_id = None
                id_fields = ['id', 'postId', 'post_id', 'shortcode']
                for field in id_fields:
                    if field in post and pd.notna(post[field]):
                        post_id = str(post[field])
                        break
                if post_id:
                    hashtag_stats[hashtag]['post_ids'].append(post_id)

        # Calculate averages and create results
        hashtag_results = []
        for hashtag, stats in hashtag_stats.items():
            count = stats['count']
            result = {
                'hashtag': f"#{hashtag}",
                'usage_count': count,
                'avg_engagement_rate': stats['total_engagement'] / count if count > 0 else 0,
                'avg_reach': stats['total_reach'] / count if count > 0 else 0,
                'avg_interactions': stats['total_interactions'] / count if count > 0 else 0,
                'total_reach': stats['total_reach'],
                'total_interactions': stats['total_interactions']
            }
            hashtag_results.append(result)

        # Sort by average engagement rate
        hashtag_results.sort(key=lambda x: x['avg_engagement_rate'], reverse=True)

        # Get overall stats
        posts_with_hashtags = 0
        posts_without_hashtags = 0

        for idx, post in posts_df.iterrows():
            post_text = ''
            for field in text_fields:
                if field in post and pd.notna(post[field]):
                    post_text = str(post[field])
                    break

            hashtags = HashtagAnalyzer.extract_hashtags(post_text)
            if hashtags:
                posts_with_hashtags += 1
            else:
                posts_without_hashtags += 1

        # Calculate average engagement for posts with vs without hashtags
        posts_df['has_hashtags'] = posts_df.apply(
            lambda row: len(HashtagAnalyzer.extract_hashtags(
                str(next((row[field] for field in text_fields if field in row and pd.notna(row[field])), ''))
            )) > 0,
            axis=1
        )

        avg_engagement_with_hashtags = posts_df[posts_df['has_hashtags']]['engagement_rate'].mean() if posts_with_hashtags > 0 else 0
        avg_engagement_without_hashtags = posts_df[~posts_df['has_hashtags']]['engagement_rate'].mean() if posts_without_hashtags > 0 else 0

        return {
            'hashtag_performance': hashtag_results,
            'total_unique_hashtags': len(hashtag_results),
            'posts_with_hashtags': posts_with_hashtags,
            'posts_without_hashtags': posts_without_hashtags,
            'avg_engagement_with_hashtags': avg_engagement_with_hashtags,
            'avg_engagement_without_hashtags': avg_engagement_without_hashtags,
            'hashtag_lift': ((avg_engagement_with_hashtags - avg_engagement_without_hashtags) / avg_engagement_without_hashtags * 100) if avg_engagement_without_hashtags > 0 else 0
        }
