from flask import Flask, request, redirect, render_template

messages = [
    "Yun: Hello there!",
    "GPT: Welcome to the guestbook :)"
]

app = Flask(__name__)

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
        return redirect('/guestbook')
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)

