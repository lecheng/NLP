import json
import math
import sys
from review import Review


params = {
    "textfilepath":"train-text.txt",
    "labelsfilepath":"train-labels.txt"
}

if len(sys.argv)>2:
    params['textfilepath'] = sys.argv[1];
    params['labelsfilepath'] = sys.argv[2];

def init_data(textfile,lablesfile):
    reviews_list = [];
    f1 = open(textfile,'r');
    f2 = open(lablesfile,'r');
    lines1 = f1.readlines();
    lines2 = f2.readlines();
    for i in range(len(lines1)):
        reviews_list += [Review(lines1[i].strip(),lines2[i].strip())]
    return reviews_list;

def fit():
    reviews = init_data(params['textfilepath'], params['labelsfilepath']);
    samples_number = len(reviews);
    training_reviews = reviews;
    save(training_reviews);

def save(reviews):
    corpus = train(reviews)
    f = open('nbmodel.txt', 'w');
    f.write(json.dumps(corpus));
    f.close();

def run():
    reviews = init_data(params['textfilepath'],params['labelsfilepath']);
    # for review in reviews:
    #     tfidf(review, reviews);
    samples_number = len(reviews);
    training_reviews = reviews[0:int(samples_number*0.75)];
    testing_reviews = reviews[int(samples_number*0.75):];
    corpus = train(training_reviews);
    test(corpus,testing_reviews)

def train(training_reviews):
    corpus = {"count": {}, "total_tokens": 0.0, "data": {}};
    total_tokens = set([]);
    label_list = []
    for review in training_reviews:
        tokens = review.tokens;
        label = review.label;
        if label not in label_list:
            label_list += [label]
        total_tokens = total_tokens | set(tokens);
        if label not in corpus['count']:
            corpus['count'][label] = 1.0;
        else:
            corpus['count'][label] += 1;

        for token in tokens:
            if token:
                if token not in corpus['data']:
                    corpus['data'][token] = {"1": 1.0, "0": 1.0, "2": 1.0, "3": 1.0};
                else:
                    if label not in corpus['data'][token]:
                        corpus['data'][token] = {label: 1.0};
                    else:
                        corpus['data'][token][label] += 1;

    corpus['total_tokens'] = len(total_tokens);
    for key, value in corpus['data'].items():
        for label in label_list:
            if label not in value:
                corpus['data'][key][label] = math.log(1 / (corpus['count'][label] + corpus['total_tokens']));
            else:
                v = corpus['data'][key][label];
                corpus['data'][key][label] = math.log((v + 1) / (corpus['count'][label] + corpus['total_tokens']));
    return corpus;

if __name__ == "__main__":
    fit();