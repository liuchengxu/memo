# macOS

## mac 上网很慢

- https://www.zhihu.com/question/35233074

1. 网络 -- DNS
2. 网络 -- 硬件 -- MTU

## 文件

Command + Shift + . 可以显示隐藏文件、文件夹，再按一次，恢复隐藏

finder下使用 Command + Shift + G 可以前往任何文件夹，包括隐藏文件夹。

命令

## 显示隐藏文件

```bash
$ defaults write com.apple.finder AppleShowAllFiles -boolean true ; killall Finder
```

恢复隐藏文件隐藏状态

```bash
$ defaults write com.apple.finder AppleShowAllFiles -boolean false ; killall Finder
default
```

- http://seanxp.com/2016/05/mac-hammerspoon/

- https://blog.kalis.me/setup-hyper-key-hammerspoon-macos/

- https://github.com/Hammerspoon/hammerspoon/wiki/Sample-Configurations

- https://github.com/jixiuf/dotfiles/blob/master/mac/hammerspoon/toggle_app.lua