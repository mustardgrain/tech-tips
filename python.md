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
