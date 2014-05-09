pip
---

If, while using `pip` you see an error like this:

```bash
clang: error: unknown argument: '-mno-fused-madd' [-Wunused-command-line-argument-hard-error-in-future]

clang: note: this will be a hard error (cannot be downgraded to a warning) in the future

error: command 'cc' failed with exit status 1
```

Try setting these environment variables first, then try again:

```bash
export CFLAGS=-Qunused-arguments
export CPPFLAGS=-Qunused-arguments
```

See: http://stackoverflow.com/a/22322645

Location of Modules
-------------------

The location of Python modules depends on a number of things (I assume). 

For example, for Python 2.7 on Ubuntu:

1. `/usr/lib/python2.7`
2. `/usr/local/lib/python2.7/dist-package`
3. `/usr/local/lib/python2.7/site-package`
4. `$HOME/.virtualenvs/<env>/lib/python2.7/site-packages`

In case 1, these are modules installed by `apt-get` (or equivalent). In case 2, these are modules installed via `pip` or `easy_install`. Case 3 is unknown. Case 4 is for using `pip` in a `virtualenv`.
