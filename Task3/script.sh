#!/bin/sh

docker pull alpine

docker run --name=task_3            \
              --restart=always      \
              --detach              \
              --publish=144:144/udp \
              alpine
