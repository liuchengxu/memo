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
