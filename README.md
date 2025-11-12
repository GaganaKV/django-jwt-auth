# 🛡️ Django JWT Authentication App

A full-featured authentication system built with **Django**, **Django REST Framework**, and **JWT (JSON Web Tokens)** — with user registration, login, logout, and protected profile pages.

🌐 **Live Demo:** [https://django-jwt-auth.onrender.com](https://django-jwt-auth.onrender.com)

---

## 🚀 Features

✅ User Registration (HTML & API)  
✅ Login / Logout system  
✅ JWT Authentication (Access + Refresh tokens)  
✅ Protected Profile page  
✅ Beautiful frontend with responsive UI  
✅ Deployed on Render (free hosting)

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Django 5, Django REST Framework |
| Auth | JWT (via djangorestframework-simplejwt) |
| Frontend | HTML, CSS (custom styled) |
| Database | SQLite (Render auto-managed) |
| Deployment | Render |
| Others | Whitenoise, Gunicorn, Dotenv |

---

## 🧠 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/GaganaKV/django-jwt-auth.git
cd django-jwt-auth

# Create virtual environment
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
