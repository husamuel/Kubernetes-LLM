#!/bin/bash
aws ecr get-login-password --region us-east-1 | \
kubectl delete secret ecr-secret --ignore-not-found

aws ecr get-login-password --region us-east-1 | \
kubectl create secret docker-registry ecr-secret \
  --docker-server=539358810919.dkr.ecr.us-east-1.amazonaws.com \
  --docker-username=AWS \
  --docker-password-stdin
