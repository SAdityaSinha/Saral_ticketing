from fileinput import filename
import smtplib
from email.message import EmailMessage
import imghdr

email_address = #"id@mail.com"
email_password = #"Pass"

def mailing(mailAdd,imgNM):
    global email_address
    global email_password

    msg = EmailMessage()
    msg['Subject'] = "Test mail 3.0"
    msg['From'] = email_address
    msg['To'] = mailAdd
    msg.set_content('Attaching an image file.')

    with open(imgNM,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email_address, email_password)
        smtp.send_message(msg)


def mailingOTP(mailAdd,otp):
    global email_address
    global email_password

    msg = EmailMessage()
    msg['Subject'] = "Otp for Saral Ticketing"
    msg['From'] = email_address
    msg['To'] = mailAdd
    msg.set_content(f"{otp}\nthis is the otp for your Saral tickiting ")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email_address, email_password)
        smtp.send_message(msg)

def mailingVerified(mailAdd,name):
    global email_address
    global email_password
    
    msg = EmailMessage()
    msg['Subject'] = "Verification of Saral Ticketing"
    msg['From'] = email_address
    msg['To'] = mailAdd
    msg.set_content(f"{name}\nYour ID is successfully created and and active \nWarm regards from the team Saral Ticketing \nEnjoy your vacations and have fun")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(email_address, email_password)
        smtp.send_message(msg)
