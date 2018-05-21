#!/bin/bash

# Print where the install will be happening
printf "Have you installed (git, curl and neovim)?"

# See if user wants to continue
read -p "Continue? [yn]: " confirm
if [[ $confirm != "y" ]]; then
    echo "Exiting"
    exit 0
fi

# Clone dotfiles repo
git clone https://github.com/grant-wade/dotfiles.git $HOME/.dotfiles

# Set dotfiles location
DOTFILES=$HOME/.dotfiles

# Download miniconda install script
curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install miniconda
bash Miniconda3-latest-Linux-x86_64.sh

# Remove miniconda installer
rm Miniconda3-latest-Linux-x86_64.sh

# Install python neovim plugin in custom env
$HOME/.miniconda3/bin/conda create -n system_env python=3

# Python env location
SYSTEM_PYTHON=$HOME/.miniconda3/envs/system_env/bin/python

# Setup system python
$SYSTEM_PYTHON -m pip install neovim psutil

# Run setup script
$SYSTEM_PYTHON $DOTFILES/install.py

# Customize dotfiles
$SYSTEM_PYTHON $DOTFILES/file_creator.py

# Link all the needed files
ln -sf $DOTFILES/zshrc ~/.zshrc
ln -sf $DOTFILES/vimrc ~/.vimrc
ln -sf $DOTFILES/vimrc ~/.config/nvim/init.vim
ln -sf $DOTFILES/tmux.conf ~/.tmux.conf
ln $DOTFILES/gww_custo.zsh-theme ~/.oh-my-zsh/themes/

# Start new prompt
zsh
