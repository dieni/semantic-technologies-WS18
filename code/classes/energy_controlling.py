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
