Disable Un-auto-complete
====

To disable the weird un-auto-complete in Ubuntu, comment out the lines about bash completion in ~/.bashrc

Loops in Bash
====

Use for combined with seq to implement a C-style for loop:

    $ for i in `seq 0 9`; do echo $i; done

And you can do fun stuff like this:

    $ for i in `seq -f "%02g" 99 -1 0`; do echo "$i bottles of beer on the wall"; done

Excluding Lines of Output
====

Use awk to omit the first N rows. For example:

    ls -l | awk '{ if (NR > 1) print }'

Password-less sudo
====

For password-less sudo, change /etc/sudoers:

    %sudo ALL=(ALL:ALL) NOPASSWD: ALL 

To use other editors (not nano) for things like visudo:

    sudo update-alternatives --config editor 

SSH
====

Make a proxy to another server:

    ssh -f -N -L <your port>:<remote host from remote>:<remote port from remote> <user>@<remote host> 

For example, to connect from my laptop/desktop to a server foo:

    ssh -f -N -L 33060:Stagedb04b:3306 ktrue@foo 

Or to connect to an EC2 instance running tinyproxy:

    ssh -f -N -L 7777:localhost:8888 -i $EC2_RSAKEYPAIR ubuntu@ec2-107-20-2-131.compute-1.amazonaws.com 

Or to connect to an EMR cluster:

    ssh -N -L 9100:localhost:9100 -L 9101:localhost:9101 hadoop@ec2-23-23-34-233.compute-1.amazonaws.com
