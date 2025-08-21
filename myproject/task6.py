from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return '''
    <h1>Salam Flask!</h1>
    <p>Bu, HTML kodudur</p>
    '''
if __name__=='__main__':
    app.run(debug=True,port=7006,host="0.0.0.0")