from owlready2 import *
from smarthome.models import Prosumer, EnergyConsumingAppliance, EnergyControlling, EnergySource

# TODO: Check relations! How do we know a energy source belongs to a specific prosumer?


class Ontology:

    def __init__(self):
        self.ontology_path = 'smarthome/Ontology_Beta.owl'
        self.onto = get_ontology(self.ontology_path)
        self.onto.load()

    def insert_energy_controlling(self, ec):
        return self.onto.Energy_Controlling(ec.id, Name=[ec.name],
                                            Type=[ec.type],
                                            Description=[ec.description],
                                            System_Type=[ec.systemType],
                                            Counter=[ec.counter],
                                            Task=[ec.task])

    def insert_energy_source(self, es):
        return self.onto.Energy_Source(es.id,
                                       Name=[es.name],
                                       Type=[es.type],
                                       Description=[es.description],
                                       Power_Supplying_Maximum=[
                                         es.powerSupplyingMaximum],
                                       Power_Supplying_Average=[
                                         es.powerSupplyingAverage],
                                       Power_Supplying_Current=[
                                         es.powerSupplyingCurrent],
                                       Supplying_Begin=[es.supplyingBegin],
                                       Supplying_End=[es.supplyingEnd],
                                       Power_Production_Maximum=[
                                         es.powerProductionMaximum],
                                       Power_Production_Average=[
                                         es.powerProductionAverage],
                                       Power_Production_Current=[
                                         es.powerProductionCurrent],
                                       Production_Begin=[es.productionBegin],
                                       Production_End=[es.productionEnd],
                                       Active=[es.active])

    def insert_energy_consuming_appliances(self, eca, ec):
        eca = self.onto.Energy_Consuming_Appliances(eca.id,
                                                    Name=[eca.name],
                                                    Type=[eca.type],
                                                    Description=[
                                                        eca.description],
                                                    Power_Consuming_Maximum=[
                                                        eca.powerConsumingMaximum],
                                                    Power_Consuming_Average=[
                                                        eca.powerConsumingAverage],
                                                    Power_Consuming_Current=[
                                                        eca.powerConsumingCurrent],
                                                    Consuming_Begin=[
                                                        eca.consumingBegin],
                                                    Consuming_End=[
                                                        eca.consumingEnd],
                                                    Active=[eca.active])

        ec.ControllingControllsConsumingAppliances.append(eca)

    def insert_prosumer(self, prosumer):

        return self.onto.Prosumer(prosumer.id,
                                  Name=[prosumer.name],
                                  Description=[prosumer.description],
                                  Private_Address=[prosumer.privateaddress],
                                  Public_Address=[prosumer.publicaddress])

    def commit(self):
        self.onto.save(self.ontology_path)

    def get_eca_contracts(self, prosumer):
        '''
        Get all the eca contracts from a prosumer.

        Return: List of contracts
        '''
        # TODO
        pass

    def get_prosumers(self):
        '''
        Get a list of all prosumer
        '''
        # TODO:
        pass

    def add_contract2prosumer(self):
        pass

    def get_energy_controlling(self):
        pass

    def get_energy_source(self):
        pass

    def get_energy_consuming_appliances(self):
        pass

    def get_prosumer(self):
        pass

    def getAllIndividuals(self):
        # return 'List of individuals'

        return list(self.onto.individuals())
