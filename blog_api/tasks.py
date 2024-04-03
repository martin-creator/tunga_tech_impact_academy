import os
import requests
from dotenv import load_dotenv
from app import app, mail
from flask_mail import Message

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")

# def send_simple_message(to, subject, body):
#     return requests.post(
#         f"https://api.mailgun.net/v3/{DOMAIN}/messages",
#         auth=("api", os.getenv("MAILGUN_API_KEY")),
#         data={"from": f"Your Name <mailgun@{DOMAIN}>",
#             "to": [to],
#             "subject": subject,
#             "text": body}
#     )

def send_simple_message(to, subject, body):
    msg = Message(subject, recipients=[to], body=body)
    mail.send(msg)


def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the Stores REST API.",
    )
    


# def send_user_registration_email(email, username):
#     return send_simple_message(
#         email,
#         "Successfully signed up",
#         f"Hi {username}! You have successfully signed up to the Stores REST API.",
#     )