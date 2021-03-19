import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # or use os

html_email = Path('email_for_spam.html').read_text()
email_template = Template(html_email)
email_template.substitute({'name':'TinTin'})
# print(f"Hi my name is spam mailer.\n {email_template.substitute({'name':'TinTin'})}")
email = EmailMessage()
email['from'] = 'Mass Mailer Project'
email['to'] = 'campermalhotra@gmail.com'
email['subject'] = 'This is a spam'

email.set_content(f"I don't like spams but this one is in the name of learning!!\n {email_template.substitute({'name':'TinTin'})}", 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<YOUR EMAIL HERE>', '<YOUR PASSWORD HERE>')
    smtp.send_message(email)
    print('user spammed!!')