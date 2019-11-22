from PIL import Image, ImageDraw, ImageOps
import cv2
import numpy as np

class ColorIt:
    def __init__(self,object):
        self._object = object
        self._index = object.key_id
        print("ID {}".format(self._index))

    def fill(self,no_of_objects_fill):
        self._image = Image.new("RGB", (300,300), color=(255,255,255))
        self._drawing = ImageDraw.Draw(self._image)
        for stroke in self._object.strokes:         
            for coordinate in range(len(stroke)-1):
                x1 = stroke[coordinate][0]
                y1 = stroke[coordinate][1]
                x2 = stroke[coordinate+1][0]
                y2 = stroke[coordinate+1][1]
                self._drawing.line((x1,y1,x2,y2), fill=(0,0,0), width=4)
        new_image = ImageOps.expand(self._image,border = 10, fill = (255,255,255))
        #new_image.show()
        open_cv_image = np.array(new_image)
        open_cv_image = open_cv_image[:, :, ::-1].copy() 
        # converting it to gray if image is color
        im_gray = cv2.cvtColor(open_cv_image,cv2.COLOR_BGR2GRAY)
        # converting it to binart image
        (thresh,im_bw) = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        # Find countours
        contours, hierarchy = cv2.findContours(im_bw,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        (_, contours, _) = cv2.findContours(image = im_bw,mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)

        lines = np.array([[194,114,1],[26,88,210],[33,175,240],[142,48,123],[48,172,122],[247,189,77],[49,19,169]])

      

        color = lines
        colorCount = len(lines)
        print(colorCount)
        ind = 0

        areas = [cv2.contourArea(c) for c in contours]
        print(areas)
        # get max Index to ignore
        # get second max to fill colour
        index = np.array(areas).argsort()[-2:][::-1]
        print(index)
        max_index = index[0]
        print(max_index)
        contour_to_color = index[1]

        cv2.drawContours(open_cv_image,contours,max_index,(255,255,255),-1)

        for i in range(len(contours)):
            if(i==contour_to_color):
                cv2.drawContours(open_cv_image,contours,i,\
                (int(lines[ind][0]),int(lines[ind][1]),int(lines[ind][2])),-1)
#                ind = if ind>=colorCount-1: ind else: ind+1
                if ind >= colorCount-1:
                    ind = 0
                else:
                    ind = ind + 1
                break

        # count1 = 255
        # count2 = 0

        # cv2.drawContours(im_input,contours,-1,(255,255,0),-1),
                    
        h , w = im_bw.shape

        for i in range(1,h-1):
            for j in range(1,w-1):

                if im_bw[i,j] == 0:
                    open_cv_image[i,j,:]=0

          # Display image
        cv2.imshow("OG",open_cv_image)
        cv2.imshow('BW',im_bw)
        cv2.waitKey(0)

