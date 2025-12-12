#!/bin/bash
TOKEN=$(aws ecr get-login-password --region us-east-1)

kubectl delete secret ecr-secret -n gateway --ignore-not-found
kubectl create secret docker-registry ecr-secret \
          --docker-server=539358810919.dkr.ecr.us-east-1.amazonaws.com \
          --docker-username=AWS \
          --docker-password=$TOKEN \
          -n gateway

TOKEN=$(aws ecr get-login-password --region us-east-1)

kubectl delete secret ecr-secret -n llm --ignore-not-found
kubectl create secret docker-registry ecr-secret \
            --docker-server=539358810919.dkr.ecr.us-east-1.amazonaws.com \
                --docker-username=AWS \
                    --docker-password="$TOKEN" \
                        -n llm

TOKEN=$(aws ecr get-login-password --region us-east-1)

kubectl delete secret ecr-secret -n storage --ignore-not-found
kubectl create secret docker-registry ecr-secret \
            --docker-server=539358810919.dkr.ecr.us-east-1.amazonaws.com \
                --docker-username=AWS \
                    --docker-password="$TOKEN" \
                        -n storage