from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Bu boyuk basliqdir</h1>
    <h2>Bu daha kicikdir</h2>
    <h3>Bu dahada kicikdir</h3>
    <p><em>Api oyrenirik Flask ile isleyirik</em></p>
    <p>
    <a href="https://google.com"target="_blank"
    style="color:orange;">
    Google-e get
    </a>
    </p>
    
    <ul>
       <li>Ciyelek</li>
       <li>Gilas</li>
       <li>Banan</li>
    </ul>
    <ol>
        <li>Birinci</li>
        <li>Ikinci</li>
        <li>Ucuncu</li>
    </ol>
    <button onclick='alert("Tebrikler buraya kliklediniz")'>Buraya klikle</button>
    '''
if __name__=="__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")


