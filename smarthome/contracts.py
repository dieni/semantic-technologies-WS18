class SmartContract:
    id = 1

    def __init__(self, tx_hash, abi, device_id):
        self.tx_hash = tx_hash
        self.abi = abi
        self.device_id = device_id
        self.msg = ''

    def set_msg(self, msg):
        self.msg = msg

    def todict(self):
        x = {
            "device_id": str(self.device_id),
            "tx_hash": str(self.tx_hash),
            "msg": str(self.msg)
        }

        return x


class LogyourEnergy:

    def __init__(self, consumption):

        self.source = '''
        pragma solidity ^0.4.25;

        
                contract LogyourEnergy {
                    
                    int loggedConsumption =''' + str(consumption) + ''';

                    function getMessage() public view returns(int){
                        return loggedConsumption;
                    }
                }
            '''

    abi = '''
                [
        {
            "constant": true,
            "inputs": [],
            "name": "getMessage",
            "outputs": [
                {
                    "name": "",
                    "type": "int256"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        }
    ]
    '''


class TradingPlatform:

    def __init__(self):

        self.source = '''
        pragma solidity ^0.4.25;

        contract Trade {
            string sell = " Watt Strom wird zum Verkauf auf Trading Platform angeboten.";
            string buy = " Watt Strom wird auf Trading Platform gekauft.";
            string breakeven = " Watt Strom. Verbrauch entspricht Eigenproduktion.";

            function getMessage(int householddelta) public view returns(int, string){
                if (householddelta>0) {
                return (householddelta,sell);
                }else if (householddelta==0){
                return (householddelta,breakeven);
                }else if(householddelta<0){
                return (householddelta*-1,buy);
                }
            }
        }
        '''

    abi = '''
            [
        {
            "constant": true,
            "inputs": [
                {
                    "name": "householddelta",
                    "type": "int256"
                }
            ],
            "name": "getMessage",
            "outputs": [
                {
                    "name": "",
                    "type": "int256"
                },
                {
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        }
    ]
    '''


class ECAContract:

    def __init__(self, id, name, maxconsumption):
        self.id = id
        self.name = name
        self.maxconsumption = maxconsumption

        self.source2 = '''
        pragma solidity ^0.4.25;

        
        contract Frigerator {
            int public energymax=89;
            

            function getMessage(int energyamount) public view returns(string){
                if (energyamount>energymax) {
                return "Garantiefall wird abgewickelt";
                }else { 
                return "Stromverbrauch entspricht Energieklasse"; 
                }
            }
        }
        '''

        self.source = '''
        pragma solidity ^0.4.25;

 
        contract Frigerator {
            int public energymax=''' + str(maxconsumption) + ''';
            

            function getMessage(int energyamount) public view returns(string){
                if (energyamount>energymax) {
                return "Garantiefall wird abgewickelt";
                }else { 
                return "Stromverbrauch entspricht Energieklasse"; 
                }
            }
        }'''

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


class HelloWorld:

    def get_source(self):
        source = '''
            pragma solidity ^0.4.25;
    
            contract helloWorld {

                function getMessage() public view returns(string memory){
                    return "Hello World!";
                }
            }
        '''

        return source

    def get_abi(self):
        abi = '''
            [
                {
                    "constant": true,
                    "inputs": [],
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
            ]
        '''

        return abi
