Search Queries
--------------

To search for an exact phrase in the logging message run the search:
```message:”${searchstring}”```

To search for multiple phrases in the logging message run the search:
```message:(”${searchstring1}” AND ${searchstring2})```

To do an `or` search in the logging message run the search:
```message:(”${searchstring1}” OR ${searchstring2})```

If there are phrases you do not want included in the search add the following to your search `-“${string}”`
