#!/bin/bash
# export _JAVA_OPTIONS=-Xmx512m
# cd /home/pi/treebank/stanford-corenlp-full-2018-10-05
cd stanford-corenlp-full-2018-10-05
java -cp "*" -Xmx250m edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,pos,parse -status_port 9000 -port 9000 -timeout 15000 &> /tmp/stanford.log &
