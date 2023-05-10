import pickle

file = open("actual.txt", "a")
tweets = pickle.load(open("twitter_data.pkl", "rb"))
labels = [x['label'] for x in tweets]

for label in labels:
    if label == 'sexism' or label == 'racism':
        file.write('1')
    else:
        file.write('0')
    file.write("\n")
