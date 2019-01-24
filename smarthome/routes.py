from smarthome import app, ont, adoI
from flask import request
from smarthome.adoxx_import import AdoxxImporter
from smarthome.ontology_handler import Ontology
from smarthome.blockchain_handler import Blockchain
import json


@app.route('/')
@app.route('/home')
def home():
    return "Home"


@app.route('/api/prosumers', methods=['GET', 'POST', 'PUT'])
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

        # The information from the model will be extracted and return as lists
        list_p = adoI.import_prosumer(request.data)
        list_ec = adoI.import_energy_controlling(request.data)
        list_es = adoI.import_energy_source(request.data)
        list_eca = adoI.import_energy_consumption_appliances(request.data)

        # Add information to ontogy
        for prosumer in list_p:
            ont.insert_prosumer(prosumer)

        for eca in list_eca:
            ont.insert_energy_consuming_appliances(eca)

        for energysource in list_es:
            ont.insert_energy_source(energysource)

        for energycontroller in list_ec:
            ont.insert_energy_controlling(energycontroller)

        ont.commit()

        # TODO: Add all information to ontology

        # Check if the prosumer is already in the ontology. If he or she is skip prosumer.
        # for ec in ec_list:
        #contract_id = bc.create_contract_consuming_appliances()

        # Maybe TODO: create smart contracts for the devices
        # for ec in ec_list:
        #     ont.addEC(ec)

        # TODO: Check smart contracts

        return "Model inserted"

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


@app.route('/api/prosumers/<prosumer_id>/contracts/')
def contracts():
    '''
        GET: Returns a list of all smart contracts a prosumer has.
    '''

    #contracts = ont.get_contracts()

    return "List of Smart contracts"


@app.route('/api/prosumers/<prosumer_id>/devices/')
def devices():
    pass


@app.route('/api/prosumers/<prosumer_id>/devices/<device_id>')
def device():
    pass
