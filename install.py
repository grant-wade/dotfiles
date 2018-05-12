#!/usr/bin/python

# ======================== #
# Standard Library Imports #
# ======================== #
import os
import sys
from subprocess import call


# ================ #
# Global Variables #
# ================ #
TAG_LINE = 'Custom Dotfile Installer v0.1'
FILES = [
    ''
]
COMMANDS = [
    'curl -o omz_install.sh https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh',
    'sh ./omz_install.sh',
    'curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim',
    'curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
]


def get_input(question, valid):
    """Asks a user for input till valid response"""
    s = "{0} [{1}]: ".format(question, valid)
    val = raw_input(s)
    while val not in valid:
        print "Not a valid answer [%s]" % valid
        val = raw_input(s)
    return val


def start():
    print TAG_LINE

    # Ask to install oh-my-zsh and then install
    val = get_input("Install oh-my-zsh", "yn")
    if val == 'y':
        print "Grabbing oh-my-zsh"
        if call(COMMANDS[0].split()):
            print "Curl error exiting"
            sys.exit(1)
        print "Installing oh-my-zsh"
        if call(COMMANDS[1].split()):
            print "oh-my-zsh install error"
            sys.exit(1)
        print "Installing oh-my-zsh"

    # Ask to install vim-plug then install
    val = get_input("Install vim-plug", "yn")
    if val == 'y':
        val = get_input("Vim or NeoVim", "vn")
        if val == 'v':
            print "Installing vim-plug for vim"
            if call(COMMANDS[2].split()):
                print "vim-plug install failed"
                sys.exit(1)
        else:
            print "Instlaling vim-plug for neovim"
            if call(COMMANDS[3].split()):
                print "vim-plug install failed"
                sys.exit(1)

    print "Setup completed"

if __name__ == '__main__':
    start()

