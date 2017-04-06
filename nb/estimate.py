predited_file = open("nboutput.txt","r");
labels_file = open("train-labels.txt","r");

lines1 = predited_file.readlines();
lines2 = labels_file.readlines();

tp1 = 0.0;
p_count1 = 0.0;
t_count1 = 0.0;
tp2 = 0.0;
p_count2 = 0.0;
t_count2 = 0.0;
tp3 = 0.0;
p_count3 = 0.0;
t_count3 = 0.0;
tp4 = 0.0;
p_count4 = 0.0;
t_count4 = 0.0;

for i in range(0,len(lines1)):
    predited_label1 = lines1[i].strip().split(" ")[1];
    predited_label2 = lines1[i].strip().split(" ")[2];
    true_label1 = lines2[i].strip().split(" ")[1];
    true_label2 = lines2[i].strip().split(" ")[2];

    #truthful
    if predited_label1=="truthful":
        if predited_label1 == true_label1: tp1 += 1;
        p_count1 += 1;
    if true_label1=="truthful":
        t_count1 += 1;

    #deceptive

    if predited_label1 == "deceptive":
        if predited_label1 == true_label1:
            tp2 += 1;
        p_count2 += 1;
    if true_label1 == "deceptive":
        t_count2 += 1;

    #positive

    if predited_label2 == "positive":
        if predited_label2 == true_label2:
            tp3 += 1;
        p_count3 += 1;
    if true_label2 == "positive":
        t_count3 += 1;
    #negative

    if predited_label2 == "negative":
        if predited_label2 == true_label2:
            tp4 += 1;
        p_count4 += 1;
    if true_label2 == "negative":
        t_count4 += 1;

precision1 = tp1/p_count1;
recall1 = tp1/t_count1;
f1 = 2*precision1*recall1/(precision1+recall1);
print "truthful:"
print "precision:" + str(precision1);
print "recall:" + str(recall1);
print "f1 score:" + str(f1);

precision2 = tp2 / p_count2;
recall2 = tp2 / t_count2;
f2 = 2 * precision2 * recall2 / (precision2 + recall2);
print "deceptive:"
print "precision:" + str(precision2);
print "recall:" + str(recall2);
print "f1 score:" + str(f2);

precision3 = tp3 / p_count3;
recall3 = tp3 / t_count3;
f3 = 2 * precision3 * recall3 / (precision3 + recall3);
print "positive:"
print "precision:" + str(precision3);
print "recall:" + str(recall3);
print "f1 score:" + str(f3);

precision4 = tp4 / p_count4;
recall4 = tp4 / t_count4;
f4 = 2 * precision4 * recall4 / (precision4 + recall4);
print "negative:"
print "precision:" + str(precision4);
print "recall:" + str(recall4);
print "f1 score:" + str(f4);

print "avg f1 score:" + str((f1+f2+f3+f4)/4);