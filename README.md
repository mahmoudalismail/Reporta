Reporta
=================

Reporta is your personal reporter. Bringing a conversational interface to news. AlJazeera Media in Context Hackathon. 

Developing on the Server
========================

Make sure you have python-dev installed in order to build numpy. On ubuntu it is:

```
apt-get install python-dev
```

You need to activate the local environment to use the python virtualenv

```
source server/venv/bin/activate
```

Then if it is your first install you should do a pip install to get the requirements

```
pip install -r server/requirements.txt
```

You also need redis installed and running. Install docker first, and then install
redis on docker with.

```
.server/redis/install.sh
```

You also need to download the NLTK files and build the NLP class.

```
python server/nltk/install.py
python server/nltk/build.py
```


Running the server
==================

First run Redis with
```
./server/redis/start_redis.sh
```

Then run the server with

```
python server/server.py
```

Persisting Data in Redis
========================

Sometimes you want the data in Redis to persist between runs, such as if you are
running Reporta in production.

First you need a data Dockerfile, such as the one here:

[https://github.com/lingz/data-docker](Data Docker)

If you don't have this, then download and run it as so

```
./server/redis/install_data.sh
./server/redis/start_data.sh
```

Once the redis-reporta data docker container exists, you can start redis with the persist
command line option

```
./server/redis/start_redis.sh persist
```

Then start the server as normal

```
python server/server.py
```

License
=======

This project is licensed under the MIT license, found in LICENSE.md
