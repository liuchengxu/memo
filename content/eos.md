## Tic-Tac-Toe

"三子棋"

```
    - | o | x      where - = empty cell
    - | x | -            x = move by host
    x | o | o            o = move by challenger

```

### struct

- create: action, 创建游戏
    - host
    - challenger

- move: action, 移动
    - host
    - challenger
    - by
    - mvt

- restart: action, 重新开始
    - host
    - challenger
    - by

- close: action, 终止游戏，释放空间
    - host
    - challenger

- game: 存储游戏相关信息
    - host
    - challenger
    - turn
    - winner
    - board

- movement: 用于记录移动
    - row
    - column


- 账户命名规则：https://github.com/EOSIO/eos/issues/56
