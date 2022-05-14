import smtplib
import os
import imghdr
from email.message import EmailMessage


Sender_Email = "<sender's email address>" #Key in sender's address
Reciever_Email = input('Enter reciever email address :') #Do not change this line
Password = input('Enter your email account password: ') #Do not change this line

newMessage = EmailMessage()  #Do not change this line  
newMessage['Subject'] = "Hello" #Defining email subject
newMessage['From'] = "<sender's email address>" #Key in sender's address / Defining sender's email address
newMessage['To'] = "<recipient's email address>"#Key in recipient's address/ Defining reciever email
newMessage.set_content("""
Hello World
                          
Cheers,\n
xxxxx                              
""") #Defining email body

#Sending attachment (i.e image file) :
with open('Success.png' , 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name

#'Success.png' is a image file. Replace it with your own image file name.

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