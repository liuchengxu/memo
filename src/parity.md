---
layout: "posts"
title: "Parity"
permalink: /parity
excerpt: "parity"
date: 2018-04-15
toc: true
categories: parity
---

### 快速同步

```bash
$ parity --warp --no-ancient-blocks --no-serve-light --max-peers 250 --snapshot-peers 50 --min-peers 50 --mode active --tracing off --pruning fast --db-compaction ssd --cache-size 4096 --force-ui
```

- `--force-ui`: Parity 1.10 以后，钱包变成了一个独立的应用，默认关闭浏览器的 `localhost:8180` 访问。

### Parity 1.10.1-beta

`--warp-barrier [BLOCK]` 指定最小块号，防止客户端同步落后很多的 snapshot。

- https://github.com/paritytech/parity/releases/tag/v1.10.1
