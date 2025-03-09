### 📜 README.md – Birthday Reminder & Auto-Wisher  

# 🎂 Birthday Reminder & Auto-Wisher  

This **Birthday Reminder & Auto-Wisher** is a Python-based tool that **notifies you of upcoming birthdays** via **desktop alerts** and optionally **sends automated birthday wishes via email**. It also includes a **GUI for adding birthdays** easily.  

---

## 🌟 Features  
✅ **Desktop notifications** when it's someone's birthday.  
✅ **Automatic email wishing** (optional).  
✅ **Simple GUI** to add and manage birthdays.  
✅ **Stores birthdays locally** in JSON format.  
✅ **Runs automatically** in the background.  

---

## 🛠️ Tech Stack  
- **Python** – Core programming language  
- **Tkinter** – GUI for adding birthdays  
- **Plyer** – Desktop notifications  
- **smtplib** – Email automation  
- **JSON** – Data storage  

---

## 📂 Project Structure  

```
📦 Birthday_Reminder
 ┣ 📜 birthday_reminder.py       # Checks birthdays & sends alerts  
 ┣ 📜 birthdays.json             # Stores saved birthdays  
 ┣ 📜 config.json                # Email settings (for auto-wishing)  
 ┣ 📜 email_wisher.py            # Sends birthday wishes via email  
 ┣ 📜 gui.py                     # GUI for adding birthdays  
 ┣ 📜 requirements.txt           # Dependencies  
 ┣ 📜 README.md                  # Documentation  
```

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/prangowda/Birthday_Reminder.git
cd Birthday_Reminder
```

### 2️⃣ Install Required Packages  
```bash
pip install -r requirements.txt
```

### 3️⃣ Add Birthdays (via GUI)  
```bash
python gui.py
```
- Enter **Name** and **Date (MM-DD format)**  
- Click **Save Birthday**  

### 4️⃣ Run Birthday Reminder (Desktop Notification)  
```bash
python birthday_reminder.py
```
- If today is someone’s birthday, a **notification** will appear!  

### 5️⃣ (Optional) Enable Auto-Wish Emails  
1. Edit `config.json` and enter your **Gmail credentials**:  
```json
{
    "email": "your_email@gmail.com",
    "password": "yourpassword",
    "recipient_email": "friend@example.com"
}
```
2. Run the email sender:  
```bash
python email_wisher.py
```
- Sends **birthday emails** automatically!  

---

## 🎨 Screenshots  

🔹 **Desktop Notification**  
![Birthday Notification](https://via.placeholder.com/400x200.png?text=Birthday+Notification)  

🔹 **GUI for Adding Birthdays**  
![GUI](https://via.placeholder.com/400x300.png?text=Birthday+Reminder+GUI)  

---

## 🎁 Future Enhancements  
🔹 Add **WhatsApp message sending**  
🔹 Sync with **Google Calendar**  
🔹 Telegram bot integration  

---

## 🤝 Contributing  
1. **Fork the repo**  
2. **Create a new branch**  
3. **Make your changes & commit**  
4. **Submit a pull request**  
