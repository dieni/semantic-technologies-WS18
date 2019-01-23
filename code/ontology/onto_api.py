from owlready2 import *


class OntologyAPI:

    def __init__(self):
        # self.onto = get_ontology('file://C:/Users/Christian/Jottacloud/Documents/Wirtschaftsinformatik/Master/workfolder/semanticTechnologiesWS18.git/code/ontology/Ontology_Beta.owl')
        self.onto = get_ontology('Ontology_Beta.owl')
        self.onto.load()

    def setclassenergycontrolling(self, id, name, type, description, systemtype, counter, task):
        self.onto.Energy_Controlling(name, Name=[id], Type=[type], Description=[
                                     description], System_Type=[systemtype], Counter=[counter], Task=[task])
        self.onto.save('Ontology_Beta.owl')

    def setclassenergysource(self, id, name, type, description, Power_Supplying_Maximum, Power_Supplying_Average, Power_Supplying_Current, Supplying_Begin, Supplying_End, Power_Production_Maximum, Power_Production_Average, Power_Production_Current, Production_Begin, Production_End, Active):
        self.onto.Energy_Source(name, Name=[id], Type=[type], Description=[description], Power_Supplying_Maximum=[Power_Supplying_Maximum], Power_Supplying_Average=[Power_Supplying_Average], Power_Supplying_Current=[Power_Supplying_Current], Supplying_Begin=[Supplying_Begin], Supplying_End=[
                                Supplying_End], Power_Production_Maximum=[Power_Production_Maximum], Power_Production_Average=[Power_Production_Average], Power_Production_Current=[Power_Production_Current], Production_Begin=[Production_Begin], Production_End=[Production_End], Active=[Active])
        self.onto.save('Ontology_Beta.owl')

    def setclassenergyconsumingappliances(self, id, name, type, description, Power_Consuming_Maximum, Power_Consuming_Average, Power_Consuming_Current, Consuming_Begin, Consuming_End, Active):
        self.onto.Energy_Consuming_Appliances(name, Name=[id], Type=[type], Description=[description], Power_Consuming_Maximum=[Power_Consuming_Maximum], Power_Consuming_Average=[
                                              Power_Consuming_Average], Power_Consuming_Current=[Power_Consuming_Current], Consuming_Begin=[Consuming_Begin], Consuming_End=[Consuming_End], Active=[Active])
        self.onto.save('Ontology_Beta.owl')

    def setclassprosumer(self, id, name, Description, Private_Address, Public_Address):
        self.onto.Prosumer(id, Name=[name], Description=[Description], Private_Address=[
                           Private_Address], Public_Address=[Public_Address])
        self.onto.save('Ontology_Beta.owl')

    def getAllIndividuals(self):
        # return 'List of individuals'

        return list(self.onto.individuals())
