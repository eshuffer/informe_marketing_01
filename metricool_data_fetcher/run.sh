#!/bin/bash

# Metricool Data Fetcher - Quick Start Script
# For Sattvica Brand Data Retrieval

echo "=================================="
echo "Metricool Data Fetcher"
echo "Brand: Sattvica"
echo "Date: 2025-08-13 to 2025-11-13"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt -q

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "🚀 Starting data fetch..."
echo ""

# Run the fetcher
python3 metricool_fetcher.py

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================="
    echo "✅ Data fetch completed!"
    echo "=================================="
    echo ""
    echo "📊 Running analysis..."
    echo ""
    python3 analyze_data.py
    echo ""
    echo "📁 All data saved in: ./data/"
    echo "📄 Check fetch_summary.json for details"
    echo "📄 Check analysis_report.txt for analysis"
    echo "📋 Check logs/metricool_fetcher.log for execution logs"
else
    echo ""
    echo "=================================="
    echo "❌ Data fetch failed"
    echo "=================================="
    echo ""
    echo "Please check logs/metricool_fetcher.log for error details"
    exit 1
fi
