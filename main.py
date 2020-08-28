import smtplib
import getpass

from email.mime.text import MIMEText


def send_email():
    senders_address = str(input("Enter you gmail account "))
    password = getpass.getpass()
    subject = 'This is an automated email'
    msg = '''
        This is the message body.
    '''

    #server initialization
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senders_address, password)

    recipients = ['1twoka24@gmail.com']
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = senders_address
    msg['To'] ='.'.join(recipients)
    msg.set_param('importance','high value')

    server.sendmail(senders_address, recipients, msg.as_string())

send_email()



