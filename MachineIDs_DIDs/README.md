# Machine Identities & DIDs

The goal of the workshop was to connect most recently developed IPDB primitives and connect them via DIDs.

The used primitives are listed below:
* IPDB
* Zenroom & Zencode
* RIDDLE&CODE SecureElement
* Raspberry PIs for rapid prototyping
* IPDB based DID methods 
* newly created IPDB tansactions schemes

## IPDB Dev System for Linux and MacOS

1. Install Bigchain according https://docs.bigchaindb.com/projects/contributing/en/latest/dev-setup-coding-and-contribution-process/run-node-with-docker-compose.html

2. Substitute the content of the existing ```transaction_v2.0.yaml``` with the content of new schema [transaction_v2.0.yaml](./transaction_v2.0.yaml). This works (do not ask why, it just works):
    ``` 
    docker exec -it <container_id> /bin/bash
    cd bigchaindb/common/schema
    rm transaction_v2.0.yaml
    vi transaction_v2.0.yaml 
    ```
    * Press ``i`` for insert mode
    * Paste with ```⌘V``` (on MacOS)
    * Press ESC - ```wq!``` - Enter
    * Restart all docker containers with ```make restart```

3. Install lua 
* On Linux with whatever package manager.
* On MacOS preferably with brew
```brew install lua````

4. Install zenroom
* On Linux install via ```pip3 install zenroom```
* On MacOS compile yourself:
    ````
    git clone https://github.com/DECODEproject/Zenroom.git
    cd Zenroom
    make embed-lua
    make osx-python3
    ````
    Copy ```zenroom.so``` to your Python application directory

    Remark: as of July 22nd the Python bindings are broken, @nestorsilk promised to fix it.

5. Test your Dev System

    Run the script [create_transaction.py](./create_transaction.py) with ```python3 create_transaction.py```. If it does not throw an error you are ready to go. 

## Interation with Secure Element on Raspberry Pi

(Coming soon...)


