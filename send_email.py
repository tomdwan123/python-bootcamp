import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Python <rickydevs@proton.me>'
email['to'] = 'letanphuc123@gmail.com'
email['subject'] = 'Hello Python'

email.set_content("Wow! Congratulations!")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login("rickydevs@proton.me", "xxxxxx")
    smtp.send_message(email)
    print("The mail e sent!")