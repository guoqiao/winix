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
touch a.txt  # scoop install touch
vim a.txt  # edit file with neovim
view a.txt  # view file in neovim in Readonly mode
cat a.txt  # show file with bat
cp a.txt b.txt # copy
ln c.txt a.txt  # mklink
ll  # list with exa --long
lll  # list with exa --long --absolute
ltree  # list with exa --tree
rm a.txt  # del
open .  # explorer.exe .
apt install git  # apt is scoop here :)
git init .
ps  # procs
ps | grep  # scoop install grep
top # scoop install btop
man cat  # help cat
~  # go back to home dir
home  # same as above
poweroff  # shutdown /s
reboot  # shutdown /r
sleep # shutdown /h
...
```

More to be added, contributions are welcome!
