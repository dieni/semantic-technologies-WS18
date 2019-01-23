from smarthome import app
from flask import request
from smarthome import adoxx_import


from smarthome.ontology_handler import Ontology
from smarthome.blockchain_handler import Blockchain


@app.route('/')
@app.route('/home')
def home():
    return "Home"

# create importer connection
ai = adoxx_import.AdoxxImporter()
# ai = AdoxxImporter()
ont = Ontology()
bc = Blockchain()


@app.route('/api/prosumers/', methods=['GET', 'POST', 'PUT'])
def prosumers():
    '''
        prosumers / smart homes

        GET:    Get a list of all prosumers
        POST:   Create a new prosumer
        PUT:    Update a prousmer
    '''

    if request.method == 'POST':
        # Add a new prosumer.
        # Upload of an adoxx model.

        # TODO: The information from the model will be extracted and return as lists
        list_p = ai.import_prosumer(request.data)
		# list_ec = ai.import_energy_controlling(request.data)
        # list_es = ai.import_energy_controlling(request.data)
        # list_esc = ai.import_energy_consumption_appliances(request.data)
        # add information to ontogy
        #  for ec in ec_list:
        #       ont.addEC(ec)

        list_p[0].getprosumer


        # TODO: Add information to ontogy
            # Check if the prosumer is already in the ontology. If he or she is skip prosumer.
            # for ec in ec_list:
                #contract_id = bc.create_contract_consuming_appliances()

        # Maybe TODO: create smart contracts for the devices
            # for ec in ec_list:
            #     ont.addEC(ec)

        # TODO: Check smart contracts

        pass

    elif request.method == 'PUT':
        # update a prosumer

        # TODO: Check smart contracts

        pass
        # update a prosumer

    else:
        return "List of prosumers"


@app.route('/api/prosumers/<id>')
def prosumer():

    return "Specific Prosumer "


@app.route('/api/prosumers/<id>/contracts/')
def contracts():
    '''
        GET: Returns a list of all smart contracts a prosumer has.
    '''

    #contracts = ont.get_contracts()

    return "List of Smart contracts"


@app.route('/api/prosumers/<id>/devices/')
def devices():
    pass


@app.route('/api/prosumers/<id>/devices/<id>')
def device():
    pass
