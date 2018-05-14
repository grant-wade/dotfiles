# ======================================== #
# Creator: Grant Wade (grant.wade@wsu.edu) #
# This program customizes and creates con- #
# fig files for the system.                #
# ======================================== #

# ======================== #
# Standard Library Imports #
# ======================== #
import os
import sys
from subprocess import call


# ================ #
# Global Variables #
# ================ #
HOME_PATH = os.environ['HOME']
DOTFILES_PATH = HOME_PATH + '/.dotfiles/'
ZSH_PATH = DOTFILES_PATH + 'zshrc'
VIM_PATH = DOTFILES_PATH + 'vimrc'

ZSH_TEMPLATE = """
# zsh variables
export ZSH={0}/.oh-my-zsh
ZSH_THEME="gww_custo"
export TERM=xterm-256color

# Plugins
plugins=(git)

# Startup oh-my-zsh
source $ZSH/oh-my-zsh.sh

# Aliases
# Clear terminal easily
alias c="clear"
# Conda source activator
alias sa="source activate"
alias sd="source deactivate"

# Conda addition to the path
export PATH="{0}/.miniconda3/bin:$PATH"
"""

NVM_STR = """
export NVM_DIR="{}/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
""".format(HOME_PATH)


VIM_TEMPLATE = """
" Escape remap
imap jj <Esc>
imap C-[ <Esc>

" Buffer Remaps
nmap <Left> :bp<cr>
nmap <Right> :bn<cr>

" Leader key setetings
let mapleader = ","
let g:mapleader = ","
nmap <leader>w :w!<cr>
nmap <leader>t :tabnew<cr>
nmap <leader>b :buffers<cr>
nmap <leader>d :w<cr> :bd<cr>
nmap <leader>f :NERDTreeToggle<cr>
nmap <leader>c I//<Esc>
nmap <leader>v :vsplit
nmap <leader>h :split

" Tab Settings
set tabstop=4
set shiftwidth=4
set expandtab
set backspace=2

" Line numbers
set number
set numberwidth=4
set virtualedit=onemore

" Pretty Colors
syntax on

" Swap Files
set swapfile
set dir=/tmp

call plug#begin()

Plug 'scrooloose/nerdtree'
Plug 'jiangmiao/auto-pairs'
Plug 'airblade/vim-gitgutter'
{}

call plug#end()
"""


def get_input (question, valid):
    """Asks a user for input till valid response"""
    s = "{} [{}]: ".format(question, valid)
    val = input(s)
    while val not in valid or len(val) == 0 or val == valid:
        print("Not a valid answer [{}]".format(valid))
        val = input(s)
    return val


def write_file (file_with_path, contents):
    """Writes a file with the given conetens"""
    try:
        with open(file_with_path, 'w') as f:
            for line in contents:
                f.write(line)
    except:
        print("File writing failed path: {}".format(file_with_path), file=sys.stderr)
        return False
    return True



def customize_zsh ():
    """Setup a custom zshrc"""
    val = get_input("Use default zsh config", 'yn')
    contents = ''
    # Set the contents of the file from the template
    if val == 'n': # Custom zshrc
        contents = ZSH_TEMPLATE.format(HOME_PATH)
        val = get_input("Include node version manager", 'yn')
        if val == 'y':
            contents += NVM_STR
    elif val == 'y': # Default zshrc
        contents = ZSH_TEMPLATE.format(HOME_PATH)

    # Write file to .dotfiles folder
    if write_file(ZSH_PATH, contents):
        print("File sucessfully saved")
    else:
        print("ZSH file saving failed", file=sys.stderr)
        return False
    return True

        
def customize_vim ():
    """Setup a custom vimrc"""
    val = get_input("Use default vim config", 'yn')
    contents = ''
    # Set the contents of the vimrc
    if val == 'n': # Custom vimrc
        plugins = ''
        val = get_input("Include Valloric/YouCompleteMe", 'yn')
        if val == 'y':
            plugins += "Plug 'Valloric/YouCompleteMe'\n"
        contents = VIM_TEMPLATE.format(plugins)
    elif val == 'y': # Default vimrc
        contents = VIM_TEMPLATE.format('')
    
    # Write new vimrc to .dotfiles folder
    if not write_file(VIM_PATH, contents):
        print("VIM file saving failed", file=sys.stderr)
        return False
    return True


def start ():
    val = get_input("Create zshrc", 'yn')
    if val == 'y':
        customize_zsh()

    val = get_input("Create vimrc", 'yn')
    if val == 'y':
        customize_vim()

if __name__ == '__main__':
    start()

