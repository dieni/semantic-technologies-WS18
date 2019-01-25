class ECAContract:

    def __init__(self, id, name, maxconsumption):
        self.id = id
        self.name = name
        self.maxconsumption = maxconsumption

    def get_source(self):

        source = '''


        '''

        return source


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
