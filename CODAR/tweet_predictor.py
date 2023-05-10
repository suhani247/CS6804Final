#!/usr/bin/python3
import torch
from BERT import BERT
import text_predict
from datetime import datetime

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
text_model = BERT().to(device)

def load_checkpoint(load_path, model):
    
    if load_path==None:
        return
    
    state_dict = torch.load(load_path, map_location=device)
    print(f'Model loaded from <== {load_path}')
    
    model.load_state_dict(state_dict['model_state_dict'])
    return state_dict['valid_loss']

load_checkpoint('models/model_initial_text.pt', text_model)


class Listener():
    def on_data(self, tweet_text):
        #Predicting toxicity for a post with image and text
        post_content_prediction = text_predict.predict_string("@sajid_fairooz @israeliregime yes they are jew hating barbarians.")
        post_content_prediction = max(post_content_prediction)
        text_toxicity = post_content_prediction

    def on_error(self, status):
        print (status)


listener = Listener()
print(listener.on_data())


