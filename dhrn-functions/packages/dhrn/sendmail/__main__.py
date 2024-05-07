import mailtrap as mt

def main(args):
    mail = mt.Mail(
        sender=mt.Address(email="mailtrap@demomailtrap.com", name="Mailtrap Test"),
        to=[mt.Address(email="dave.e.best@gmail.com")],
        subject="You are awesome!",
        text="Congrats for sending test email with Mailtrap!",
        category="Integration Test",
    )
    client = mt.MailtrapClient(token="REPLACE_ME")
    client.send(mail)