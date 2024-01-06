#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

LTL=$(/gensys/tools/raboniel/opt/syfco/syfco -f ltl -q double -m fully $1)
INS=$(/gensys/tools/raboniel/opt/syfco/syfco -f ltl --print-input-signals $1)
OUTS=$(/gensys/tools/raboniel/opt/syfco/syfco -f ltl --print-output-signals $1)

echo $DIR/strix -f "$LTL" --ins "$INS" --outs "$OUTS" ${@:2}
LD_LIBRARY_PATH=$DIR $DIR/strix -f "$LTL" --ins "$INS" --outs "$OUTS" ${@:2}
tools/raboniel/opt/syfco/syfco