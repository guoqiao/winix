# Winix

Work on Windows with CLI like on Unix/Linux.

Target Users: Unix/Linux CLI users, but have to use Windows some how.

## Setup

- checkout this repo to your disk, such as `D:\winix`
- add `D:\winix\bin` to your user's `Path` envvar.

To change envvar on Windows:

Settings -> System -> About -> Advanced system settings -> Environment Variables

Or just run this cmd:

```
bin\edit-env-vars.cmd
```

Please note, `Path` envvar exists in both `User variables for xxx` and `System variables`.

For this project, you only need to change the user one.

## Showcase

In Windows Terminal -> Command Prompt, now you can do common tasks just like you are on Unix/Linux:

```
touch a.txt  # create file with touch, installed by scoop
vim a.txt  # edit file with neovim
view a.txt  # view file in vim in Readonly mode
cat a.txt  # show file with bat
cp a.txt b.txt
ln c.txt a.txt  # create sym link, c.txt is the link though
ll  # list all files
lll  # list all files with full path
ltree  # show file in tree
rm a.txt
open .  # open current folder in file explorer
apt install git  # apt is actually scoop here :D
git init .
ps  # procs
ps | grep  # grep is installed by scoop
top # btop
man cat  # help cat
~  # go back to home dir
home  # same as above
poweroff  # shutdown /s
reboot  # shutdown /r
sleep # shutdown /h
```
