import os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from_address = "os.environ.get('EMAIL_HOST_USER')"
to_address = "to_email@email.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test email"
msg['From'] = from_address
msg['To'] = to_address

# Create the message (HTML).
html = """
We are sending an email using Python and Gmail, \nhow fun! We can fill this with html, \nand gmail supports a decent range of css style attributes too - \n https://developers.google.com/gmail/design/css#example.
"""

# Record the MIME type - text/html.
part1 = MIMEText(html, 'html')

# Attach parts into message container
msg.attach(part1)

# Credentials
username = os.environ.get('EMAIL_HOST_USER')
password = os.environ.get('EMAIL_HOST_PASSWORD')

# Sending the email
## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work3

server = smtplib.SMTP('smtp.gmail.com', 587) 
server.ehlo()
server.starttls()
server.login(username,password)  
server.sendmail(from_address, to_address, msg.as_string())  
server.quit()