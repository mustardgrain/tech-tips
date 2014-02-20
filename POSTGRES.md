Initial Setup
=============

The first step is installing PostgreSQL, create the redlaser database, and install the PostGIS extensions.

```bash
# Install Postgres
sudo apt-get update --fix-missing
sudo apt-get install -y postgresql-9.1
```

Next, you'll want to configure Postgres to be available to outside hosts:

```bash
sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/9.1/main/postgresql.conf
sudo sed -i "s/127.0.0.1\/32/0.0.0.0\/0/g" /etc/postgresql/9.1/main/pg_hba.conf
sudo service postgresql restart
```bash
