from fpdf import FPDF
import os
from datetime import date

def clean_text(text):
    """Remove characters fpdf cannot handle."""
    replacements = {
        "\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": "-", "\u2022": "*", "\u25cf": "*",
        "\u20b9": "Rs.", "\u00a0": " ", "\u2026": "...", "\u00ae": "(R)",
        "\u2122": "(TM)", "\u00a9": "(C)"
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text.encode("latin-1", errors="ignore").decode("latin-1")

def generate_report(research_text, company_name):
    """Generates a formatted PDF report from research findings."""

    pdf = FPDF()
    pdf.set_margins(20, 20, 20)
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, "Market Research Report", ln=True, align="C")

    pdf.set_font("Helvetica", "I", 12)
    pdf.cell(0, 8, clean_text(company_name), ln=True, align="C")

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, f"Generated on: {date.today().strftime('%B %d, %Y')}",
             ln=True, align="C")
    pdf.ln(4)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(8)

    # Content
    for line in research_text.split("\n"):
        line = clean_text(line.strip())
        if not line:
            pdf.ln(2)
            continue
        if line.startswith("##") or line.isupper():
            pdf.set_font("Helvetica", "B", 13)
            line = line.replace("##", "").replace("#", "").strip()
        elif line.startswith("#"):
            pdf.set_font("Helvetica", "B", 11)
            line = line.replace("#", "").strip()
        elif line.startswith("**") and line.endswith("**"):
            pdf.set_font("Helvetica", "B", 10)
            line = line.replace("**", "").strip()
        else:
            pdf.set_font("Helvetica", "", 10)
        try:
            pdf.multi_cell(0, 6, line)
        except Exception:
            continue

    # Save
    os.makedirs("reports", exist_ok=True)
    output_path = f"reports/{company_name.replace(' ', '_')}_research.pdf"
    pdf.output(output_path)
    return output_path