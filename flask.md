By default flask deploys the server on 127.0.0.1 as opposed to 0.0.0.0, so in order to make it visible to machines other than what it runs on, in the command to run flask do this:
```
app.run(host='0.0.0.0')
```
