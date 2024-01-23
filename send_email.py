import smtplib, ssl
import os

port = 465

smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
message = """\
Subject: Github Email Report 

this is your daily email
"""
context = ss.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME,USER_PASSWORD)
    server.sendmail(USERNAME,USERNAME,message) #from,to,message