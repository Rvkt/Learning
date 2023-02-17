import email
import smtplib
from email.message import EmailMessage

email = EmailMessage()
# sender
email['from'] = 'Test Account'
# receiver
email['to'] = 'Rvkntin@gmail.com'
# Sunject of the email
email['subject'] = 'python'

# content of the email
email.set_content('Content of the email.')

with smtplib.SMTP(host='SMTP.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('hunnyunnh@gmail.com', 'password@123')
    smtp.send_message(email)
    print('Email Sent!!')