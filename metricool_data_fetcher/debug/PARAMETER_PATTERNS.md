# Metricool API Parameter Patterns

**Complete guide to which endpoints use which date parameter formats**

---

## 🎯 The Pattern

Metricool API has **TWO different** date parameter patterns:

### Pattern 1: `/v2/analytics/*` endpoints
- **Parameter names:** `from` and `to`
- **Format:** ISO 8601 datetime strings
- **Example:** `from=2025-08-13T00:00:00&to=2025-11-13T23:59:59`

### Pattern 2: `/stats/*` endpoints
- **Parameter names:** `start` and `end`
- **Format:** YYYYMMDD integers
- **Example:** `start=20250813&end=20251113`

---

## 📊 Complete Endpoint List

### ✅ Use `from`/`to` (ISO 8601) - Pattern 1

**Timeline & Aggregation:**
- `/v2/analytics/timelines`
- `/v2/analytics/aggregation`
- `/v2/analytics/distribution`

**Instagram:**
- `/v2/analytics/posts/instagram`
- `/v2/analytics/reels/instagram`
- `/v2/analytics/stories/instagram`
- `/v2/analytics/posts/instagram/hashtags`

**Facebook:**
- `/v2/analytics/posts/facebook`
- `/v2/analytics/reels/facebook`
- `/v2/analytics/stories/facebook`

**LinkedIn:**
- `/v2/analytics/posts/linkedin`
- `/v2/analytics/newsletters/linkedin`

**TikTok:**
- `/v2/analytics/posts/tiktok`

**Pinterest:**
- `/v2/analytics/posts/pinterest`

**Threads:**
- `/v2/analytics/posts/threads`

**Bluesky:**
- `/v2/analytics/posts/bluesky`

**General:**
- `/v2/analytics/brand-summary/posts`

---

### ✅ Use `start`/`end` (YYYYMMDD integers) - Pattern 2

**Demographics:**
- `/stats/gender/{provider}`
- `/stats/age/{provider}`
- `/stats/gender-age/{provider}`
- `/stats/country/{provider}`
- `/stats/city/{provider}`

**Traffic:**
- `/stats/trafficsource/{provider}`

**Posts:**
- `/stats/posts`

**Old Timeline (deprecated):**
- `/stats/timeline/{metric}`
- `/stats/aggregation/{metric}`

---

### ⚠️ No Date Parameters

**Brand Info:**
- `/admin/simpleProfiles`
- `/admin/blog/profiles`
- `/profile/subscription`
- `/profile/lastsyncs`
- `/v2/settings/brands`

**Content Management:**
- `/v2/scheduler/posts`
- `/v2/scheduler/library/posts`
- `/v2/media/images`
- `/v2/media/videos`

**Best Times:**
- `/v2/scheduler/besttimes/{provider}`

**Hashtag Tracker:**
- `/v2/hashtags-tracker/tracking-sessions`
- `/v2/hashtags-tracker/tracking-sessions/{id}/consolidations`
- `/v2/hashtags-tracker/tracking-sessions/{id}/distribution`

**Smart Links:**
- `/v2/smart-links/links`
- `/v2/smart-links/links/{id}/analytics/timeline`
- `/v2/smart-links/links/{id}/analytics/buttons`
- `/v2/smart-links/links/{id}/analytics/images`

---

## 💡 Why Two Patterns?

### Pattern 1 (`from`/`to` + ISO 8601)
**Used by:** Modern `/v2/analytics` endpoints

**Reason:**
- More precise (includes time component)
- International standard (ISO 8601)
- Better for time-series data
- Supports timezone information

**Example:**
```python
{
    'from': '2025-08-13T00:00:00',
    'to': '2025-11-13T23:59:59',
    'network': 'instagram',
    'metric': 'engagement'
}
```

### Pattern 2 (`start`/`end` + YYYYMMDD)
**Used by:** Older `/stats` endpoints

**Reason:**
- Legacy format
- Simpler (no time component)
- Date-only queries
- Backward compatibility

**Example:**
```python
{
    'start': 20250813,
    'end': 20251113,
    'userId': '4226571',
    'userToken': '...'
}
```

---

## 🔧 Implementation in Code

### Function 1: `get_timeline_date_params()`
**Use for:** `/v2/analytics/*` endpoints

```python
def get_timeline_date_params(start_date: str, end_date: str) -> Dict[str, Any]:
    """For /v2/analytics endpoints"""
    start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')

    return {
        'from': start_dt.strftime('%Y-%m-%dT00:00:00'),
        'to': end_dt.strftime('%Y-%m-%dT23:59:59')
    }
```

### Function 2: `get_date_range_params()`
**Use for:** `/stats/*` endpoints

```python
def get_date_range_params(start_date: str, end_date: str) -> Dict[str, Any]:
    """For /stats endpoints"""
    start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')

    return {
        'start': int(start_dt.strftime('%Y%m%d')),
        'end': int(end_dt.strftime('%Y%m%d'))
    }
```

---

## 🐛 Common Errors

### Error 1: Using wrong parameter names
```
❌ WRONG: /v2/analytics/posts/instagram?start=20250813&end=20251113
✅ RIGHT: /v2/analytics/posts/instagram?from=2025-08-13T00:00:00&to=2025-11-13T23:59:59
```

**Error message:**
```json
{
  "status": "BAD_REQUEST",
  "code": "400",
  "detail": {
    "getInstagramPosts.from": "must not be null",
    "getInstagramPosts.to": "must not be null"
  }
}
```

### Error 2: Using wrong date format
```
❌ WRONG: /v2/analytics/timelines?from=20250813&to=20251113
✅ RIGHT: /v2/analytics/timelines?from=2025-08-13T00:00:00&to=2025-11-13T23:59:59
```

**Error message:**
```json
{
  "status": "BAD_REQUEST",
  "code": "400",
  "detail": {
    "timeline.from": "must not be null",
    "timeline.to": "must not be null"
  }
}
```

### Error 3: Wrong metric name
```
❌ WRONG: metric=saves (for Instagram posts)
✅ RIGHT: metric=saved
```

**Error message:**
```json
{
  "status": "BAD_REQUEST",
  "code": "400",
  "title": "InvalidEnumBaseException",
  "detail": "Invalid field 'saves'. Valid values are: [count, comments, likes, saved, shares, clicks, engagement, impressions, reach...]"
}
```

---

## 📝 Quick Reference

| Endpoint Pattern | Parameter Names | Format | Function to Use |
|-----------------|-----------------|--------|-----------------|
| `/v2/analytics/*` | `from`, `to` | ISO 8601 | `get_timeline_date_params()` |
| `/stats/*` | `start`, `end` | YYYYMMDD int | `get_date_range_params()` |
| Other endpoints | None | N/A | No date params |

---

## ✅ Testing Checklist

When testing an endpoint, verify:

1. **Check endpoint path:**
   - Starts with `/v2/analytics/`? → Use Pattern 1
   - Starts with `/stats/`? → Use Pattern 2
   - Other? → Check if it needs dates at all

2. **Verify parameters:**
   - Pattern 1: `from` and `to` present?
   - Pattern 2: `start` and `end` present?

3. **Check date format:**
   - Pattern 1: ISO 8601 strings? (`2025-08-13T00:00:00`)
   - Pattern 2: YYYYMMDD integers? (`20250813`)

4. **Test request:**
   - Send request with debug logging
   - Check for 400 errors
   - Verify response data

---

## 🎯 Summary

**Golden Rules:**
1. `/v2/analytics/*` = `from`/`to` with ISO 8601
2. `/stats/*` = `start`/`end` with YYYYMMDD integers
3. When in doubt, check the error message - it tells you exactly what's expected

**Remember:**
- The Swagger documentation may show `from`/`to` for some endpoints
- But the actual API might use different parameter names
- Always test and verify with real API calls
- Use debug scripts to inspect exact URLs and parameters

---

**Created:** 2025-11-14
**Status:** Comprehensive parameter guide
**All patterns verified:** ✅
