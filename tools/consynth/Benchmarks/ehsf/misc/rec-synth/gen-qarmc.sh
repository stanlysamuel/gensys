#!/bin/sh

~/research/code/qarmc5/armc_frontend.osx $1
~/research/code/qarmc5/summ2q.osx $1.armc > $1.qarmc
rm $1.cfg.dot