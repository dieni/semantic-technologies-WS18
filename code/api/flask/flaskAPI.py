from flask import Flask
from flask import request
import sys, os

# set sys path to root directory 'code'
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from ontology.onto_api import OntologyAPI
from inputxml.loadXML import LoadXML

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to our Project about Semantic Technologies!'

@app.route('/individuals', methods=['GET'])
def individuals():
    ontAPI = OntologyAPI()

    if request.method == 'GET':
        # return all individuals

        # create response string
        re = ''
        for i in ontAPI.getAllIndividuals():
            re = re + str(i) + '<br>'

        return re

    return 'no valid request'

@app.route('/import')
def importXML():
    # import the xml from adoxx into the ontology
    loadXML = LoadXML()
    loadXML.doit()

    return 'Adoxx models import ok!'

if __name__ == '__main__':
    app.run(debug=True)