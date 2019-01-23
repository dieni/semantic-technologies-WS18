import os
import xml.dom.minidom as dom
from smartenergy.ontology_handler import OntologyAPI
from smartenergy.models import SmartHome, Prosumer, EnergySource, EnergyControlling, EnergyConsumingAppliance


class AdoxImporter:

    def setsmarthomefromxml(self, model):
        self.id = model[0].getAttribute("id")

    def getsmarthome(self):
        print("Die Ausgabe von der Smart Home Class")
        print(self.id)

    def doit(self):
        print('here to do so')
        ontAPI = OntologyAPI()
        print('loaded api')

        # get xml
        xml_path = os.path.join(os.path.dirname(__file__), "smarthome.xml")
        baum = dom.parse(xml_path)
        print('xml loaded')

        # get all instances
        instances = baum.getElementsByTagName("instance")
        # connectors = baum.getElementsByTagName("connector")

        # get model instance
        model = baum.getElementsByTagName("model")
        modelinstance = SmartHome()
        modelinstance.setsmarthomefromxml(model)
        modelinstance.getsmarthome()

        for instance in instances:

            idpara = instance.getAttribute("id")
            namepara = instance.getAttribute("name")

            if instance.getAttribute("class") == "Prosumer":
                ec = Prosumer()
                ec.setprosumerfromxml(idpara, namepara, instance)
                # replace all blanks an hyphen
                nameNoBlank = ec.name.replace(" ", "")
                nameNoBlankHyphen = nameNoBlank.replace("-", "")
                print("++++++++++" + nameNoBlankHyphen)
                ontAPI.setclassprosumer(ec.id, nameNoBlankHyphen, ec.description, ec.privateaddress, ec.publicaddress)
                print("saved class Prosumer to ontology")
                ec.getprosumer()

            if instance.getAttribute("class") == "Energy Controlling":
                ec = EnergyControlling()
                ec.setenergycontrollingfromxml(idpara, namepara, instance)
                # replace all blanks an hyphen
                nameNoBlank = ec.name.replace(" ", "")
                nameNoBlankHyphen = nameNoBlank.replace("-", "")
                print("++++++++++" + nameNoBlankHyphen)
                ontAPI.setclassenergycontrolling(ec.id, nameNoBlankHyphen, ec.type, ec.description, ec.systemType,
                                                 ec.counter, ec.task)
                print("saved class Energy_Controlling to ontology")
                ec.getenergycontrolling()

            if instance.getAttribute("class") == "Energy Consuming Appliances":
                eca = EnergyConsumingAppliance()
                eca.setenergyconsuminappliancefromxml(idpara, namepara, instance)
                # def setclassenergyconsumingappliances(self, onto, id, name, type, description, Power_Consuming_Maximum, Power_Consuming_Average, Power_Consuming_Current, Consuming_Begin, Consuming_End, Active):
                # replace all blanks an hyphen
                nameNoBlank = eca.name.replace(" ", "")
                nameNoBlankHyphen = nameNoBlank.replace("-", "")
                print("++++++++++" + nameNoBlankHyphen)
                ontAPI.setclassenergyconsumingappliances(eca.id, nameNoBlankHyphen, eca.type, eca.description,
                                                         eca.powerConsumingMaximum, eca.powerConsumingAverage,
                                                         eca.powerConsumingCurrent, eca.consumingBegin,
                                                         eca.consumingEnd, eca.active)
                print("saved class Energy_Consuming Appliances to ontology")
                eca.getenergyconsumingappliance()

            if instance.getAttribute("class") == "Energy Source":
                es = EnergySource()
                # def setclassenergysource(self, onto, id, name, type, description, Power_Supplying_Maximum, Power_Supplying_Average, Power_Supplying_Current, Supplying_Begin, Supplying_End, Power_Production_Maximum, Power_Production_Average, Power_Production_Current, Production_Begin, Production_End):
                es.setenergysourcefromxml(idpara, namepara, instance)
                # replace all blanks an hyphen
                nameNoBlank = es.name.replace(" ", "")
                nameNoBlankHyphen = nameNoBlank.replace("-", "")
                print("++++++++++" + nameNoBlankHyphen)
                ontAPI.setclassenergysource(es.id, nameNoBlankHyphen, es.type, es.description, es.powerSupplyingMaximum,
                                            es.powerSupplyingAverage, es.powerSupplyingCurrent, es.supplyingBegin,
                                            es.supplyingEnd, es.powerProductionMaximum, es.powerProductionAverage,
                                            es.powerProductionCurrent, es.productionBegin, es.productionEnd, es.active)
                print("saved class Energy_Source to ontology")
                es.getenergysource()

