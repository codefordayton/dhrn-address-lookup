import os
import mailtrap as mt
from jinja2 import Template

def main(args):
    MAILTRAP_API_TOKEN = os.environ.get("MAILTRAP_API_TOKEN")
    MAILTRAP_SENDER_ADDRESS = os.environ.get("MAILTRAP_SENDER_ADDRESS") 
    MAILTRAP_TO_ADDRESS = os.environ.get("MAILTRAP_TO_ADDRESS")

    with open("template.html") as f:
        template = Template(f.read())

    filled_template = template.render(data=args)

    mail = mt.Mail(
        sender=mt.Address(email=MAILTRAP_SENDER_ADDRESS, name="Code For Dayton"),
        to=[mt.Address(email=MAILTRAP_TO_ADDRESS)],
        subject="New submission from the DHRN Screener",
        text="Please enable HTML to view this message",
        html=filled_template,
        category="Integration Test",
    )
    try:
        client = mt.MailtrapClient(token=MAILTRAP_API_TOKEN)
        client.send(mail)
    except mt.exceptions.AuthorizationError as e:
        # Handle the authorization error here
        return {"error": f"Mailtrap authorization error {MAILTRAP_API_TOKEN}, {MAILTRAP_SENDER_ADDRESS}, {MAILTRAP_TO_ADDRESS}", "body": args, "filled_template": filled_template}

    return {"body": args}