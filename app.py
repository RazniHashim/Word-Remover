from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    search_string = request.form['search_string']

    # Use regex to remove occurrences of the search string from the text
    modified_text = re.sub(search_string, '', text)

    return render_template('result.html', modified_text=modified_text)

if __name__ == '__main__':
    app.run(debug=True)
