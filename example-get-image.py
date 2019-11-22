from quickdraw import QuickDrawData
from PIL import Image, ImageDraw, ImageOps
import cv2
import numpy as np

qd = QuickDrawData()
anvil = qd.get_drawing("circle")

anvil_image = Image.new("RGB", (600,600), color=(255,255,255))
anvil_drawing = ImageDraw.Draw(anvil_image)

for stroke in anvil.strokes:
    # anvil_drawing.line(stroke, fill=(0,0,0), width=2)

    for coordinate in range(len(stroke)-1):
        x1 = stroke[coordinate][0]*2
        y1 = stroke[coordinate][1]*2
        x2 = stroke[coordinate+1][0]*2
        y2 = stroke[coordinate+1][1]*2
        anvil_drawing.line((x1,y1,x2,y2), fill=(0,0,0), width=2)

old_size = anvil_image.size  # old_size[0] is in (width, height) format

new_im = ImageOps.expand(anvil_image,border = 10, fill = (255,255,255))

new_im.show()

anvil_image.show()
anvil_image = new_im
#image processing
open_cv_image = np.array(anvil_image)
open_cv_image = open_cv_image[:, :, ::-1].copy() 

th, im_th = cv2.threshold(open_cv_image, 220, 255, cv2.THRESH_BINARY_INV)
 
# Copy the thresholded image.
im_floodfill = im_th.copy()
 
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255)
 
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
 
# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()
 
# Detect blobs.
keypoints = detector.detect(im_out)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im_out, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints

# Display images.
cv2.imshow("Thresholded Image", im_th)
cv2.imshow("Floodfilled Image", im_floodfill)
cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
cv2.imshow("Foreground", im_out)
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)