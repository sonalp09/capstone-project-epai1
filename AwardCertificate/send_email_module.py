# Check internet connection
# This is a closure function where function checks whether internet connection is there or not by try except method.
# As this is a closure, we will use this function as a decorator.

# Importing required package
from datetime import datetime
import time, os, requests
from termcolor import colored
import functools
from functools import cache, lru_cache

def check_connection(func):
    '''
    check_connection: checks whether internet connection is there or not.
    Input:
        a function
    Output:
        Inner function
    '''
    def inner1(*args, **kwargs):
        '''
        inner1 function: prints connected in green when connection is there, otherwise prints status code is not 200 in red.
        '''
        os.system('color')
        url = 'https://www.google.com/'
        timeout = 2
        # sleep_time = 10
        op = None

        while True:
            now = datetime.now()
            try:
                op = requests.get(url, timeout=timeout).status_code
                if op == 200:
                    returned_value = func(*args, **kwargs)
                    print(now, colored("Connected", "green"))
                    sleep_time = 30
                else:
                    returned_value = func(*args, **kwargs)
                    print(now, colored("Status Code is not 200", "red"))
                    print("status Code", op)
            except:
                print(now, colored("Not Connected", "red"))
                print("status Code", op)
                sleep_time = 5
            time.sleep(sleep_time)
            return returned_value
    return inner1

# Sending emails
# This function gathers all the data in one email content and sends to the desired email address.
# This function takes large number of parameters

# Importing required packages
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

@check_connection
@lru_cache(maxsize = 100)
def send_email(filepath:'string', name:'string', receiver_email:'string', score:'string'):
    '''
    send_email: this function sends email to desired email address
    Input:
        filepath: path of the attachment file to be taken
        name: name of the receiver
        receiver_email: receiver's email address
        score: receiver's score in the course.
    '''
    if receiver_email != "Invalid Email":
        if name != "Invalid Name":
            subject = "Award of Excellence"
            sender_email = "mail.testsonalbt@gmail.com"
            password = '********'
            
            # Reading file where email content is written
            f = open("email_content.txt", "r")
            email_content = f.read()

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails

            body = email_content.format(name, score)

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            # Selecting attachment based on names
            filename = f'{filepath}Excellence_Award_{name}.jpg'.format(filepath, name) # In same directory as script

            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

                # Encode file in ASCII characters to send by email    
                encoders.encode_base64(part)

                # Add header as key/value pair to attachment part
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= Excellence_Award_{name}.jpg".format(name),
                )

                # Add attachment to message and convert message to string
                message.attach(part)
                text = message.as_string()

                # Log in to server using secure context and send email

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, text)
        else:
            print("Invalid Name")        
    else:
        print("Invalid Email")
