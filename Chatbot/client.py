from flask import session,render_template ,request, Flask
import random
from datetime import date
import sys
import re
import html
import urllib.request
import urllib.parse
from langdetect import detect
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy as np
import webbrowser
from keras.models import load_model
model = load_model('model/chatbot_model.h5')
intents = json.loads(open('order.json').read())
words = pickle.load(open('model/words.pkl','rb'))
classes = pickle.load(open('model/classes.pkl','rb'))

agent = {'User-Agent':
         "Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}


def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words
# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words) 
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(text):
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res


def get_Date():
    today = date.today()
    res = "Today's date : " + str(today)
    return res




def unescape(text):
    if (sys.version_info[0] < 3):
        parser = HTMLParser.HTMLParser()
    else:
        parser = html
    return (parser.unescape(text))

#Fonction that translate the question if the language is French
def translate(to_translate, to_language="en", from_language="auto"):
    base_link = "http://translate.google.com/m?tl=%s&sl=%s&q=%s"
    to_translate = urllib.parse.quote(to_translate)
    link = base_link % (to_language, from_language, to_translate)
    request = urllib.request.Request(link, headers=agent)
    raw_data = urllib.request.urlopen(request).read()
    data = raw_data.decode("utf-8")
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    re_result = re.findall(expr, data)
    if (len(re_result) == 0):
        result = ""
    else:
        result = unescape(re_result[0])
    return (result)




app = Flask(__name__)

key = "AIzaSyCPYjoc79wxfU2yU2Bv3uQB9LKGndpIlHs"

test1 = list()

@app.route("/",methods=['GET','POST'])
def index():
   return render_template('chatbot.html',test=test1)

@app.route("/envoiMessage",methods=['POST'])
def envoiMessage():
   request_message = request.form.get('message')

   if ( request_message != ''):
    if (detect(request_message) == 'fr'):
        request_message = translate(request_message)

   if ( request_message == ''):
       return render_template("chatbot.html",test=test1)
   reponse = chatbot_response(request_message)
   if ('date' in request_message or 'day' in request_message):
       reponse = get_Date()
   test1.append(request_message)
   test1.append(reponse)
   
   classe = predict_class(request_message,model)
   if (classe[0]['intent'] == "google" or classe[0]['intent']=="wikipedia" or classe[0]['intent']=="weather" or classe[0]['intent']=="news"):
       webbrowser.open(reponse, new=1)

   return render_template("chatbot.html",test=test1)


if __name__ == '__main__':
    app.run()