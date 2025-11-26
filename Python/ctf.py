# Python example
from PIL import Image

img = Image.open("flight_record.png")
r, g, b = img.split()
r.save("layer_R.png")
g.save("layer_G.png")
b.save("layer_B.png")
