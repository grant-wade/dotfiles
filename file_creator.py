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

export SYSTEM_PYTHON=$HOME/.miniconda3/envs/system_env/bin/python

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
alias spy="$SYSTEM_PYTHON"

# Conda and custom binaries to path
export PATH="{0}/.dotfiles/bin:{0}/.miniconda3/bin:$PATH"

export NVM_DIR="{0}/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Display login message
$SYSTEM_PYTHON {0}/.dotfiles/motd.py
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
nmap <leader>1 1gt
nmap <leader>2 2gt
nmap <leader>3 3gt
nmap <leader>4 4gt
nmap <leader>5 5gt
nmap <leader>6 6gt
nmap <leader>7 7gt
nmap <leader>8 8gt
nmap <leader>9 9gt

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

" Plugin Config
let g:python3_host_prog = "{0}/.miniconda3/envs/system_env/bin/python3"
autocmd InsertLeave,CompleteDone * if pumvisible() == 0 | pclose | endif

" Plugin setup
call plug#begin()

" File viewer
Plug 'scrooloose/nerdtree'

" Completer for braces
Plug 'jiangmiao/auto-pairs'

" Git information 
Plug 'airblade/vim-gitgutter'

" Extra Information
Plug 'itchyny/lightline.vim'

" completion engine
if has('nvim')
  Plug 'Shougo/deoplete.nvim', {{ 'do': ':UpdateRemotePlugins' }}
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
let g:deoplete#enable_at_startup = 1

" Add python jedi to completion
Plug 'zchee/deoplete-jedi'

call plug#end()
""".format(HOME_PATH)


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
    contents = VIM_TEMPLATE
    
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

