#!/bin/bash
# export _JAVA_OPTIONS=-Xmx512m
# cd /home/pi/treebank/stanford-corenlp-full-2018-10-05
cd stanford-corenlp-full-2018-10-05
java -cp "*" -Xmx500m edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos,lemma,parse -status_port 9000 -port 9000 -timeout 30000 &> /tmp/stanford.log &
