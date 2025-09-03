from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    mesaj = "Merhaba, Flask!"
    return render_template('index.html', mesaj=mesaj)

if __name__ == '__main__':
    app.run(debug=True)