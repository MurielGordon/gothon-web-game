## In which we document every single thing we learned with very little organization

## The error messages and their corresponding fixes
> ImportError: cannot import name 'escape' from 'flask'
- Fix: flask.escape has been depricated, use markupsafe.escape instead
- Since flask owns markupsafe you can just add a line to the import section:
- >**from markupsafe import escape**
> First room works but submission of answer doesn't result in any change