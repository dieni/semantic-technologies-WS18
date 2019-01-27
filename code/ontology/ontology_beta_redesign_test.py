# Short example: What can I do with Owlready?

# Load an ontology from a local repository, or from Internet:
from owlready2 import *

onto = get_ontology("file://C:/Users/Ifangelium/workspace-pycharm/semanticTechnologiesWS18.git/code/ontology/Ontology_Beta.owl")
onto.load()
print(list(onto.classes()))
# print(onto.search(iri="Energy*"))

print 


#Energy Source
#myenergysource = onto.Photovoltaic_System("Photovoltaic", Name = [], Type = [], Description = [], Power_Supplying_Maximum = [], Power_Supplying_Average = [], Power_Supplying_Current = [], Supplying_Begin = [], Supplying_End = [], Power_Production_Maximum = [], Power_Production_Average = [], Power_Production_Current = [], Production_Begin = [], Production_End = [])
#print(myenergysource)

#Energy Consuming Appliances
#myenergyconsuming = onto.Energy_Consuming_Appliances("EnergyApp01", Name = [], Type = [], Description = [], Power_Consuming_Maximum = [], Power_Consuming_Average = [], Power_Consuming_Current = [], Consuming_Begin = [], Consuming_End = [], Active = [])
#print(myenergyconsuming)
   
#Energy Controlling
#x = "Smartmeter"
#myenergycontrolling = onto.Energy_Controlling(x, Name = [x], Type = [], Description = [], System_Type = [], Counter = [], Task = [])
#print(myenergycontrolling)

#Energy Storage Appliances
#myenergystorage = onto.Battery("mybattery", Name = [], Type = [], Description = [], Power_Storage_Maximum = [], Power_Storage_Current = [], Storage_Begin = [], Storage_End = [], Active = [])

# Access the classes of the ontology, and create new instances with Data Properties and with relation:
#myprosumer = onto.Prosumer("Prosumer1", Name = ["Heinz"], Description = ["daurschwule"], Private_Address = ["bei1dein1vater"], Public_Address = ["mit0couse2ng"])
#myprosumer.ProsumerTradesThroughTransaction = [onto.Blockchain_Transaction("trans01", Name = ["trans01"], Description = ["Cryptotrade"], Transaction_Fee = [17], Type = ["Fast"] )]
#print(myprosumer)

#get all properties from one instance
#for prop in onto.47601.get_properties():
 #   for value in prop[onto.47601]:
  #    print(".%s == %s" % (prop.label, value))
      

#get specific data property of instance (At first you have to add an annotation to your data property; I used the label tag)
#print(myprosumer.Name)
#print(myprosumer.Private_Address)
#print(onto.trans01.Transaction_Fee)

print(list(onto.individuals()))

print(onto.EnergyConsumingAppliances47619.Name)


# Export to OWL file:
#onto.save()

#iterate through instances of example class
#for i in myprosumer.instances(): print(i)

# Get all Properties 

#print(list(onto.classes()))
#print(list(onto.individuals()))
#print(list(onto.data_properties()))
#print(list(onto.annotation_properties()))
#print(myenergystorage)

#print(onto.search(iri = "*battery"))
#print(onto.search(iri = "*Prosumer"))
#print(onto.search(iri = "*Name"))

#print(onto.Prosumer1.get_properties())




