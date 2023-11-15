## In which we document every single thing we learned with very little organization
1. It's a good idea to have a copy of each of your files in their original state so that you can compare and contrast to improvements as you make them.

## The error messages and their corresponding fixes
> ImportError: cannot import name 'escape' from 'flask'
- Fix: flask.escape has been depricated, use markupsafe.escape instead
- Since flask owns markupsafe you can just add a line to the import section:
- >**from markupsafe import escape**
> export: not valid in this context: .
- Changing python environment variable fails and the above error message appears.
- In zsh, [Command Substitution](https://zsh.sourceforge.io/Doc/Release/Expansion.html#Command-Substitution) result performs word splitting if not enclosed in double quotes. So if your command substitution result contain any whitespace, tab, or newline, the export command will be broken into parts.
- [Fix:](https://unix.stackexchange.com/questions/208607/zsh-export-not-valid-in-this-context) instead of export PYTHONPATH=$PYTHONPATH: .
- Use export **PYTHONPATH=$PYTHONPATH:"."** instead
> Weird import issue with app.py: importing planisphere.py into app.py doesn't appear to work
- Fix (allegedly): [use sys.path.append](https://ioflood.com/blog/python-import-from-another-directory/) to tell your machine to look in a different directory for the goods to run a file
- Why is this only an "alleged" fix? Because the issue below is still present --v
> First room works but submission of answer doesn't result in any change
- Fix: /templates/show_room.html, line 15: 
- **form method** needed to not be **form mehtod**. Yes. That's right. I spent nearly 2 hours in my .py files trying to fix something that was just a typo in one of my templates.

## Where I left off
Cannot for the life of me get the wildcard input option to work for these rooms. If a there is no specific path to get to the death room (i.e. you type "shoot!" in the first room) nothing changes when you submit your answer.