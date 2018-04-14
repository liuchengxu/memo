Docker
======

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

- http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html

#### 在 Ubuntu16.04 的 docker 里面安装 vim

```bash
# 先执行 update 再安装软件
$ apt update
$ apt install vim
```
