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