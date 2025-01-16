from markdown import markdown
from weasyprint import HTML

input_file = "index_copy.md"
output_file = "CapstoneProject.pdf"

with open(input_file, 'r') as f:
    html_content = markdown(f.read())

HTML(string=html_content).write_pdf(output_file)
print(f"Converted {input_file} to {output_file}")