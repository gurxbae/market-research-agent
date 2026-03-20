# Multi-Source Market Research Agent

An agentic AI that researches any company or market using real-time web search,
synthesizes findings from multiple sources, and generates a comprehensive
competitive analysis report — in seconds.

## What it does
- Accepts any company or market name as input
- Searches multiple live web sources in real time using Claude AI
- Extracts company overview, financials, news, market position and risks
- Identifies top competitors with comparative analysis
- Generates a structured PDF report with full citations

## Tech Stack
Python, Anthropic Claude API (with web search), FPDF2, python-dotenv

## How to run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Anthropic API key to `.env` as `ANTHROPIC_API_KEY=your_key`
4. Run: `python main.py`
5. Enter any company or market name when prompted

## Example Output
Tested on Zomato (March 2026):
- Revenue: ₹20,243 crore (67% YoY growth)
- Market Cap: $22.87 billion
- Market Share: 55-58% of India food delivery market
- 6 key risks identified including GST liability and labor law changes
- 5 competitors analyzed including Swiggy, Zepto and Amazon Food

## How to run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Anthropic API key to `.env` as `ANTHROPIC_API_KEY=your_key`
4. Run the web app: `streamlit run app.py`
5. Open browser at `http://localhost:8501`
6. Enter any company name and click Research!