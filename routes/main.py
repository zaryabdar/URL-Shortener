from flask import Blueprint, render_template, redirect, url_for, flash
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
        while True:
            short_code = generate_short_code()
            exists = Link.query.filter_by(short_code = short_code).first()
            if not exists:
                break

        link = Link(
            original_url =original_url,
            short_code = short_code,
            user_id = current_user.id
        )
        db.session.add(link)
        db.session.commit()
        flash("URL shortened successfully!", "success")

        return redirect(url_for("main.dashboard"))
    
    Links = Link.query.filter_by(user_id = current_user.id).all()

    return render_template("dashboard.html", form = form, links = Links)


@main.route("/<short_code>")
def redirect_to_url(short_code):
    link = Link.query.filter_by(short_code = short_code).first()
    if link:
        link.click_count+=1
        db.session.commit()
        return redirect(link.original_url)
    flash("Something went wrong.", "danger")
    return "Short URL Not Found",404

@main.route("/delete/<int:link_id>",methods = ["POST"])
@login_required
def delete_url(link_id):
    link = Link.query.filter_by(
    id=link_id,
    user_id=current_user.id
    ).first()
    db.session.delete(link)
    db.session.commit()
    flash("URL deleted successfully!", "success")
    return redirect(url_for("main.dashboard"))