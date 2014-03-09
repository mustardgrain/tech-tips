Determine Version of Installed Package
====

To determine the installed version of a package installed via `apt-get`, run `apt-cache policy <package name>`.

Disable Un-auto-complete
====

To disable the weird un-auto-complete in Ubuntu, comment out the lines about bash completion in `~/.bashrc`.

Loops in Bash
====

Use for combined with seq to implement a C-style for loop:

    $ for i in `seq 0 9`; do echo $i; done

And you can do fun stuff like this:

    $ for i in `seq -f "%02g" 99 -1 0`; do echo "$i bottles of beer on the wall"; done

Excluding Lines of Output
====

Use awk to omit the first N rows. For example:

    ls -l | awk '{ if (NR > 1) print }'

Password-less sudo
====

For password-less sudo, change `/etc/sudoers`:

    %sudo ALL=(ALL:ALL) NOPASSWD: ALL 

To use other editors (not nano) for things like visudo:

    sudo update-alternatives --config editor 
