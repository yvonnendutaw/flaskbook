from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class NameForm(Form):
    user = StringField('What is your name?', validators=[Required()])
    password = PasswordField('What is your password?' validators=[Required()])
    submit = SubmitField('Submit')
