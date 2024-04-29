@echo off
echo.
exa --color=always --long --header --sort time --modified --reverse --time-style long-iso --absolute %*
