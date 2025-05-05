from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

DATA_FILE = 'messages.txt'

def load_messages():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def save_messages(messages):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        for msg in messages:
            f.write(msg + '\n')

messages = load_messages()


@app.route('/')
def home():
    return render_template("guestbook.html", messages=messages)

@app.route('/guestbook')
def guestbook():
    return '<br>'.join(messages)

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        name = request.form['name']
        msg = request.form['message']
        messages.append(f"{name}: {msg}")
        save_messages(messages)
        return redirect('/guestbook')
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)

