from email import message
import smtplib
import os
import imghdr

from email.message import EmailMessage
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

Sender_Email = "<sender's email address>" #Key in sender's address
Reciever_Email = input('Enter reciever email address :') #Do not change this line
Password = input('Enter your email account password: ') #Do not change this line

newMessage = EmailMessage()  #Do not change this line  
newMessage['Subject'] = "Hello" #Defining email subject
newMessage['From'] = "<sender's email address>"  #Key in sender's address / Defining sender email
newMessage['To'] = input('Enter reciever email address :')  #Defining reciever email

    # Create the plain-text and HTML version of your message
html = """\
    <html>
    <body>
      <p>
       <img src="(input own personal pastepixel URL)" alt=""/>
      </p>
     </body>
    </html>
    """
def new_func(message, html):
    message.attach(MIMEText(html, "html"))

new_func(message, html)

with open('Success.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name

def new_func(newMessage, image_data, image_type, image_name):
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

new_func(newMessage, image_data, image_type, image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password) #Login to SMTP server
    smtp.send_message(newMessage)      #Sending email using send_message method by passing EmailMessage object

try:
    print("Email Successfully Sent!")
except Exception as ex:
    print("Something went wrong….")
