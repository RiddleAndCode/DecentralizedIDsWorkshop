# IPDB DID Method (WIP)

#####  Draft Community Group Report, 19 Jule 2019

##### Participate: Jürgen E., Markus S., Reza S., Daniel. G., Raphael, friends from Jolocom, RIAT Institute for Future Cryptoeconomics, RIDDLE & CODE GmbH...

## Abstract

The Interplanetary Database (IPDB, aka BigchainDB) Reference Decentralized Identifiers (DIDs) Method is a first attempt to fullfill the requirements specified in the DID specification currently published by the W3C Credentials Community Group (v0.13, 10 July 2019). For more information about DIDs and DID method specifications, please see the [DID Primer.](https://w3c-ccg.github.io/didm-btcr/)


## 1. Introduction (WIP)

Initially, we will use

https://ipdb2.riddleandcode.com/

as a reference.

there is a transaction explorer
http://explorer.riddleandcode.com:9001/ (be aware to configure the explorer to query the above mentioned IPDB node).

Transactions do have an identifier as

bc1dcd0fb64d4df9b5168461306ecaf11d82a91e5c347faf6f54f556d7c7200c
and can be viewed at 	
the following API
https://ipdb2.riddleandcode.com/api/v1/transactions/

by e.g. calling  https://ipdb2.riddleandcode.com/api/v1/transactions/bc1dcd0fb64d4df9b5168461306ecaf11d82a91e5c347faf6f54f556d7c7200c
DID Method Spec
We need to discuss and specify the following:

What is the DID Method name? e.g. did:ipdb:xxxxx or did:bigch:xxxxx, etc?
Do we want/need to support "sub-namespaces", e.g. did:ipdb:main:xxxxx or did:ipdb:test:xxxxx or did:ipdb:mynet:xxxxx or ...
What is the format of the method-specific identifier (the xxxxx above)?
It must be unique
It must be persistent (not change)
It must somehow point to the DID Document
Could be a BigchainDB transaction ID? Or an asset ID?

did:ipdb:<optional:namespace>:b5340f8955456ad918334c305232452a36da3bd199eab6211891160e8f2c0d69

Define the standard DID operations
Create
generate key pair
create asset by sending a "create" transaction
asset: {}
metadata: { *services* , optional: *keys* }
Read/Resolve: the optional namespace should contain an identifier being listed at IPDB. 
the method specific identifier represents the asset id of the DID asset upon IPDB. It can be looked up by requesting the content of https://<namespace or default service>/api/v1/assets?search=<method specific identifier
DID Document: "id": "<method specific identifier"
DID Document: "services": <services from metadata object>
DID Document: "publicKeys": <publicKeys from metadata object> OR public key is taken from the IPDB transaction creator (this is the public key of the input (the signer))
Update
The owner transfers the asset (DID document) to itself with the new metadata (DID document).
Public key can be changed by transferring the DID document (the asset) to a new public key. 
Deactivate
Transfer the asset to a well-known hardcoded burn address 00000000000000000000000000000000000000000000 (45 times 0)
Further Steps
Register DID Method Spec here:
https://w3c-ccg.github.io/did-method-registry/
Maybe write a driver for the Universal Resolver:
https://uniresolver.io/

Create a few example DIDs.






Trusted Sharing

https://github.com/rafaelppires/trusted-sharing

https://github.com/rafaelppires/trusted-sharing/tree/master/sgx_grpshr

everything by 

https://gitlab.securecloud.works/rafael.pires


Initial question that lead to research for IBBE-SGX
http://conferences.inf.ed.ac.uk/EuroDW2018/papers/eurodw18-Contiu.pdf

IBBE-SGX research paper
https://arxiv.org/pdf/1805.01563.pdf

Intel SGX briefing
https://software.intel.com/sites/default/files/managed/c3/8b/intel-sgx-product-brief-2019.pdf

Prototype on Azure?
https://azure.microsoft.com/en-us/blog/protect-data-in-use-with-the-public-preview-of-azure-confidential-computing/


## 2. IPDB DID resolver (WIP)
