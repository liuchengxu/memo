# Filecoin

## IPNS

DNS -> 


IPFS 每次更新，都会得到一个新的 CID, 也就是一个新的地址。

IPNS 就是指向最新版本的内容。

MFS: Mutable File System

DNSLink 也可以实现类似的效果，而且目前比 IPNS 快得多。

A DNSLink address looks like an IPNS address, but it uses a domain name in place of a hashed public key:

```
/ipns/myexampledomain.org
```

现在的 http 寻址是按照地址寻址, 在哪儿

https://en.wikipedia.org/wiki/Aardvark
/Users/Alice/Documents/term_paper.doc
C:\Users\Joe\My Documents\project_sprint_presentation.ppt

按地址寻址的问题是一旦文件位置挪动，就找不到了

IPFS 是按照内容寻址, 是什么。

按内容寻址的问题是一旦内容更新，就找不到了。

Merkle-DAGs are similar to Merkle Trees [20] but there are no balance requirements and every node can carry a payload

没有平衡要求，每个节点可以携带内容

merkle tree 是平衡二叉树，只有叶子节点携带内容

Merkle-DAG 的一个好处是将存储分割为 block, 每次版本更新尽量存储 diff,  类似 Git


p2p 节点发现

bitswap 节点内容交换


libp2p 的点对点连接的优势

connection multiplexing 连接多路复用



DHT

分布式哈希表


## Pinning

IPFS 的节点进行 GC 时会删除非 pin 的内容。





一个文件的每次改动


 改动1  ->  改动2
   |        |
commit1  commit2

address    address




Merkle Trees: What They Are and the Problems They Solve
https://www.codementor.io/blog/merkle-trees-5h9arzd3n8
