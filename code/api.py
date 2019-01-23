'''
This file represents the rest api to the system.

Ressources for interaction:
/contracts
- GET: See all smart contracts

/prosumers
- GET:      Get a list of all prosumers
- (POST:    Add a new prosumer)
- (PUT:     Update a prosumer)
- (DELETE:  Delete a prosumer)



'''
from flask import Flask, render_template
from flask import request


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/prosumers')
def prosumers():

    re = 'List of prosumer is comming'

    return re


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


if __name__ == '__main__':
    app.run(debug=True)
