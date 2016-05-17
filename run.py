from flask import Flask
from flask import redirect
app = Flask(__name__)

@app.route('/')
def index():
	return redirect('http://google.com')

#@app.route('/user/<name>')
#def user(name):
	#return 'hello, %s!' % name

if __name__ == '__main__':
	app.run(debug=True)
