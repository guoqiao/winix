@echo off

echo winix\rc.cmd loaded

rem builtin cmd alias
doskey cp=copy %*
doskey mv=move %*
doskey rm=del %*
doskey ln=mklink %*
doskey lnd=mklink /d %*
doskey rmd=rd /s %*
doskey man=help %*
doskey open=explorer %*
doskey which=where %*

doskey home=cd /D %USERPROFILE%
doskey ~=cd /D %USERPROFILE%

doskey poweroff=shutdown /s /soft
doskey reboot=shutdown /r /soft
doskey sleep=shutdown /h /soft

doskey ev=rundll32 sysdm.cpl,EditEnvironmentVariables


doskey ls=exa --color=always %*
doskey la=exa --color=always --all %*

doskey ll=exa --color=always --long --header --time-style long-iso %*

doskey lpath=exa --color=always --long --header --time-style long-iso --absolute %*
doskey lll=exa --color=always --long --header --time-style long-iso --absolute %*

doskey ltree=exa --color=always --tree %*
doskey tree=exa --color=always --tree %*

doskey lsize=eza --color=always --long --header --sort size --reverse --time-style long-iso %*
doskey ltime=exa --color=always --long --header --sort time --modified --reverse --time-style long-iso %*

doskey vi=nvim %*
doskey vim=nvim %*
doskey view=nvim -Mmn %*

doskey df=duf %*
doskey ps=procs %*
doskey apt=scoop %*
doskey cat=bat %*
doskey top=btop %*
doskey diff=delta %*
doskey find=fd %*

doskey gti=git %*
doskey gst=git status %*
