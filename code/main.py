from platform.platform_class import Platform

if __name__ == "__main__":
    # execute only if run as a script

    # create an instance of the platform
    p = Platform()

    # import the xml from adoxx into the ontology
    p.importXML()