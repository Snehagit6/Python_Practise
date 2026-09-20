import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = "snehatech611@gmail.com"
email["to"] = "snehaclass12@gmail.com"
email['sub'] = "Automated Email"
email.set_content("Email sent via Sneha's code") ## content of email
with smtplib.SMTP(host='smtp.gmail.com', port=587)as smtp:
## sending request to server
    smtp.ehlo()          ## server object
smtp.starttls()      ## used to send data between server and client
smtp.login("snehaclass12@gmail.com","Personalmail6!") ## login id and password of gmail
smtp.send_message(email)   ## Sending email
print("email send")
