import smtplib
from email_pwd import email_pwd

# Set your email credentials
email_address = ''
email_password = email_pwd
smtp_server = 'smtp.gmail.com'
smtp_port = 587
to_phone_number = ''
carrier_domain = 'msg.fi.google.com'
to_email_address = f'{to_phone_number}@{carrier_domain}'
message = ''

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, to_email_address, message)

print(f"SMS message sent to {to_phone_number}")
