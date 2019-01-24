import os
import xml.dom.minidom as dom
from smarthome.models import SmartHome, Prosumer, EnergySource, EnergyControlling, EnergyConsumingAppliance


class AdoxxImporter:

    def import_prosumer(self, xml):
        list = []
        baum = dom.parseString(xml)
        # get all instances
        instances = baum.getElementsByTagName("instance")
        for instance in instances:

            idpara = instance.getAttribute("id")
            namepara = instance.getAttribute("name")

            if instance.getAttribute("class") == "Prosumer":
                p = Prosumer()
                p.id = idpara
                p.name = namepara
                children = instance.getElementsByTagName("attribute")
                i = 0
                while i < children.length:
                    try:
                        name = children[i].getAttribute("name")
                        # print(children[i].firstChild.data)
                        if name == "Description":
                            p.description = children[i].firstChild.data
                        if name == "Public Address":
                            p.publicaddress = children[i].firstChild.data
                        if name == "Private Address":
                            p.privateaddress = children[i].firstChild.data
                    except AttributeError:
                        print("\n")
                        # print("indexError")
                    i = i + 1
                list.append(p)

        return list

    def import_energy_consumption_appliances(self, xml):
        list = []
        baum = dom.parseString(xml)
        # get all instances
        instances = baum.getElementsByTagName("instance")
        for instance in instances:

            idpara = instance.getAttribute("id")
            namepara = instance.getAttribute("name")

            if instance.getAttribute("class") == "Energy Consuming Appliances":
                eca = EnergyConsumingAppliance()
                eca.id = idpara
                eca.name = namepara
                children = instance.getElementsByTagName("attribute")
                i = 0
                while i < children.length:
                    try:
                        name = children[i].getAttribute("name")
                        # print(children[i].firstChild.data)
                        if name == "Description":
                            eca.description = children[i].firstChild.data
                        if name == "Power Consuming Maximum":
                            eca.powerConsumingMaximum = children[i].firstChild.data
                        if name == "Power Consuming Average":
                            eca.powerConsumingAverage = children[i].firstChild.data
                        if name == "Power Consuming Current":
                            eca.powerConsumingCurrent = children[i].firstChild.data
                        if name == "Consuming Begin":
                            eca.consumingBegin = children[i].firstChild.data
                        if name == "Consuming End":
                            eca.consumingEnd = children[i].firstChild.data
                        if name == "Active":
                            eca.active = children[i].firstChild.data
                        if name == "Type":
                            eca.type = children[i].firstChild.data
                    except AttributeError:
                        print("\n")
                        # print("indexError")
                    i = i + 1
                list.append(eca)
        return list

    def import_energy_controlling(self, xml):

        list = []
        baum = dom.parseString(xml)
        # get all instances
        instances = baum.getElementsByTagName("instance")

        for instance in instances:

            idpara = instance.getAttribute("id")
            namepara = instance.getAttribute("name")

            if instance.getAttribute("class") == "Energy Controlling":
                ec = EnergyControlling()
                ec.id = idpara
                ec.name = namepara
                children = instance.getElementsByTagName("attribute")
                i = 0
                while i < children.length:
                    try:
                        name = children[i].getAttribute("name")
                        # print(children[i].firstChild.data)
                        if name == "Description":
                            ec.description = children[i].firstChild.data
                        if name == "System Type":
                            ec.systemType = children[i].firstChild.data
                        if name == "Counter":
                            ec.counter = children[i].firstChild.data
                        if name == "Task":
                            ec.task = children[i].firstChild.data
                        if name == "Type":
                            ec.type = children[i].firstChild.data
                    except AttributeError:
                        print("\n")
                        # print("indexError")
                    i = i + 1
                list.append(ec)
        return list

    def import_energy_source(self, xml):

        list = []
        baum = dom.parseString(xml)
        # get all instances
        instances = baum.getElementsByTagName("instance")

        for instance in instances:
            idpara = instance.getAttribute("id")
            namepara = instance.getAttribute("name")
            if instance.getAttribute("class") == "Energy Source":
                es = EnergySource()
                es.id = idpara
                es.name = namepara
                children = instance.getElementsByTagName("attribute")
                i = 0
                while i < children.length:
                    try:
                        name = children[i].getAttribute("name")
                        # print(children[i].firstChild.data)
                        if name == "Power Supplying Maximum":
                            es.powerSupplyingMaximum = children[i].firstChild.data
                        if name == "Power Supplying Average":
                            es.powerSupplyingAverage = children[i].firstChild.data
                        if name == "Power Supplying Current":
                            es.powerSupplyingCurrent = children[i].firstChild.data
                        if name == "Supplying Begin":
                            es.supplyingBegin = children[i].firstChild.data
                        if name == "Supplying End":
                            es.supplyingEnd = children[i].firstChild.data
                        if name == "Description":
                            es.description = children[i].firstChild.data
                        if name == "Power Production Maximum":
                            es.powerProductionMaximum = children[i].firstChild.data
                        if name == "Power Production Average":
                            es.powerProductionAverage = children[i].firstChild.data
                        if name == "Power Production Current":
                            es.powerProductionCurrent = children[i].firstChild.data
                        if name == "Production Begin":
                            es.productionBegin = children[i].firstChild.data
                        if name == "Production End":
                            es.productionEnd = children[i].firstChild.data
                        if name == "Active":
                            es.active = children[i].firstChild.data
                        if name == "Type":
                            es.type = children[i].firstChild.data
                    except AttributeError:
                        print("\n")
                        # print("indexError")
                    i = i + 1
                list.append(es)
        return list
