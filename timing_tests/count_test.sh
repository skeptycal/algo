#!/usr/bin/env zsh

# To focus exclusively on the performance of each type of increment
# statement, we should exclude bash performing while loops from the
# performance measure. So, let's time individual scripts that
# increment $i in their own unique way.
# https://askubuntu.com/questions/385528/how-to-increment-a-variable-in-bash

#? Results:
#   Expr is 1000x slower at least ... unbelievable
#   functions with the word 'let' are 50 - 120% slower

#   t0 and t1 with $ were next slowest (~20% slower than pack)

#   fucntions with (( = )) were slowest next (~5 to 10%)
#
#   ((i++)) is ~0 - 10% slower than ((++i))
#   ((++i)) is ~ even with 'i' WITH declare
#   ((++i)) is ~10 - 50% slower than 'i' functions (no declare)

#?  And the winner is ...
#?  t13: 'i+=1' with no declare (0 - 5% faster than t12: 'i=i+1')
#?  the slowest (barring the train wreck t14)
#?      is t6 'let "i=i+1"' ... 2x - 2.5x slower

# lessons:  avoid (( )) ... don't use 'let' ...
#           don't declare things ... don't use expr at all!!!!




# Declare i as an integer for tests 12 and 13.
# echo > t12 'declare -i i; i=i+1'
# echo > t13 'declare -i i; i+=1'
# Set i for test 14.
# echo > t14 'i=0; i=$(expr $i + 1)'

# x = 100000
x=4000
while ((x--)); do
    echo >> t6 'let "i=i+1"'
    echo >> t13 'i+=1'
done

for script in t6 t13; do
    line1="$(head -1 "$script")"
    printf "%-24s" "$line1"
    { time bash "$script"; } |& grep user
    # Since stderr is being piped to grep above, this will confirm
    # there are no errors from running the command:
    eval "$line1"
    rm "$script"
done

# while ((x--)); do
    # echo >> t0 'i=$((i+1))'
    # echo >> t1 'i=$((i++))'
    # echo >> t2 '((i=i+1))'
    # echo >> t3 '((i+=1))'
    # echo >> t4 '((i++))'
    # echo >> t5 '((++i))'
    # echo >> t6 'let "i=i+1"'
    # echo >> t7 'let "i+=1"'
    # echo >> t8 'let "i++"'
    # echo >> t9 'let i=i+1'
    # echo >> t10 'let i+=1'
    # echo >> t11 'let i++'
    # echo >> t12 'i=i+1'
    # echo >> t13 'i+=1'
    # echo >> t14 'i=$(expr $i + 1)' # omg this one is horrible!! forking a new shell??
# done
