#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import Porter_Stemmer_Python

#setup
sentenceFile = open("sentences.txt","r")
sentences = sentenceFile.readlines()
sentenceFile.close()

stopwordsFile = open("stop_words.txt","r")
stopwords = stopwordsFile.readlines()
stopwordsFile.close()

FV = {} #empty feature vector

#processing
for line in sentences:
	
	#remove punctuation, special characters, and numbers
	line = re.sub('[^A-Za-z ]', ' ', line)
	
	#convert to lower case
	line = line.lower()
	
	#remove stopwords
	for word in stopwords:
		word = re.sub('[^A-Za-z]','',word)
		word1 = '\W' + word + '\W'
		line = re.sub(word1,' ',line)
		word2 = '^' + word + '\W'
		line = re.sub(word2,' ',line)
	
	#remove excess spaces
	line = re.sub('\s+',' ',line)
	line = re.sub('^\s','',line)

	print line