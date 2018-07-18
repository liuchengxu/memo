---
layout: "posts"
title: "Shell"
permalink: /shell excerpt: "shell"
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

## 终端颜色

- https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux/5947788#5947788
- https://linux.101hacks.com/ps1-examples/prompt-color-using-tput/

```bash
for (( i = 0; i < 17; i++ ));
do echo "$(tput setaf $i)This is ($i)$(tput sgr0)";
done
```

## Bash Prompt

- https://github.com/oviung/git-colored-prompt

## tail

```bash
# 将进程日志重定向到一个文件
$ nodeos > nodeos.log
# The -f option causes tail to not stop when end of file is reached, but rather to wait for additional data to be appended to the input.  The -f option is ignored if the standard input is a pipe, but not if it is a FIFO.
$ tail -f nodeos.log
```

- https://www.linuxquestions.org/questions/linux-general-1/ultimate-prompt-and-bashrc-file-4175518169/

## openwrt 路由器翻墙

- https://github.com/softwaredownload/openwrt-fanqiang

## kcptun 加速 ss

- https://blog.kuoruan.com/110.html

## MySQL 导入 database schema

- https://stackoverflow.com/questions/26015521/mysql-import-database-schema

## scp vs rsync

- https://stackoverflow.com/questions/20244585/how-does-scp-differ-from-rsync


## awesome shell

- https://github.com/agarrharr/awesome-cli-apps
    - https://github.com/agarrharr/awesome-cli-apps#database
    - https://github.com/agarrharr/awesome-cli-apps#command-line-learning
    - https://github.com/agarrharr/awesome-cli-apps#data-manipulation

- https://github.com/alebcay/awesome-shell
    - https://github.com/alebcay/awesome-shell#guides

- https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md#%E5%8D%95%E8%A1%8C%E8%84%9A%E6%9C%AC


## 在文件第一行插入

- https://unix.stackexchange.com/questions/99350/how-to-insert-text-before-the-first-line-of-a-file

```bash
# -i[SUFFIX] -ibak 原地修改源文件 并以 bak 命名结尾备份源文件
# '1i[insert content]'
#     - i   行前插入
#     - a   行后插入
#     - c   行替换
$ sed -ibak '1iaddress,name,key,asset' snapshot.csv
```

## find

```bash

$ find /

# 在用户目录下查找所有的 JPEG 文件
$ find ~ -name '*jpg'

# 同上，但是不区分大小写
$ find ~ -iname '*jpg'


# -o 表示 ||，查找 jpeg 或者 jpg
# 注意括号加 (, 前后留空格
$ find ~ \( -iname '*jpeg' -o -iname '*jpg' \)

# -type f 指定查找文件
$ find ~ \( -iname '*jpeg' -o -iname '*jpg' \) -type f

# -type d 指定查找目录
$ find ~ \( -iname '*jpeg' -o -iname '*jpg' \) -type d

# 缩小到上周更改的文件
# ctime 文件状态更改时间   cmin
# mtime 修改时间           mmin
# atime 访问时间           amin
$ find ~ \( -iname '*jpeg' -o -iname '*jpg' \) -type f -mtime -7

# 在 /var/log 查找大于 1 GB 的文件
$ find /var/log -size +1G

# 在 /data 找到 xlc 拥有的文件
$ find /data/ -owner xlc

```

- https://unix.stackexchange.com/questions/209068/how-do-i-delete-the-first-n-lines-and-last-line-of-a-file-using-shell-commands


## 首次给 root 用户设置密码

```bash
$ sudo passwd
```
