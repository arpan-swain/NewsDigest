import smtplib
import ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # for sending emails securely
    context = ssl.create_default_context()

    username = "arpanswain754@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "arpanswain754@gmail.com"


    with smtplib.SMTP_SSL(host,port, context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver, message)