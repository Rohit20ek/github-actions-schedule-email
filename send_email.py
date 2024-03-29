# import smtplib, ssl
# import os

# port = 465

# smtp_server = "smtp.gmail.com"
# USERNAME = os.environ.get('USER_EMAIL')
# USERPASSWORD = os.environ.get('USER_PASSWORD')
# message = """\
# Subject: Github Email Report 

# this is your daily email
# """
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(USERNAME,USERPASSWORD)
#     server.sendmail(USERNAME,USERNAME,message) #from,to,
    
# ----------------------------------------------------
import smtplib, ssl
import os


port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
USER_PASSWORD = os.environ.get('USER_PASSWORD')
message = """\
Subject: GitHub Email Report

This is your daily email report.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME,USER_PASSWORD)
    server.sendmail(USERNAME,USERNAME,message)
# ----------------------------------------------------
# 
# rohitflowtest1@gmail.com