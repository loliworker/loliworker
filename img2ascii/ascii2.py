import sys
from PIL import Image
import shutil
import time

input_file = sys.argv[1]
im = Image.open(input_file)

pre_width, pre_height = im.size
aspect_ratio = pre_height / pre_width
new_width = shutil.get_terminal_size().columns
new_height = int(new_width*aspect_ratio)
im = im.resize((new_width,new_height))
print(f"The specified image resized {pre_width}x{pre_height} to {new_width}x{new_height}. (Ratio: {aspect_ratio})")

im_gray = im.convert("L")
im_rgb = im.convert("RGB")

#ascii_chars = ".:-=+#"
ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_art = ""

def rgb_to_ascii_color(r,g,b):
    return f"\x1b[38;2;{r};{g};{b}m"

art = ""
for y in range(new_height):
    for x in range(new_width):
        art += rgb_to_ascii_color(*im_rgb.getpixel((x,y)))
        art += ascii_chars[int(im_gray.getpixel((x,y)) / 256 * len(ascii_chars))]
    art += "\n"
art += f"\x1b[0m"

for l in art.splitlines():
    print(l)
    time.sleep(0.02)
