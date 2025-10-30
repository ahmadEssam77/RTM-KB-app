from flask import Flask, render_template ,send_from_directory
import os

app = Flask(__name__)

# Fav Icon
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, ''),
#                                'favicon.ico', mimetype='image/x-icon')

# Main Route
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/ssc-kb')
def ssc_kb():
    return render_template("SSC_KB.html")

@app.route('/dispatch-kb')
def dispatch_kb():
    return render_template("Dispatch_KB.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
