import streamlit as st
import sys
import os
from agent.researcher import research_company
from agent.reporter import generate_report

# Page config
st.set_page_config(
    page_title="Market Research Agent",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0f1117; }
    .stTextInput > div > div > input {
        background-color: #1e2130;
        color: white;
        border: 1px solid #3d4466;
        border-radius: 8px;
        font-size: 16px;
        padding: 12px;
    }
    .stButton > button {
        background-color: #4f6ef7;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 32px;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        transition: background-color 0.2s;
    }
    .stButton > button:hover {
        background-color: #3d5ce0;
    }
    .result-box {
        background-color: #1e2130;
        border: 1px solid #3d4466;
        border-radius: 12px;
        padding: 24px;
        margin-top: 16px;
    }
    .metric-card {
        background-color: #1e2130;
        border: 1px solid #3d4466;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🔍 Market Research Agent")
st.markdown("##### Powered by Claude AI — Real-time multi-source research in seconds")
st.divider()

# Input section
col1, col2 = st.columns([3, 1])
with col1:
    company = st.text_input(
        "Company or Market to Research",
        placeholder="e.g. Zomato, Tesla, Indian EV market...",
        label_visibility="collapsed"
    )
with col2:
    research_btn = st.button("🔍 Research", use_container_width=True)

# Examples
st.caption("💡 Try: Infosys · Swiggy · Reliance Industries · Indian fintech market · Ola Electric")
st.divider()

# Research logic
if research_btn and company:
    with st.spinner(f"Researching {company} from multiple sources... This may take 30 seconds."):
        try:
            research = research_company(company)
            report_path = generate_report(research, company)
            st.session_state["research"] = research
            st.session_state["report_path"] = report_path
            st.session_state["company"] = company
        except Exception as e:
            st.error(f"Something went wrong: {e}")

elif research_btn and not company:
    st.warning("Please enter a company or market name first.")

# Display results
if "research" in st.session_state:
    company_name = st.session_state["company"]
    research = st.session_state["research"]
    report_path = st.session_state["report_path"]

    st.success(f"✅ Research complete for **{company_name}**!")

    # Download button
    if os.path.exists(report_path):
        with open(report_path, "rb") as f:
            st.download_button(
                label="📥 Download PDF Report",
                data=f,
                file_name=f"{company_name}_research.pdf",
                mime="application/pdf"
            )

    st.divider()

    # Display research in tabs
    tab1, tab2 = st.tabs(["📋 Full Report", "📄 Raw Text"])

    with tab1:
        sections = research.split("##")
        for section in sections:
            if section.strip():
                lines = section.strip().split("\n")
                if lines:
                    st.markdown(f"## {lines[0].strip()}")
                    st.markdown("\n".join(lines[1:]))
                    st.divider()

    with tab2:
        st.text_area("Raw Output", research, height=600)

# Footer
st.markdown("---")
st.caption("Built with Python + Anthropic Claude API | Market Research Agent v1.0")