# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 19:41:08 2017

@author: Shobhit
"""

import pandas as pd
from PIL import Image
import numpy as np
#from PIL import ImageDraw              #Import this module to plot BBox

path = "/diskb/tmp/CXR8/.csv"
df = pd.read_csv(path)
    
index = df['Image Index']
x = df['bbox x']
y = df['bbox y']
w = df['bbox w']
h = df['bbox h'] 
label = df['Finding Label']

imgarray = []

def GenImages(iterations, cropUnit, cropIteration):
     print("Iteration : "+str(cropIteration))
     xred = 100
     yred = 100
     for i in range(0,iterations):
        test = Image.open("F://PyProjects//BBox//Images//test.png").convert('RGBA')
        img = Image.new('RGBA', [int(max(w)), int(max(h))])
        #bbox = ImageDraw.Draw(test)
        try:     
            if(cropIteration == 0):
                p1 = (min(x), min(y))
                xadj = (min(x) + max(w)) 
                yadj = (min(y)+max(h))
                p2 = (xadj - xred, yadj)
            
            elif(cropIteration == 1):
                p1 = (min(x), min(y))
                xadj = (min(x) + max(w)) 
                yadj = (min(y)+max(h))
                p2 = (xadj, yadj - yred)
            
            elif(cropIteration == 2):
                p1 = (min(x), min(y)+yred)
                xadj = (min(x) + max(w)) 
                yadj = (min(y)+max(h))
                p2 = (xadj, yadj)
            
            elif(cropIteration == 3):
                p1 = (min(x)+xred, min(y))
                xadj = (min(x) + max(w)) 
                yadj = (min(y)+max(h))
                p2 = (xadj, yadj)    
            
            print("p1 = "+ str(p1) + "p2 = " +str(p2))
#           xy = [p1, p3]                                    #To plot the BBOX you're cropping
#           bbox.rectangle(xy, outline= 'red')               #To plot the BBOX you're cropping
            xy = p1[0], p1[1], p2[0], p2[1]
            img = test.crop(xy)
            #imgarray.append(np.array(img))
            img.save("F://PyProjects//BBox//Images//Cropped//"+str(cropIteration)+"//"+str(i)+".png")
        except (SystemError):
            print("Cannot crop the image any more. Moving to next iteration")
            i = 40
        
        xred += cropUnit;
        yred += cropUnit;

def cropImages(image, cropIteration, reduction):    
    if(cropIteration == 0):
        p1 = (min(x), min(y))
        xadj = (min(x) + max(w)) 
        yadj = (min(y)+max(h))
        p2 = (xadj - reduction, yadj)
    
    elif(cropIteration == 1):
        p1 = (min(x), min(y))
        xadj = (min(x) + max(w)) 
        yadj = (min(y)+max(h))
        p2 = (xadj, yadj - reduction)
    
    elif(cropIteration == 2):
        p1 = (min(x), min(y)+reduction)
        xadj = (min(x) + max(w)) 
        yadj = (min(y)+max(h))
        p2 = (xadj, yadj)
    
    elif(cropIteration == 3):
        p1 = (min(x)+reduction, min(y))
        xadj = (min(x) + max(w)) 
        yadj = (min(y)+max(h))
        p2 = (xadj, yadj)    
    
    print("p1 = "+ str(p1) + "p2 = " +str(p2))
    #           xy = [p1, p3]                                    #To plot the BBOX you're cropping
    #           bbox.rectangle(xy, outline= 'red')               #To plot the BBOX you're cropping
    xy = p1[0], p1[1], p2[0], p2[1]
    img = test.crop(xy) 
    
    for xyz in range(1,4):
        GenImages(40, 10, xyz)
        
def loadImages(array, cropIteration, cropUnit):
    imgarray = []
    for k in range(0, len(array)):
       test = Image.open(path+"//"+str(index[2])).convert('RGBA')
       img = Image.new('RGBA', [int(max(w)), int(max(h))])
       try:     
            if(cropIteration == 0):
                p1 = (min(x), min(y))
                xadj = (min(x) + max(w)) 
                yadj = (min(y)+max(h))
                p2 = (xadj - cropUnit, yadj)
            
            elif(cropIteration == 1):
                p1 = (min(x), min(y))
                xadj = (min(x) + max(w)) 
                yadj = (min(y)+max(h))
                p2 = (xadj, yadj - cropUnit)
            
            elif(cropIteration == 2):
                p1 = (min(x), min(y)+ cropUnit)
                xadj = (min(x) + max(w)) 
                yadj = (min(y)+max(h))
                p2 = (xadj, yadj)
            
            elif(cropIteration == 3):
                p1 = (min(x)+ cropUnit, min(y))
                xadj = (min(x) + max(w)) 
                yadj = (min(y)+max(h))
                p2 = (xadj, yadj)    
            
            print("p1 = "+ str(p1) + ", p2 = " +str(p2))
            xy = p1[0], p1[1], p2[0], p2[1]
            img = test.crop(xy)
            imgarray.append(np.array(img))
            
       except (SystemError):
            print("Cannot crop the image any more")
       except (FileNotFoundError):
            print("Please check the path syntax pecified")
            