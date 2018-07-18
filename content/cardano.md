- https://www.zhihu.com/people/huang-yi-58-63-25/posts

- epoch ==> 在每个 epoch 结束的时候选出下一个 epoch 所有的 slot leader
    - slot ==> slot leader 负责出块

- [Cardano（ADA）的共识算法Ouroboros](https://zhuanlan.zhihu.com/p/33824015)

- Follow the satoshi: https://github.com/Realiserad/fts-tree

- https://forum.cardano.org/t/ada/12298

epoch ==>


## 9. 攻击探讨

### Double spending


Cardano whiteboard

- https://www.youtube.com/watch?v=nB6eDbnkAk8

### how to design a secure protocol

+--------------------------+
      objective
      |       |
    |           |
resources    threat model

algorithm    assumptions

         Proof
+---------------------------+

Proof establish that the algorithm meets the objective given the resources in the threat model under the assumptions

Algorithm --> Specification --> Implementation

Ouroboros

Blockchain protocol comes as a solution to the ledger problem.

distributed ledger

- persistence: 所有节点的日志都一样，并且随着时间变化不会改变。
- liveness: 发送给足够多的节点一定会被接受。

resources:
- parties have private memory and ability to sample random strings
- access to the network

------

BYRON -> SHELLEY -> GOGUEN -> BASHO -> VOLTAIRE

### Goguen

- sidechains, accouting, multi-currency -- 现在是形式化阶段，下一阶段是原型实现。

- plutus -- 已经完成了设计和 Plutus 核心语言的证明，Plutus 智能合约如何记录在链上。接下来是实现 Haskell 库的第一部分，用于将 Plutus 代码处理以后供编译器和虚拟机使用。

- marlowe -- 一个在线编辑器，通过 Haskell 的子集生成 Marlowe 智能合约。它可以得出一个合约执行的可能结果，确保你投入了足够的钱保证执行，这对于创建可用的金融智能合约非常重要。

- IELE -- 已经有了 IELE 虚拟机的 demo。IELE 测试网 7 月 30 日发布。

- https://github.com/runtimeverification

#### 测试网

- KEVM: 5 月 28
- IELE: 7 月 30

KEVM IELE 测试网都可以用 Solidity 写合约，并且推荐使用 solidity 。可以用 IELE 写，这样就是更底层一些，但是也更可控。

KEVM 和 IELE 测试网使用的都是 https://github.com/input-output-hk/mantis Scala 客户端，fork 的 ETC 。mantis 的特点是可应用各种 VM，可插拔共识。

K interpreter ==> EVM

KEVM 可以看成是 K 语言写的 EVM。

- https://github.com/kframework/evm-semantics

Runtime Verification (K framework)

K 框架可以对合约进行验证，检测整形溢出，栈溢出，gas 不够等问题。

The KEVM is a stack-based machine, as opposed to a register-based machine. The primary difference between these two architectures is in the way in which operands and their results are stored and retrieved.

[Solidity-to-IELE compiler](https://github.com/runtimeverification/solidity)

KEVM --> IELE

- 编写：解释器，编译器
- 执行：虚拟机

- [cardanoroadmap](https://cardanoroadmap.com/)
- https://testnet.iohkdev.io/goguen/
- https://forum.cardano.org/t/summary-of-project-goguen-june-2018-update/13762
