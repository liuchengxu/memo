---
layout: "posts"
title: "Vim"
permalink: /vim
excerpt: "vim"
date: 2018-04-15
toc: true
categories: vim
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

#### 过滤 quickfix

- https://www.reddit.com/r/vim/comments/8fb2ua/refiltering_the_quickfix_list/
- https://stackoverflow.com/questions/15406138/is-it-possible-to-grep-vims-quickfix
- https://gist.github.com/PeterRincker/33345cf7fdeb9038611e4a338a0067f3
- https://github.com/romainl/vim-qf

### YouCompleteMe

- 使用 gocode 补全时，先要在项目目录下面执行 `go install` 才能补全第三方库。

### 检查是否支持某 event

```vim
:echo exists('##TerminalOpen')
```

### 正则表达式

- [vim正则表达式](https://mrlongx.com/index.php/2018/01/18/vim-regexp/)

### Reddit

- https://www.reddit.com/r/vim/comments/8d9bh1/vimrc_review_thread_40/

### help

- `:h index`: 默认快捷键。

    ```
    1. 插入模式				|insert-index|
    2. 普通模式				|normal-index|
       2.1. 文本对象			|objects|
       2.2. 窗口命令			|CTRL-W|
       2.3. 方括号命令			|[|
       2.4. 'g' 开头的命令			|g|
       2.5. 'z' 开头的命令			|z|
    3. 可视模式				|visual-index|
    4. 命令行编辑				|ex-edit-index|
    5. EX 命令				|ex-cmd-index|
    ```

### syntax

- https://www.reddit.com/r/vim/comments/8gfj3t/my_professor_developed_a_programming_language_and/

### 文件是否存在

- https://github.com/junegunn/fzf.vim/issues/573


### 使用本地 vim 打开远程文件

```bash
# 在本地打开 192.168.1.6 指定文件 ~/.bashrc
$ vim scp://eos@192.168.1.6/~/.bashrc
```

### Modern Vim

- https://www.reddit.com/r/vim/comments/8gsefa/modern_vim_is_out/

### tab 补全

如果只有补全插件的话，其实比较简单，一般的做法就是判断是否有弹出菜单，有的话，就更改一下 tab, shift-tab, cr 这些键的变为，变为 c-n, c-p, <c-y><cr>，也就是下一个补全项，上一个补全项

    ```vim
    function! spacevim#util#ExpandSnippetOrCarriageReturn()
      if exists("*UltiSnips#ExpandSnippet")
        if get(g:, 'ulti_expand_res', 0) > 0
          return UltiSnips#ExpandSnippet()
        endif
      endif
      return "\<c-y>\<cr>"
    endfunction
    ```
- 不使用 `code-snippets`
    - ycmd: tab 上下选择，enter 换行
    - `auto-completion`: tab 上下选择，enter 换行

- 使用 `code-snippets`
    - ycmd: tab 选择，enter 换行
    - `auto-completion`: tab 上下选择，enter 换行

```vim
"i_CTRL-R
inoremap <Tab> <C-R>=CleverTab()<CR>


inoremap <expr> CleverTab()
```

------

- https://zhuanlan.zhihu.com/p/38150203

    ```vim
    function! spacevim#util#ExpandSnippetOrCarriageReturn()
      if exists("*UltiSnips#ExpandSnippet")
        if get(g:, 'ulti_expand_res', 0) > 0
          return UltiSnips#ExpandSnippet()
        endif
      endif
      if spacevim#load('ycmd')
        return "\<cr>"
      elseif spacevim#load('deoplete')
        return "\<c-y>"
      else
        return "\<c-y>\<cr>"
      endif
    endfunction
    ```

- 使用 `code-snippets`
    - auto-completion: tab 选择，enter 换行
    - ycmd: tab 选择，enter 换行

- fugitive
    - `Gblame`

- https://www.reddit.com/r/vim/comments/8oti4x/does_vim_slow_down_depending_on_the_programming/

- https://github.com/lymslive/vimllearn

- https://www.reddit.com/r/vim/comments/8jb9r7/complete_latex_suite_in_vim/dyzddkg/

- https://github.com/echuraev/translate-shell.vim

- https://jamesbvaughan.com/markdown-pandoc-notes/

- https://github.com/jbgutierrez/vim-better-comments

- https://www.reddit.com/r/vim/comments/8ohlgv/plugin_manager_support_for_gitlab/

- https://github.com/inkarkat/vim-ingo-library

- https://github.com/hauleth/asyncdo.vim

- https://github.com/vim-scripts/grep.vim/blob/master/plugin/grep.vim

- https://www.reddit.com/r/vim/comments/8rcbd0/what_was_the_latest_vim_feature_youve_discovered/

- https://gitlab.com/yramagicman/stow-dotfiles/blob/master/vim/.vim/autoload/status.vim


#### cdo, cfdo

- windo, tabdo, bufdo, cdo, ldo, cfdo, lfdo

- http://vim.wikia.com/wiki/Implement_your_own_interactive_finder_without_plugins

- https://github.com/LucHermitte/lh-vim-lib

#### if quickfix window exists

- https://www.reddit.com/r/vim/comments/5ulthc/how_would_i_detect_whether_quickfix_window_is_open/

#### index

- CTRL-G: 显示当前文件名和位置
- CTRL-I: forward jump list
- CTRL-O: back jump list
- CTRL-]
- CTRL-V: 块操作
- CTRL-X: 光标处数字减 N
- #
- %
- ,
- ZZ
- f
- m
- q

#### haskell

- https://github.com/Twinside/vim-haskellConceal


#### startuptime

```bash
for i in $(seq 1 50); do nvim --startuptime /dev/stdout +q | tail -n1; done | awk '{ sum += $1 } END { print sum / NR }'
```

#### Practise

- https://stackoverflow.com/questions/253380/how-do-i-insert-text-at-beginning-of-a-multi-line-selection-in-vi-vim

- https://github.com/autozimu/LanguageClient-neovim/issues/379


- https://github.com/vim/vim/issues/2191  `buffer wiped out`




#### tab space

将现有的 4 个 space 换成 2 个 space:

```
将每 2 个空格变成一个 tab
:setlocal ts=2 sts=2 noet | retab!
将每个 tab 变成 4 个 space
:setlocal ts=2 sts=2 et | retab
```

- https://stackoverflow.com/questions/16888658/change-2-space-indent-to-4-space-in-vim
