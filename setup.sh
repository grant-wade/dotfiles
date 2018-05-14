#!/bin/bash

# Print where the install will be happening
printf "Installing files to %s\n" $HOME

# See if user wants to continue
read -p "Continue? [yn]: " confirm
if [[ $confirm != "y" ]]; then
    echo "Exiting"
    exit 0
fi

# Clone dotfiles repo
git clone https://github.com/grant-wade/dotfiles.git $HOME/.dotfiles

# Download miniconda install script
curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install miniconda
bash Miniconda3-latest-Linux-x86_64.sh

# Remove miniconda installer
rm Miniconda3-latest-Linux-x86_64.sh

# Run setup script
$HOME/.miniconda3/bin/python $HOME/.dotfiles/install.py

# Customize dotfiles
$HOME/.miniconda3/bin/python $HOME/.dotfiles/file_creator.py

# Link all the needed files
ln -sf ~/.dotfiles/zshrc ~/.zshrc
ln -sf ~/.dotfiles/vimrc ~/.vimrc
ln -sf ~/.dotfiles/tmux.conf ~/.tmux.conf
ln ~/.dotfiles/gww_custo.zsh-theme ~/.oh-my-zsh/themes/

# Start new prompt
zsh
