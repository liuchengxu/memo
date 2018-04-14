Git
===

#### fork 的仓库与上游同步

- 原仓库 https://github.com/paritytech/polkadot
- fork 的仓库 https://github.com/chainpool/polkadot

将原仓库的更新同步到 fork 仓库：

```bash
# 将原仓库添加为新的远程仓库并命令为 upstream
$ git remote add upstream https://github.com/paritytech/polkadot

# 获取原仓库的 master 分支
$ git fetch upstream master

# 切换到本地的 master
$ git checkout master

# 使本地提交基于上游的最新提交，不要用 merge
$ git rebase upstream/master

# 将上游更新推送到 fork 仓库的 master 分支
$ git push origin master
```

- [Configuring a remote for a fork](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
- [Syncing a fork](https://help.github.com/articles/syncing-a-fork/)

#### 更新 submodule

```bash
$ git submodule update --init --recursive
```
