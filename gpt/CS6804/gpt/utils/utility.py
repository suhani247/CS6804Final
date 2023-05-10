labels = []
classified = []

with open("../../actual.txt") as f:
    labels = f.readlines()

with open("../../classified.txt") as f:
    classified = f.readlines()

labels = [x.strip() for x in labels]
classified = [x.strip() for x in classified]

print(len(labels))
print(len(classified)*25)

tp = 0
tn = 0
fp = 0
fn = 0
for i in range(len(classified)):
    actual = labels[i]
    predicted = classified[i]
    if(actual == predicted):
        if(actual == "1"):
            tp+=1
        else:
            tn += 1
    else:
        if(actual == "1"):
            fn+=1
        else:
            fp+=1

accuracy = (tp+tn)/(tp+tn+fp+fn)
recall = tp/(tp+fn)
precision = tp/(tp+fp)

print(accuracy, precision, recall)

