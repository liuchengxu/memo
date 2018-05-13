# Bash

### Bash 脚本中 (、((、[、[[ 的区别

- https://www.zhihu.com/question/266787434/answer/314413359


### 单引号内展开变量

```bash
cleos push action eosio.token maping '["'$user'", '$id']' -p eosio > /dev/null
```

### 按行读取文件

```bash
#!/bin/bash
while read line
do
    echo $line     #这里可根据实际用途变化
done < filename      #filename 为需要读取的文件名
```

```bash
#!/bin/bash

cat filename| while read line   #filename 为需要读取的文件名,也可以放在命令行参数里。
do
    echo $line
done
```

### 判断 GitHub URL

- https://stackoverflow.com/questions/9610131/how-to-check-the-validity-of-a-remote-git-repository-url

### 字符串截取

```bash
user="${url#*:}"

```

```bash
# 如果 url 以 .git 结尾，去除 .git
# https://github.com/liuchengxu/space-vim.git -> https://github.com/liuchengxu/space-vim
if [[ $url =~ .git$ ]]; then
  url="${url%.*}"
fi
```
