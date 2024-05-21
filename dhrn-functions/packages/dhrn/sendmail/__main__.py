import os
import mailtrap as mt

def main(args):
    MAILTRAP_API_TOKEN = os.environ.get("MAILTRAP_API_TOKEN")

    mail = mt.Mail(
        sender=mt.Address(email="mailtrap@demomailtrap.com", name="Mailtrap Test"),
        to=[mt.Address(email="dave.e.best@gmail.com")],
        subject="New submission from the DHRN Screener",
        text="Congrats for sending test email with Mailtrap!",
        category="Integration Test",
    )
    client = mt.MailtrapClient(token=MAILTRAP_API_TOKEN)
    client.send(mail)