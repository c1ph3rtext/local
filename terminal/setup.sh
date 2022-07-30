#!/bin/bash

echo "
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

if [ -f ~/.funcs ]; then
    . ~/.funcs
fi
" #>> $HOME/../usr/etc/bash.bashrc #this is for termux change for your .bashrc file location here

cat aliases > ~/.bash_aliases
cat funcs > ~/.funcs
