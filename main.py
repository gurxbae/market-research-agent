import sys
from agent.researcher import research_company
from agent.reporter import generate_report

def main():
    print("=" * 55)
    print("   Multi-Source Market Research Agent")
    print("=" * 55)
    print("\nThis agent searches multiple web sources and")
    print("generates a full competitive analysis report.")
    print("\nExamples:")
    print("  - Infosys")
    print("  - Tesla")
    print("  - Indian IT services market")
    print("  - Zomato")
    print("=" * 55)

    company = input("\nEnter company or market to research: ").strip()

    if not company:
        print("No input entered. Exiting.")
        sys.exit(1)

    print(f"\n[1/3] Researching '{company}' from multiple sources...")
    print("      This may take 20-30 seconds...")
    research = research_company(company)
    print("      Research complete!")

    print("\n[2/3] Generating PDF report...")
    report_path = generate_report(research, company)
    print(f"      Report saved to: {report_path}")

    print("\n" + "=" * 55)
    print("   RESEARCH SUMMARY")
    print("=" * 55)
    print(research)

if __name__ == "__main__":
    main()