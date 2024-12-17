# Load the SVG file and modify its fill color to white
file_path = '/mnt/data/discord.svg'

# Read the content of the SVG file
with open(file_path, 'r') as file:
    svg_content = file.read()

# Replace fill and stroke colors with white (#FFFFFF)
import re

# Replace all fill and stroke attributes, except those set to "none"
svg_content_white = re.sub(r'fill="[^none][^"]*"', 'fill="#FFFFFF"', svg_content)
svg_content_white = re.sub(r'stroke="[^none][^"]*"', 'stroke="#FFFFFF"', svg_content_white)

# Save the updated SVG file
output_path = '/mnt/data/discord_white.svg'
with open(output_path, 'w') as file:
    file.write(svg_content_white)

output_path
