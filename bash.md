Upgrading/Using `bash` on macOS
============

The word on the street is that macOS Catalina will switch to using `zsh`
instead of `bash` as the default shell. If you use `bash` as your default
shell and plan to upgrade to Catalina, this change will probably break
some things for you in weird ways. Regardless of that, though, the version
of `bash` that ships with macOS is very old and should probably be updated
anyway.

One way to get a current version of `bash` on macOS is to install via 
Homebrew:

```
brew install bash
```

However you prefer to get `bash` is up to you. However, the next two steps
are the same regardless -

Now, to _use_ this version of `bash` (or any other shell, for that matter),
you need to add the path of the shell to the list of "allowed" shells:

```
sudo bash -c 'echo /usr/local/bin/bash >> /etc/shells'
```

Next, you need to **ch**ange your **sh**ell to use your version of `bash`:

```
chsh -s /usr/local/bin/bash
```

References:

* https://support.apple.com/en-us/HT208050
* https://linux.die.net/man/5/shells
* https://clubmate.fi/upgrade-to-bash-4-in-mac-os-x/

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

Redirect stdout to stderr
=========================

Use the command as follows:

```bash
echo "Hello, World" 1>&2
echo "Hello, World" >&2
```

The second form is short-hand for the first.

See [here](http://www.kindle-maps.com/blog/how-to-echo-to-stderr.html) for more details.

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
