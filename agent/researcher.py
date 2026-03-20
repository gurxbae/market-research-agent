import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def research_company(company_name):
    """
    Uses Claude with web search to research a company
    from multiple sources and return structured findings.
    """

    prompt = f"""
You are a market research analyst. Research the company or market: "{company_name}"

Using web search, find and analyze the following:

1. COMPANY OVERVIEW
   - What the company does, founding year, headquarters
   - Current CEO and key leadership
   - Business model and revenue streams

2. FINANCIAL PERFORMANCE
   - Latest revenue and profit figures
   - Revenue growth rate (YoY)
   - Market capitalization (if public)
   - Key financial ratios if available

3. RECENT NEWS & DEVELOPMENTS
   - Latest 3-4 major news stories
   - Recent product launches or acquisitions
   - Strategic initiatives

4. MARKET POSITION
   - Market share estimates
   - Key competitive advantages
   - Target customer segments

5. TOP COMPETITORS
   - List top 3-5 competitors
   - Brief comparison of strengths

6. RISKS & CHALLENGES
   - Key business risks
   - Industry headwinds
   - Regulatory challenges if any

7. OUTLOOK
   - Growth prospects
   - Analyst sentiment if available
   - Key opportunities ahead

Format your response with clear headers for each section.
Be specific with numbers and dates wherever possible.
Cite the sources you used for key facts.
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        tools=[
            {
                "type": "web_search_20250305",
                "name": "web_search"
            }
        ],
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract text from response
    research = ""
    for block in message.content:
        if block.type == "text":
            research += block.text

    return research