#https://www.youtube.com/watch?v=iICg4Vn2Rkk
#How to Send Emails Through Python (2021) - Plain Text, Adding File Attachments

####################################-Plaint Text-#########################################
#Importing Packages
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

mails = open('emails.txt', 'r')
mailList = mails.readlines()

#Sender, Reciever, Body of Email
sender = 'menno.natanael@gmail.com'
receivers = mailList
body_of_email = 'This was sent through Python'

#Creating the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'Phyton email'
msg['From'] = sender
msg['To'] = ','.join(receivers)

# #Adds a csv file as an attachment to the email 
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('Terimakasih.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="Terimakasih.csv"')
msg.attach(part)

#Connecting to Gmail SMTP Server
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = sender, password = '...')
s.sendmail(sender, receivers, msg.as_string())
s.quit()
