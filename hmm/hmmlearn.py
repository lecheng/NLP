#encoding = utf-8
from collections import Counter
import json
import sys
import math

class Sentence:
	def __init__(self,sentence):
		self.tokens = sentence.split(' ')
		self.words = map(lambda k:k[:-3],self.tokens)
		self.tags = map(lambda k:k[-2:],self.tokens)
		self.length = len(self.words)

	def __str__(self):
		s = ""
		for i in range(0,self.length):
			s = s + self.words[i] + " " + self.tags[i] + "\n"
		return s

	def getWordList(self):
		return self.words

	def getTagList(self):
		return self.tags

	def getLength(self):
		return self.length

#TAGS = ['VA', 'P0', 'SP', 'FF', 'DI', 'CC', 'DD', 'VM', 'AO', 'DA', 'WW', 'VS', 'II', 'ZZ', 'CS', 'DT', 'DR', 'DP', 'PR', 'AQ', 'PP', 'PT', 'PX', 'NC', 'RG', 'PD', 'NP', 'RN', 'PI']
def smooth(tags,dic):
	m = len(tags)
	total = sum(dic.values())
	for tag in tags:
		dic[tag] += 1.0
	return dict(map(lambda (k,v):(k,(v/(m+total))),dic.iteritems()))

def freq(dic):
	total = sum(dic.values())
	return dict(map(lambda (k,v):(k,(v/total)),dic.iteritems()))

def train(path):
	f = open(path,'r')
	emission_dict = {}
	transition_dict = {}
	start_tran_dict = Counter()
	tags = set([])
	total = set([])

	lines = f.readlines()
	for line in lines:
		sentence = Sentence(line.strip())
		wordlist = sentence.getWordList()
		taglist = sentence.getTagList()
		n = sentence.getLength()
		total |= set(wordlist)
		tags |= set(taglist)
		for i in range(-1,n-1):
			if(i==-1):
				key = taglist[i+1]
				start_tran_dict[key] += 1.0
			else:
				prev_tag = taglist[i]
				post_tag = taglist[i+1]
				if prev_tag not in transition_dict:
					transition_dict[prev_tag] = Counter([post_tag])
				else:
					transition_dict[prev_tag][post_tag] += 1.0
			word = wordlist[i+1]
			key = taglist[i+1]
			if key not in emission_dict:
				emission_dict[key] = Counter([word])
			else:
				emission_dict[key][word] += 1.0

	f = open('hmmmodel.txt','w')

	dic = {}
	tags = list(tags)
	dic['tags'] = tags
	dic['words'] = list(total)
	
	dic['transition_dict'] = dict(map(lambda (k,v): (k,smooth(tags,v)),transition_dict.iteritems()))
	dic['start_tran_dict'] = freq(start_tran_dict)
	dic['emission_dict'] = dict(map(lambda (k,v): (k,freq(v)),emission_dict.iteritems()))
	

	f.write(json.dumps(dic)+'\n')

def run():
	
	if len(sys.argv)>1:
		path = sys.argv[1]
	else:
		path = 'hw5-data-corpus/catalan_corpus_train_tagged.txt'
		#path = 'hw5-data-corpus/test.txt'
	train(path)

if __name__ == '__main__':
	run()
	