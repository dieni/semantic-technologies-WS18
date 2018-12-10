class Ontology:

    def setclassenergycontrolling(self, onto, id, name, type, description, systemtype, counter, task):
        onto.Energy_Controlling(name, Name = [id], Type = [type], Description = [description], System_Type = [systemtype], Counter = [counter], Task = [task])

    def setclassenergysource(self, onto, id, name, type, description, Power_Supplying_Maximum, Power_Supplying_Average, Power_Supplying_Current, Supplying_Begin, Supplying_End, Power_Production_Maximum, Power_Production_Average, Power_Production_Current, Production_Begin, Production_End, Active):
        onto.Energy_Source(name, Name = [id], Type = [type], Description = [description], Power_Supplying_Maximum = [Power_Supplying_Maximum], Power_Supplying_Average = [Power_Supplying_Average], Power_Supplying_Current = [Power_Supplying_Current], Supplying_Begin = [Supplying_Begin], Supplying_End = [Supplying_End], Power_Production_Maximum = [Power_Production_Maximum], Power_Production_Average = [Power_Production_Average], Power_Production_Current = [Power_Production_Current], Production_Begin = [Production_Begin], Production_End = [Production_End], Active = [Active])
        
    def setclassenergyconsumingappliances(self, onto, id, name, type, description, Power_Consuming_Maximum, Power_Consuming_Average, Power_Consuming_Current, Consuming_Begin, Consuming_End, Active):
        onto.Energy_Consuming_Appliances(name, Name = [id], Type = [type], Description = [description], Power_Consuming_Maximum = [Power_Consuming_Maximum], Power_Consuming_Average = [Power_Consuming_Average], Power_Consuming_Current = [Power_Consuming_Current], Consuming_Begin = [Consuming_Begin], Consuming_End = [Consuming_End], Active = [Active])

    def setclassprosumer(self, onto, id, name, Description, Private_Address, Public_Address):
        onto.Prosumer(id, Name = [name], Description = [Description], Private_Address = [Private_Address], Public_Address = [Public_Address])

