from PIL import Image, ImageDraw
from itertools import product
import time


start_time = time.time()
IMAGE = Image.open("InputImage.jpg")
IMG_DATA = IMAGE.load()


def get_average_colour(x0,y0,x1,y1):
    r,g,b = 0, 0, 0
    area = (x1-x0)*(y1-y0)
    for x in xrange(x0,x1):
        for y in xrange(y0,y1):
            pixel = IMG_DATA[x,y]
            r += pixel[0]
            g += pixel[1]
            b += pixel[2]
    return (r/area, g/area, b/area)

#def get_dominant_colour(x0,y0,x1,y1):

def get_error_sum(x0,y0,x1,y1,average):
    re, ge, be = 0,0,0
    area = (x1-x0)*(y1-y0)
    for x in xrange(x0,x1):
        for y in xrange(y0,y1):
            pixel = IMG_DATA[x,y]
            re += abs(average[0] - pixel[0])
            ge += abs(average[1] - pixel[1])
            be += abs(average[2] - pixel[2])
    return (re/area, ge/area, be/area)

def fill_rectangle(location, colour):
    draw = ImageDraw.Draw(new_Image)
    draw.ellipse(location,colour)
    del draw

def fill_image(x,y):
    img_width = IMAGE.size[0]
    img_height = IMAGE.size[1]

    print img_width, img_height

    for width in xrange(0,img_width-x,x):
        for height in xrange(0,img_height-y,y):
            #print (width, height)
            colour =  get_average_colour(width, height, width+x, height+y)
            fill_rectangle((width,height,width+x,height+y),colour)

class Node():


    def __init__(self, parent, rect):
        self.parent = parent
        self.children = [None,None,None,None]



#new_Image = Image.new(IMAGE.mode,IMAGE.size,(255,255,255))
#fill_image(4,4)
#print (get_error_sum(0,0,500,500, get_average_colour(0,0,500,500)))
#new_Image.save('/Users/Stefan/Google Drive/Side Projects/QuadTree Pictures/Output.png', "PNG")


class Node():


class QuadTree():



print(time.time() - start_time)
