import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import socket
import os
import config

sender = config.SMPT_CONFIG['sender']
recipient = config.SMPT_CONFIG['recipient']
smpt_server = config.SMPT_CONFIG['smpt_server']
port = config.SMPT_CONFIG['port']
password = config.SMPT_CONFIG['password']
icon_path = config.SMPT_CONFIG['icon_path']

msg = MIMEMultipart()

msg['From'] = sender
msg['To'] = recipient
# msg['Subject'] = "Notification"

duration = ""
if len(sys.argv) == 2:
    modifier = "Duration: " + sys.argv[1] + " seconds"

body = "{0} job completed.\nDirectory: {1}\nDuration: {2} seconds".format(socket.gethostname(), os.getcwd(), duration)

msg.attach(MIMEText(body, 'plain'))

fp = open(icon_path, 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

server = smtplib.SMTP(smpt_server, port)
server.starttls()
server.login(sender, password)
text = msg.as_string()
server.sendmail(sender, recipient, text)
server.quit()
