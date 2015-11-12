Cheat Sheets
============

https://gist.github.com/JoshuaEstes/2627607#file-bash-cheat-sheet-md

Redirect stderr to stdout
=========================

Use the command as follows:

```bash
some-command 2>&1
```

Or:

```bash
some-command > myfile.txt 2>&1
```

Loops
=====

Use `for` combined with `seq` to implement a C-style `for` loop:

```bash
for i in `seq 0 9`; do echo $i; done
```

And you can do fun stuff like this:

```bash
for i in `seq -f "%02g" 99 -1 0`; do echo "$i bottles of beer on the wall"; done
```

Excluding Lines of Output
=========================

Use `awk` to omit the first N rows. For example:

```bash
ls -l | awk '{ if (NR > 1) print }'
```
