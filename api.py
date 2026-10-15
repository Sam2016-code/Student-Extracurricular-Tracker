import os
import logging
from functools import wraps
from datetime import date
from urllib.parse import urlparse

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)
from dotenv import load_dotenv
from supabase import create_client

# ------------------------------
# Configuration
# ------------------------------
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

logging.basicConfig(level=logging.INFO)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not app.secret_key:
    raise RuntimeError("SECRET_KEY is missing from your .env file.")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        "SUPABASE_URL or SUPABASE_KEY is missing from your .env file."
    )

parsed_url = urlparse(SUPABASE_URL)
if parsed_url.scheme != "https" or not parsed_url.netloc:
    raise RuntimeError("Check the SUPABASE_URL in your .env file.")


def get_client():
    """Create a Supabase client using the project's public/anon key."""
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def get_user_client():
    """Create a client that sends the logged-in user's access token."""
    token = session.get("access_token")
    if not token:
        return None

    client = get_client()
    client.postgrest.auth(token)
    return client


def get_profile(client, user_id):
    response = (
        client.table("profiles")
        .select("id, full_name, role")
        .eq("id", user_id)
        .limit(1)
        .execute()
    )
    return response.data[0] if response.data else None


# ------------------------------
# Access control
# ------------------------------
def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in first.", "error")
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


def mentor_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if session.get("role") != "mentor":
            flash("You do not have mentor access.", "error")
            return redirect(url_for("dashboard"))
        return view(*args, **kwargs)

    return wrapped


# ------------------------------
# Home
# ------------------------------
@app.route("/")
def home():
    if session.get("user_id"):
        if session.get("role") == "mentor":
            return redirect(url_for("mentor_dashboard"))
        return redirect(url_for("dashboard"))
    return render_template("index.html")


# ------------------------------
# Student registration
# ------------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not full_name or not email or not password:
            flash("Please fill in all fields.", "error")
            return render_template("register.html")

        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
            return render_template("register.html")

        try:
            client = get_client()
            result = client.auth.sign_up(
                {
                    "email": email,
                    "password": password,
                    "options": {"data": {"full_name": full_name}},
                }
            )

            user = result.user
            auth_session = result.session

            if not user:
                flash("Registration failed. Please try again.", "error")
                return render_template("register.html")

            if not auth_session:
                flash(
                    "Account created. Confirm your email, then log in.",
                    "success",
                )
                return redirect(url_for("login"))

            profile = get_profile(client, user.id)
            if not profile:
                flash(
                    "Your account was created, but its profile is missing. "
                    "Check the Supabase profile trigger.",
                    "error",
                )
                return redirect(url_for("login"))

            session.clear()
            session["user_id"] = str(user.id)
            session["access_token"] = auth_session.access_token
            session["role"] = profile.get("role", "student")
            session["full_name"] = profile.get("full_name") or full_name

            if session["role"] == "mentor":
                return redirect(url_for("mentor_dashboard"))
            return redirect(url_for("dashboard"))

        except Exception:
            app.logger.exception("Registration error")
            flash(
                "Registration failed. Check the VS Code terminal for details.",
                "error",
            )

    return render_template("register.html")


# ------------------------------
# Login
# ------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Enter your email and password.", "error")
            return render_template("login.html")

        try:
            client = get_client()
            result = client.auth.sign_in_with_password(
                {"email": email, "password": password}
            )

            user = result.user
            auth_session = result.session

            if not user or not auth_session:
                flash("Login failed. Please try again.", "error")
                return render_template("login.html")

            profile = get_profile(client, user.id)
            if not profile:
                flash("Your profile was not found. Check Supabase.", "error")
                return render_template("login.html")

            session.clear()
            session["user_id"] = str(user.id)
            session["access_token"] = auth_session.access_token
            session["role"] = profile.get("role", "student")
            session["full_name"] = profile.get("full_name") or email

            if session["role"] == "mentor":
                return redirect(url_for("mentor_dashboard"))
            return redirect(url_for("dashboard"))

        except Exception:
            app.logger.exception("Login error")
            flash(
                "Login failed. Check your email, password, and email confirmation.",
                "error",
            )

    return render_template("login.html")


# ------------------------------
# Logout
# ------------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# ------------------------------
# Student dashboard
# ------------------------------
@app.route("/dashboard")
@login_required
def dashboard():
    if session.get("role") == "mentor":
        return redirect(url_for("mentor_dashboard"))

    activities = []
    client = get_user_client()

    if client is None:
        session.clear()
        return redirect(url_for("login"))

    try:
        result = (
            client.table("activities")
            .select("*")
            .eq("student_id", session["user_id"])
            .order("activity_date", desc=True)
            .execute()
        )
        activities = result.data or []
    except Exception:
        app.logger.exception("Student dashboard error")
        flash(
            "Could not load activities. Check the activities table and "
            "Supabase permissions.",
            "error",
        )

    return render_template(
        "dashboard.html",
        full_name=session.get("full_name", "Student"),
        activities=activities,
        today=date.today().isoformat(),
    )


# ------------------------------
# Add activity
# ------------------------------
@app.route("/add_activity", methods=["POST"])
@login_required
def add_activity():
    if session.get("role") != "student":
        flash("Only students can add activities.", "error")
        return redirect(url_for("home"))

    activity_name = request.form.get("activity_name", "").strip()
    activity_type = request.form.get("activity_type", "").strip()
    organization = request.form.get("organization", "").strip()
    activity_date = request.form.get("activity_date", "").strip()
    description = request.form.get("description", "").strip()
    certificate_url = request.form.get("certificate_url", "").strip()

    if not activity_name or not activity_type:
        flash("Activity name and type are required.", "error")
        return redirect(url_for("dashboard"))

    if activity_date:
        try:
            date.fromisoformat(activity_date)
        except ValueError:
            flash("Enter a valid activity date.", "error")
            return redirect(url_for("dashboard"))

    if certificate_url:
        parsed_certificate = urlparse(certificate_url)
        if parsed_certificate.scheme not in ("http", "https") or not parsed_certificate.netloc:
            flash("Enter a valid certificate URL.", "error")
            return redirect(url_for("dashboard"))

    data = {
        "student_id": session["user_id"],
        "activity_name": activity_name,
        "activity_type": activity_type,
        "organization": organization or None,
        "activity_date": activity_date or None,
        "description": description or None,
        "certificate_url": certificate_url or None,
    }

    try:
        client = get_user_client()
        if client is None:
            session.clear()
            return redirect(url_for("login"))

        client.table("activities").insert(data).execute()
        flash("Activity added successfully!", "success")
    except Exception:
        app.logger.exception("Add activity error")
        flash(
            "Could not add activity. Check the activities table columns "
            "and Supabase permissions.",
            "error",
        )

    return redirect(url_for("dashboard"))


# ------------------------------
# Delete activity
# ------------------------------
@app.route("/delete_activity/<activity_id>", methods=["POST"])
@login_required
def delete_activity(activity_id):
    if session.get("role") != "student":
        flash("Only students can delete activities.", "error")
        return redirect(url_for("home"))

    try:
        client = get_user_client()
        if client is None:
            session.clear()
            return redirect(url_for("login"))

        client.table("activities").delete().eq(
            "id", activity_id
        ).eq(
            "student_id", session["user_id"]
        ).execute()

        flash("Activity deleted if it belonged to your account.", "success")
    except Exception:
        app.logger.exception("Delete activity error")
        flash(
            "Could not delete activity. Check the activity ID column "
            "and Supabase permissions.",
            "error",
        )

    return redirect(url_for("dashboard"))


# ------------------------------
# Mentor dashboard
# ------------------------------
@app.route("/mentor")
@login_required
@mentor_required
def mentor_dashboard():
    client = get_user_client()
    if client is None:
        session.clear()
        return redirect(url_for("login"))

    try:
        students_result = (
            client.table("profiles")
            .select("id, full_name, role")
            .eq("role", "student")
            .execute()
        )
        activities_result = (
            client.table("activities")
            .select("*")
            .order("activity_date", desc=True)
            .execute()
        )

        students = students_result.data or []
        activities = activities_result.data or []
        names = {
            str(student["id"]): student.get("full_name") or "Student"
            for student in students
        }

        for activity in activities:
            activity["student_name"] = names.get(
                str(activity.get("student_id")), "Student"
            )

        return render_template(
            "mentor.html",
            students=students,
            activities=activities,
            full_name=session.get("full_name", "Mentor"),
        )

    except Exception:
        # Do not redirect back to /mentor here; that would repeat the same error.
        app.logger.exception("Mentor dashboard failed")
        flash(
            "Unable to load mentor dashboard. Check the VS Code terminal "
            "and Supabase Row Level Security policies.",
            "error",
        )
        return render_template(
            "mentor.html",
            students=[],
            activities=[],
            full_name=session.get("full_name", "Mentor"),
        ), 500


# ------------------------------
# Start server
# ------------------------------
if __name__ == "__main__":
    # Local development only. Use a production WSGI server when deployed.
    app.run(host="127.0.0.1", port=5000, debug=False)
