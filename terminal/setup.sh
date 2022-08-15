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

blue(){
echo -en "\033[1;94m"
}

pkgs="git python3 binwalk nikto"
for i in $pkgs; do
#   echo $i
  blue "Installing ${i}..."
  apt install $i -y 2>/dev/null  || sudo apt install $i -y 2>/dev/null
done
