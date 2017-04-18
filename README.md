# NLP
This is a course-based project including two models and a final project.

## nb
Training Naive Bayes model to classify hotel reviews.
```
python nblearn.py train-text.txt train-label.txt
python nbclassify.py train-text.txt
```
note: nblearn.py and nbclassify.py should be in the same folder.
## hmm
Training Hidden Markov Model to do part-of-speech given training set.
```
python hmmlearn.py hw5-data-corpus/catalan_corpus_train_tagged.txt
python hmmdecode.py hw5-data-corpus/catalan_corpus_dev_raw.txt
```
note: hmmlearn.py and hmmdecode.py should be in the same folder.
## bleu
Calculate the bleu value to evaluate machine translation
```
python calculatebleu.py path/to/candidate.txt path/to/reference
```
note: the first parameter is a simple file, but the second parameter is the folder path containing all the reference files.
