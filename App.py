from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hello Ahmad!</h1>
        <p>Here is the link you need: <a target="_blank" href="https://www.google.com">Click here</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
