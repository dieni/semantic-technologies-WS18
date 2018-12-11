import sys
import os

from owlready2 import *
import xml.dom.minidom as dom

#get path to input classes
src_path_layer_up = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
print(src_path_layer_up)
sys.path.append(src_path_layer_up)
from inputxml.classes import EnergyControlling
from inputxml.classes import SmartHome
from inputxml.classes import EnergyConsumingAppliance
from inputxml.classes import EnergySource

from pathlib import Path

#get path to ontology class
src_path_layer_up = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(src_path_layer_up)
from ontology.ontology_class import Ontology
print("fertig")


#get path to ontology
#src_path_layer_up = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
#ontology_path = os.path.join(src_path, "ontologyprint\Ontology_Beta.owl" )
#print(ontology_path)


#connect to ontology
#owl_output_path = os.path.join(os.path.abspath(''), 'ontology')
#onto_output_path_full = os.path.join(owl_output_path, "Ontology_Beta.owl" )
#print("+++++++++++++++++++"+onto_output_path_full)
#onto_path.append(onto_output_path_full)
"""
owl_output_path = os.path.join(os.path.abspath(''), 'ontology', 'output')
print("+++++"+owl_output_path)

owl_output_path_slashturn = owl_output_path.replace("\\", "/")

owl_output_path_slashturn_plusfile = "file://" + owl_output_path_slashturn + "/Ontology_Beta.owl"
print("-----" + owl_output_path_slashturn_plusfile)
onto_path.append(owl_output_path)
"""
#onto = get_ontology("file://C:/Users/felix/CloudStation/_Studium/_Master_Wirtschaftsinformatik/SEMTEC_Project_GIT/code/ontology/Ontology_Beta.owl")
#"file://C:/Users/Ifangelium/workspace-pycharm/semanticTechnologiesWS18.git/code/inputxml/ontology/output/Ontology_Beta.owl")
onto = get_ontology("Ontology_Beta.owl")
onto.load()


#onto.load()

#create object from ontology class
ontologyobject = Ontology()


#xml path
src_path = os.path.abspath(os.path.dirname(__file__))
#get xml
xml_path = os.path.join(src_path, "smarthome.xml" )
print(xml_path)
baum = dom.parse(xml_path)

#get all instances
instances = baum.getElementsByTagName("instance")
connectors = baum.getElementsByTagName("connector")

#get model instance
model = baum.getElementsByTagName("model")
modelinstance = SmartHome()
modelinstance.setsmarthome(model)

#add text to id, because ontology dont likes integer and special charakters
idplustext = "id" + modelinstance.id
print(idplustext)
ontologyobject.setclassprosumer(onto, idplustext, "Joseph Volt", "Faster than Bolt", "secret", "0xc6s4df5s64d1cfs300")
print("saved class prosumer to ontology")
modelinstance.getsmarthome()


for instance in instances:
    print("\n")
    #print(instance.getAttribute("id"))
    #print(instance.getAttribute("class"))
    #print(instance.getAttribute("name"))

    idpara = instance.getAttribute("id")
    namepara = instance.getAttribute("name")

    if instance.getAttribute("class") == "Energy Controlling":
        ec = EnergyControlling()
        ec.setenergycontrolling(idpara, namepara, instance)
        # def setclassenergycontrolling(self, onto, id, name, type, description, systemtype, counter, task):
        #replace all blanks an hyphen
        nameNoBlank = ec.name.replace(" ","")
        nameNoBlankHyphen = nameNoBlank.replace("-","")
        print("++++++++++" + nameNoBlankHyphen)
        ontologyobject.setclassenergycontrolling(onto, ec.id, nameNoBlankHyphen, ec.type, ec.description, ec.systemType, ec.counter, ec.task)
        print("saved class Energy_Controlling to ontology")
        ec.getenergycontrolling()

    if instance.getAttribute("class") == "Energy Consuming Appliances":
        eca = EnergyConsumingAppliance()
        eca.setenergyconsuminappliance(idpara, namepara, instance)
        #def setclassenergyconsumingappliances(self, onto, id, name, type, description, Power_Consuming_Maximum, Power_Consuming_Average, Power_Consuming_Current, Consuming_Begin, Consuming_End, Active):
        #replace all blanks an hyphen
        nameNoBlank = eca.name.replace(" ","")
        nameNoBlankHyphen = nameNoBlank.replace("-","")
        print("++++++++++" + nameNoBlankHyphen)
        ontologyobject.setclassenergyconsumingappliances(onto, eca.id, nameNoBlankHyphen, eca.type, eca.description, eca.powerConsumingMaximum, eca.powerConsumingAverage, eca.powerConsumingCurrent, eca.consumingBegin, eca.consumingEnd, eca.active)
        print("saved class Energy_Consuming Appliances to ontology")           
        eca.getenergyconsumingappliance()

    if instance.getAttribute("class") == "Energy Source":
        es = EnergySource()
        #def setclassenergysource(self, onto, id, name, type, description, Power_Supplying_Maximum, Power_Supplying_Average, Power_Supplying_Current, Supplying_Begin, Supplying_End, Power_Production_Maximum, Power_Production_Average, Power_Production_Current, Production_Begin, Production_End):
        es.setenergysource(idpara, namepara, instance)
        #replace all blanks an hyphen
        nameNoBlank = es.name.replace(" ","")
        nameNoBlankHyphen = nameNoBlank.replace("-","")
        print("++++++++++" + nameNoBlankHyphen)
        ontologyobject.setclassenergysource(onto, es.id, nameNoBlankHyphen, es.type, es.description, es.powerSupplyingMaximum, es.powerSupplyingAverage, es.powerSupplyingCurrent, es.supplyingBegin, es.supplyingEnd, es.powerProductionMaximum, es.powerProductionAverage, es.powerProductionCurrent, es.productionBegin, es.productionEnd, es.active)
        print("saved class Energy_Source to ontology")
        es.getenergysource()


onto.save("Ontology_Beta.owl")
