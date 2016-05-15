from flask import render_template

from flask_login import login_required

from . import app
from .util import check_expired

@app.route('/use_app')
@login_required
@check_expired
def use_app():
    """Use our amazing app."""
    # [...]
    return render_template('use_app.html')

@app.route('/account/billing')
@login_required
def account_billing():
    """Update your billing info."""
    # [...]
    return render_template('account/billing.html')

#forms
from flask import render_template, redirect, url_for

from . import app
from .forms import EmailPasswordForm

@app.route('/login', methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():

        # Check the password and log the user in
        # [...]

        return redirect(url_for('index'))
    return render_template('login.html', form=form)
