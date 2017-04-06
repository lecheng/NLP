#encoding=utf-8
import json
from collections import Counter
import sys
import math
import operator

reload(sys)  
sys.setdefaultencoding('utf8')

def transfer(d):
	return dict(map(lambda (k,v):(k,Counter(v)),d.iteritems()))

def loadModel():
	f = open('hmmmodel.txt','r')
	jsondata = json.loads(f.read())
	edict = transfer(jsondata['emission_dict'])
	tdict = transfer(jsondata['transition_dict'])
	sdict = Counter(jsondata['start_tran_dict'])
	tags = jsondata['tags']
	words = set(jsondata['words'])
	return edict,tdict,sdict,tags,words

emission_dict, transition_dict, start_tran_dict, tags, words = loadModel()

def viterbi(tokens):
	n = len(tokens)
	m = len(tags)
	k = len(words)
	prob = {}
	backpointer = {}
	prob[1] = {}
	backpointer[1] = {}
	for state in tags:
		a = start_tran_dict[state]
		word = tokens[0]
		if word not in words:
			b = 1.0
		else:
			b = emission_dict[state][word]
		prob[1][state] = a*b
		backpointer[1][state] = 'q0';
	for i in range(2,n+1):
		prob[i] = {}
		backpointer[i] = {}
		word = tokens[i-1]
		for q in tags:
			emission_p = emission_dict[q][word]
			if word not in words:
				b = 1.0
			else:
				if emission_p == 0:
					prob[i][q] = 0.0
					backpointer[i][q] = ''
					continue
				b = emission_p
			flag = ""
			maxp = -1
			for qq in tags:
				if prob[i-1][qq] == 0.0:
					continue
				a = transition_dict[qq][q]
				p = prob[i-1][qq]*a*100
				if maxp <= p:
					flag = qq
					maxp = p
			prob[i][q] = maxp*b
			backpointer[i][q] = flag
	most_q = max(prob[n].iteritems(), key=operator.itemgetter(1))[0]
	res = tokens[n-1]+'/'+most_q
	while(n>1):
		prev = ''
		if most_q != '':
			prev = backpointer[n][most_q]
		res = tokens[n-2] + '/'+ prev + " "+ res
		most_q = prev
		n -= 1
	return res

def run():
	
	if len(sys.argv)>1:
		path = sys.argv[1]
	else:
		path = 'hw5-data-corpus/catalan_corpus_dev_raw.txt'
		#path = 'hw5-data-corpus/debug.txt'
	f = open(path,'r')
	output = open('hmmoutput.txt','w')
	lines = f.readlines()
	for line in lines:
		tokens = line.strip().split(' ')
		res = viterbi(tokens)
		output.write(res+'\n')
	output.close()
	f.close()

if __name__ == '__main__':
	run()
