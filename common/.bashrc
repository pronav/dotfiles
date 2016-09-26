#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

parse_git_dir() {
	local GIT_BRANCH="$(git branch 2>/dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\ \1/')"
	local GIT_COMMIT="$(git log -1 --format="/%h" 2>/dev/null)"
	local GIT_ALL="$(git status --porcelain 2>/dev/null | wc -l)"
	local GIT_MOD="$(git status --porcelain -uno 2>/dev/null | wc -l )"
	local GIT_UNT="$(($GIT_ALL-$GIT_MOD))"
	echo -n "$GIT_BRANCH$GIT_COMMIT"
	if [ $GIT_UNT -gt "0" ]; then
		echo -n " ?$GIT_UNT"
	fi
	if [ $GIT_MOD -gt "0" ]; then
		echo -n " !$GIT_MOD"
	fi
}

function _update_ps1() {
#    PS1="$(~/repos/powerline-shell/powerline-shell.py --cwd-mode dironly $? 2> /dev/null)"
PS1="\[\e[95m\]\W\[\e[93m\]\$(parse_git_dir) \[\e[95m\]\$ \[\e[39m\]"
}

if [ "$TERM" != "linux" ]; then
    PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
fi


TERM=xterm
ANDROID_HOME=/opt/android-sdk
shopt -s globstar
export PATH="${PATH}:/home/p/bin"

alias apidbr='for db in api_live api_test; do echo "DROP DATABASE IF EXISTS $db; CREATE DATABASE $db;"; done | mysql -u root -p && php artisan rzp:dbr --install --seed'

#git aliases
alias gb='git branch'
alias gc='git commit'
alias ga='git add'
alias gco='git checkout'
alias gd='git diff --color'
alias gp='git push origin HEAD'
alias gpu='git pull --rebase'
alias gst='git status'
alias grh='git reset --hard HEAD'

alias ls='ls --color=auto'
alias sss='sudo systemctl start'
alias ssr='sudo systemctl restart'
alias ss='sudo systemctl'
alias weinre='weinre --boundHost -all-'

