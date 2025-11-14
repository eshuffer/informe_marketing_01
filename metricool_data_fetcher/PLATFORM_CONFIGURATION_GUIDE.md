# Platform Detection and Configuration Guide

**Auto-detect connected platforms and control what data to fetch!**

---

## 🎯 What This Does

The fetcher now:
1. **Automatically detects** which platforms Sattvica has connected
2. **Shows you** a clear status of each platform at startup
3. **Only fetches** from platforms you want (configured in config.py)
4. **Saves time** by skipping unavailable or disabled platforms

---

## 📊 Startup Output Example

When you run the fetcher, you'll see:

```
================================================================================
PLATFORM AVAILABILITY FOR SATTVICA
================================================================================

✅ CONNECTED PLATFORMS:
   • INSTAGRAM      - ✓ ENABLED
   • FACEBOOK       - ✓ ENABLED
   • LINKEDIN       - ✗ DISABLED IN CONFIG
   • TIKTOK         - ✓ ENABLED

⚠️  DISABLED IN CONFIG (will skip even if connected):
   • TWITTER
   • YOUTUBE
   • BLUESKY

💡 PLATFORMS THAT WILL BE FETCHED:
   • INSTAGRAM
   • FACEBOOK
   • TIKTOK

📝 To enable/disable platforms, edit: config/config.py -> PLATFORMS_ENABLED
================================================================================
```

This tells you exactly what will happen before fetching starts!

---

## ⚙️ How to Configure Platforms

### Edit: `config/config.py`

```python
# Platform Configuration
# Set to True to fetch data from that platform, False to skip
PLATFORMS_ENABLED = {
    'instagram': True,    # ✅ Fetch Instagram data
    'facebook': True,     # ✅ Fetch Facebook data
    'linkedin': True,     # ✅ Fetch LinkedIn data (if connected)
    'twitter': False,     # ❌ Skip Twitter even if connected
    'tiktok': True,       # ✅ Fetch TikTok data (if connected)
    'youtube': False,     # ❌ Skip YouTube even if connected
    'pinterest': True,    # ✅ Fetch Pinterest data (if connected)
    'threads': True,      # ✅ Fetch Threads data (if connected)
    'bluesky': False,     # ❌ Skip Bluesky even if connected
}
```

**Rules:**
- `True` = Fetch data IF the platform is connected
- `False` = Skip data EVEN IF the platform is connected

---

## 🎛️ Feature Configuration

You can also enable/disable entire features:

```python
# Features Configuration
FETCH_TIMELINES = True           # Time-series data (growth over time)
FETCH_AGGREGATIONS = True        # Aggregated totals for the period
FETCH_DEMOGRAPHICS = True        # Age/gender/location data
FETCH_TRAFFIC_SOURCES = True     # Where your audience comes from
FETCH_BEST_TIMES = True          # Optimal posting times
FETCH_SMART_LINKS = True         # Smart links analytics
FETCH_HASHTAG_TRACKER = True     # Hashtag tracking data
```

**Use cases:**
- **Quick test:** Disable timelines/aggregations to speed up testing
- **Focused analysis:** Only fetch demographics and traffic sources
- **Basic data:** Disable advanced features, keep platform analytics

---

## 📁 Platform Status File

After detection, a status file is saved:

**Location:** `data/brand_info/platform_status.json`

**Contents:**
```json
{
  "connected": ["instagram", "facebook", "tiktok"],
  "enabled_in_config": ["instagram", "facebook", "linkedin", "tiktok", "pinterest", "threads"],
  "will_fetch": ["instagram", "facebook", "tiktok"],
  "detection_time": "2025-11-14T09:30:00"
}
```

This helps you track:
- Which platforms are actually connected
- What's enabled in your config
- What will actually be fetched
- When the detection was run

---

## 💡 Common Scenarios

### Scenario 1: Only Fetch Instagram and Facebook
```python
PLATFORMS_ENABLED = {
    'instagram': True,
    'facebook': True,
    'linkedin': False,
    'twitter': False,
    'tiktok': False,
    'youtube': False,
    'pinterest': False,
    'threads': False,
    'bluesky': False,
}
```

**Result:** Only Instagram and Facebook data is fetched (if connected)

---

### Scenario 2: Test Run - Skip Timeline Analytics
```python
# Keep platforms as they are, but disable slow features
FETCH_TIMELINES = False       # Skip timeline analytics (27 endpoints)
FETCH_AGGREGATIONS = False    # Skip aggregations (9 endpoints)

# Keep these enabled
FETCH_DEMOGRAPHICS = True
FETCH_TRAFFIC_SOURCES = True
FETCH_BEST_TIMES = True
```

**Result:** Faster execution, only fetch basic analytics

---

### Scenario 3: Everything Enabled
```python
PLATFORMS_ENABLED = {
    'instagram': True,
    'facebook': True,
    'linkedin': True,
    'twitter': True,
    'tiktok': True,
    'youtube': True,
    'pinterest': True,
    'threads': True,
    'bluesky': True,
}

FETCH_TIMELINES = True
FETCH_AGGREGATIONS = True
FETCH_DEMOGRAPHICS = True
FETCH_TRAFFIC_SOURCES = True
FETCH_BEST_TIMES = True
FETCH_SMART_LINKS = True
FETCH_HASHTAG_TRACKER = True
```

**Result:** Fetch everything from all connected platforms (longest execution)

---

## 🚀 How It Works

### 1. Detection Phase
```
Starting data fetch...
↓
Get blog ID → Success (3991897)
↓
Query /admin/blog/profiles
↓
Parse response for connected platforms
↓
Show platform status report
```

### 2. Filtering Phase
```
For each platform in config:
  ├─ Is it connected?
  │  ├─ YES: Is it enabled in config?
  │  │  ├─ YES: ✅ Will fetch
  │  │  └─ NO:  ❌ Skip (disabled in config)
  │  └─ NO:  ❌ Skip (not connected)
```

### 3. Execution Phase
```
Only fetch from platforms that are:
  ✅ Connected to Sattvica
  AND
  ✅ Enabled in config.py
```

---

## ❓ FAQ

### Q: What if I enable a platform that's not connected?
**A:** It will be skipped automatically. The fetcher only fetches from platforms that are BOTH connected AND enabled.

### Q: Can I disable just one feature?
**A:** Yes! Just set the feature flag to `False` in config.py:
```python
FETCH_TIMELINES = False  # Skip timeline analytics
```

### Q: How do I know what's actually connected?
**A:** Run the fetcher and look at the startup output. It will show:
- ✅ Connected platforms
- Configuration status
- What will be fetched

### Q: Where is the detection result saved?
**A:** `data/brand_info/platform_status.json`

### Q: Can I change settings mid-execution?
**A:** No. Configuration is loaded at startup. Stop the script, edit config.py, then restart.

### Q: What if detection fails?
**A:** The script will log a warning and continue with all platforms enabled in config (may result in 403 errors for unconnected platforms).

---

## 🔧 Troubleshooting

### Issue: All platforms showing as not connected

**Cause:** Detection endpoint failed or returned unexpected format

**Solution:**
1. Check logs for errors
2. Verify authentication (token, user ID, blog ID)
3. Check `data/brand_info/connected_profiles.json` for raw data

---

### Issue: Platform is connected but showing as disabled

**Cause:** Platform is set to `False` in config.py

**Solution:**
Edit `config/config.py` and set the platform to `True`:
```python
PLATFORMS_ENABLED = {
    'instagram': True,  # Change False to True
}
```

---

### Issue: Want to fetch from all connected platforms

**Solution:**
Set all platforms to `True` in config.py:
```python
PLATFORMS_ENABLED = {
    'instagram': True,
    'facebook': True,
    'linkedin': True,
    'twitter': True,
    'tiktok': True,
    'youtube': True,
    'pinterest': True,
    'threads': True,
    'bluesky': True,
}
```

---

## 📝 Benefits Summary

✅ **No more wasted API calls** to unconnected platforms
✅ **Clear visibility** of what will be fetched
✅ **Easy configuration** with simple True/False flags
✅ **Faster execution** when you only need specific platforms
✅ **Status tracking** with saved detection results
✅ **Flexible control** over platforms and features

---

**Created:** 2025-11-14
**Status:** Ready to use
**Configuration:** config/config.py
