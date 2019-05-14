#!/usr/bin/env ksh
# Changed from <ksh> to <zsh>
#
# SCRIPT: 12_ways_to_parse.ksh.ksh
#
#
# REV: 1.2.A
#
# PURPOSE:  This script shows the different ways of reading
#       a file line by line.  Again there is not just one way
#       to read a file line by line and some are faster than
#       others and some are more intuitive than others.
#
# REV LIST:
#
#       03/15/2002 - Randy Michael
#       Set each of the while loops up as functions and the timing
#       of each function to see which one is the fastest.
#
#######################################################################
#
#       NOTE: To output the timing to a file use the following syntax:
#
#          12_ways_to_parse.ksh file_to_process  > output_file_name 2>&1
#
#       The actaul timing data is sent to standard error, file
#       descriptor (2), and the function name header is sent
#       to standard output, file descriptor (1).
#
##################################################################
#
# set -n  # Uncomment to check command syntax without any execution
# set -x  # Uncomment to debug this script
#

FILENAME="$1"
TIMEFILE="/tmp/loopfile.out"
THIS_SCRIPT=$(basename $0)

# a few colors ...
        MAIN="\e[38;5;229m"
        WARN="\e[38;5;203m"
        COOL="\e[38;5;38m"
        GO="\e[38;5;28m"
        CHERRY="\e[38;5;124m"
        CANARY="\e[38;5;226m"
        ATTN="\e[38;5;178m"
        PURPLE="\e[38;5;93m"
        RESET="\e[0m"
#######################################################################
#
# funcction to equalize echo syntax
# function echo
# {
#     # This makes echo more consistent and portable
#     if [ "$#" -gt 0 ]; then
#         printf %s "$1"
#         shift
#     fi
#     if [ "$#" -gt 0 ]; then
#         printf ' %s' "$@"
#     fi
#     printf '\n'
# }
function ce
{
    if [ "$#" -gt 0 ]; then
        printf "$MAIN%b" "$1"
        shift
    fi
    if [ "$#" -gt 0 ]; then
        printf " %b" "$@"
        printf "%b" $RESET
    fi
    printf '\n'
}
function echoit
{
if [ "$#" -gt 0 ]; then
        printf "$ATTN%b" "$1"
        shift
    fi
    if [ "$#" -gt 0 ]; then
        printf " %b" "$@"
        printf "%b" $RESET
    fi
    printf '\n'
}
######################################
function usage
{
ce "\nUSAGE: $THIS_SCRIPT  file_to_process\n"
echoit "OR - To send the output to a file use: "
echoit "\n$THIS_SCRIPT  file_to_process  > output_file_name 2>&1 \n"
exit 1
}
######################################
function while_read_LINE
{
cat $FILENAME | while read LINE
do
        echoit "$LINE"
        :
done
}
######################################
function while_read_LINE_bottom
{
while read LINE
do
        echoit "$LINE"
        :

done <$FILENAME
}
######################################
function while_line_LINE_bottom
{
while line LINE
do
        echoit $LINE
        :
done
}
######################################
function cat_while_LINE_line
{
cat $FILENAME | while LINE=$(line)
do
        echoit "$LINE"
        :
done
}
######################################
function while_line_LINE
{
cat $FILENAME | while line LINE
do
        echoit "$LINE"
        :
done
}
######################################
function while_LINE_line_bottom
{
while LINE=$(line)
do
        echoit "$LINE"
        :

done
} <$FILENAME
######################################
function while_LINE_line_cmdsub2
{
cat $FILENAME | while LINE=$(line)
do
        echoit "$LINE"
        :
done
}
######################################
function while_LINE_line_bottom_cmdsub2
{
while LINE=$(line)
do
        echoit "$LINE"
        :

done <$FILENAME
}
######################################
function while_read_LINE_FD
{
exec 3<&0
exec 0<$FILENAME
while read LINE
do
        echoit "$LINE"
        :
done
exec 0<&3
}
######################################
function while_LINE_line_FD
{
exec 3<&0
exec 0<$FILENAME
while LINE=$(line)
do
        echoit "$LINE"
        :
done
exec 0<&3
}
######################################
function while_LINE_line_cmdsub2_FD
{
exec 3<&0
exec 0<$FILENAME
while LINE=$(line)
do
        print "$LINE"
        :
done
exec 0<&3
}
######################################
function while_line_LINE_FD
{
exec 3<&0
exec 0<$FILENAME

while line LINE
do
        echoit "$LINE"
        :
done

exec 0<&3
}
######################################
########### START OF MAIN ############
######################################
# FILENAME="$1"
# TIMEFILE="/tmp/loopfile.out"
# # >$TIMEFILE
# THIS_SCRIPT=$(basename $0)


>$TIMEFILE
ce "############################################################"
ce "Params (\$@) : $@"
ce "Filename: (\$1): $FILENAME"
ce "Timefile: (default /tmp/loopfile.out): $TIMEFILE"
ce "Script (basename \$0): $THIS_SCRIPT"
ce "############################################################"
ce ''

# Test the Input

# Looking for exactly one parameter
(( $# == 1 )) || usage

# Does the file exist as a regular file?
[[ -f $1 ]] || usage

ce "\nStarting File Processing of each Method\n"

ce "Method 1:"
echo "\nfunction while_read_LINE\n" >> $TIMEFILE
echoit "function while_read_LINE"
time while_read_LINE >>  $TIMEFILE
ce "\nMethod 2:"
echo "\nfunction while_read_LINE_bottom\n" >> $TIMEFILE
echoit "function while_read_LINE_bottom"
time while_read_LINE_bottom >> $TIMEFILE
ce "\nMethod 3:"
echo "\nfunction while_line_LINE_bottom\n" >> $TIMEFILE
echoit "function while_line_LINE_bottom"
time while_line_LINE_bottom >> $TIMEFILE < $FILENAME
ce "\nMethod 4:"
echo "\nfunction cat_while_LINE_line\n" >> $TIMEFILE
echoit "function cat_while_LINE_line"
time cat_while_LINE_line >> $TIMEFILE
ce "\nMethod 5:"
echo "\nfunction while_line_LINE\n" >> $TIMEFILE
echoit "function while_line_LINE"
time while_line_LINE >> $TIMEFILE
ce "\nMethod 6:"
echo "\nfunction while_LINE_line_bottom\n" >> $TIMEFILE
echoit "function while_LINE_line_bottom"
time while_LINE_line_bottom >> $TIMEFILE
ce "\nMethod 7:"
echo "\nfunction while_LINE_line_cmdsub2\n" >> $TIMEFILE
echoit "function while_LINE_line_cmdsub2"
time while_LINE_line_cmdsub2 >> $TIMEFILE
ce "\nMethod 8:"
echo "\nfunction while_LINE_line_bottom_cmdsub2\n" >> $TIMEFILE
echoit "function while_LINE_line_bottom_cmdsub2"
time while_LINE_line_bottom_cmdsub2 >> $TIMEFILE
ce "\nMethod 9:"
echo "\nfunction while_read_LINE_FD\n" >> $TIMEFILE
echoit "function while_read_LINE_FD"
time while_read_LINE_FD >> $TIMEFILE
ce "\nMethod 10:"
echo "\nfunction while_LINE_line_FD\n" >> $TIMEFILE
echoit "function while_LINE_line_FD"
time while_LINE_line_FD >> $TIMEFILE
ce "\nMethod 11:"
echo "\nfunction while_LINE_line_cmdsub2_FD\n" >> $TIMEFILE
echoit "function while_LINE_line_cmdsub2_FD"
time while_LINE_line_cmdsub2_FD >> $TIMEFILE
ce "\nMethod 12:"
echo "\nfunction while_line_LINE_FD\n" >> $TIMEFILE
echoit "function while_line_LINE_FD"
time while_line_LINE_FD >> $TIMEFILE
