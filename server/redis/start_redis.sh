#!/bin/bash
if [[ $1 = "persist" ]]; then
  docker run -d -p 6379:6379 -v redis-reporta:/data --name redis dockerfile/redis
else
  docker run -d --name redis -p 6379:6379 dockerfile/redis
fi
