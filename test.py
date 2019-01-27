from owlready2 import *

if __name__ == '__main__':

    ontology_path = "smarthome/Ontology_Beta.owl"
    onto = get_ontology(ontology_path)
    onto.load()

    # UC2
    print("from energy source object obj.47635")
    print(onto["obj.47635"].Power_Production_Current)

    # print("Get all ECA")
    # print(onto.search(type=onto.Energy_Consuming_Appliances))

    # -------------------------------------------------------------------------
    print("Get current energy consumption of all ECAs")
    ecas = onto.search(type=onto.Energy_Consuming_Appliances)
    ppc = 0
    for eca in ecas:
        ppc += int(eca.Power_Consuming_Current[0])
    print(ppc)
    # -------------------------------------------------------------------------
    # UC3
    print("Get avg energy consumption of all ECAs")
    ecas = onto.search(type=onto.Energy_Consuming_Appliances)
    ppc = 0
    for eca in ecas:
        ppc += int(eca.Power_Consuming_Average[0])
    print(ppc)
    # -------------------------------------------------------------------------
    # UC1
    print("Get current energy consumption from eca")
    print(int(onto["obj.47631"].Power_Consuming_Current[0]))

    print("Get current energy consumption from eca")
    # print(int(onto["obj.47631"].Power_Consuming_Maximum[0])) # wrong data type int needed!!

    print("Get all prosumer")
    prosumers = onto.search(type=onto.Prosumer)
    print(prosumers[0])

    print("Get all properties of an object")
    print(list(onto["obj.48600"].get_properties()))

    for prop in list(onto["obj.48600"].get_properties()):
        print(prop.Name)
