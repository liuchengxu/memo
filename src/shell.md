---
layout: "posts"
title: "Shell"
permalink: /shell
excerpt: "shell"
date: 2018-04-15
toc: true
categories: shell
---

- [explainshell](https://explainshell.com/)

- [Linux Shell Scripting Tutorial (LSST) v2.0](https://bash.cyberciti.biz/guide/Main_Page)

- [Unix - What is Shells?](http://www.tutorialspoint.com/unix/unix-shell.htm)

- [Advanced Bash-Scripting Guide](http://tldp.org/LDP/abs/html/)


### 递归找到文件并删除

```bash
$ find . -name cscope.* | xargs rm
```

```bash
$ find . -name ‘*.exe’ -type f -print -exec rm -rf {} ;
```

https://blog.csdn.net/robberboyboy/article/details/8239810

### Bash 脚本中 (、((、[、[[ 的区别

- https://www.zhihu.com/question/266787434/answer/314413359


## centos7 开启端口

mosh (60000, 61000) udp

```bash
# 添加端口
$ firewall-cmd --zone=public --add-port=60001/udp --permanent

# 重新载入
$ firewall-cmd --reload

# 查看所有打开的端口
$ firewall-cmd --zone=public --list-ports

# 删除端口
$ firewall-cmd --zone= public --remove-port=60001/udp --permanent
```

- https://www.cnblogs.com/hubing/p/6058932.html

## 磁盘大小

查看目录大小

```bash
$ du -sh *
```

查看文件夹大小

```bash
$ du -h --max-depth=1
```

## ssh

生成 ssh 公钥并拷贝到 node@myserver.com 实现 ssh 免密钥登录

```bash
ssh-keygen -t rsa
ssh-copy-id node@myserver.com
```

~/.ssh/id_rsa.pub 拷贝到 ~/.ssh/authorized_keys

- https://www.liaohuqiu.net/cn/posts/ssh-public-key-auto-login/

## netstat

- https://linux.cn/article-2434-1.html

## bashrc 中不要 exit

单独的脚本可以 exit，bashrc 中不要 exit，否则会导致当前的 shell 进程结束。

- https://stackoverflow.com/questions/39419818/terminal-freezes-after-exit-command-in-bash-script
