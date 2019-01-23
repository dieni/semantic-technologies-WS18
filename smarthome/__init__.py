from flask import Flask

app = Flask(__name__)
from smarthome import routes  # must be after app instantiation
