#!/bin/bash

usage()
{
cat << EOF

usage: $0 <options> <directories>

OPTIONS:
  -h      Show this message
  -t <x>  Timeout for each test (in seconds)

EXAMPLES:
$0 -t 15 unit           # run unit tests with 15 seconds for timeout
$0 -t 5 NRC ocaml       # run NRC and OCaml tests with 5 seconds for timeout
$0 -horn-core-simplify  # run all tests with -horn-core-simplify

EOF
}

DIRS=
TIMELIMIT=60
EXTRAOPTS=


while (( "$#" )); do
  if [[ "$1" == "-h" ]]; then
    usage
    exit -1
  elif [[ "$1" == "-t" ]]; then
    TIMELIMIT=$2
    shift
  elif [[ ${1:0:1} == "-" ]]; then
    EXTRAOPTS="$EXTRAOPTS $1"
  elif [[ $(ls "$1" 2>/dev/null) == "" ]]; then
    echo "empty directory: $1"
    exit -1
  else
    DIRS="$DIRS $1"
  fi

  shift
done

FILES=`find -L $DIRS -name '*.qarmc' -o -name '*.pl' | sort`

# --------------------------------------------------------------------------------

echo "Running tests.."
echo "qarmc$EXTRAOPTS"
echo "timeout: $TIMELIMIT"
echo "directories:$DIRS"
echo

GOOD=0
FAILED=0
TIMEOUT=0
MEMORY=0
BEGIN_TIME=`date +%s`

for file in $FILES; do
  echo -n "$file.. "

  START=`date +%s`
  logfile=$file.`date +%Y.%m.%d.%H.%M`.log
  OUTPUT=`timeout $TIMELIMIT ./qarmc $EXTRAOPTS $file > $logfile 2>&1`
#  timeout $TIMELIMIT ./qarmc $EXTRAOPTS $file > $OUTPUT 2>&1
#  OUTPUT=`timeout $TIMELIMIT ./qarmc $EXTRAOPTS "$file" >& "$file.log"`
#  OUTPUT=`timeout $TIMELIMIT ./qarmc $EXTRAOPTS "$file" 2>&1`
  RES=$?
  END=`date +%s`

  echo $file | grep -q 'false\|fail\|BUG\|error\|unsafe'
  SHOULDPASS=$?

  if [ $RES -eq 124 ] ; then
    echo -n -e "\033[1;33mTIMEOUT\033[0m"
    : $(( ++TIMEOUT ))
#  TODO: reenable when MCC is in place
#  elif ( grep -q "Q'ARMC: program is correct" "$TMP" && grep -A1 "verifying fixpoint..." "$TMP" | grep -q "done." ) ; then
  elif ( ( test $SHOULDPASS == 1 && cat $logfile | grep -q "Q'ARMC: program is correct" ) ||
	 ( test $SHOULDPASS == 0 && cat $logfile| grep -q "Q'ARMC: program is not correct" ) ) ; then
    echo -n -e "\033[1;32mPASSED\033[0m"
    : $(( ++GOOD ))
  elif ( echo $OUTPUT | grep -q "Resource error: insufficient memory" ) ; then
    echo -n -e "\033[1;33mOUT OF MEMORY\033[0m"
    : $(( ++MEMORY ))
  else
    echo -n -e "\033[1;31mFAILED\033[0m"
    : $(( ++FAILED ))
  fi

  TIME=$(( END-START ))
  echo " (in" `printf "%'8.0f" "$TIME"` "sec)"
done

END_TIME=`date +%s`
TIME=$(( END_TIME-BEGIN_TIME ))

NUMBER_OF_TESTS=$((GOOD + FAILED + TIMEOUT + MEMORY))
PERCENT=$((GOOD * 100 / NUMBER_OF_TESTS))

echo
echo "passed ${GOOD} out of ${NUMBER_OF_TESTS} tests (${PERCENT}%)"
echo "timeout: ${TIMEOUT}   out of memory: ${MEMORY}"

echo "Total time:" `printf "%'8.0f" "$TIME"` "seconds"


if [ $GOOD -ne $NUMBER_OF_TESTS ] ; then
  exit 1
fi
