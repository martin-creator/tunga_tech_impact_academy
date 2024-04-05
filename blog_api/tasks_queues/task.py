import os
from flask_mail import Message, Mail
from flask import current_app
from dotenv import load_dotenv
# from blog_api import mail

load_dotenv()

mail = Mail()

def init_mail(app):
    mail.init_app(app)

def send_simple_message(to, subject, body):
    app = current_app._get_current_object()
    msg = Message(subject, recipients=[to], body=body)

    with app.app_context():
        mail.send(msg)

def send_user_registration_email(email, username):
    subject = "Successfully signed up"
    body = f"Hi {username}! You have successfully signed up to the Stores REST API."
    send_simple_message(email, subject, body)



# import os
# import requests
# from dotenv import load_dotenv
# from flask_mail import Message, Mail

# load_dotenv()



# load_dotenv()

# def init_mail(app, mail):
#     # mail = Mail()
#     mail.init_app(app)
#     return mail

# def send_simple_message(mail, to, subject, body):
#     msg = Message(subject, recipients=[to], body=body)
#     mail.send(msg)

# def send_user_registration_email(mail, email, username):
#     subject = "Successfully signed up"
#     body = f"Hi {username}! You have successfully signed up to the Stores REST API."
#     send_simple_message(mail, email, subject, body)

# # mail = Mail()

# # app = create_app()

# # DOMAIN = os.getenv("MAILGUN_DOMAIN")

# # def init_mail(app, mail):
# #     mail.init_app(app)

# # # def send_simple_message(to, subject, body):
# # #     return requests.post(
# # #         f"https://api.mailgun.net/v3/{DOMAIN}/messages",
# # #         auth=("api", os.getenv("MAILGUN_API_KEY")),
# # #         data={"from": f"Your Name <mailgun@{DOMAIN}>",
# # #             "to": [to],
# # #             "subject": subject,
# # #             "text": body}
# # #     )

# # def send_simple_message(to, subject, body):
# #     msg = Message(subject, recipients=[to], body=body)
# #     mail.send(msg)


# # def send_user_registration_email(email, username):
# #     return send_simple_message(
# #         email,
# #         "Successfully signed up",
# #         f"Hi {username}! You have successfully signed up to the Stores REST API.",
# #     )
    


# # # def send_user_registration_email(email, username):
# # #     return send_simple_message(
# # #         email,
# # #         "Successfully signed up",
# # #         f"Hi {username}! You have successfully signed up to the Stores REST API.",
# # #     )