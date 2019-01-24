pragma solidity ^0.4.25;
// pragma solidity ^0.5.0;
 
contract helloWorld {

    function getMessage() public view returns(string memory){
        return "Hello World!";
    }
}