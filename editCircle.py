from quickdraw import QuickDrawDataGroup
from PIL import Image, ImageDraw, ImageOps
import cv2
import numpy as np
from color_it import ColorIt

qdg = QuickDrawDataGroup("circle")
results = qdg.search_drawings(key_id=int(4865367048454144))
anvil = results[0]

#anvil_image = Image.new("RGB", (255,255), color=(255,255,255))
#anvil_drawing = ImageDraw.Draw(anvil_image)

# for stroke in anvil.strokes:
#     # anvil_drawing.line(stroke, fill=(0,0,0), width=2)

#     for coordinate in range(len(stroke)-1):
#         x1 = stroke[coordinate][0]
#         y1 = stroke[coordinate][1]
#         x2 = stroke[coordinate+1][0]
#         y2 = stroke[coordinate+1][1]
#         anvil_drawing.line((x1,y1,x2,y2), fill=(0,0,0), width=4)

#old_size = anvil_image.size  # old_size[0] is in (width, height) format

#clearnew_im = ImageOps.expand(anvil_image,border = 10, fill = (0,0,0))

#new_im.show()

c = ColorIt(anvil)
c.fill(3)

