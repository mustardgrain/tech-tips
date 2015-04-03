https://gist.github.com/JoshuaEstes/2627607#bash

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
