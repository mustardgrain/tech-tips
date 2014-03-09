Stopping Hadoop
---------------

On a system with the Hadoop binaries in the `$PATH`, run this:

```bash
stop-all.sh
```

For good measure I throw in a `sleep 10` afterward.

Clearing Out Temporary Files
----------------------------

After stopping the server, run this (assuming `$HADOOP_HOME` is set):

```bash
rm -rf /tmp/hadoop* \
       /tmp/Jetty* \
       $HADOOP_HOME/logs/*
```

Formatting HDFS
---------------

Assuming HDFS is stopped, run this:

```bash
hadoop namenode -format
```

Killing a Single Hadoop Job
---------------------------

Here's a little lazy script that I use to delete a job:

```bash
hadoop job -list | grep "job_" | awk '{ print $1 }' | xargs hadoop job -kill
```
