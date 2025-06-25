# DjangoTask - Internship Assignment

A Django REST Framework project that includes:
- ✅ Public & Protected REST APIs
- ✅ JWT Authentication
- ✅ Celery & Redis for asynchronous tasks
- ✅ Email sending (Gmail SMTP)
- ✅ Telegram bot integration
- ✅ Organized project structure

---

## 🛠️ Features
- REST APIs:
  - Public: `/api/public/`
  - Protected: `/api/protected/`
  - Registration: `/api/register/`
- JWT Auth for protected endpoints
- Asynchronous welcome email using **Celery**
- Telegram bot that saves usernames when the user sends `/start`
- `.env` for secret settings (no secrets in the code)

---

## ⚡️ Tech Stack
- **Django 4+**
- **Django REST Framework**
- **Celery + Redis**
- **Python-Telegram-Bot v20+**

---

## 🐍 Setup Instructions

✅ 1️⃣ Clone the repository

- git clone https://github.com/Vedan8/DJangoTask.git
- cd DjangoTask


✅ 2️⃣ Create Virtual Environment

- python -m venv env
- source env/bin/activate  # Linux/Mac
- env\Scripts\activate      # Windows

✅ 3️⃣ Install Requirements

- pip install -r requirements.txt

✅ 4️⃣ Create .env
- Add .env in the root directory:

- SECRET_KEY=your-django-secret
- DEBUG=False
- DB_NAME=djangotask_db
- DB_USER=youruser
- DB_PASSWORD=yourpass
- DB_HOST=localhost
- DB_PORT=5432
- CELERY_BROKER_URL=redis://127.0.0.1:6379/0
- CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/0
- TELEGRAM_TOKEN=your_telegram_bot_token_here
- EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
- EMAIL_HOST=smtp.gmail.com
- EMAIL_PORT=587
- EMAIL_USE_TLS=True
- EMAIL_HOST_USER=your_email@gmail.com
- EMAIL_HOST_PASSWORD=your_app_password
- DEFAULT_FROM_EMAIL=your_email@gmail.com

🗄️ 5️⃣ Database Setup

- Edit settings.py for your database and run:

- python manage.py migrate

👤 6️⃣ Create Superuser

- python manage.py createsuperuser

🚀 7️⃣ Run Django Development Server

- python manage.py runserver

⚡️ 8️⃣ Run Celery Worker

- celery -A DjangoTask worker -l INFO

🤖 9️⃣ Run the Telegram Bot

- python api/bot.py




| Endpoint               | Method | Auth         | Purpose                              |
| ---------------------- | ------ | ------------ | ------------------------------------ |
| `/api/public/`         | GET    | No           | Public "hello" message               |
| `/api/register/`       | POST   | No           | Register a new user (triggers email) |
| `/auth/login/`         | POST   | No           | Get JWT token                        |
| `/auth/refresh/`       | POST   | No           | Refresh JWT token                    |
| `/api/protected/`      | GET    | JWT required | Returns protected data               |




🤖 Telegram Bot
- Command: /start

- Action: Collects the user’s Telegram username and saves it to the database.


📂 Directory Structure

- DjangoTask/
- ├─ DjangoTask/
- ├─ api/
- ├─ .env
- ├─ manage.py
- ├─ requirements.txt
- ├─ README.md


👥 Contact
- For any questions, contact: vedanjyadav@gmail.com