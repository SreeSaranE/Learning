import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import udemy.Archives.credentials as credentials

def create_image_attachment(path):
    raise NotImplementedError('Image not implemented')

def send_mail(to_mail: str, subject: str, body: str,image = None):
    host: str = 'smtp.gmail.com'
    port: int = 587

    context = ssl.create_default_context()

    with smtplib.SMTP(host=host, port=port) as server:
        print("Logging in...")
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(credentials.EMAIL, credentials.PASSWORD)

        print("Attempting to send Email")
        message = MIMEMultipart()
        message['From'] = credentials.EMAIL
        message['To'] = to_mail
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        server.sendmail(from_addr=credentials.EMAIL,
                        to_addrs=to_mail,
                        msg=message.as_string())
        
        print("success")

if __name__ == "__main__":
    send_mail(to_mail='srnsaran1007@gmail.com',
              subject="Test 1",
              body="This is an auto-genereated Email.")