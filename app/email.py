from app import create_app, db

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = 'this is a text plain example body' #render_template(template + '.txt', **kwargs)
    msg.html = 'this is a example <b>HTML</b> body' #render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr