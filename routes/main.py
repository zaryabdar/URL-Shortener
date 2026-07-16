from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from forms import UrlForm
from models import Link
from extensions import db
import secrets
import string

main = Blueprint("main",__name__)

def generate_short_code(length = 6):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

@main.route("/", methods = ["GET","POST"])
@login_required
def dashboard():
    form = UrlForm()


    if form.validate_on_submit():
        original_url = form.original_url.data
        short_code = generate_short_code()
        link = Link(
            original_url =original_url,
            short_code = short_code,
            user_id = current_user.id
        )
        db.session.add(link)
        db.session.commit()

        return redirect(url_for("main.dashboard"))
    
    Links = Link.query.filter_by(user_id = current_user.id).all()

    return render_template("dashboard.html", form = form, links = Links)


@main.route("/<short_code>")
def redirect_to_url(short_code):
    link = Link.query.filter_by(short_code = short_code).first()
    if link:
        return redirect(link.original_url)
    
    return "Short URL Not Found",404