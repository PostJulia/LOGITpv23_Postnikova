import smtplib, ssl
from email.message import EmailMessage
smtp_server="smtp.gmail.com"
port=587 #For starttls
sender_email="postjulia2007@gmail.com"
password=input("Kirjuta oma salasõna ja vajuta enter: ")
context=ssl.create_default_context()
#msg="Tere tulemast!"
msg=EmailMessage()
msg.set_content("Tere tulemast! Olen kirja keha!")
msg['Subject']="Kirja teema"
msg['From']="Julia Postnikova" #Nimi ka saab kirjutada #Kellelt
msg['To']="marina.oleinik@tthk.ee" #Kellele
try:
    server=smtplib.SMTP(smtp_server,port)
    server.starttls(context=context) #Secure the connection
    server.login(sender_email,password)
    server.send_message(msg) #server.sendmail(sender_email,to_email,msg)
    print("Kiri on saadetud")
except Exception as e:
    print(e)
finally:
    server.quit()
