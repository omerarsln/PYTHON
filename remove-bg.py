from rembg import remove
from PIL import Image

input_path = "ataturk.jpg"
output_path = "ataturk.png"

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
