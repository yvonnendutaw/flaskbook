from flask import Flask, make_response, redirect, abort, render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
#
#@app.route('/index')
#def index():
#    return render_template('index.html')
#
#@app.route('/user/<name>')
#def user(name):
#    return render_template('user.html',
#                           user=user)

class NameForm(Form):
    user = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


#@app.route('/index')
#def index():
#     user = {'nickname':'jane'}
#     return render_template('index.html',
#                           user=user)

@app.route('/', methods=['GET', 'POST'])
def index():
    user = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.user.data
        form.user.data = ''
        return render_template('index.html',
                               form=form,
                               user=user)

##response
#@app.route('/')
#def index():
#    response = make_response('<h1>This document carries a cookie!</h1>')
#    response.set_cookie('answer', '42')
#    return response

##redirects to a different url
#@app.route('/')
#def index():
#    return redirect('http://www.example.com')

#aborts if it finds that the user is not a valid user

#@app.route('/user/<id>')
#def get_user(id):
#    user = load_user(id)
#    if not user:
#        abort(404)
#        return '<h1>Hello, %s</h1>' % user.name


if __name__ == '__main__':
    app.run(debug=True)
