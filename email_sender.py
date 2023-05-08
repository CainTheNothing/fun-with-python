from email.message import EmailMessage
import ssl
import smtplib
from email_pwd import email_pwd

sender = 'SENDER_EMAIL'
pwd = email_pwd # app password from gmail

receiver = ''
subject = 'test'
body = """test"""

email = EmailMessage()
email['from'] = sender
email['to'] = receiver
email['subject'] = subject
email.set_content(body)

contxt = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contxt) as smtp:
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver, email.as_string())
