import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("snehaclass12@gmail.com", "Pleasebeaware6!")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("snehaclass12@gmail.com", "madhumita312@gmail.com", message)

# terminating the session
s.quit()