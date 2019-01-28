from owlready2 import *
from web3 import Web3, HTTPProvider
from smarthome.blockchain_handler import *
from smarthome.contracts import *


def normalize_32_byte_hex_address(value):
    as_bytes = eth_utils.to_bytes(hexstr=value)
    return eth_utils.to_normalized_address(as_bytes[-20:])


if __name__ == '__main__':

    ontology_path = "smarthome/Ontology_Beta.owl"
    onto = get_ontology(ontology_path)
    onto.load()

    # UC2
    # print("from energy source object obj.47635")
    # print(onto["obj.47635"].Power_Production_Current)

    # print("Get all ECA")
    # print(onto.search(type=onto.Energy_Consuming_Appliances))

    # -------------------------------------------------------------------------
    # print("Get current energy consumption of all ECAs")
    # ecas = onto.search(type=onto.Energy_Consuming_Appliances)
    # ppc = 0
    # for eca in ecas:
    #     ppc += int(eca.Power_Consuming_Current[0])
    # print(ppc)
    # -------------------------------------------------------------------------
    # UC3
    # print("Get avg energy consumption of all ECAs")
    # ecas = onto.search(type=onto.Energy_Consuming_Appliances)
    # ppc = 0
    # for eca in ecas:
    #     ppc += int(eca.Power_Consuming_Average[0])
    # print(ppc)
    # # -------------------------------------------------------------------------
    # UC1
    # print("Get current energy consumption from eca")
    # print(int(onto["obj.47631"].Power_Consuming_Current[0]))

    # print("Get current energy consumption from eca")
    # print(int(onto["obj.47631"].Power_Consuming_Maximum[0])) # wrong data type int needed!!

    # print("Get all prosumer")
    # prosumers = onto.search(type=onto.Prosumer)
    # print(prosumers[0])

    # print("Get all properties of an object")
    # print(list(onto["obj.48600"].get_properties()))

    # print(onto.search(iri="*48600")[0])  # this

    # prop = list(onto.search(iri="*48600")[0].get_properties())[0].iri
    # print(prop)

    # print("begin")
    # for prop in list(onto["obj.48600"].get_properties()):
    #     for value in prop[onto["obj.48600"]]:
    #         print(prop.name)
    #         print(value)

    # print("sdf")

    # print(list(onto.search(iri="*48600")[0].get_properties())[1])

    # for prop in onto.drug_1.get_properties():
    #     for value in prop[onto.drug_1]:
    #         print(".%s == %s" % (prop.python_name, value))

    # print(onto.search(type=onto.Energy_Consuming_Appliances))

    print("Get all ecas from a prosumer")
    # print(list(list(onto.search(iri="*48600")
    #                 [0].ProsumerOwnsControlling)[0].ControllingControllsConsumingAppliances))

    # print(list(list(onto[str("obj.48600")].ProsumerOwnsControlling)[
    #       0].ControllingControllsConsumingAppliances))

    # Connect to test net

    abi = '''[
        {
            "constant": true,
            "inputs": [],
            "name": "energymax",
            "outputs": [
                {
                    "name": "",
                    "type": "int256"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [
                {
                    "name": "energyamount",
                    "type": "int256"
                }
            ],
            "name": "getMessage",
            "outputs": [
                {
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        }
    ]'''

    w3 = Web3(HTTPProvider(
        'https://ropsten.infura.io/v3/d15fc63d1e504344be7954571d2d813d'))

    privatekey = "B99D08E11DD90D55DB8A4442479BAFB1E8B18EEEDBF6F7BE54500DFBBDBC9DFE"
    bh = BlockchainHandler(privatekey)

    tx_hash = '0x1A6C85cFAfB5627FD2E96F29a534c3432cC9Ee82'
    print(w3.isAddress(tx_hash))

    # tx_hash = w3.toChecksumAddress(tx_hash)
    contract = w3.eth.contract(
        address=tx_hash, abi=abi)

    eca = ""
    print(bh.run_eca_contract(tx_hash, abi, eca))
