from flask import Blueprint, render_template, redirect, url_for, flash
from forms import RegistrationForm,LoginForm,ForgotPasswordForm, ResetPasswordForm
from models import User
from flask_login import login_required, logout_user, login_user, current_user
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from email_utils import send_reset_email

auth = Blueprint("auth",__name__)

@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = generate_password_hash(form.password.data)
        user = User(
            username = form.username.data,
            email = form.email.data,
            password_hash = hash_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form = form, show_footer = False) 

@auth.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Welcome back!", "success")
            if current_user.is_authenticated:
                return redirect(url_for("main.dashboard"))
        flash("Invalid email or password.", "danger")
    return render_template("login.html", form = form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user:
            send_reset_email(user)

        flash(
            "If an account exists, a reset link has been sent.",
            "success"
        )

        return redirect(url_for("auth.login"))

    return render_template(
        "forgot_password.html",
        form=form
    )

@auth.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):

    user = User.verify_reset_token(token)

    if not user:
        flash("Invalid or expired token.", "danger")
        return redirect(url_for("auth.login"))

    form = ResetPasswordForm()

    if form.validate_on_submit():

        user.password_hash = generate_password_hash(
            form.password.data
        )

        db.session.commit()

        flash("Password updated successfully!", "success")

        return redirect(url_for("auth.login"))

    return render_template(
        "reset_password.html",
        form=form
    )