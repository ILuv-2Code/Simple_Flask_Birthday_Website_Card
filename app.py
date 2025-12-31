from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    name = "Name Here"
    text = "Birthday Message Here"
    return render_template('index.html', name=name, text=text)

if __name__ == "__main__":
    app.run(debug=True)