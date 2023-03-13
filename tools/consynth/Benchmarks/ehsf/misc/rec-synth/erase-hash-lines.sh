#!/bin/sh

sed '/^#/d' $1 > $1.bak
mv $1.bak $1