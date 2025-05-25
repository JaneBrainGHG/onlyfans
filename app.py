from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def landing_page():
    return send_file('onlymaster.html')

if __name__ == '__main__':
    app.run(debug=True)