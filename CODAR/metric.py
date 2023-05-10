with open("actual.txt") as file:
    actual = [line.strip() for line in file]

with open("classified_gpt3.txt") as file:
    classified = [line.strip() for line in file]

with open("exp2_classified_gpt3.txt") as file:
    classified2 = [line.strip() for line in file]

tp = 0
tn = 0
fp = 0
fn = 0
for i in range(len(classified)):
    if actual[i] == classified[i]:
        if classified[i] == '0':
            tn+=1
        else:
            tp+=1
    else:
        if actual[i] == '1' and classified[i] == '0':
            fn+=1
        else:
            fp+=1

precision = tp/(tp+fp)
recall = tp/(tp+fn)
f1 = 2*(precision*recall)/(precision+recall)

print("precision: " + str(precision))
print("recall: " + str(recall))
print("f1: " + str(f1))

tp = 0
tn = 0
fp = 0
fn = 0

for i in range(len(classified2)):
    if actual[i] == classified2[i]:
        if classified2[i] == '0':
            tn+=1
        else:
            tp+=1
    else:
        if actual[i] == '1' and classified2[i] == '0':
            fn+=1
        else:
            fp+=1


precision = tp/(tp+fp)
recall = tp/(tp+fn)
f1 = 2*(precision*recall)/(precision+recall)

print('Experiment 2')
print("precision: " + str(precision))
print("recall: " + str(recall))
print("f1: " + str(f1))