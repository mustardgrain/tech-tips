Determine Version of Installed Package
--------------------------------------

To determine the installed version of a package installed via `apt-get`, run `apt-cache policy <package name>`.

Disable Un-auto-complete
------------------------

To disable the weird un-auto-complete in Ubuntu, comment out the lines about bash completion in `~/.bashrc`.

Password-less sudo
------------------

For password-less `sudo`, change `/etc/sudoers`:

```
%sudo ALL=(ALL:ALL) NOPASSWD: ALL 
```

Using a Different Editor
------------------------

To use other editors (not `nano`) for things like `visudo`:

```bash
sudo update-alternatives --config editor 
```

Fixing Radeon Issues
--------------------

Due to weird lock-ups with the `radeon` driver, I tried the following which seems to have worked.

In a file named `/usr/share/X11/xorg.conf.d/40-monitor.conf`, put the following:

```
Section "Device"
  Identifier  "RadeonHD 7750"
  Option      "Monitor-DVI-0" "DVI screen"
  Option      "NoAccel" "On"
EndSection
Section "Monitor"
  Identifier  "DVI screen"
  Option      "PreferredMode" "2560x1600"
EndSection
```

The key part is the `NoAccel` bit.
