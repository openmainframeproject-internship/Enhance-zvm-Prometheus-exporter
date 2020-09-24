# Mock Server
The mock server allows user to mock zvmsdk server. It is used for automated testing. User could access the mock server via REST APIs or ZVMConnector. 

## Responses
All responses are copied from [Feilong's official repository](https://github.com/openmainframeproject/python-zvm-sdk/tree/master/zvmsdk/tests/fvt/api_templates). It will return specific responses for different requests. It supports:
* GET /token
* GET /
* GET /host
* GET /guests
* GET /vswitches

## Dependency
The mock server is based on [Flask](https://github.com/pallets/flask). 