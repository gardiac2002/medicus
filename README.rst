
Medicus
=======


Requirements
------------

* Python3.5 or higher
* Psycopg2 (PostgreSQL driver)
* Python Development Libs
* PostgreSQL
* Git
* Vim

Installation::

    >>> sudo apt-get update
    >>> sudo apt-get -y install python3-pip libxml2-dev libxslt1-dev python-dev zlib1g-dev python3-lxml
    >>> sudo apt install git postgresql vim python-psycopg2

If you host a Postgres database you should as well create a database::

   >>> sudo -u postgres psql

   # Now we add a password for the user
   >>> \password postgres
   <ask_your_project_lead_for_the_password>

   >>> CREATE DATABASE medicus WITH OWNER postgres ENCODING 'utf-8';
   >>> CREATE DATABASE test_medicus WITH OWNER postgres ENCODING 'utf-8';
   >>> \q

   # Usually Postgres does not allow connection from
   # remote computers. Configure the following file.
   >>> sudo vim /etc/postgresql/9.6/main/postgresql.conf

   # change the configuration in the file
   # by the way, you can search in vim with /
   >>> listen_addresses = '*'

   # restart postgres
   >>> sudo service postgresql restart


Installation
------------
Follow those installation steps::

    >>> 
    >>> virtualenv <your_envs_location>/medicus --python=python3.5
    >>> source <your_envs_location>/medicus/bin/activate
    
    >>> # Go to the medicus directory
    >>> (medicus) cd .../medicus

    >>> # Check if you are in the correct directory
    >>> (medicus) pwd
    .../medicus 

    >>> (medicus) pip install -r requirements/requirements-dev.txt

    # Test your installation in the browser (http://127.0.0.1:8000/)
    >>> (medicus) python manage.py runserver --settings medicus.settings.development


Testing
-------
Now, let's check if your tests are running::

    # Go to the root directory of your project
    >>> (medicus) pwd
    .../medicus

    >>> python -m pytest


Debugging
---------
Now, let's check if you can log into your local shell::

    # Go to the root directory of your project
    >>> (medicus) pwd
    .../medicus

    >>> python manage.py shell
    >>> In [1]: import medicus
