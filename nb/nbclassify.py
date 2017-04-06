import json
import math
import sys
from review import Review;


def read_model(path):
    f = open(path,'r');
    line = f.read();
    corpus = json.loads(line);
    f.close();
    return corpus;

def read_data(path):
    reviews_list = [];
    f1 = open(path, 'r');
    lines1 = f1.readlines();
    for i in range(len(lines1)):
        reviews_list += [Review(lines1[i].strip(),"")]
    return reviews_list;

def classify(model,tokens):
    label = "";
    max = -sys.maxint-2;
    total_samples = 0.0;
    label_list = []
    for key,value in model['count'].items():
        total_samples += value
        label_list += [key]
    for l in label_list:
        p = math.log(model['count'][l]/total_samples);
        for token in tokens:
            if token:
                if token in model['data']:
                    p += model['data'][token][l];
        if(p > max):
            max = p;
            label = l;
    return label

def run():
    if len(sys.argv)>1:
        filepath = sys.argv[1];
    else:
        filepath = "train-text.txt";
    modelpath = "nbmodel.txt";
    corpus_list = read_model(modelpath);
    reviews = read_data(filepath);
    f = open('nboutput.txt','w');
    for review in reviews:
        result =  classify(corpus_list,review.tokens);
        label = "";
        if result == "0":   label = "truthful positive";
        elif result == "1": label = "deceptive positive";
        elif result == "2": label = "truthful negative";
        else: label = "deceptive negative";
        f.write(review.id + " " + label + "\n");
    f.close();

if __name__ == "__main__":
    run();
