# IPDB DID Method (WIP)

#####  Draft Community Group Report, 19 Jule 2019

##### Participate: Jürgen E., Markus S., Reza S., Daniel. G., Raphael, friends from Jolocom, RIAT Institute for Future Cryptoeconomics, RIDDLE & CODE GmbH...

## Abstract

The Interplanetary Database (IPDB, aka BigchainDB) Reference Decentralized Identifiers (DIDs) Method is a first attempt to fullfill the requirements specified in the DID specification currently published by the W3C Credentials Community Group (v0.13, 10 July 2019). For more information about DIDs and DID method specifications, please see the [DID Primer.](https://w3c-ccg.github.io/didm-btcr/)


## 1. Introduction (WIP)

Initially, we will use
https://ipdb-eu2.riddleandcode.com/
as a reference IPDB node. There is a transaction/block explorer at
http://r3c.network/ (be aware to configure the explorer to query the above mentioned IPDB node, domain = ipdb-eu2.riddleandcode.com, port = 443, secure = true).

<<<<<<< HEAD
The transaction ID of the transcation creating the asset is the asset id being used to transfer the asset.
That means that asset ID of a created DID document is defined by its transaction ID.

The following asset ID does for example exist
d6f0f042c639552c6217a14443aebe9ed1dce7096927fa63fc3a45de25b937df
and can be viewed at the following API
https://ipdb-eu2.riddleandcode.com/api/v1/transactions?asset_id=d6f0f042c639552c6217a14443aebe9ed1dce7096927fa63fc3a45de25b937df

Assets can be transfered and it is important to get the last transaction in order to identify the owner of the asset and the latest state. Therefore, it is important to use the last_tx=true switch to be able to direclty access the last transaction of the defined asset.
https://ipdb-eu2.riddleandcode.com/api/v1/transactions?asset_id=d6f0f042c639552c6217a14443aebe9ed1dce7096927fa63fc3a45de25b937df&last_tx=true


## Defintion of the standard DID operations (WIP)

### Asset/DID creation
IPDB transactions come in a well defined structure and contain immutable assets specifications and changeable metadata fields.
The creation of the asset is usually easily performed by utilizing a public/private key pair and creating a create transaction and sending this to the network (http://docs.bigchaindb.com/en/latest/transaction-concepts.html).

#### did:ipdb method specification
The used key pair being associated with this creation process is usually the initial owner of the DID/asset.
The asset should contain the following JSON defintion

asset :{ 'did':'ipdb' }

This qualifies the asset to be an IPDB DID together the corresponding transaction ID (TX ID).
The metadata has to contain the potentially changeable aspects as

metadata: { *services*, optional: *keys* }

### Read/Resolve DIDs on IPDB: the did:ipdb method

The DID:IPDB method has the following structure
did:ipdb:optional_namespace:did_identifier
did:ipdb:d6f0f042c639552c6217a14443aebe9ed1dce7096927fa63fc3a45de25b937df

The optional namespace is solely known by its users as IPDB is first and foremost used as federated network. Therefore, a huge number of IPDB networks can exists and all of them might utilize DIDs within it.
The method specific identifier represents the asset id of the DID asset on the IPDB network. The DID document can be resolved by requesting the content of asset. This is achieved by resolving this URL

https://ipdb-eu2.riddleandcode.com/api/v1/transactions?asset_id=d6f0f042c639552c6217a14443aebe9ed1dce7096927fa63fc3a45de25b937df&last_tx=true

The metadata of the transaction reveals the details of the DID as authentication keys (public ones), supported services, ...

### Updating DID documents

The owner of an asset can transfers the asset (DID document) to itself with the new metadata (DID document).
Old metadata can be changed or new data can be addded during that process. The ownership can be changed by transferring the DID document (the asset) to a another public key.

Important: All valid data points should be added to the last or most recent metadata so that this is always present to the user.


### Deactivation of DID documents

Transfer the asset to a well-known hardcoded burn address 00000000000000000000000000000000000000000000 (45 times 0) defined a deleted DID.



# TODOs
Further Steps
=======
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


## DID Method Specs

The following got drafted and will be pushed finished soon:

did:ipdb:<optional:namespace>:b5340f8955456ad918334c305232452a36da3bd199eab6211891160e8f2c0d69




Define the standard DID operations
* Create
  * generate key pair
  * create asset by sending a "create" transaction
    * asset: {}
    * metadata: { *services* , optional: *keys* }
* Read/Resolve 
  * the optional namespace should contain an identifier being listed at IPDB. 
  * the method specific identifier represents the asset id of the DID asset upon IPDB. It can be looked up by requesting the content of https://<namespace or default service>/api/v1/assets?search=<method specific identifier
    * DID Document: "id": "<method specific identifier"
    * DID Document: "services": <services from metadata object>
    * DID Document: "publicKeys": <publicKeys from metadata object> OR public key is taken from the IPDB transaction creator (this is the public key of the input (the signer))
* "Update"
  * the owner transfers the asset (DID document) to itself with the new metadata (DID document).
  * Public key can be changed by transferring the DID document (the asset) to a new public key. 
* "Deactivate"
  * Transfer the asset to a well-known hardcoded burn address 00000000000000000000000000000000000000000000 (45 times 0)


### Further Steps
>>>>>>> 317647a5f8a13cb63109048bfa322ef845ad26c8
Register DID Method Spec here:
https://w3c-ccg.github.io/did-method-registry/

Maybe write a driver for the Universal Resolver:
https://uniresolver.io/

Create a few example DIDs.


## 2. IPDB DID resolver (WIP)
The official IPDB DID resolver will be published soon.
