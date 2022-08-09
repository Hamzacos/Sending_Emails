import smtplib, ssl

port = 465  
password = input("Type your password and press enter: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here