from flask import Flask
from smarthome.ontology_handler import Ontology
from smarthome.adoxx_import import AdoxxImporter


adoI = AdoxxImporter()
onto = Ontology()
app = Flask(__name__)
from smarthome import routes  # must be after app instantiation
