import os
import pickle
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from config import SENDER_EMAIL

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def send_email(to_email, subject, message_text):
    service = get_gmail_service()
    message = MIMEText(message_text)
    message['to'] = to_email
    message['from'] = SENDER_EMAIL
    message['subject'] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw}

    try:
        sent_message = service.users().messages().send(userId='me', body=body).execute()
        print(f"Email sent successfully. Message ID: {sent_message['id']}")
    except Exception as e:
        print("An error occurred while sending email:", e)
