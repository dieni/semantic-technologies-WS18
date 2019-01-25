from owlready2 import *

ontology_path = 'smarthome/Ontology2.owl'
onto = get_ontology(ontology_path)


class SmartHome:
    id = 0

    def setsmarthomefromxml(self, model):
        self.id = model[0].getAttribute("id")

    def getsmarthome(self):
        print("Die Ausgabe von der Smart Home Class")
        print(self.id)


class Prosumer:
    id = 0
    name = "null"
    description = "null"
    publicaddress = "null"
    privateaddress = "null"

    def getprosumer(self):
        print("Die Ausgabe von der Prosumer Class")
        print(self.id)
        print(self.name)
        print(self.description)
        print(self.publicaddress)
        print(self.privateaddress)


class EnergySource:
    id = 0
    name = "null"
    powerSupplyingMaximum = 0
    powerSupplyingAverage = 0
    powerSupplyingCurrent = 0
    supplyingBegin = "01.01.1900"
    supplyingEnd = "01.01.1900"
    description = "null"
    powerProductionMaximum = 0
    powerProductionAverage = 0
    powerProductionCurrent = 0
    productionBegin = "01.01.1900"
    productionEnd = "01.01.1900"
    active = "null"
    type = "null"

    def getenergysource(self):
        print("Die Ausgabe von der Energy Consuming Appliance Class")
        print(self.id)
        print(self.name)
        print(self.powerSupplyingMaximum)
        print(self.powerSupplyingAverage)
        print(self.powerSupplyingCurrent)
        print(self.supplyingBegin)
        print(self.supplyingEnd)
        print(self.description)
        print(self.powerProductionMaximum)
        print(self.powerProductionAverage)
        print(self.powerProductionCurrent)
        print(self.productionBegin)
        print(self.productionEnd)
        print(self.active)
        print(self.type)


class EnergyControlling:
    id = 0
    name = "null"
    description = "null"
    systemType = "null"
    counter = 0
    task = "null"
    type = "null"

    def getenergycontrolling(self):
        print("Die Ausgabe von der Energy Controlling Class")
        print(self.id)
        print(self.name)
        print(self.description)
        print(self.systemType)
        print(self.counter)
        print(self.task)
        print(self.type)


class EnergyConsumingAppliance:
    id = 0
    name = "null"
    description = "null"
    powerConsumingMaximum = 0
    powerConsumingAverage = 0
    powerConsumingCurrent = 0
    consumingBegin = "01.01.1900"
    consumingEnd = "01.01.1900"
    active = "null"
    type = "null"

    def getenergyconsumingappliance(self):
        print("Die Ausgabe von der Energy Consuming Appliance Class")
        print(self.id)
        print(self.name)
        print(self.description)
        print(self.powerConsumingMaximum)
        print(self.powerConsumingAverage)
        print(self.powerConsumingCurrent)
        print(self.consumingBegin)
        print(self.consumingEnd)
        print(self.active)
        print(self.type)
