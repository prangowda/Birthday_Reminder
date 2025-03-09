import smtplib
import json
from email.message import EmailMessage
import datetime

# Load configuration
with open("config.json", "r") as file:
    config = json.load(file)

# Load birthdays
with open("birthdays.json", "r") as file:
    birthdays = json.load(file)

# SMTP Email Setup
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = config["email"]
PASSWORD = config["password"]

# Check if today is someone's birthday
today = datetime.datetime.today().strftime("%m-%d")
for name, date in birthdays.items():
    if date == today:
        msg = EmailMessage()
        msg.set_content(f"Happy Birthday, {name}! 🎂 Have a wonderful day! 🎉")
        msg["Subject"] = "🎂 Happy Birthday!"
        msg["From"] = EMAIL
        msg["To"] = config["recipient_email"]

        # Send Email
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
            server.quit()
            print(f"🎉 Birthday email sent to {name}!")
        except Exception as e:
            print(f"Error sending email: {e}")
