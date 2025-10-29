from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hello Team!</h1>
        <p>Here is the link you need: <a target="_blank" href="https://google.com">Click here</a></p>
    '''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
