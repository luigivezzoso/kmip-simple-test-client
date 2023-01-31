# Simple KMIP Client

This basic tool is created to test KMIP connection to [Thales CipherTrust Manager](https://cpl.thalesgroup.com/encryption/key-management-interoperability-protocol-kmip). Will be still as smallest and simple as possible like a kmip-ping tool.

The tool execute the following tasks:
- open a connection to KMIP Server
- generate a symetric AES256 Key (using random name)
- activate the new key
- revoke the new key
- detroy the key
- close the connection
- print the time required to complete all the steps


This tool is based on https://pykmip.readthedocs.io/en/latest/ which provide a complete toolset to interact with KMIP server.


