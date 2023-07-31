#!/bin/bash
set -xe
sudo docker pull tomerkul/mysql:latest
sudo docker pull tomerkul/myflask:latest


sudo docker-compose -f /home/ec2-user/docker-compose.yaml up -d

