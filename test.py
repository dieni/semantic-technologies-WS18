from web3 import Web3, HTTPProvider
from solc import compile_files, compile_source


wallet_private_key = 'B99D08E11DD90D55DB8A4442479BAFB1E8B18EEEDBF6F7BE54500DFBBDBC9DFE'
# wallet_address = '0xBed036b94d57c46F3c4F16cD5a10D6668d7FDc3a'


# Connect to test net
w3 = Web3(HTTPProvider(
    'https://ropsten.infura.io/v3/d15fc63d1e504344be7954571d2d813d'))

acct = w3.eth.account.privateKeyToAccount(wallet_private_key)


def deploy_contract(contract_interface):
    # Instantiate and deploy contract
    contract = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )

    construct_txn = contract.constructor().buildTransaction({
        'from': acct.address,
        'nonce': w3.eth.getTransactionCount(acct.address),
        'gas': 1728712,
        'gasPrice': w3.toWei('21', 'gwei')})

    signed = acct.signTransaction(construct_txn)

    tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    return tx_hash, contract_interface['abi']


if __name__ == '__main__':

    # compile all contract files
    contracts = compile_files(["test.sol"])

    # separate main file and link file
    main_contract = contracts.pop("test.sol:helloWorld")

    print(main_contract['abi'])

    transaction_address, api = deploy_contract(main_contract)

    print("Transaction ID")
    print(transaction_address.hex())

    print('ABI')
    print(api)
