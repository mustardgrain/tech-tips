Generate Eclipse Project
========================

```bash
mvn eclipse:clean eclipse:eclipse -DdownloadSources=true $*
```

Maven Plugin Help
=================

To see the help (configuration parameters, etc.) for a given plugin, use this command:

```bash
mvn help:describe \
    -DgroupId=<group ID> \
    -DartifactId=<artifact ID> \
    -Dversion=<version> \
    -Dfull=true
```

For example, for Jetty:

```bash
mvn help:describe \
    -DgroupId=org.mortbay.jetty \
    -DartifactId=maven-jetty-plugin \
    -Dversion=6.1.16 \
    -Dfull=true
```
