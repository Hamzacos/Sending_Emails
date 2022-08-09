import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "hamza.laqraa@gmail.com"
receiver_email = "test@gmail.com"
password = input("Type your password :")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email


text = """\
Hi,
How are you?
"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
      
    </p>
  </body>
</html>
"""


part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")


message.attach(part1)
message.attach(part2)


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )