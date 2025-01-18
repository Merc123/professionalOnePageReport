import streamlit as st
from jinja2 import Template

# Sample executive summary template
EXECUTIVE_SUMMARY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive Summary Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
        h1 { color: #2C3E50; }
        h2 { color: #2980B9; }
        p { margin: 10px 0; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    <h2>Summary</h2>
    <p>{{ summary }}</p>
    <h2>Key Findings</h2>
    <ul>
    {% for finding in key_findings %}
        <li>{{ finding }}</li>
    {% endfor %}
    </ul>
    <h2>Recommendations</h2>
    <p>{{ recommendations }}</p>
</body>
</html>
"""

def main():
    st.title("Executive Summary Report Generator")

    # Input fields for the user to enter report data
    report_title = st.text_input("Report Title", "Executive Summary")
    summary = st.text_area("Summary", "Enter a concise summary of the report here.")
    key_findings = st.text_area("Key Findings (one per line)").splitlines()
    recommendations = st.text_area("Recommendations", "Provide actionable recommendations here.")

    if st.button("Generate Report"):
        # Render the template with user input
        template = Template(EXECUTIVE_SUMMARY_TEMPLATE)
        context = {
            'title': report_title,
            'summary': summary,
            'key_findings': key_findings,
            'recommendations': recommendations
        }
        rendered_html = template.render(context)

        # Save the rendered report to an HTML file
        with open("executive_summary_report.html", "w") as file:
            file.write(rendered_html)

        st.success("Report has been generated as 'executive_summary_report.html'.")
        st.markdown("[View Report](./executive_summary_report.html)", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
