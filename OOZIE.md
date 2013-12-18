Prerequisites
====

You need to update your Hadoop cluster's core-site.xml file with properties similar to this:

    <property>
      <name>hadoop.proxyuser.<your user ID>.hosts</name> 
      <value>localhost</value>
    </property>
    <property>
      <name>hadoop.proxyuser.<your user ID>.groups</name>
      <value><your primary group></value>
    </property>

You will also need to have access to the MySQL JDBC driver JAR. Developers can find this at a location similar to $HOME/.m2/repository/mysql/mysql-connector-java/5.1.25/mysql-connector-java-5.1.25.jar.

Building
====

These instructions assume you're downloading and building Oozie from its source. Using the following instructions we've built a binary distribution which is hosted at https://mustard-grain-dev.s3.amazonaws.com/bin/oozie-4.0.0-bin.tar.gz.
Installation of Oozie appears to be a major pain. I have figured out my progress so far from these two sources:

* http://oozie.apache.org/docs/4.0.0/DG_QuickStart.html
* http://practicalcloudcomputing.com/post/26337621577/installing-and-running-apache-oozie-3-2-x-and-possibly

The latter actually being more useful than the official documentation.

    #!/bin/bash -e

    OOZIE_VERSION=4.0.0
    OOZIE_URL=http://archive.apache.org/dist/oozie/$OOZIE_VERSION/oozie-$OOZIE_VERSION.tar.gz
    EXTJS_URL=http://extjs.com/deploy/ext-2.2.zip

    curl -L -s $OOZIE_URL | tar xz

    cd oozie-$OOZIE_VERSION
    ./bin/mkdistro.sh -DskipTests -DjavaVersion=1.7
    cd distro/target/oozie-$OOZIE_VERSION-distro/oozie-$OOZIE_VERSION

    mkdir libext
    cd libext
    cp ../../../../../hadooplibs/hadoop-1/target/hadooplibs/hadooplib-1.1.1.oozie-$OOZIE_VERSION/*.jar .
    wget $EXTJS_URL 
    cd ../..
    tar czf oozie-$OOZIE_VERSION-bin.tar.gz oozie-4.0.0

    echo "Oozie $OOZIE_VERSION binary distribution has been built at `pwd`/oozie-$OOZIE_VERSION-bin.tar.gz"

Installing
====

Installation is easier from the pre-packaged binary.

    wget https://mustard-grain-dev.s3.amazonaws.com/bin/oozie-4.0.0-bin.tar.gz
    tar xzf oozie-4.0.0-bin.tar.gz
    rm oozie-4.0.0-bin.tar.gz
    cd oozie-4.0.0
 
    # Copy shared directory to HDFS, but first updating Hive libraries with our versions
    hadoop fs -rmr share
    tar xzf oozie-sharelib-4.0.0.tar.gz
    rm share/lib/hive/*
    cp $HOME/bin/hive/lib/*.jar share/lib/hive
    cp $HOME/.m2/repository/mysql/mysql-connector-java/5.1.25/mysql-connector-java-5.1.25.jar share/lib/hive
    hadoop fs -put share share
    rm -rf share

    ./bin/oozie-setup.sh prepare-war
    ./bin/ooziedb.sh create -run

Running
====

Running is easy.

    ./bin/oozied.sh run

You should be able to view the Oozie web console at http://localhost:11000/oozie.

Submitting Jobs via the REST API
====

Take a look at these two sources:

* http://blog.cloudera.com/blog/2013/06/how-to-use-the-apache-oozie-rest-api/
* http://oozie.apache.org/docs/4.0.0/WebServicesAPI.html#Proxy_Hive_Job_Submission
