# Tanvir Mahmud — Digital Marketing Portfolio

A responsive personal portfolio built with **Python 3.14, Flask, PostgreSQL, HTML, CSS, and JavaScript**. The contact form stores inquiries in the database.

## Features
- Responsive desktop/mobile layout
- Tanvir's uploaded portrait
- Hero, experience stats, about, services, workflow, contact form, footer
- Mobile navigation and subtle reveal animations
- PostgreSQL contact-message storage via SQLAlchemy
- `/health` endpoint to check app/database connectivity
- Local SQLite fallback if `DATABASE_URL` is not configured

## 1. Open in PyCharm
1. Extract the ZIP.
2. Open the `tanvir_mahmud_portfolio` folder in PyCharm.
3. Configure a Python 3.14 interpreter (Settings → Project → Python Interpreter).
4. Open PyCharm Terminal in the project folder.

## 2. Create a virtual environment and install packages

Windows PowerShell:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, use `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`, then run with `.\.venv\Scripts\python.exe app.py`.

## 3. Configure PostgreSQL
Make sure PostgreSQL is installed and running. In pgAdmin Query Tool, or `psql`, run:

```sql
CREATE DATABASE tanvir_portfolio;
```

Copy `.env.example` to `.env` and set your actual PostgreSQL username/password. Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/tanvir_portfolio
SECRET_KEY=put-a-long-random-secret-here
FLASK_DEBUG=true
```

Use URL-encoding for special characters in the database password (for example, `@` becomes `%40`). Do not share or commit `.env`.

**Alternative:** If you leave `DATABASE_URL` unset, the app uses a local SQLite database automatically, so you can preview it without configuring PostgreSQL.

## 4. Run the website

```powershell
python app.py
```

Open http://127.0.0.1:5000 in your browser. The first run creates the `contact_message` table automatically. Submit the contact form to test saving an inquiry. Visit http://127.0.0.1:5000/health to check database connectivity.

## Important before publishing
- Replace social/contact placeholders with Tanvir's real email, WhatsApp, and social URLs (not supplied yet).
- Only add genuine testimonials and verified performance metrics; this starter deliberately does not invent campaign results or reviews.
- Change `SECRET_KEY`, set `FLASK_DEBUG=false`, and use a production WSGI server (e.g. Waitress on Windows) before deployment.
- Use HTTPS and protect database credentials. A public deployment should also add spam protection/rate limiting to the contact form.

## Project layout

```text
tanvir_mahmud_portfolio/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    ├── js/main.js
    └── images/tanvir.png
```
