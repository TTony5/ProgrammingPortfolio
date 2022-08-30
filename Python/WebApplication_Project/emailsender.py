from email.message import EmailMessage
from app_info import password
import ssl
import smtplib

sender = "a.egbujor@gmail.com"
passw = password

print(passw)

receiver = 'nigela9334@rxcay.com'

subject = "Hello from the Future!"
body = """This is a message from me in the future!"""

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, passw)
    smtp.sendmail(sender,receiver,em.as_string())

