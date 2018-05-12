#!/bin/bash

# Clone dotfiles repo
git clone https://github.com/grant-wade/dotfiles.git .dotfiles

# Run setup script
python2 ~/.dotfiles/install.py

# Download miniconda install script
curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install miniconda
bash Miniconda3-latest-Linux-x86_64.sh

# Remove miniconda installer
rm Miniconda3-latest-Linux-x86_64.sh

# Link all the needed files
ln -sf ~/.dotfiles/zshrc ~/.zshrc
ln -sf ~/.dotfiles/vimrc ~/.vimrc
ln -sf ~/.dotfiles/tmux.conf ~/.tmux.conf
ln ~/.dotfiles/gww_custo.zsh-theme ~/.oh-my-zsh/themes/

# Start new prompt
zsh
