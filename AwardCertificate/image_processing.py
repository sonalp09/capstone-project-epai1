# Image processing: This module processes image based on the requirements. Basic image processing are:
# 1. Reading image from the filepath
# 2. Writing the required text on the image. 
# In this module, we are writing to create a certificate. 

# Importing required packages
import cv2
import csv
import os.path
from os import path

def create_certi(read_path:'string', write_path:'string', name:'string'):
    '''
    create_certi: 
    Input:
        read_path: path from where image needs to be read
        write_path: path where image will be stored
        name: name to write on the image
    Output: 
        Ready image after writing based on the requirement
    '''
    if name != "Invalid Name":
        path = write_path + 'Excellence_Award_' + name + '.jpg'
        if not os.path.exists(path):
            img = cv2.imread(read_path)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_name = cv2.FONT_HERSHEY_DUPLEX
            font_signature = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
            (test_width, text_height), text_baseline = cv2.getTextSize('Python 101',font,1, 2)
            cv2.putText(img,'Python 101', (520-(test_width>>1), 300), font, 1, (0, 0, 0), 2)
            (name_width, name_height), name_baseline = cv2.getTextSize(name,font_name,1, 2)
            cv2.putText(img,name, (520-(name_width>>1), 445), font_name, 1, (0, 0, 0), 2)
            (date_width, date_height), date_baseline = cv2.getTextSize(name,font,1, 2)
            cv2.putText(img, "24th April 2021", (220, 525), font, 0.75, (0, 0, 0), 2)
            cv2.putText(img, "spandey", (700, 525), font_signature, 1, (0, 0, 0), 2)
            cv2.imwrite(path, img)
