from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self, name, email, phone_number, message):
        self.message  = message
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def load_email(self):
        body = self.message
        subject = 'APPLICATION REQUEST'

        user_name = "EMAIL@EMAILPROVIDER.COM"
        password = 'PASSWORD'

        message = MIMEMultipart()
        message['To'] = user_name
        message['From'] = user_name
        message['Subject'] = subject

        message.attach(MIMEText(body, "plain"))

        with SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login(user_name, password)
            server.send_message(message)

        print('EMAIL SENT SUCCESSFULLY')