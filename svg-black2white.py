from bs4 import BeautifulSoup
import re

file_path = '/mnt/data/d.svg'

with open(file_path, 'r') as file:
    svg_content = file.read()

soup = BeautifulSoup(svg_content, "xml")

for tag in soup.find_all(True):
    if 'fill' in tag.attrs:
        tag['fill'] = '#FFFFFF'
    if 'stroke' in tag.attrs:
        tag['stroke'] = '#FFFFFF'

for style in soup.find_all('style'):
    style.string = re.sub(r'fill:[^;]+;', 'fill:#FFFFFF;', style.string)
    style.string = re.sub(r'stroke:[^;]+;', 'stroke:#FFFFFF;', style.string)

output_path_fixed = '/mnt/data/dd.svg'
with open(output_path_fixed, 'w') as file:
    file.write(str(soup))

output_path_fixed
