class SmartHome:
    id = 0

    def setsmarthome(self, model):
        self.id = model[0].getAttribute("id")


    def getsmarthome(self):
        print("Die Ausgabe von der Smart Home Class")
        print(self.id)


class EnergyControlling:
    id = 0
    name = "null"
    description = "null"
    systemType = "null"
    counter = 0
    task = "null"
    type = "null"

    def setenergycontrolling(self, id, name, instance):
            self.id = id
            self.name = name
            children = instance.getElementsByTagName("attribute")
            #print(children.length)
            print("\n")
            i = 0
            while i < children.length:
                #print(i)
                try:
                    name = children[i].getAttribute("name")
                   #print(children[i].firstChild.data)
                    if name == "Description":
                        self.description = children[i].firstChild.data
                    if name == "System Type":
                        self.systemType = children[i].firstChild.data
                    if name == "Counter":
                        self.counter = children[i].firstChild.data
                    if name == "Task":
                        self.task = children[i].firstChild.data
                    if name == "Type":
                        self.type = children[i].firstChild.data
                except AttributeError:
                    print("\n")
                    #print("indexError")
                i = i + 1

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

    def setenergyconsuminappliance(self, id, name, instance):
            self.id = id
            self.name = name
            children = instance.getElementsByTagName("attribute")
            #print(children.length)
            print("\n")
            i = 0
            while i < children.length:
                #print(i)
                try:
                    name = children[i].getAttribute("name")
                    #print(children[i].firstChild.data)
                    if name == "Description":
                        self.description = children[i].firstChild.data
                    if name == "Power Consuming Maximum":
                        self.powerConsumingMaximum = children[i].firstChild.data
                    if name == "Power Consuming Average":
                        self.powerConsumingAverage = children[i].firstChild.data
                    if name == "Power Consuming Current":
                        self.powerConsumingCurrent = children[i].firstChild.data
                    if name == "Consuming Begin":
                        self.consumingBegin = children[i].firstChild.data
                    if name == "Consuming End":
                        self.consumingEnd = children[i].firstChild.data
                    if name == "Active":
                        self.active = children[i].firstChild.data
                    if name == "Type":
                        self.type = children[i].firstChild.data
                except AttributeError:
                    print("\n")
                    #print("indexError")
                i = i + 1

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

    def setenergysource(self, id, name, instance):
            self.id = id
            self.name = name
            children = instance.getElementsByTagName("attribute")
            #print(children.length)
            print("\n")
            i = 0
            while i < children.length:
                #print(i)
                try:
                    name = children[i].getAttribute("name")
                    #print(children[i].firstChild.data)
                    if name == "Power Supplying Maximum":
                        self.powerSupplyingMaximum = children[i].firstChild.data
                    if name == "Power Supplying Average":
                        self.powerSupplyingAverage = children[i].firstChild.data
                    if name == "Power Supplying Current":
                        self.powerSupplyingCurrent = children[i].firstChild.data
                    if name == "Supplying Begin":
                        self.supplyingBegin = children[i].firstChild.data
                    if name == "Supplying End":
                        self.supplyingEnd = children[i].firstChild.data
                    if name == "Description":
                        self.description = children[i].firstChild.data
                    if name == "Power Production Maximum":
                        self.powerProductionMaximum = children[i].firstChild.data
                    if name == "Power Production Average":
                        self.powerProductionAverage = children[i].firstChild.data
                    if name == "Power Production Current":
                        self.powerProductionCurrent = children[i].firstChild.data
                    if name == "Production Begin":
                        self.productionBegin = children[i].firstChild.data
                    if name == "Production End":
                        self.productionEnd = children[i].firstChild.data
                    if name == "Active":
                        self.active = children[i].firstChild.data
                    if name == "Type":
                        self.type = children[i].firstChild.data
                except AttributeError:
                    print("\n")
                    #print("indexError")
                i = i + 1

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
