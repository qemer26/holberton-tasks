from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return '''
    <h1>Bu boyuk basliqdir</h1>
    <h2>Bu daha kicikdir</h2>
    <h3>Bu dahada kicikdir</h3>
    <p>Bu sade bir praqrafdir</p>
    <p><em>Api oyrenirik ve Flask ile isleyirik.</em></p>
    <p>
    <a href="https://google.com"target="_blank"style="text-decoration:none;color: orange;">
    Googla-e get
    </a>


    <ul>
        <li>Ciyelek</li>
        <li>Banan</li>
        <li>Qarpiz</li>
    </ul>
    <ol>
        <li>Birinci</li>
        <li>Ikinci</li>
        <li>Ucuncu</li>
    </ol>
    <button onclick="alert('tebrikler Siz kiliklediniz')">Buraya kilikleyin</button>
    <hr style="border:2px dashed gray;">
    <footer>
    '''
if __name__=="__main__":
    app.run(debug=True,port=5001,host="0.0.0.0")    