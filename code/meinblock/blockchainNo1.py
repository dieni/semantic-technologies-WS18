from web3 import Web3
from solc import compile_files, compile_source
import os


contract_source_code = '''
pragma solidity ^0.4.25;
// pragma solidity ^0.5.0;

contract helloWorld {

    function getMessage() public view returns(string memory){
        return "Hello World!";
    }
}
'''

if __name__ == '__main__':

    # Connect to test net
    # w3 = Web3()
    cwd = os.getcwd()
    print(cwd)

    # compile all contract files
    contracts = compile_files(['test.sol'])
    # contracts = compile_source(contract_source_code)

    # separate main file and link file
    # main_contract = contracts.pop("test.sol:helloWorld")

    # print(str(main_contract))
