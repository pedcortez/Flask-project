#!/bin/bash
docker build -t todo-app:latest .
docker build -t todo-mysql:latest ./database .