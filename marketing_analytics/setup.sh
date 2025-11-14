#!/bin/bash

# Marketing Analytics Setup Script

echo "================================"
echo "Marketing Analytics Setup"
echo "================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python --version 2>&1)
echo "Found: $python_version"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "Next steps:"
echo "1. Set your OpenAI API key:"
echo "   export OPENAI_API_KEY='your-api-key-here'"
echo ""
echo "2. Run the analytics:"
echo "   python analyze.py"
echo ""
echo "Reports will be saved to: ./reports/"
echo ""
