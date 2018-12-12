from platform.platform_class import Platform
from ontology.onto_api import OntologyAPI

if __name__ == "__main__":
    # execute only if run as a script

    # create an instance of the platform
    p = Platform()

    # import the xml from adoxx into the ontology
    p.importXML()

    onto = OntologyAPI()

    for i in onto.getAllIndividuals():
        print(i)


