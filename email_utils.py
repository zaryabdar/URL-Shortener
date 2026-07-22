from flask import current_app, url_for
from flask_mail import Message
from extensions import mail

def send_reset_email(user):
    token = user.get_reset_token()

    reset_url = url_for(
        "auth.reset_password",
        token=token,
        _external=True
    )

    msg = Message(
        subject="Password Reset Request",
        sender=current_app.config["MAIL_USERNAME"],
        recipients=[user.email]
    )

    msg.body = f"""Hello {user.username},

To reset your password, visit the following link:

{reset_url}

If you did not request a password reset, simply ignore this email.
"""
    print(reset_url)
    mail.send(msg)