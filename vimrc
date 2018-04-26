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

call plug#end()
