from flask import Flask, render_template, request
import ssl

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="443", debug=True, ssl_context='adhoc')