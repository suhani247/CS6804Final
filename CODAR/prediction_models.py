# Models
def predict_text(model,sentence,device):  
  from transformers import BertTokenizer
  import torch
  import torch.nn as nn

  tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')

  # Model parameter
  MAX_SEQ_LEN = 256
  PAD_INDEX = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
  UNK_INDEX = tokenizer.convert_tokens_to_ids(tokenizer.unk_token)
  tokenized = tokenizer.tokenize(sentence)
  tokenized = tokenizer.convert_tokens_to_ids(tokenized)
  tensor = torch.LongTensor(tokenized).to(device)
  tensor = tensor.unsqueeze(1).T
  length_tensor = torch.LongTensor([MAX_SEQ_LEN])
  prediction = model(tensor,torch.LongTensor([1]).to(device).unsqueeze(1).T)
  _, output = prediction
  category = torch.argmax(output,1)
  return nn.functional.softmax(prediction[1][0],dim=0).tolist()[1]

def predict_chat_toxicity(model,chat_file,device):
  import csv
  total = 0
  toxic = 0
  with open(chat_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      message = row['message']
      score = predict_text(model,message,device)
      if(score>0.9):
        toxic+=1
      total+=1

  print((toxic/total)*100)
  return (toxic/total)*100
