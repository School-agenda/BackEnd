#!/usr/bin/env python3
import os
import enviormentVar
import smtplib
enviormentVar.setVar()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()


senderEmail = os.environ.get('EMAIL_USER')
senderPass = os.environ.get('EMAIL_PASS')

s.login(senderEmail, senderPass)

#TODO write whatever message  
message = "Measdsaadasdasdasdas"

#TODO add way to grab email from user account and place as second argument 
s.sendmail("senderEmail", "", message)
s.quit()
