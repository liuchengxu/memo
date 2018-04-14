---
layout: "posts"
title: "Parity"
permalink: /parity/
excerpt: "parity"
---

### 快速同步

```bash
$ parity --warp --no-ancient-blocks --no-serve-light --max-peers 250 --snapshot-peers 50 --min-peers 50 --mode active --tracing off --pruning fast --db-compaction ssd --cache-size 4096 --force-ui
```

- `--force-ui`: Parity 1.10 以后，钱包变成了一个独立的应用，默认关闭浏览器的 `localhost:8180` 访问。
