import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT = 465
EMAIL_SERVER = 'smtp.gmail.com'
EMAIL = 'venurasvpussella@gmail.com'
PASSWORD = 'alphastranger@123'

# Load Environmental Variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
# Read Environmental variables
sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")

def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    # Create the base text message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Dozen Pvt.ltd", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        quick note on {amount}USD
        Invoice No {invoice_no} is due {due_date}.
        please confirm your payment
        BR,
        Dozen Pvt Ltd
        """
    )
    msg.add_alternative(
        f"""\
        <html>
            <body>
                <p>Hi {name},</p>
                <p>Quick note on {amount}USD.</p>
                <p>Invoice No {invoice_no} is due {due_date}.</p>
                <p>Please confirm your payment.</p>
                <p>Best regards,<br>Dozen Pvt Ltd</p>
            </body>
        </html>
        """,
        subtype="html",
    )
    
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="John doe",
        receiver_email="venurajithmal@gmail.com",
        due_date="11 Sep 2023",
        invoice_no="INV-21-12-008",
        amount="5,")

