---
layout: "posts"
title: "Git"
categories: git
---

#### tutorial

- https://learngitbranching.js.org/?demo

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

`git rebase --help`:

>       Assume the following history exists and the current branch is "topic":
>
>                     A---B---C topic
>                    /
>               D---E---F---G master
>
>       From this point, the result of either of the following commands:
>
>           git rebase master
>           git rebase master topic
>
>       would be:
>
>                             A'--B'--C' topic
>                            /
>               D---E---F---G master
>
>       NOTE: The latter form is just a short-hand of git checkout topic followed by git rebase master. When rebase exits topic will remain the
>       checked-out branch.
>

- [Configuring a remote for a fork](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
- [Syncing a fork](https://help.github.com/articles/syncing-a-fork/)

#### 更新 submodule

```bash
$ git submodule update --init --recursive
```

#### remote branch missing

`--depth` --> `--single-branch`

- https://stackoverflow.com/questions/20338500/git-repository-lost-its-remote-branches

#### git hook

- `chmod +x .git/hooks/pre-commit` 脚本要有执行权限 git 才会执行

#### 切到本地尚不存在的远端分支


```bash
$ git branch -a

$ git checkout -b slim origin/slim
```

#### git diff

```bash
# 与 <x> 为基准
# git diff base +- 都是以 base 为基准显示
# 想要查看 v1 相对于 v2 有什么差别，那么 git diff v2 v1
$ git diff <x> <x+∆x>

# 比较最新提交的上一笔提交与最新提交
$ git diff HEAD^ HEAD

# 比较 branch
$ git diff dev master
```

#### ssh key

将 ~/.ssh/id_rsa.rsa 加入 GitHub deploy keys

```bash
~/eos ❯❯❯ ssh -T git@github.com
The authenticity of host 'github.com (52.74.223.119)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,52.74.223.119' (RSA) to the list of known hosts.
Hi chainpool/eosdev! You've successfully authenticated, but GitHub does not provide shell access.
```

- https://developer.github.com/v3/guides/using-ssh-agent-forwarding/

#### 保留空白目录并 ignore 该目录下所有内容

- https://stackoverflow.com/questions/115983/how-can-i-add-an-empty-directory-to-a-git-repository

#### 查看指定文件的所有 commits

```bash
$ git log --follow file
```

#### 终端打 tag

```bash
$ git tag -a v0.8.0
$ git push origin v0.8.0
```

- https://www.learnenough.com/git-tutorial#sec-prompt_branches_and_tab_completion

#### 带有 .gitsubmodules 的 repo 删除 .git 后 git submodule 失效

- https://stackoverflow.com/questions/3336995/git-will-not-init-sync-update-new-submodules

#### 如果 git 仓库有 submodule 直接 .git 会有很多问题，重置提交历史

- https://gist.github.com/heiswayi/350e2afda8cece810c0f6116dadbe651

#### 修改 release 对应的 commit

```bash
git tag -f -a <tagname>
git push -f --tags
```

- https://stackoverflow.com/questions/24849362/change-connected-commit-on-release-github


#### 如何 fork 一个 repo 到 private 仓库

```bash
# 首先 clone 要 fork 的 repo
$ git clone https://github.com/forked-repo

# remote 添加 私有 repo
$ git remote add xlc https://github.com/private-repo

# 接下来可以 git push --all xlc
# https://stackoverflow.com/questions/4181861/src-refspec-master-does-not-match-any-when-pushing-commits-in-git/44163991#44163991
$ git push --all xlc

################
# 或者在一开始的时候就使用 --bare，--mirror 进行 clone 和 push
# https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private
$ git clone --bare https://github.com/exampleuser/public-repo.git
$ cd public-repo.git
$ git push --mirror https://github.com/yourname/private-repo.git
```

#### sync repo

- https://gist.github.com/CristinaSolana/1885435

#### git merge --squash

```bash
git checkout master
git merge --squash bugfix
git commit
```

https://stackoverflow.com/questions/5308816/how-to-use-git-merge-squash

#### git merge/rebase 解决冲突

git merge:

```bash
# 在 merge 时，ours 指代的是当前分支, 扔掉当前分支改动
$ git checkout --ours .

# theirs 代表需要被合并的分支, 扔掉待合并分支改动
$ git checkout --theirs .
```

git rebase:

```
# 在 rebase 过程中，ours 指向了待合并分支, 扔掉待合并分支改动
$ git checkout --ours

# theirs 却是当前分支
$ git checkout --theirs
```

- https://bitmingw.com/2017/02/16/git-merge-rebase-ours-and-theirs/


travis ci 部署 上传二进制

- https://github.com/dandavison/delta/blob/master/src/bat/.travis.yml
