#!/usr/bin/env bash
# prevent resource leaks ...
# http://redsymbol.net/articles/bash-exit-traps/
scratch=$(mktemp -d -t tmp.XXXXXXXXXX)
function finish {
  rm -rf "$scratch"
}
trap finish EXIT
