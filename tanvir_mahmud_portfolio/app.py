import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-this-secret-key-before-deployment")
database_url = os.getenv("DATABASE_URL", "sqlite:///portfolio.db")
# Render/Railway sometimes provide postgres://; SQLAlchemy expects postgresql://
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(180), nullable=False)
    service = db.Column(db.String(120), nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


SERVICES = [
    {"icon": "◈", "title": "Social Media Marketing", "desc": "Build a consistent brand presence and connect with the right audience."},
    {"icon": "◎", "title": "Facebook & Instagram Ads", "desc": "Reach relevant people with carefully planned paid campaigns."},
    {"icon": "↗", "title": "Google Ads", "desc": "Put your business in front of people actively searching for your offer."},
    {"icon": "⌕", "title": "SEO", "desc": "Improve search visibility and help the right audience discover you."},
    {"icon": "▤", "title": "Content Strategy", "desc": "Plan engaging content that communicates your value clearly."},
    {"icon": "▥", "title": "Analytics & Reporting", "desc": "Understand campaign performance and make more informed decisions."},
]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        service = request.form.get("service", "").strip()
        message = request.form.get("message", "").strip()
        if not all([name, email, message]):
            flash("Please complete your name, email, and message.", "error")
            return redirect(url_for("home") + "#contact")
        db.session.add(ContactMessage(name=name, email=email, service=service, message=message))
        db.session.commit()
        flash("Thanks! Your message has been saved. Tanvir can follow up with you.", "success")
        return redirect(url_for("home") + "#contact")
    return render_template("index.html", services=SERVICES)


@app.route("/health")
def health():
    try:
        db.session.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as exc:
        app.logger.exception("Database health check failed")
        return {"status": "error", "database": "unavailable"}, 503


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "true").lower() == "true")
