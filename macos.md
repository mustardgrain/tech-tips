## List Listening Ports

```bash
lsof -P -n | grep -i listen
```

* `-P` "inhibits the conversion of port numbers to port names for network files"
* `-n` "inhibits the conversion of network numbers to host names for network files"
* `grep`-ing by `listen` lists only those ports that we're serving

## Install macOS Catalina from Scratch

https://appleinsider.com/articles/19/10/09/how-to-create-a-bootable-macos-catalina-installer-on-a-usb-drive
