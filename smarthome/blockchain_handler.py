from web3 import Web3, HTTPProvider
from solc import compile_files, compile_source
from smarthome.contracts import ECAContract, HelloWorld, SmartContract, LogyourEnergy, TradingPlatform


class BlockchainHandler:

    def __init__(self, privatekey):

        # Connect to test net
        self.w3 = Web3(HTTPProvider(
            'https://ropsten.infura.io/v3/d15fc63d1e504344be7954571d2d813d'))

        self.acct = self.w3.eth.account.privateKeyToAccount(privatekey)

    def deploy_contract(self, contract_interface):
        '''
            Deploy the contract on the blockchain.

            Returns: Transaction hash, abi
        '''

        # Instantiate and deploy contract
        contract = self.w3.eth.contract(
            abi=contract_interface['abi'],
            bytecode=contract_interface['bin']
        )

        construct_txn = contract.constructor().buildTransaction({
            'from': self.acct.address,
            'nonce': self.w3.eth.getTransactionCount(self.acct.address),
            'gas': 1728712,
            'gasPrice': self.w3.toWei('21', 'gwei')})

        signed = self.acct.signTransaction(construct_txn)

        tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)

        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return str(tx_receipt['contractAddress']), contract_interface['abi']

    def deploy_contract_ECA(self, eca):
        '''
            Deploy a energy consuming appliance contract
            Define variables in the solidity contract and deploy it on the blockchain.

            Returns: Transaction hash, abi
        '''
        # contract = ECAContract(
        #     eca.id, eca.name, eca.powerConsumingMaximum)
        contract = ECAContract(
            eca.name, eca.Name, eca.Power_Consuming_Maximum[0])

        contracts = compile_source(contract.source)

        main_contract = contracts.pop('<stdin>:Frigerator')

        return self.deploy_contract(main_contract)

    def deploy_contract_Logger(self, consumption):
        contract = LogyourEnergy(consumption)

        contracts = compile_source(contract.source)

        main_contract = contracts.pop('<stdin>:LogyourEnergy')

        return self.deploy_contract(main_contract)

    def deploy_contract_trade(self):
        contract = TradingPlatform()

        contracts = compile_source(contract.source)

        main_contract = contracts.pop('<stdin>:Trade')

        return self.deploy_contract(main_contract)

    def deploy_contract_helloWorld(self):
        '''
            Deploy a hello world contract

            Returns: Transaction hash, abi
        '''

        # get contract source .sol
        hello = HelloWorld()
        source = hello.get_source()

        # compile contract
        contracts = compile_source(source)
        main_contract = contracts.pop('<stdin>:helloWorld')

        return self.deploy_contract(main_contract)

    def run_eca_contract(self, tx_hash, abi, eca):
        '''

        '''
        contract = self.w3.eth.contract(
            address=tx_hash, abi=abi)

        return contract.functions.getMessage(int(eca.Power_Consuming_Current[0])).call()

    def run_log_contract(self, tx_hash, abi):
        contract = self.w3.eth.contract(
            address=tx_hash, abi=abi)

        return contract.functions.getMessage().call()

    def run_trade_contract(self, tx_hash, abi, delta):
        contract = self.w3.eth.contract(
            address=tx_hash, abi=abi)

        return contract.functions.getMessage(int(delta)).call()
