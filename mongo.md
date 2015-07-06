Pretty-Printing
---------------

Add the following line to your `$HOME/.mongorc.js` file to enable pretty print globally by default:

```
DBQuery.prototype._prettyShell = true
```

Searching in Mongo
---------------

To search for a substring in a particular field run the following in the Mongo shell:

```
db.xxxxxx.findOne({"field" : {$regex : ".*string.*"}});
```

Running via Brew (Mac OS X)
---------------------------

From the output of Homebrew:

```bash
To have launchd start mongodb at login:
    ln -sfv /usr/local/opt/mongodb/*.plist ~/Library/LaunchAgents
Then to load mongodb now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist
Or, if you don't want/need launchctl, you can just run:
    mongod --config /usr/local/etc/mongod.conf
```

Comparing Two Fields in a Document
----------------------------------

If the _where_ clause is the comparison, you can use a nested JavaScript _comparator_ function:

```
db.fr_sessions.find("this.created > this.end_date")
```
