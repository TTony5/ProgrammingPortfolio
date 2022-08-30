from email.message import EmailMessage
from app_info import password
import ssl
import smtplib
import getpass


print("Thank you for using AOE Email Sender. This sender is for gmail emails only. Please use this app with Gmail addresses. Let's Begin! \n")

sender = input("Enter Email Address: ")
passw = getpass.getpass("Enter Password or App Password: ")


receiver = input("Enter Email Receiver: ")

subject = input("What is your subject?: ")
body = input("What is your message?: ")
body_message = """{0}""".format(body)

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body_message)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, passw)
    smtp.sendmail(sender,receiver,em.as_string())


