#!/usr/bin/env bash

set -e

IMAGE_NAME="fyp-sdn"

if [[ "$1" == "-b" || "$1" == "--build" ]]; then
  echo "Building $IMAGE_NAME..."
  docker build -t "$IMAGE_NAME" .
fi

echo "Starting $IMAGE_NAME..."

docker run -it --rm \
  --privileged \
  -e DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /lib/modules:/lib/modules \
  "$IMAGE_NAME"
