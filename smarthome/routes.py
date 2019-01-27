from smarthome import app, onto, adoI
from flask import request, jsonify
from smarthome.blockchain_handler import BlockchainHandler
from smarthome.contracts import SmartContract
import time


@app.route('/')
@app.route('/home')
def home():
    return "Home"


@app.route('/api/prosumers', methods=['GET', 'POST', 'PUT'])
def prosumers():
    '''
        prosumers / smart homes

        GET:    Get a list of all prosumers
        POST:   Create a new prosumer and smart contracts --> upload of an adoxx model
        PUT:    Run smart contracts with new model values and see if contract triggers --> upload of an adoxx model
    '''

    if request.method == 'POST':
        # Add a new prosumer.
        # Upload of an adoxx model.

        # The information from the model will be extracted and return as lists
        # Only one prosumer per model!
        prosumer = adoI.import_prosumer(request.data)[0]

        # There is only one energy controller per smarthome
        energycontroller = adoI.import_energy_controlling(request.data)[0]

        # There is only one energy Source
        energysource = adoI.import_energy_source(request.data)[0]

        # List of Consumption Appliances
        list_eca = []
        list_eca = adoI.import_energy_consumption_appliances(request.data)

        # TODO: Check if Information is already in the ontology

        # Add information to ontogy
        # order of insert is important because of relationship insert
        # 1. prosumer 2. controlling 3. source
        # 4. Appliances
        ont_p = onto.insert_prosumer(prosumer)
        ont_ec = onto.insert_energy_controlling(energycontroller)
        ont_es = onto.insert_energy_source(energysource)

        # set Relation ProsumerOwnsControlling
        ont_p.ProsumerOwnsControlling = [ont_ec]
        # set Relation ControllingReceivesFromSource
        ont_ec.ControllingReceivesFromSource = [ont_es]

        # insert alle consuming appliances and set relation Energysource -> Consuming Appliances
        # happens in insert methode
        for eca in list_eca:
            ont_eca = onto.insert_energy_consuming_appliances(eca)
            ont_ec.ControllingControllsConsumingAppliances.append(ont_eca)

        onto.commit()

        # create smart contracts for the devices
        # TODO: privatekey = prosumer.privateaddress

        privatekey = 'B99D08E11DD90D55DB8A4442479BAFB1E8B18EEEDBF6F7BE54500DFBBDBC9DFE'
        bh = BlockchainHandler(privatekey)

        string = ""
        onto_ecas = onto.get_eca_from_prosumer(ont_p.name)

        for eca in onto_ecas:
            string = string + str(eca.name) + "\n"

        onto.commit()
        return string

        contracts = []
        for eca in onto_ecas:
            bh = BlockchainHandler(privatekey)
            tx_hash, abi = bh.deploy_contract_ECA(eca)
            contract = SmartContract(tx_hash, abi, eca.name)

            # save contract in ontology

            # append as dict so we can serialize it to json later
            contracts.append(contract.todict())
            time.sleep(40)  # We need to wait befor we deploy the next contract

        # Add contract tx_hash to eca

        return jsonify(contracts)

    elif request.method == 'PUT':
        # update a prosumer

        # TODO: Check smart contracts

        # retriev all ecas from model
        prosumer = adoI.import_prosumer(request.data)[0]
        list_eca = adoI.import_energy_consumption_appliances(request.data)

        # get prosumer private key
        # TODO: privatekey = onto.get_privatekey(prosumer)
        privatekey = 'B99D08E11DD90D55DB8A4442479BAFB1E8B18EEEDBF6F7BE54500DFBBDBC9DFE'
        bh = BlockchainHandler(privatekey)

        # get all contracts from ontology for ecas
        # TODO: contracts = onto.get_eca_contracts(prosumer)

        # run contracts
        # for eca in list_eca:
        #     for c in contracts:
        #         if c.device_id == eca.id:
        #             bh.run_eca_contract(c, eca)

        # TODO: create json

        return "ecas and contract msgs"

    else:
        return jsonify(onto.get_prosumers())


@app.route('/api/prosumers/<urn>')
def prosumer(urn):
    return jsonify(onto.get_prosumer_dict(urn))


@app.route('/api/prosumers/<prosumer_id>/contracts')
def contracts():
    '''
        GET: Returns a list of all smart contracts a prosumer has.
    '''

    #contracts = onto.get_contracts()

    return "List of Smart contracts"


@app.route('/test')
def test():
    # return str(len(onto.get_ecas()))
    return "asd"

# @app.route('/api/prosumers/<prosumer_id>/devices/')
# def devices():
#     pass


# @app.route('/api/prosumers/<prosumer_id>/devices/<device_id>')
# def device():
#     pass
