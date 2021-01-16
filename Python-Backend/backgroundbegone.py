import object_detect as od
import numpy as np
import cv2
from matplotlib import pyplot as plt
import PIL
from PIL import Image
from os import remove as osremove

def removeBackground(image_name): 

    #Opening File
    img = cv2.imread(image_name, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #Getting rectangle aroudn coordinates using more opencv
    startX, startY, endX, endY = od.getBox(image_name)

    #Cropping image to the region of interest (ROI)
    img = img[startY:endY, startX:endX]

    height, width, channel = img.shape

    #Defining Rectangle around region of interest (the whole picture)
    rect = (0,0,width-1,height-1)

    #Filling in mask, bgdModel and fgdModel
    mask = np.zeros(img.shape[:2],np.uint8)

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    #grabcutting the image
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,20,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]

    tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(img)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    dst = cv2.cvtColor(dst, cv2.COLOR_BGRA2RGBA)

    #Saving
    save_path = 'images/' + image_name.split('/')[1]
    cv2.imwrite(save_path, dst)   
    
    osremove(image_name)
    print('Done!')

    return save_path

