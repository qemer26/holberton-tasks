from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return '''
    <h1>Bu Istifadeci basliqidir</h1>
    <h2>Bu daha kicikdir</h2>
    <p>Bu paraqrafdir</p>
'''
if __name__=="__main__":
    app.run(debug=True)