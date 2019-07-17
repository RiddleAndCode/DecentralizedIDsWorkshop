# DID and TLS

## W3C Specs

* [W3C Decentralized Identifiers Spec](https://w3c-ccg.github.io/did-spec/)
* [W3C Verifiable Credentials Spec](https://www.w3.org/TR/verifiable-claims-data-model/)


## Introduction to DIDs

Taken from [https://github.com/WebOfTrustInfo/](https://github.com/WebOfTrustInfo/),

* [DID Primer](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/did-primer.md) — Decentralized Identifiers ([extended version](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/did-primer-extended.md) also available)
* [Functional Identity Primer](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/functional-identity-primer.md) — A different way to look at identity
* [Verifiable Credentials Primer](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/verifiable-credentials-primer.md) — the project formerly known as Verifiable Claims
* [Glossary of Terms](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/glossary-primer.md) — a brief dictionary of technical terms used at RWOT


## DID-TLS, DID-Auth

* [Sabadello (DanubeTech) web of trust 6 paper on did-auth](https://github.com/WebOfTrustInfo/rwot6-santabarbara/blob/master/final-documents/did-auth.pdf)
* hyperledger indy
    * [Converstations](https://jira.hyperledger.org/browse/IS-268?attachmentSortBy=fileName)
    * [Specifications](https://docs.google.com/document/d/1-aPY1eeHdR_TnF7_WpEs58RZ_jNdDeptVrNEu3groFc/edit#heading=h.4dabf3er5xg1)
    * it seems that we are not yet able to implement tls-did, see the indy discussion about it
        * the path they are moving forward with is [https://wiki.hyperledger.org/pages/viewpage.action?pageId=6426680](https://wiki.hyperledger.org/pages/viewpage.action?pageId=6426680)
* DID-JWT
    * The did-JWT library allows you to sign and verify JSON Web Tokens (JWT) using ES256K, ES256K-R and Ed25519 algorithms.
    * [https://github.com/uport-project/did-jwt](https://github.com/uport-project/did-jwt)
    * [https://github.com/decentralized-identity/did-auth-jose](https://github.com/decentralized-identity/did-auth-jose)
* [TLS in Rust](https://github.com/ctz/rustls)
* [Sidetree](https://github.com/decentralized-identity/sidetree)
    * A blockchain agnostic DID implementation
* [Universal DID Resolver based on drivers](https://github.com/decentralized-identity/universal-resolver/)

## Notable Orgs

* [DIF](https://identity.foundation/)
* [Sovrin](https://sovrin.org/)
* [DanubeTech](https://danubetech.com/)
* [uPort](https://www.uport.me/)
