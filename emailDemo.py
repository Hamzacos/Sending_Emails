import smtplib, ssl

port = 587 
smtp_server = "smtp.gmail.com"
sender_email = "hamza.laqraa@gmail.com"
receiver_email = "test@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo() 
    server.starttls(context=context)
    server.ehlo()  
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)