from smarthome import app
from Flask import request

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


ai = AdoxxImporter()
ont = Ontology()


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
            ec_list = ai.importEnergyConsumption(request.data)
        # add information to ontogy
            for ec in ec_list:
                ont.addEC(ec)
        pass

    elif request.method == 'PUT':
        # update a prosumer
        pass

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
