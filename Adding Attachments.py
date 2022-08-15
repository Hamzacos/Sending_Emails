import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment "
body = "This is an email with attachment sent "
sender_email = "hamza.laqraa@gmail.com"
receiver_email = "test@gmail.com"
password = input("Type your password and press enter:")


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  


message.attach(MIMEText(body, "plain"))

filename = "document.pdf"  


with open(filename, "rb") as attachment:
   
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())


encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)


message.attach(part)
text = message.as_string()


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)