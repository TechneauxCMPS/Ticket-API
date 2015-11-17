from flask import Flask
from ticketapi.data.logger import logger

__version__ = '0.0.5'
__all__ = ['app']

# Setup our package level flask application
app = Flask(__name__)

# Add our log handler for flask to handle our logs
app.logger.addHandler(logger.handlers[0])
