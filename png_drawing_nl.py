from PIL import Image, ImageDraw

# Create a blank image for the flag
width, height = 25, 18
flag = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(flag)

# Define the colors of the Dutch flag
colors = ["#21468B", "#FFFFFF", "#AE1C28"]  # Blue, White, Red

# Draw the flag
stripe_height = height // 3
for i, color in enumerate(colors):
    y0 = i * stripe_height
    y1 = (i + 1) * stripe_height
    draw.rectangle([0, y0, width, y1], fill=color)

# Save the flag as a PNG file
file_path = "/mnt/data/Dutch_flag_25x18.png"
flag.save(file_path)
file_path
