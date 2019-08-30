import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmailaddress = "noreplyqrcodes@gmail.com"
gmailpassword = "8Y&(d2bu"
mailto = input("what email address do you want to send your message to? \n ")
msg = MIMEMultipart()
msg['From'] = gmailaddress
msg['To'] = mailto
msg['Subject'] = "QR Code"
body = "Buen día, adjuntamos tu código QR, que tengas un buen día."
msg.attach(MIMEText(body, 'plain'))
text = str(msg)
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, mailto , text)
print(" \n Sent!")
mailServer.quit()