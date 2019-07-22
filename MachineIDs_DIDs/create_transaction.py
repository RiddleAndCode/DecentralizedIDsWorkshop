import time
import json

import base58
import sha3

from zenroom import zenroom
from zenroom.zenroom import ZenroomException 

from cryptoconditions import Ed25519Sha256

from bigchaindb_driver import BigchainDB
bdb_root_url = 'http://localhost:9984/'
bdb = BigchainDB(bdb_root_url)

# generate the keypairs/wallets for producer and the buyer
# the pacemaker will only e represented by its public key address
# derived from the attached RFID tag's EPC code

from bigchaindb_driver.crypto import generate_keypair, CryptoKeypair

# For each run a new keypair is generated
producer = generate_keypair()

print("\nProducer Private Key:" + producer.private_key)
print("Producer Public Key:" + producer.public_key)

## CREATE TRANSACTION

# create a digital asset for producer
asset = {
    'data': {
        'Id': 'did:data:NGI4NzExNWYxNTRkZGViNDgwM2JkNTU4MTdlZGI4MTAxZDk0NjBlNDczYWFiZGI0NDM5YzUzMGFkMDQxZTg1NWQxZDYxZDhmNGM3OGNhMzBmMDJjZjk5YWE3MTc5ZGZlZWYzNDVhZjNiODI3NDIwMWY4MGIyYjk5MWI2MjVhOGY=',
        "Producer": {
            "CompanyName": "Wunderbar Krems GmbH",
            "AddressLine": "Schmidstrasse 5",
            "ZipCode": "3500",
            "City": "Krems",
            "Country": "AT",
            "VAT_Id": "ATU36909999"
        },
        "Product": "S275J2H",
        "Quantity": "2400",
        "QuantityUnit": "g"
    }
}

metadata = {
    'Units': 2400,
    'Type': 'g'
}

# IPDB transaction schema version
version = '2.0'

# Policies written in Zencode - see https://github.com/DECODEproject/Zenroom
# To apply it it has to be given as a parameter in line 95.
script = """Scenario 'coconut': "To run over the mobile wallet the first time and store the output as keypair.keys"
Given that I am known as 'identifier'
When I create my new keypair
Then print all data
"""

# CRYPTO-CONDITIONS: instantiate an Ed25519 crypto-condition for buyer
ed25519 = Ed25519Sha256(public_key=base58.b58decode(producer.public_key))

# CRYPTO-CONDITIONS: generate the condition uri
condition_uri = ed25519.condition.serialize_uri()

# CRYPTO-CONDITIONS: construct an unsigned fulfillment dictionary
unsigned_fulfillment_dict = {
    'type': ed25519.TYPE_NAME,
    'public_key': base58.b58encode(ed25519.public_key).decode(),
}

output = {
    'amount': '2400',
    'condition': {
        'details': unsigned_fulfillment_dict,
        'uri': condition_uri,
    },
    'script': '',
    'keys': '',
    'data': '',
    'conf': '',
    'verbosity': '0',
    'public_keys': (producer.public_key,),
}

input_ = {
    'fulfillment': None,
    'fulfills': None,
    'owners_before': (producer.public_key,)
}

token_creation_tx = {
    'operation': 'CREATE',
    'asset': asset,
    'metadata': None,
    'outputs': (output,),
    'inputs': (input_,),
    'version': version,
    'id': None,
}

# JSON: serialize the transaction-without-id to a json formatted string
message = json.dumps(
    token_creation_tx,
    sort_keys=True,
    separators=(',', ':'),
    ensure_ascii=False,
)

message = sha3.sha3_256(message.encode())

# CRYPTO-CONDITIONS: sign the serialized transaction-without-id
ed25519.sign(message.digest(), base58.b58decode(producer.private_key))

# CRYPTO-CONDITIONS: generate the fulfillment uri
fulfillment_uri = ed25519.serialize_uri()

# add the fulfillment uri (signature)
token_creation_tx['inputs'][0]['fulfillment'] = fulfillment_uri

print("\nTransaction to be submitted")
print(json.dumps(token_creation_tx, indent=2))

# JSON: serialize the id-less transaction to a json formatted string
json_str_tx = json.dumps(
    token_creation_tx,
    sort_keys=True,
    separators=(',', ':'),
    ensure_ascii=False,
)

# SHA3: hash the serialized id-less transaction to generate the id
shared_creation_txid = sha3.sha3_256(json_str_tx.encode()).hexdigest()

# add the id
token_creation_tx['id'] = shared_creation_txid

# send CREATE tx into the bdb network
returned_creation_tx = bdb.transactions.send_async(token_creation_tx)

print("\nTransaction received")
print(json.dumps(returned_creation_tx, indent=2))
print("\nTransaction\n " + bdb_root_url + "api/v1/transactions/" + returned_creation_tx['id'])