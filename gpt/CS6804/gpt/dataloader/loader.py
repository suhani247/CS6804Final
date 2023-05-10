import pickle
import sys

from api import ChatGpt

with open('/home/suhanik/Documents/CS6804/gpt/CS6804/twitter_data.pkl', 'rb') as f:
    data = pickle.load(f)

tweets = []
labels = []
classified_labels = []
for record in data:
    tweets.append(record['text'])
    labels.append(record['label'])


print(len(tweets))

for i in range(1524,3324):
    print(str(i) + ": " + tweets[i])

print(len(labels))
gpt = ChatGpt()
start = int(sys.argv[1])
end = int(sys.argv[2])

# if end > len(labels):
#     end = len(labels)
# for i in range(start,end):
#     tweet = tweets[i]
#     file = open("/home/suhanik/Documents/CS6804/gpt/CS6804/classified.txt", "a")
#     response = gpt.ask_question(tweet)
#     classified_label = gpt.identify_reponse(response)
#     classified_labels.append(classified_label)
#     print(classified_labels)
#     file.write(str(classified_label) + "\n")
#     file.close()
