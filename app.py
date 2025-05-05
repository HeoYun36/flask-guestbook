from flask import Flask, request, redirect

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

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        name = request.form['name']
        msg = request.form['message']
        messages.append(f"{name}: {msg}")
        return redirect('/guestbook')
    return '''
    <form method="post">
        Name: <input name="name"><br>
        Message: <input name="message"><br>
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

