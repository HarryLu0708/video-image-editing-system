import cv2
import numpy as np
from scipy.interpolate import UnivariateSpline

def greyscale(img):
    greyscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return greyscale

def bright(img,value=-50):
    img_bright = cv2.convertScaleAbs(img,beta=value)
    return img_bright

def sharpen(img):
    kernel = np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])
    img_sharpen = cv2.filter2D(img,-1,kernel)
    return img_sharpen

def sepia(img):
    img_sepia = np.array(img,dtype=np.float64)
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.272,0.534,0.131],[0.349,0.686,0.168],[0.393,0.769,0.189]]))
    img_sepia[np.where(img_sepia>255)] = 255
    img_sepia = np.array(img_sepia,dtype=np.uint8)
    return img_sepia

def pencil_g(img):
    sk_grey, sk_color = cv2.pencilSketch(img,sigma_s=60,sigma_r=0.07,shade_factor=0.03)
    return sk_grey

def pencil_c(img):
    sk_grey, sk_color = cv2.pencilSketch(img,sigma_s=60,sigma_r=0.07,shade_factor=0.03)
    return sk_color

def HDR(img):
    hdr = cv2.detailEnhance(img,sigma_s=12,sigma_r=0.15)
    return hdr

def invert(img):
    inv = cv2.bitwise_not(img)
    return inv

def LookupTable(x,y):
    spline = UnivariateSpline(x,y)
    return spline(range(256))

def summer(img):
    increaseTable = LookupTable([0,64,128,256],[0,80,160,256])
    decreaseTable = LookupTable([0,64,128,256],[0,50,100,256])
    blue,green,red=cv2.split(img)
    red = cv2.LUT(red,increaseTable).astype(np.uint8)
    blue = cv2.LUT(blue,decreaseTable).astype(np.uint8)
    s = cv2.merge((blue,green,red))
    return s

def winter(img):
    increaseTable = LookupTable([0,64,128,256],[0,80,160,256])
    decreaseTable = LookupTable([0,64,128,256],[0,50,100,256])
    blue,green,red=cv2.split(img)
    red = cv2.LUT(red,decreaseTable).astype(np.uint8)
    blue = cv2.LUT(blue,increaseTable).astype(np.uint8)
    s = cv2.merge((blue,green,red))
    return s

def canny(img):
    r = cv2.Canny(img,100,200,5,L2gradient=True)
    return r

def sketch(img):
    img_g = greyscale(img)
    img_b = cv2.GaussianBlur(img_g,(21,21),0,0)
    img = cv2.divide(img_g,img_b,scale=256)
    return img
