class SmartHome:
    id = 0

    def setsmarthome(self, model):
        self.id = model[0].getAttribute("id")


    def getsmarthome(self):
        print("Die Ausgabe von der Smart Home Class")
        print(self.id)