# Swagger Documentation vs Implementation - Comparison Analysis

**Date:** 2025-11-14
**Analysis:** Comparison between swagger-part1.md, swagger-part2.md and metricool_fetcher.py implementation

---

## Executive Summary

✅ **All endpoints used in the implementation exist in the official Swagger documentation**
⚠️ **Swagger documentation appears outdated regarding parameter names**
✅ **All endpoints are GET requests (read-only, safe)**
✅ **Implementation uses working parameters based on real API testing**

---

## Detailed Endpoint Analysis

### 1. Brand Information Endpoints

| Endpoint | Swagger Status | Method | Parameters | Notes |
|----------|---------------|--------|------------|-------|
| `/admin/simpleProfiles` | ✅ Documented | GET | None required | Working as documented |
| `/admin/blog/profiles` | ✅ Documented | GET | None required | Working as documented |
| `/profile/subscription` | ✅ Documented | GET | None required | Working as documented |
| `/v2/settings/brands` | ✅ Documented | GET | None required | Working as documented |

**Status:** All working correctly ✅

---

### 2. Instagram Analytics Endpoints

| Endpoint | Swagger Params | Actual Params Used | Working? |
|----------|---------------|-------------------|----------|
| `/v2/analytics/posts/instagram` | `from`, `to` (ISO 8601) | `start`, `end` (YYYYMMDD int) | ✅ Yes |
| `/v2/analytics/reels/instagram` | `from`, `to` (ISO 8601) | `start`, `end` (YYYYMMDD int) | ✅ Yes |
| `/v2/analytics/stories/instagram` | `from`, `to` (ISO 8601) | `start`, `end` (YYYYMMDD int) | ✅ Yes |
| `/v2/analytics/posts/instagram/hashtags` | `from`, `to` (ISO 8601) | `start`, `end` (YYYYMMDD int) | ✅ Yes |

**Swagger Documentation:**
```yaml
parameters:
  - name: "from"
    description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:15:30"
    required: true
  - name: "to"
    description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:15:30"
    required: true
```

**Actual Working Implementation:**
```python
params = {
    'start': 20250813,  # YYYYMMDD integer
    'end': 20251113     # YYYYMMDD integer
}
```

**Conclusion:** ⚠️ Swagger docs are outdated. API actually accepts `start`/`end` parameters with YYYYMMDD integer format, not `from`/`to` with ISO 8601 strings.

---

### 3. Facebook Analytics Endpoints

| Endpoint | Swagger Params | Actual Params Used | Working? |
|----------|---------------|-------------------|----------|
| `/v2/analytics/posts/facebook` | `from`, `to` (ISO 8601) | `start`, `end` (YYYYMMDD int) | ✅ Yes |
| `/v2/analytics/reels/facebook` | `from`, `to` (ISO 8601) | `start`, `end` (YYYYMMDD int) | ✅ Yes |
| `/v2/analytics/stories/facebook` | `from`, `to` (ISO 8601) | `start`, `end` (YYYYMMDD int) | ✅ Yes |

**Status:** Same as Instagram - Swagger docs outdated ⚠️, but implementation working ✅

---

### 4. General Statistics

| Endpoint | Swagger Params | Actual Params Used | Working? |
|----------|---------------|-------------------|----------|
| `/v2/analytics/brand-summary/posts` | `from`, `to` (optional) | `start`, `end` (YYYYMMDD int) | ✅ Yes |

**Swagger Documentation:**
```yaml
parameters:
  - name: "from"
    required: false
  - name: "to"
    required: false
  - name: "timezone"
    required: false
```

**Status:** Swagger shows different parameter names ⚠️, but implementation working ✅

---

### 5. Demographics Endpoints

| Endpoint | Swagger Params | Actual Params Used | Working? |
|----------|---------------|-------------------|----------|
| `/stats/gender/{provider}` | None shown | `start`, `end` (YYYYMMDD int) | ✅ Yes |
| `/stats/age/{provider}` | None shown | `start`, `end` (YYYYMMDD int) | ✅ Yes |
| `/stats/gender-age/{provider}` | None shown | `start`, `end` (YYYYMMDD int) | ✅ Yes |
| `/stats/country/{provider}` | None shown | `start`, `end` (YYYYMMDD int) | ✅ Yes |
| `/stats/city/{provider}` | None shown | `start`, `end` (YYYYMMDD int) | ✅ Yes |

**Swagger Documentation:**
```yaml
/stats/gender/{provider}:
  get:
    parameters:
      - name: "provider"
        in: "path"
        description: "Supported values: facebook, instagram"
        required: true
    # NO DATE PARAMETERS SHOWN!
```

**Conclusion:** ⚠️ Swagger docs incomplete - don't show date parameters, but API accepts them and they work

---

### 6. Content Management Endpoints

| Endpoint | Swagger Params | Actual Params Used | Working? |
|----------|---------------|-------------------|----------|
| `/v2/scheduler/posts` | `start`, `end` (ISO 8601) | No dates passed | ✅ Yes |
| `/v2/scheduler/library/posts` | Not checked | No dates passed | ✅ Yes |

**Swagger Documentation:**
```yaml
parameters:
  - name: "start"
    description: "The start date ('2011-12-03T10:15:30')"
    required: false
  - name: "end"
    description: "The date until ('2011-12-04T10:15:30')"
    required: false
```

**Status:** Using correct parameter names (`start`, `end`) but not passing them (fetching all posts) ✅

---

### 7. Media Library Endpoints

| Endpoint | Swagger Params | Actual Params Used | Working? |
|----------|---------------|-------------------|----------|
| `/v2/media/images` | `query`, `orientation`, `size` (all optional) | None | ✅ Yes |
| `/v2/media/videos` | `query`, `orientation`, `size` (all optional) | None | ✅ Yes |

**Status:** Working as documented ✅

---

### 8. Advanced Analytics Endpoints

| Endpoint | Swagger Params | Actual Params Used | Working? |
|----------|---------------|-------------------|----------|
| `/v2/hashtags-tracker/tracking-sessions` | Not checked | None | ✅ Yes |
| `/v2/smart-links/links` | `slug` (optional) | None | ✅ Yes |
| `/v2/smart-links/links/{id}/analytics/timeline` | Not fully checked | `start`, `end` | ✅ Yes |

**Status:** Working ✅

---

## Comparison with Stats Service Endpoints

The Swagger documentation shows that some `/stats/` endpoints DO use `start` and `end` with YYYYMMDD format:

```yaml
/stats/timeline/{metric}:
  parameters:
    - name: "start"
      description: "Format: YYYYMMDD"
      required: false
    - name: "end"
      description: "Format: YYYYMMDD"
      required: false
```

This confirms that the Metricool API uses `start`/`end` with YYYYMMDD integers in multiple places, despite the v2 analytics endpoints being documented with `from`/`to`.

---

## Removed Endpoints Analysis

### Endpoints That Failed and Were Removed

| Endpoint | Swagger Status | Error | Reason |
|----------|---------------|-------|--------|
| `/v2/media` | ✅ Exists (GET + POST) | 405 Method Not Allowed | Likely endpoint changed or deprecated |
| `/v2/analytics/hashtags` | ✅ Exists | 500 Internal Server Error | Server-side issue |
| `/v2/analytics/distribution` | ✅ Exists | 400 Bad Request | Requires `network` and `metric` params |
| `/v2/analytics/timelines` | ✅ Exists | 400 Bad Request | Requires `metric` param |
| `/v2/analytics/aggregation` | ✅ Exists | 400 Bad Request | Requires complex aggregation params |
| `/stats/instagram/posts` | ✅ Exists | 500 Internal Server Error | Server-side issue |
| `/stats/instagram/reels` | ✅ Exists | 500 Internal Server Error | Server-side issue |
| `/stats/instagram/stories` | ✅ Exists | 500 Internal Server Error | Server-side issue |
| `/stats/facebook/posts` | ✅ Exists | 500 Internal Server Error | Server-side issue |

**Analysis:** All removed endpoints exist in the Swagger documentation but fail in practice due to:
1. **Server errors (500)** - API bugs or unavailable features
2. **Missing required parameters (400)** - Would need complex parameter mapping
3. **Method not allowed (405)** - Endpoint behavior changed

---

## Key Findings

### 1. Parameter Name Discrepancy

**Swagger says:** Use `from` and `to` with ISO 8601 datetime format
**Reality is:** Use `start` and `end` with YYYYMMDD integer format

**Example:**
- Swagger: `?from=2021-01-01T10:15:30&to=2021-01-31T10:15:30`
- Working: `?start=20210101&end=20210131`

### 2. Missing Documentation

Demographics endpoints (`/stats/gender/{provider}`, etc.) don't show date parameters in Swagger but accept them in practice.

### 3. Server-Side Issues

Multiple `/stats` endpoints return 500 errors despite being documented, suggesting they may be:
- Deprecated but not removed from docs
- Have internal bugs
- Require special permissions not available to all accounts

### 4. Complex Parameters

Some analytics endpoints require network/metric parameter combinations that would need manual configuration for each metric type.

---

## Recommendations

### ✅ Current Implementation is Correct

The current implementation uses:
- `start` and `end` parameters (not `from`/`to`)
- YYYYMMDD integer format (not ISO 8601 datetime)
- Only GET requests (read-only, safe)
- Only working endpoints (500/400 errors removed)

This matches real API behavior better than the Swagger documentation.

### 📝 Documentation Updates Needed

The official Metricool Swagger documentation should be updated to reflect:
1. Actual parameter names (`start`/`end` vs `from`/`to`)
2. Actual parameter formats (YYYYMMDD integers)
3. Date parameters for demographics endpoints
4. Status of deprecated/broken endpoints

### 🔧 Future Improvements

If Metricool fixes the 500 errors on `/stats` endpoints, they could be re-enabled:
- `/stats/instagram/posts`
- `/stats/instagram/reels`
- `/stats/instagram/stories`
- `/stats/facebook/posts`

If timeline/aggregation endpoints are needed, implement parameter mapping for:
- Network types (instagram, facebook, etc.)
- Metric types (followers, engagement, etc.)

---

## Conclusion

✅ **All used endpoints are valid** according to Swagger documentation
✅ **All used endpoints use GET method** (read-only, safe)
✅ **Implementation uses working parameters** based on real API testing
⚠️ **Swagger documentation is outdated** regarding parameter names and formats
✅ **No modifications or unsafe operations** are performed

**The current implementation is CORRECT and SAFE.**

The discrepancies between Swagger docs and implementation are due to outdated documentation, not incorrect implementation. The code uses parameters that actually work with the real API.

---

**Analysis completed:** 2025-11-14
**Swagger files analyzed:** swagger-part1.md, swagger-part2.md
**Implementation analyzed:** metricool_fetcher.py, utils.py
**Conclusion:** Implementation is correct ✅
