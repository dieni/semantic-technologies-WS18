from smarthome import app
from flask import request
from smarthome import adoxx_import
from smarthome import ontology_handler

'''
    Ressource:

    - Prosumer
    - Transaction
    - Devices


'''


@app.route('/')
@app.route('/home')
def home():
    return "Home"


# create importer connection
ai = adoxx_import.AdoxxImporter()
# creat ontology connection
ont = ontology_handler.OntologyAPI()


@app.route('/api/prosumers/', methods=['GET', 'POST', 'PUT'])
def prosumers():
    '''
        prosumer / smart home

        GET:    Get a list of all prosumers
        POST:   Create a new prosumer
        PUT:    Update a prousmer
    '''

    if request.method == 'POST':
        # Add a new prosumer.
        # Upload of an adoxx model.

        # The information from the model will be extracted and return as lists
        list_p = ai.import_prosumer(request.data)
        # list_ec = ai.import_energy_controlling(request.data)
        # list_es = ai.import_energy_controlling(request.data)
        # list_esc = ai.import_energy_consumption_appliances(request.data)
        # add information to ontogy
        #  for ec in ec_list:
        #       ont.addEC(ec)

        list_p[0].getprosumer

    elif request.method == 'PUT':
        pass
        # update a prosumer

    else:
        return "List of prosumers"


@app.route('/api/prosumers/<id>')
def prosumer():
    pass


@app.route('/api/prosumers/<id>/devices/')
def devices():
    pass


@app.route('/api/prosumers/<id>/devices/<id>')
def device():
    pass


@app.route('/api/prosumers/<id>/contracts/')
def contracts():
    pass


@app.route('/api/prosumers/<id>/contracts/<id>')
def contract():
    pass
