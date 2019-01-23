class Prosumer:
    id = 0
    name = "null"
    description = "null"
    publicaddress = "null"
    privateaddress = "null"

    def setprosumerfromxml(self, id, name, instance):
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
                    if name == "Public Address":
                        self.publicaddress = children[i].firstChild.data
                    if name == "Private Address":
                        self.privateaddress = children[i].firstChild.data
                except AttributeError:
                    print("\n")
                    #print("indexError")
                i = i + 1

    def getprosumer(self):
        print("Die Ausgabe von der Prosumer Class")
        print(self.id)
        print(self.name)
        print(self.description)
        print(self.publicaddress)
        print(self.privateaddress)
