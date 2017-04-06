def evaluate(resultfile,taggedfile):
	f_result = open(resultfile)
	f_tagged = open(taggedfile)
	lines_r = f_result.readlines()
	lines_t = f_tagged.readlines()
	total = 0.0
	count = 0.0
	for i in range(0,len(lines_r)):
		if lines_r[i]:
			tokens_r = lines_r[i].split(' ')
			tokens_t = lines_t[i].split(' ')
			for j in range(0,len(tokens_r)):
				total += 1
				if tokens_r[j] == tokens_t[j]:	count += 1
	return count/total

if __name__ == '__main__':
	path1 = 'hmmoutput.txt'
	path2 = 'hw5-data-corpus/catalan_corpus_dev_tagged.txt'
	#path2 = 'hw5-data-corpus/test.txt'
	print 'Accuracy: '+ str(evaluate(path1,path2))