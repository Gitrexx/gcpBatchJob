import os
import smtplib
from email.mime.text import MIMEText


def send_email():
    # Sender email credentials (use environment variables for security)
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    if not sender_email or not sender_password or not recipient_email:
        raise ValueError("Missing email configuration")

    # Email content
    subject = "Cloud Run Job Notification"
    body = "Your Cloud Run job has completed successfully!"

    # Create the email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    # Send the email using Gmail SMTP
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":

    send_email()