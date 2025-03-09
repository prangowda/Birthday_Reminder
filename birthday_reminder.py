import json
import datetime
import plyer

# Load birthdays from file
def load_birthdays():
    try:
        with open("birthdays.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Show desktop notification
def show_notification(name):
    plyer.notification.notify(
        title="🎂 Birthday Reminder 🎂",
        message=f"Today is {name}'s birthday! Don't forget to wish them! 🎉",
        timeout=10
    )

# Check and notify birthdays
def check_birthdays():
    today = datetime.datetime.today().strftime("%m-%d")
    birthdays = load_birthdays()

    for name, date in birthdays.items():
        if date == today:
            show_notification(name)

if __name__ == "__main__":
    check_birthdays()
