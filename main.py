import os
os.getcwd()
os.chdir('H:\Sonal\Python_TSAI_Epai\capstone-project')
os.getcwd()
import os
import requests
import termcolor
import functools
import email
import smtplib
import ssl
import cv2
import csv
import os.path
import re
import AwardCertificate
from AwardCertificate import data_processing
from AwardCertificate import image_processing

data_name = data_processing.csv_to_column('score_test.csv', 'Name')
data_email = data_processing.csv_to_column('score_test.csv', 'Email_Address')
data_score = data_processing.csv_to_column('score_test.csv', 'Score')
print(data_score)

# Regex check
data_email = list(map(data_processing.regex_check, data_email))

# check valid name
data_name = list(map(data_processing.check_valid_name, data_name))

# convert to proper 
data_name = list(map(str.title, data_name))
data_score = list(map(data_processing.check_valid_score, data_score))

# Final code for image processing

read_path_new = 'H:\\Sonal\\Python_TSAI_Epai\\capstone-project\\Excellence_Award.jpg'
write_path_new = 'H:\\Sonal\\Python_TSAI_Epai\\capstone-project\\Certificates\\'

list(map(lambda x: image_processing.create_certi(read_path_new, write_path_new, x), data_name))

# Sending emails
from AwardCertificate import send_email_module

filepath = 'H:\\Sonal\\Python_TSAI_Epai\\capstone-project\\Certificates\\'
name = data_processing.csv_to_column('score_test.csv', 'Name')
name = list(map(data_processing.check_valid_name, name))

# convert to proper 
name = list(map(str.title, name))

receiver_email = data_processing.csv_to_column('score_test.csv', 'Email_Address')
receiver_email = list(map(data_processing.regex_check, receiver_email))
score = data_processing.csv_to_column('score_test.csv', 'Score')

list(map(lambda x, y, z: send_email_module.send_email(filepath, x, y, z), name, receiver_email, score))
print("Completed")
