# Debug Scripts for Metricool API Testing

This folder contains debug scripts to test specific Metricool API endpoints.

---

## 🎯 Purpose

These scripts help you:
- Test individual API endpoints without running the full fetcher
- Debug parameter format issues
- Verify authentication and credentials
- Inspect API responses in detail

---

## 📁 Files

### 1. `test_timeline_endpoint.py`
**Single endpoint test**

Tests one specific timeline metric with detailed output.

**What it tests:**
- `/v2/analytics/timelines` endpoint
- Instagram posts impressions timeline
- Correct parameter format (`from`/`to` with ISO 8601)

**Usage:**
```bash
cd /home/user/informe_marketing_01/metricool_data_fetcher
python debug/test_timeline_endpoint.py
```

**Output:**
- Shows exact URL and parameters being sent
- Displays full API response
- Saves response to `timeline_test_response.json`

---

### 2. `test_multiple_timelines.py`
**Multiple metrics test**

Tests multiple timeline metrics across Instagram and Facebook.

**What it tests:**
- 13 different timeline metrics
- Instagram: posts (count, impressions, engagement, reach, likes)
- Instagram: reels (count, engagement, videoviews)
- Facebook: posts (count, impressions, engagement)
- Facebook: account (likes, follows)

**Usage:**
```bash
cd /home/user/informe_marketing_01/metricool_data_fetcher
python debug/test_multiple_timelines.py
```

**Output:**
- Tests each metric one by one
- Shows success/failure for each
- Saves successful responses to individual JSON files
- Displays summary of results

---

## 🔧 Configuration

Both scripts automatically use your configuration from `config/config.py`:

- **Token:** `METRICOOL_TOKEN`
- **User ID:** `METRICOOL_USER_ID` (4226571)
- **Blog ID:** 3991897 (Sattvica)
- **Date Range:** `START_DATE` to `END_DATE` (2025-08-13 to 2025-11-13)

**No configuration needed!** Just run the scripts.

---

## 📊 Expected Output

### Successful Response (200)
```
✅ SUCCESS (Status: 200)
   Data points: 93
   First entry: ['2025-08-13', 1234]
   Saved to: timeline_instagram_impressions_posts.json
```

### Failed Response (400)
```
❌ FAILED (Status: 400)
   Error: {
     "status": "BAD_REQUEST",
     "code": "400",
     "detail": {
       "timeline.from": "must not be null"
     }
   }
```

---

## 🐛 Common Issues

### 1. Import Error
```
ModuleNotFoundError: No module named 'config'
```

**Solution:** Make sure you run from the correct directory:
```bash
cd /home/user/informe_marketing_01/metricool_data_fetcher
python debug/test_timeline_endpoint.py
```

### 2. Authentication Error (401)
```
❌ FAILED (Status: 401)
```

**Solution:** Check that your `METRICOOL_TOKEN` in `config/config.py` is correct and hasn't expired.

### 3. Bad Request Error (400)
```
"detail": {"timeline.from": "must not be null"}
```

**Solution:** This means the date parameters are wrong. The fix should already handle this.

### 4. Forbidden Error (403)
```
❌ FAILED (Status: 403)
   "detail": "There is no instagram connection for blog: 3991897"
```

**Solution:** The platform is not connected to the Sattvica brand. Try a different network.

---

## 📝 Example: Testing a Specific Metric

To test a different metric, edit `test_timeline_endpoint.py`:

```python
# Change these lines:
params = {
    # ...
    'network': 'facebook',      # Change network
    'metric': 'engagement',     # Change metric
    'subject': 'posts',         # Change subject
    # ...
}
```

**Valid combinations:**

| Network | Subject | Metrics |
|---------|---------|---------|
| instagram | posts | count, impressions, engagement, reach, likes, comments, saves, interactions |
| instagram | reels | count, likes, comments, engagement, reach, videoviews, interactions |
| facebook | posts | count, impressions, engagement, clicks, comments, shares, reactions, interactions |
| facebook | reels | count, engagement |
| facebook | account | likes, pageFollows, pageImpressions, postsCount, postsInteractions |

---

## 💾 Output Files

Successful tests save responses to:

```
debug/
├── timeline_test_response.json                  # Single test result
├── timeline_instagram_count_posts.json          # Multiple test results
├── timeline_instagram_impressions_posts.json
├── timeline_instagram_engagement_posts.json
├── timeline_facebook_likes_account.json
└── ... (one file per successful test)
```

These files contain the actual API response data in JSON format.

---

## 🔍 Debugging Tips

1. **Check the exact URL and parameters:**
   - The script prints everything being sent
   - Compare with Swagger documentation

2. **Verify date format:**
   - Should be: `2025-08-13T00:00:00` (ISO 8601)
   - NOT: `20250813` (YYYYMMDD integer)

3. **Test incrementally:**
   - Start with `test_timeline_endpoint.py` (single test)
   - If that works, run `test_multiple_timelines.py`
   - If issues persist, check specific network/metric combinations

4. **Check API response:**
   - 200 = Success
   - 400 = Bad Request (parameter error)
   - 401 = Authentication failed
   - 403 = Forbidden (platform not connected)
   - 404 = Endpoint not found
   - 500 = Server error

---

## ✅ Quick Test

Run this to verify everything works:

```bash
cd /home/user/informe_marketing_01/metricool_data_fetcher
python debug/test_timeline_endpoint.py
```

If you see `✅ SUCCESS!` then the fix is working!

---

**Created:** 2025-11-14
**Purpose:** Debug timeline endpoint parameter issues
**Status:** Ready to use
