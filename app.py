
from flask import Flask, render_template, request, redirect, url_for
from joblib import load




pipeline = load("text_classification.joblib")

first_value=""
re=''

def requestResults(name):
    
    re = pipeline.predict([name])
    first_value = str(re)
    return first_value

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        re= str(requestResults(user))

        re="Your sentence gives sentiments "+re
        
        return render_template("Index.html",Sentiment=re,your_message="your message = "+user)


if __name__ == '__main__' :
    app.run(debug=True)
