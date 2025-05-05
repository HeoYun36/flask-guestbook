from flask import Flask

messages = [
    "Yun: Hello there!",
    "GPT: Welcome to the guestbook :)"
]

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/guestbook')
def guestbook():
    return '<br>'.join(messages)

if __name__ == '__main__':
    app.run(debug=True)

