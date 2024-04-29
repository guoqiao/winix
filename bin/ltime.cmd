@echo off
echo.
exa --color=always --long --sort time --modified --reverse --time-style long-iso %*
