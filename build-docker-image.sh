#!/usr/bin/env bash

# Override this to use e.g. podman instead of docker:
DOCKER="${DOCKER:=docker}"

export DOCKER_IMAGE="${DOCKER_IMAGE:=vl-convert_arm64_test}"

"${DOCKER}" build . -t "${DOCKER_IMAGE}"