from flask import Flask
app = Flask(__name__)
@app.route('/')
def love():
    return "Ich liebe dich"
if __name__=="__main__":
    app.run()
