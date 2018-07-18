# Bash

### Bash 脚本中 (、((、[、[[ 的区别

- https://www.zhihu.com/question/266787434/answer/314413359


### 单引号内展开变量

```bash
cleos push action eosio.token maping '["'$user'", '$id']' -p eosio > /dev/null
```

- https://github.com/dylanaraps/pure-bash-bible


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

### 当前函数名

```bash
func() {
    echo "Current function: $FUNCNAME"
}
```

- https://unix.stackexchange.com/questions/261305/how-to-determine-callee-function-name-in-a-script

### curl 下载脚本并执行

- https://stackoverflow.com/questions/4642915/passing-parameters-to-bash-when-executing-a-script-fetched-by-curl

## array

- 只支持一维数组
- 初始化时不需要定义数组大小（与 PHP 类似）
- 下标由 0 开始

```bash
arr=(a b 'c' 123)


# 读取单个数组元素: ${array_name[index]}
echo "第一个元素为: ${arr[0]}"
echo "第二个元素为: ${arr[1]}"
echo "第三个元素为: ${arr[2]}"
echo "第四个元素为: ${arr[3]}"

# 获取数组所有元素
echo "获取数组所有元素: ${arr[*]}"
echo "获取数组所有元素: ${arr[@]}"

# 获取数组长度，与获取字符串长度相同
echo "数组元素个数为: ${#arr[*]}"
echo "数组元素个数为: ${#arr[@]}"
```

## 算数运算

```bash
val=$(( 1 + 2 ))
echo $val
```
