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

#prompt setup

cd ~/
curl -O https://starship.rs/install.sh
chmod 700 install.sh
./install -b ~/bin #edit location for custom binary
echo "eval '$(starship init bash)'" >> ~/.bashrc

