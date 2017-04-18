import os
import math
import sys
from collections import Counter

def reference_files(path):
    '''
        reference files path generator
    '''
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            yield os.path.join(path,file)

def get_n_gram(N,s):
    '''
        get N-GRAM model of a sentence
    '''
    res = []
    slist = s.strip().split(' ')
    for i in range(len(slist)-N+1):
        l = []
        for j in range(N):
            l += [slist[i+j]]
        res += [" ".join(l)]
    return res

def geometric_mean(nums):
    '''
        calculate geometric mean of a list
    '''
    if len(nums) == 0:    return 0
    return (reduce(lambda x,y:x*y,nums)) ** (1.0/len(nums))

def calculate_bleu(candidate_path,reference_path,N=4):
    '''
        calculate the bleu value
    '''
    with open(candidate_path,'r') as f:
        candidate_lines = f.readlines()
        reference_lines = [open(file,'r').readlines() for file in reference_files(reference_path)]
        total = 0.0
        total2 = 0.0
        for j in range(N):
            plist = []
            for reference_line in reference_lines:
                denominator = 0.0
                numerator = 0.0
                for i in range(len(candidate_lines)):
                    candidate_count = Counter(get_n_gram(j+1,candidate_lines[i]))
                    reference_count = Counter(get_n_gram(j+1,reference_line[i]))
                    temp = sum([min(candidate_count[k],reference_count[k]) for k in reference_count & candidate_count])
                    numerator += temp
                    denominator += sum(candidate_count.values())
                p = numerator / denominator
                # print "numerator:" + str(numerator) + " denominator:" + str(denominator)
                plist += [p]
            total += ((1.0/N)*math.log(geometric_mean(plist)))
        can_word_count_sum = 0.0
        best_match_sum = 0.0
        for i in range(len(candidate_lines)):
            cur_can = len(candidate_lines[i].strip().split(' '))
            # print "cur_can" + str(i) + ": " + str(cur_can)
            can_word_count_sum += cur_can
            interval = 10*can_word_count_sum
            best_match_length = cur_can
            for lines in reference_lines:
                cur_ref = len(lines[i].strip().split(' '))
                # print "cur_ref" + str(i) + ": " + str(cur_ref)
                if abs(cur_ref-cur_can) < interval:
                    interval = abs(cur_ref-cur_can)
                    best_match_length = cur_ref
            # print "best_match_length:" + str(best_match_length)
            best_match_sum += best_match_length
        # print "r:" + str(best_match_sum)
        # print "c:" + str(can_word_count_sum)

        bp = 1.0
        if can_word_count_sum <= best_match_sum:
            bp = math.exp(1.0-(best_match_sum/can_word_count_sum))

        # print "bp:" + str(bp)

        bleu = bp * math.exp(total)
        # print "bleu:" + str(bleu)
        return bleu

if __name__ == '__main__':
    if len(sys.argv) > 2:
        candidate_path = sys.argv[1]
        reference_path = sys.argv[2]
    else:
        candidate_path = 'data/greek/candidate-2.txt'
        reference_path = 'data/greek/reference'
    with open('bleu_out.txt','w') as f:
        f.write(str(calculate_bleu(candidate_path,reference_path)))
        f.close()