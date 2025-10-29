from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Team Link</title>
        <link rel="icon" href="/favicon.png" type="image/png">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        </head>
        <body class="container text-center mt-5">
        <h1 class="mb-3">Hello Team!</h1>
        <p>Here is the link you need:</p>
        <a class="btn btn-primary" target="_blank" href="https://google.com">Click here</a>
        </body>
        </html>
    '''

@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, ''),
                               'favicon.png', mimetype='image/png')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
