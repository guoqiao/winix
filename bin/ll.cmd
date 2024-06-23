@echo off
echo.
REM sort by name by default
exa --color=always --long --header --time-style long-iso %*
