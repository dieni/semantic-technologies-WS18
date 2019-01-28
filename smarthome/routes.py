from smarthome import app, onto, adoI
from flask import request, jsonify
from smarthome.blockchain_handler import BlockchainHandler
from smarthome.contracts import SmartContract, ECAContract
from smarthome.ontology_handler import Ontology
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

        if not onto.get_prosumer(prosumer.id):

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

            return "Prosumer inserted!"

        return "Error: Prosumer exists already!"

    elif request.method == 'PUT':
        # update a prosumer

        # retriev all ecas from model
        # prosumer = adoI.import_prosumer(request.data)[0]
        # list_eca = adoI.import_energy_consumption_appliances(request.data)
        onto_ecas = onto.get_ecas()

        # get prosumer private key
        # TODO: privatekey = onto.get_privatekey(prosumer)
        privatekey = "B99D08E11DD90D55DB8A4442479BAFB1E8B18EEEDBF6F7BE54500DFBBDBC9DFE"
        bh = BlockchainHandler(privatekey)

        # get all contracts from ontology for ecas

        abi = ECAContract.abi

        contracts = []
        # run contracts
        for eca in onto_ecas:
            contract = onto.get_contract("sc" + str(eca.name))

            tx_hash = contract.Contract_Address[0]
            c = SmartContract(tx_hash, abi, eca.name)
            msg = bh.run_eca_contract(tx_hash, abi, eca)
            c.set_msg(msg)
            contracts.append(c.todict())

        return jsonify(contracts)

    else:
        return jsonify(onto.get_prosumers())


@app.route('/api/prosumers/<urn>')
def prosumer(urn):
    return jsonify(onto.get_prosumer_dict(urn))


@app.route('/api/prosumers/<prosumer_id>/trade')
def trade(prosumer_id):
    privatekey = "B99D08E11DD90D55DB8A4442479BAFB1E8B18EEEDBF6F7BE54500DFBBDBC9DFE"
    bh = BlockchainHandler(privatekey)

    onto_ecas = onto.get_ecas()
    onto_ess = onto.get_ess()

    consumption = 0
    for eca in onto_ecas:
        consumption += int(eca.Power_Consuming_Current[0])

    production = 0
    for es in onto_ess:
        production += int(es.Power_Production_Current[0])

    delta = production - consumption

    tx_hash, abi = bh.deploy_contract_trade()

    delta, msg = bh.run_trade_contract(tx_hash, abi, delta)

    return str(delta) + str(msg)


@app.route('/api/prosumers/<prosumer_id>/logconsumption')
def logconsumption(prosumer_id):
    '''
        UC: Log energyconsumption
    '''

    privatekey = "B99D08E11DD90D55DB8A4442479BAFB1E8B18EEEDBF6F7BE54500DFBBDBC9DFE"
    bh = BlockchainHandler(privatekey)

    onto_ecas = onto.get_ecas()

    consumption = 0
    for eca in onto_ecas:
        consumption += int(eca.Power_Consuming_Current[0])

    tx_hash, abi = bh.deploy_contract_Logger(consumption)

    msg = bh.run_log_contract(tx_hash, abi)

    return "Your cunsumption was logged with: " + str(msg) + " Watt!"


@app.route('/prosumers/<prosumer_id>/deploycontracts')
def deployContracts(prosumer_id):

    # create smart contracts for the devices
    # TODO: privatekey = prosumer.privateaddress

    privatekey = 'B99D08E11DD90D55DB8A4442479BAFB1E8B18EEEDBF6F7BE54500DFBBDBC9DFE'
    bh = BlockchainHandler(privatekey)

    # prosumer = onto.get_prosumer(str(prosumer_id))
    # onto_ecas = onto.get_eca_from_prosumer(prosumer)
    onto_ecas = onto.get_ecas()

    contracts = []
    for eca in onto_ecas:
        bh = BlockchainHandler(privatekey)
        tx_hash, abi = bh.deploy_contract_ECA(eca)
        contract = SmartContract(tx_hash, abi, eca.name)

        # save contract in ontology
        c = onto.insert_contract_ECA(tx_hash, eca)
        eca.ConsumingAppliancehasSmartContract = [c]

        # append as dict so we can serialize it to json later
        contracts.append(contract.todict())
        # We need to wait befor we deploy the next contract

    onto.commit()

    # Add contract tx_hash to eca

    return jsonify(contracts)
