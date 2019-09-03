import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import qrtest

gmailaddress = ""
gmailpassword = ""
mailto = input("Cuál es tu correo? \n ")
msg = MIMEMultipart()
msg['From'] = gmailaddress
msg['To'] = mailto
msg['Subject'] = "QR Code"
msg_content = MIMEText('Buen dia, adjuntamos su código qr.', 'plain', 'utf-8')
msg.attach(msg_content)
# set attachment mime and file name, the image type is png
with open('C:/Users/David Cantú/OneDrive/Documents/Proyectos/PythonSmallProjects/myQR.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='myQR.jpg')
    # add required header data:
    mime.add_header('Content-Disposition', 'attachment', filename='myQR.jpg')
    mime.add_header('X-Attachment-Id', '0')
    mime.add_header('Content-ID', '<0>')
    # read attachment file content into the MIMEBase object
    mime.set_payload(f.read())
    # encode with base64
    encoders.encode_base64(mime)
    # add MIMEBase object to MIMEMultipart object
    msg.attach(mime)
text = str(msg)
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, mailto , text)
print(" \n Sent!")
mailServer.quit()
