from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')
app.config.from_object('config')

#calls list converter in util.py

from flask import Flask

app = Flask(__name__)

from .util import ListConverter

app.url_map.converters['list'] = ListConverter
