#!/bin/bash
docker run -it --rm --link redis:redis dockerfile/redis bash -c 'redis-cli -h redis'
