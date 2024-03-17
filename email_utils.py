from flask_mail import Message, Mail
from flask import Flask, current_app
from flask import render_template


def send_email(to, subject, app: Flask, mail: Mail, html_msg):
    msg = Message(
        subject,
        recipients=[to],
        sender=app.config["MAIL_USERNAME"])
    msg.html = html_msg
    msg.attach('font_aside.jpeg', 'image/gif', open(f"{current_app.template_folder}/img/font_aside.jpeg", 'rb').read(), 
            'inline', 
            headers=[['Content-ID', '<BackgroundImg>'],])
    mail.send(msg)
