import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load Environmental Variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read Environmental variables
sender_email = os.getenv("EMAIL", "venurasvpussella@gmail.com")
sender_password = os.getenv("PASSWORD", "your_generated_app_password")

# Print the loaded values for debugging
print("Loaded sender_email:", sender_email)
print("Loaded sender_password:", sender_password)

# Print debugging information about environment variable loading
if sender_email == "venurasvpussella@gmail.com":
    print("INFO: The EMAIL environmental variable is using the default value. Check .env file.")
if sender_password == "your_generated_app_password":
    print("INFO: The PASSWORD environmental variable is using the default value. Check .env file.")

def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    # Create the base text message objects
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

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:  # Application used by mail servers to send and receive emails.
        # Protocol commands
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
