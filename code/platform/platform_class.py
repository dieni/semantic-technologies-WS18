import sys, os
from classes.energy_controlling import EnergyControlling
from inputxml.loadXML import LoadXML


# import ontology api

class Platform():
    def __init__(self):
        pass

    def importXML(self):
        loadXML = LoadXML()
        loadXML.doit()


