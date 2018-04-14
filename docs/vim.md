---
title: "Vim"
permalink: /vim/
excerpt: "vim"
---

### quickfix

```vim
:copen " Open the quickfix window
:ccl   " Close it
:cw    " Open it if there are "errors", close it otherwise (some people prefer this)
:cn    " Go to the next error in the window
:cnf   " Go to the first error in the next file
:cc 2  " Jump to the second error in the quickfix window
```

- [How do you use vim's quickfix feature?](https://stackoverflow.com/questions/1747091/how-do-you-use-vims-quickfix-feature)

```vim
" In the quickfix window, <CR> is used to jump to the error under the
" cursor, so undefine the mapping there.
autocmd BufReadPost quickfix nnoremap <buffer> <CR> <CR>
```

- [Hitting enter in the quickfix window doesn't work](https://superuser.com/questions/815416/hitting-enter-in-the-quickfix-window-doesnt-work)

### YouCompleteMe

- 使用 gocode 补全时，先要在项目目录下面执行 `go install` 才能补全第三方库。

### 正则表达式

- [vim正则表达式](https://mrlongx.com/index.php/2018/01/18/vim-regexp/)
