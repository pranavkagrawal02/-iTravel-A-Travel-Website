# iTravel — Simple Django Travel Website

iTravel is a lightweight Django-based web application designed to showcase travel destinations. It features a clean UI that displays destinations with images, pricing, and promotional offers, making it an ideal template for travel agencies or tour operators.

## 🚀 Features

* **Destination Management:** Dynamic models for Name, Description, Image uploads, Price, and Offer flags.
* **Media Support:** Automated handling of image uploads stored under `media/dest_pics`.
* **Modern UI:** Styled with **Bootstrap** and custom CSS for a responsive experience.
* **User System:** Includes a scaffolded `users` app for basic registration and login functionality.
* **Database Flexibility:** Configured for MySQL by default, with easy switching to SQLite for local development.

---

## 📁 Project Structure

The project is organized into the following key files and directories:

| Component | Path | Description |
| --- | --- | --- |
| **Settings** | `settings.py` | Core configuration, including Static/Media and DB settings. |
| **Main View** | `travello/views.py` | Renders the homepage by loading `Destination` objects. |
| **Models** | `travello/models.py` | Defines the `Destination` database schema. |
| **Templates** | `templates/index.html` | The primary frontend UI for the landing page. |
| **URLs** | `urls.py` & `travello/urls.py` | Routing for the main site and the travello app. |

---

## 🛠️ Prerequisites

* **Python:** 3.8+ recommended.
* **Django:** 3.0.5 (Project developed with this version).
* **Database:** MySQL (Database name: `travello_db`) or SQLite.
* **Optional:** `mysqlclient` (if using MySQL).

---

## ⚡ Quick Start (Local Development)

### 1. Setup Environment

```bash
# Create a virtual environment
python -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install django==3.0.5
# Optional: pip install mysqlclient

```

### 2. Configure Database

If you wish to use **SQLite** for a quick test, update the `DATABASES` section in `settings.py`:

```python
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

```

### 3. Initialize & Run

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```

Visit `http://127.0.0.1:8000` to view the site.

---

## 📝 Known Issues & Notes

* **Context Mismatch:** The homepage view returns `{'dest': dests}`, but the template expects `dests`. Update `travello/views.py` to return `{'dests': dests}` to fix rendering.
* **User App:** The `users` app is present but must be added to `INSTALLED_APPS` in `settings.py` for Django to manage it.
* **DB Alignment:** The repository contains a `db.sqlite3` file, but `settings.py` defaults to MySQL. Ensure these match before running migrations.

## 🤝 How to Contribute

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Add tests for your models and views.
4. Open a Pull Request.

* *Planned:* Integration of **Django REST Framework** for API endpoints (see `serializers.py`).

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
