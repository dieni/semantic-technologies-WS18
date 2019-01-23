from smartenergy import app


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


@app.route('/prosumers/')
def prosumers():
    pass


@app.route('/prosumers/<id>')
def prosumer():
    pass


@app.route('/prosumers/<id>/devices/')
def devices():
    pass


@app.route('/prosumers/<id>/devices/<id>')
def device():
    pass


@app.route('/prosumers/<id>/transactions/')
def devices():
    pass


@app.route('/prosumers/<id>/devices/<id>')
def device():
    pass
