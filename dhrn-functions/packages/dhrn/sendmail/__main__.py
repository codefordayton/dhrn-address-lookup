import os
import mailtrap as mt
from jinja2 import Template

def main(args):
    MAILTRAP_API_TOKEN = os.environ.get("MAILTRAP_API_TOKEN")

    with open("template.html") as f:
        template = Template(f.read())

    mail = mt.Mail(
        sender=mt.Address(email="mailtrap@demomailtrap.com", name="Mailtrap Test"),
        to=[mt.Address(email="dave.e.best@gmail.com")],
        subject="New submission from the DHRN Screener",
        text="Please enable HTML to view this message",
        html=template.render(data=args),
        category="Integration Test",
    )
    client = mt.MailtrapClient(token=MAILTRAP_API_TOKEN)
    client.send(mail)
    return {"body": "Email sent"}