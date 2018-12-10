import sys, os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(src_path)
from classes.energy_controlling import EnergyControlling

# import ontology api

class Platform():
    def __init__(self):
        ec = EnergyControlling( 'name1', 'type1', 'age1', 'description1', 'system_type1', 'counter1', 'task1')

        print(ec)

    
    # define methods to access ontology
        # get all   (GET)
        # get one   (GET)
        # set one   (POST)
        #           (PUT)
        # remove one (DELETE)
    


