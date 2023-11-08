## In which we document every single thing we learned with very little organization

## The error messages and their corresponding fixes
> ImportError: cannot import name 'escape' from 'flask'
- Fix: flask.escape has been depricated, use markupsafe.escape instead
- Since flask owns markupsafe you can just add a line to the import section:
- >**from markupsafe import escape**
> export: not valid in this context: .
- Changing python environment variable fails and the above error message appears.
- In zsh, [Command Substitution](https://zsh.sourceforge.io/Doc/Release/Expansion.html#Command-Substitution) result performs word splitting if not enclosed in double quotes. So if your command substitution result contain any whitespace, tab, or newline, the export command will be broken into parts.
- Fix: instead of export PYTHONPATH=$PYTHONPATH: .
- Use export **PYTHONPATH=$PYTHONPATH:"."** instead
> First room works but submission of answer doesn't result in any change