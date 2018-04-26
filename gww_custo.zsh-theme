# Modification of the robbyrussell theme
# to include the name of the server if connected
# through ssh, and include the full path 
# instead of just the current folder.
# gww_custo

local ret_status="%(?:%{$fg_bold[green]%}➜ :%{$fg_bold[red]%}➜ )"
NEWLINE=$'\n'

RPROMPT='%F{8}${SSH_TTY:+%n@%m}%f'
PROMPT='%{$fg[cyan]%}%d%{$reset_color%} $(git_prompt_info)${NEWLINE}${ret_status}%{$reset_color%}'


ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg_bold[blue]%}git:(%{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%} "
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[blue]%}) %{$fg[yellow]%}✗"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[blue]%})"
