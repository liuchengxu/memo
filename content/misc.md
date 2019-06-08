---
layout: "posts"
title: "Misc"
permalink: /misc
excerpt: "misc"
toc: true
---


#### 翻墙

```bash
$ brew cask install shadowsocksx-ng
```

ShadowsocksX-ng 自动启动 http 代理，在终端设置 `http_proxy` 即可

查看是否成功：

```bash
$ curl ip.cn
$ curl cip.cc
```

```
export http_proxy=http://127.0.0.1:1087
export https_proxy=http://127.0.0.1:1087
```

```
npm config set proxy http://127.0.01:8123
npm config set https-proxy http://127.0.0.1:8123
```

```
git config --global http.proxy http://localhost:8123
git config --global https.proxy http://localhost:8123
```

- https://teddysun.com/342.html
- https://medium.com/@zoomyale/%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91%E7%9A%84%E7%BB%88%E6%9E%81%E5%A7%BF%E5%8A%BF-%E5%9C%A8-vultr-vps-%E4%B8%8A%E6%90%AD%E5%BB%BA-shadowsocks-fd57c807d97e


telegram --> Privacy and Security --> 127.0.0.1 1086

#### 开启 BBR

- https://teddysun.com/489.html
- https://teddysun.com/525.html

#### err_unsafe_port

- https://superuser.com/questions/188058/which-ports-are-considered-unsafe-on-chrome

#### ssh 免密码登录

```bash
$ ssh-copy-id user@remote-host
```

- http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html

#### docker 访问主机

- https://blog.csdn.net/ownfire/article/details/48006893

#### 自动化 GitHub release

- https://github.com/tcnksm/ghr

#### docker从容器中怎么访问宿主机

- https://blog.csdn.net/ownfire/article/details/48006893

#### Mongo

```bash
$ docker run --name monitor-mongo -p 27017:27017 -d mongo
```

#### 找到公网 IP

- https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-centos-7

#### web

- https://github.com/wxyyxc1992/Web-Series

#### mac 多开微信

```bash
$ open -n /Applications/WeChat.app/Contents/MacOS/WeChat
```

#### nginx

- https://www.itcodemonkey.com/article/4359.html

#### tcp

- https://www.v2ex.com/t/466168#reply27

TCPL：《C程序设计语言》
CPPP：《C++ Primer》
SICP：《计算机程序的构造和解释》
CSAPP：《深入理解计算机系统》
MOS：《现代操作系统》
CAAQA：《计算机体系结构-量化研究方法》
GOF：《设计模式：可复用面向对象软件的基础》
CLRS：《算法导论》
- TAOCP：《计算机程序设计艺术》
- Modern operating systems, C++ Primer

- https://www.zhihu.com/question/53436266

### SSR

- https://fangeqiang.com/1091.html

### Websocket 在线测试

- websocket 测试： https://easyswoole.com/wstool.html
