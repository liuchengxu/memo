# Polkadot

## Issue

- [#131: Light-client friendly storage tracking](https://github.com/paritytech/polkadot/issues/131)

- [#136: Runtime: "DAO"/community funding manager](https://github.com/paritytech/polkadot/issues/136)

- [#140: Sandboxing and the simplest smart-contract runtime](https://github.com/paritytech/polkadot/pull/140)

- [#142 Preparing light client structure](https://github.com/paritytech/polkadot/pull/142)

- [#149 node-key CLI option](https://github.com/paritytech/polkadot/pull/149)

- [#150 light client](https://github.com/paritytech/polkadot/pull/150#discussion_r189261080)

- [#113 Miminal parachain framework](https://github.com/paritytech/polkadot/pull/113)

## Repo

- https://github.com/w3f/polkadot-overview

- https://github.com/polkadot-js

## Articles

- https://polkadot.network/Polkadot-lightpaper.pdf

- https://medium.com/@polkadotnetwork/now-live-polkadot-proof-of-concept-1-3e718512a8d

### Slides

- [Parity Substrate](http://slides.com/paritytech/paritysubstrate#/)


5CXLKZQuZcr1j68hBoFkbNEQSPuL5bt82qpGcwmksNm2kdeS

5HpwNVVXyGTFDjgcRcnqugJaNWTornAbfE9utbQmWWCXRVe2


- 0xd328428cb8913d6a448bca27a626cc1d937c04a618030a7d35dd77f10fcc9858
- 5DDjW9wWFaYsw8VPcjoXyq8whG5XWhVRkLpwesxF6BGB2RAa

## wiki

### Governance

- https://github.com/paritytech/polkadot/wiki/Governance
- https://www.youtube.com/watch?v=VsZuDJMmVPY&feature=youtu.be&t=24734

- an amorphous state-transition function stored on-chain
- a platform-neutral intermediate language(i.e. WebAssembly)
- serveral on-chain voting mechanisims
    - referenda with adaptive super-majority thresholds
    - batch approval voting

> A key and unfailing rule is:
>
> All changes to the protocol must be agreed upon by stake-weighted referendum; >50% of stake will always command the network

- Council
    选举
    - represent passive stakeholders

- Rederenda
    全民公决
    - proposal `set_code`

    absention votes


### Spec

- consensus `hard-coded`

    - PBFT
    - Zyzzyva [Zyzzyva: Speculative Byzantine Fault Tolerance](http://www.cs.cornell.edu/lorenzo/papers/kotla07Zyzzyva.pdf)
    - Aardvark [Making Byzantine Fault Tolerant Systems Tolerate Byzantine Faults](https://www.usenix.org/legacy/event/nsdi09/tech/full_papers/clement/clement.pdf)
