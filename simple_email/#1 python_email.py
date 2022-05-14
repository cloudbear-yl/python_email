import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg['From'] = "<sender's email address>" #replace values accordingly
msg['To'] = input('Enter the receiver email address :\n')
msg['Subject'] = input('Enter your email subject :\n') 
msg.set_content(input('Enter your message.\n'))

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("<sender's email address>", "<email account password>") #replace values accordingly
server.send_message(msg)

try:
    server.quit()
    print("Email Successfully Sent!")
except Exception as ex:
    print("Something went wrong….")

