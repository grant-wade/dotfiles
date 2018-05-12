#!/bin/bash

# Clone dotfiles repo
git clone https://github.com/grant-wade/dotfiles.git .dotfiles

# Run setup script
python2 ~/.dotfiles/install.py

# Link all the needed files
ln -sf ~/.dotfiles/zshrc ~/.zshrc
ln -sf ~/.dotfiles/vimrc ~/.vimrc
ln -sf ~/.dotfiles/tmux.conf ~/.tmux.conf
ln ~/.dotfiles/gww_custo.zsh-theme ~/.oh-my-zsh/themes/

# Start new prompt
zsh
