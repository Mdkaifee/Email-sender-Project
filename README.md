python -m venv venv

venv\Scripts\activate          # Windows

source venv/bin/activate       # macOS/Linux

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib python-dotenv

pip freeze > requirements.txt

python main.py

Email will be sent successsfully