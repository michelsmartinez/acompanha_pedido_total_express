#coding: utf-8
import smtplib
from email.mime.text import MIMEText

def send(de, senha, para, titulo, texto):
    lpara = [para]
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465) #verificar isto caso não for utilizar Gmail
    smtp.login(de, senha)

    msg = MIMEText(texto)

    msg['Subject'] = titulo
    msg['From'] = de
    msg['To'] = para

    smtp.sendmail(de, [para], msg.as_string())
    smtp.quit()
    return 0
