from flask import Blueprint, render_template
from flask_login import login_required
from forms import UrlForm

main = Blueprint("main",__name__)

@main.route("/", methods = ["GET","POST"])
@login_required
def dashboard():
    form = UrlForm()

    print("Submitted:", form.is_submitted())
    print("Validated:", form.validate_on_submit())
    print(form.errors)

    if form.validate_on_submit():
        original_url = form.original_url.data
        print(original_url)

    return render_template("dashboard.html", form = form)
