#!/bin/bash

# We want to build a new image with name "code_example".
# The input argument must be a git sha value to match with the
# right code while running.
# Use file from the root directory (we are not in the root of the repo
# at the moment)
docker build --tag=code_example \
    --build-arg GITHUB_SHA_ARG=123456 \
    --file="../../Dockerfile" \
    ../..
