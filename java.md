jmap
----

Here's a gentle introduction:

http://prefetch.net/blog/index.php/2007/10/27/summarizing-java-heap-utilization-with-jmap/

When you do this:

```bash
jmap -heap `pgrep java`
```

Do you get errors like this:

```
Attaching to process ID 6377, please wait...
Error attaching to process: sun.jvm.hotspot.debugger.DebuggerException: Can't attach to the process
```

Then do this:

```bash
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
```

JMX
---

Getting JMX to work on a firewalled system is crazy. System properties for an unprotected system:

    com.sun.management.jmxremote (sometimes wants to be set to "true"?)
    com.sun.management.jmxremote.authenticate=false
    com.sun.management.jmxremote.ssl=false
    com.sun.management.jmxremote.port=<port used by client>
    java.rmi.server.hostname=<public host name of server>

For EC2 we can set java.rmi.server.hostname to:

    `wget -q -O - http://169.254.169.254/latest/meta-data/public-hostname`

The server will assign a secondary, ephemeral port that the client also needs to have access. I'm not sure how to get this port off of a system without netstat and guesswork.

The `jmxterm` tool is great for probing server applications via JMX from the command line.

Installing the Oracle JDK Under Ubuntu
--------------------------------------

To install the Oracle JDK under Ubuntu, do the following:

```bash
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java7-installer
sudo update-alternatives --config java
```
