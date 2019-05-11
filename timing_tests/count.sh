#!/usr/bin/env zsh

for file in $(ls -r $1); do


for script in t0 t1 t2 t3 t4 t5 t6 t7 t8 t9 t10 t11 t12 t13 t14; do
    line1="$(head -1 "$script")"
    printf "%-24s" "$line1"
    { time bash "$script"; } |& grep user
    # Since stderr is being piped to grep above, this will confirm
    # there are no errors f

    echo > t13 'declare -i i; i+=1'
    echo >> t13 'i+=1'
