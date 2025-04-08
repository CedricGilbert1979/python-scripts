from email import policy
from email.parser import BytesParser
import os

# Load the .eml file
eml_path = "/mail.eml"
with open(eml_path, "rb") as file:
    msg = BytesParser(policy=policy.default).parse(file)

# Extract HTML content
html_part = None
for part in msg.walk():
    if part.get_content_type() == "text/html":
        html_part = part.get_content()
        break

# Save HTML content to a file
html_output_path = "/mail.html"
if html_part:
    with open(html_output_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_part)

# It's Done
html_output_path
