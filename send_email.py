import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    #Initializing email message object
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
                <p>Invoice No <strong>{invoice_no} is due {due_date}<strong>.</p>
                <p>Please confirm your payment.</p>
                <p>Best regards,<br>Dozen Pvt Ltd</p>
            </body>
        </html>
        """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:  # Application used by mail servers to send and receive emails.
        # Protocol commands
        server.starttls()
        server.login(sender_email, password_email)
        server.send_message(msg)

if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="Check Owner",
        receiver_email="venurajithmal@gmail.com",
        due_date="11 Sep 2023",
        invoice_no="INV-21-12-008",
        amount="5,")
