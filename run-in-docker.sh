#!/usr/bin/env bash

set -euo pipefail

# Override this to use e.g. podman instead of docker:
DOCKER="${DOCKER:=docker}"

export DOCKER_IMAGE="${DOCKER_IMAGE:=vl-convert_arm64_test}"

cd "$(dirname $0)"
./build-docker-image.sh

time "${DOCKER}" run --rm \
  -v "$(pwd)"/vega-lite:/vega-lite:rw \
  "${DOCKER_IMAGE}"