from email_service import send_email

if __name__ == "__main__":
    send_email(
        to_email="kaifeeeminence@gmail.com",
        subject="Test Email from Gmail API",
        message_text="Hello, this is a test email sent using Gmail API and Python!"
    )
