from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return '''
    <h1 style="color:red;">Taylor Swift!</h1>
    <h2 style="color:black;">Look what you made me do!</h2>
    <h3 style="color:blue;">Bad blood!</h3>

    <p style="color:orange;">Showgirl</p>
    <p style="color:pink;">Enchanted</p>
    '''
if __name__=="__main__":
    app.run(debug=True,port=5006,host="0.0.0.0")