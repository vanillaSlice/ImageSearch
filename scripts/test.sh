#!/usr/bin/env bash

WORKING_DIR=$(dirname "$0")

pytest --cov=$WORKING_DIR/../imagesearch/
