import xml.dom.minidom as dom
import classes as adox


baum = dom.parse("smarthome.xml")

instances = baum.getElementsByTagName("instance")
connectors = baum.getElementsByTagName("connector")

model = baum.getElementsByTagName("model")
modelinstance = adox.SmartHome()
modelinstance.setsmarthome(model)
modelinstance.getsmarthome()

for instance in instances:
    print("\n")
    #print(instance.getAttribute("id"))
    #print(instance.getAttribute("class"))
    #print(instance.getAttribute("name"))

    idpara = instance.getAttribute("id")
    namepara = instance.getAttribute("name")

    if instance.getAttribute("class") == "Energy Controlling":
        ec = adox.EnergyControlling()
        ec.setenergycontrolling(idpara, namepara, instance)
        ec.getenergycontrolling()

    if instance.getAttribute("class") == "Energy Consuming Appliances":
        eca = adox.EnergyConsumingAppliance()
        eca.setenergyconsuminappliance(idpara, namepara, instance)
        eca.getenergyconsumingappliance()

    if instance.getAttribute("class") == "Energy Source":
        eca = adox.EnergySource()
        eca.setenergysource(idpara, namepara, instance)
        eca.getenergyyource()
