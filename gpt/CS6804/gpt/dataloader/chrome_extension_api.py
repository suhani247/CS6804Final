import json

import flask
from flask import Flask, request, send_from_directory, render_template
from api import ChatGpt
app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return render_template('/home/suhanik/Documents/CS6804/gpt/CS6804/doc.html')

@app.route('/gptdetect/', methods=['POST'])
def detect():
    #request_data = request.get_json()
    request_data = json.loads(request.data, strict=False)
    text = request_data['text']
    gpt = ChatGpt()
    result = gpt.ask_question(text)
    result = gpt.identify_reponse(result)

    if result == 1:
        response = flask.jsonify({'answer': 'yes'})
    else:
        response = flask.jsonify({'answer': 'no'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)