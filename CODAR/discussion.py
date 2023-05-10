import pickle

with open("actual.txt") as file:
    actual = [line.strip() for line in file]

with open("classified_gpt3.txt") as file:
    classified = [line.strip() for line in file]

with open("exp2_classified_gpt3.txt") as file:
    classified2 = [line.strip() for line in file]

file = open("classified.txt", "a")
tweets = pickle.load(open("twitter_data.pkl", "rb"))

#
# for i in range(len(classified)):
#     if actual[i] != classified[i] and actual[i]=='1':
#         print("Tweet: " + tweets[i]['text'])
#
#
# print('Experiment 2')
# for i in range(len(classified2)):
#     if actual[i] == classified2[i] and classified2[i]!=classified[i]:
#         print('Tweet: ' + tweets[i]['text'])

# print('Experiment 3')
# for i in range(len(classified)):
#     if actual[i] == classified[i] and actual[i]=='1':
#         print("Tweet: " + tweets[i]['text'])

print('Experiment 4')
for i in range(len(classified)):
    if classified2[i] == classified[i] and classified[i] == '0' and actual[i]=='1':
        print("Tweet: " + tweets[i]['text'])