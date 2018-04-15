---
layout: "posts"
title: "Docker"
permalink: /docker
excerpt: "docker"
date: 2018-04-15
toc: true
categories: docker
---

```bash
# 列出本机的所有 image
$ docker image ls

# 从 image 文件启动容器
$ docker container run -it {image}

# 手动 kill container
$ docker container kill {containerID}

# 列出本机正在运行的容器
# container ls 的输出中包含了 containerID
$ docker container ls

# 列出本机所有容器，包括已停止运行的容器
$ docker container ls --all

# 终止容器运行，但是容器仍会占据磁盘空间，使用 rm 删除
$ docker container rm {containerID}
```

- [Docker 入门教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)

### 在 Ubuntu16.04 的 docker 里面安装 vim

```bash
# 先执行 update 再安装软件
$ apt update
$ apt install vim
```

### 配置镜像加速器

由于网络问题，国内从默认的 Docker Hub 拉取镜像可能会有困难，“重新配置源”。

- [镜像加速器](https://yeasy.gitbooks.io/docker_practice/content/install/mirror.html)
- [Docker 中国官方镜像加速](https://www.docker-cn.com/registry-mirror)
