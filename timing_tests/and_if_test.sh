#!/usr/bin/env zsh

# To focus exclusively on the performance of each type of increment
# statement, we should exclude bash performing while loops from the
# performance measure. So, let's time individual scripts that
# increment $i in their own unique way.
# https://askubuntu.com/questions/385528/how-to-increment-a-variable-in-bash


export MAIN="\e[38;5;229m"

# MAIN echo
export t0() {
    i=5
    color_code="$MAIN"
    if [ "$i" -gt 0 ]; then
        x=1
    fi
}
# red WARN echo
export t1() {
    i=5
    color_code="$MAIN"
    [[ "$i" -gt 0 ]] && x=1
}

# x = 100000
x=5000
while ((x--)); do
    echo >> t0 't0'
    echo >> t1 't1'
done

for script in t0 t1; do
    line1="$(head -1 "$script")"
    printf "%-24s" "$line1"
    { time bash "$script"; } |& grep user
    # Since stderr is being piped to grep above, this will confirm
    # there are no errors from running the command:
    eval "$line1"
    rm "$script"
done
