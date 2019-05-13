#!/usr/bin/env bash

here() {
    # for macOS, requires GNU coreutils - 'brew install coreutils'
    # grealpath can be changed to realpath
    if [[ $(realpath "$1" &>/dev/null) ]]; then
        echo "$(realpath "$1" &>/dev/null)"
    else
        echo "$([[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}")"
    fi
}

echo here $0
