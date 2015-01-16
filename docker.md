Will Sargent's Docker Cheat Sheet
---------------------------------

https://github.com/wsargent/docker-cheat-sheet

Installing on Ubuntu (on EC2)
-----------------------------

```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
sudo sh -c "echo deb http://get.docker.com/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
sudo apt-get update
sudo apt-get install -y lxc-docker
```

Allow non-root User to Invoke Docker
------------------------------------

```bash
sudo gpasswd -a $USER docker
sudo service docker restart
newgrp docker
```

Verify Docker is Running 
------------------------

```bash
docker run ubuntu:14.04 /bin/echo 'Hello world'
```

Connecting to a Running Container
---------------------------------

```bash
docker exec -it <container ID> bash
```
