import smtplib,ssl
from Poemas import poema
from email.mime.text import MIMEText
email="your email"
passw="your password"
port=465
recibido="receiver"
msg=MIMEText(poema()[0])
msg['Subject']=poema()[1] 
msg['From']=email
msg['To']=recibido

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
    server.login(email,passw)
    server.sendmail(email,recibido,msg.as_string())
    server.quit()
print("Enviado")