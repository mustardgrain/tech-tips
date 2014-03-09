Determine Version of Installed Package
====

To determine the installed version of a package installed via `apt-get`, run `apt-cache policy <package name>`.

Disable Un-auto-complete
====

To disable the weird un-auto-complete in Ubuntu, comment out the lines about bash completion in `~/.bashrc`.

Password-less sudo
====

For password-less sudo, change `/etc/sudoers`:

```
%sudo ALL=(ALL:ALL) NOPASSWD: ALL 
```

Using a Different Editor
========================

To use other editors (not nano) for things like visudo:

```bash
sudo update-alternatives --config editor 
```
