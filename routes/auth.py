from flask import Blueprint, render_template, redirect, url_for
from forms import RegistrationForm

auth = Blueprint("auth",__name__)

@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for(auth.login))
    return render_template("register.html", form = form) 