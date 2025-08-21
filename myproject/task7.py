from flask import Flask
app = Flask(__name__)
@app.route('/')
def Taylor():
    return '''
    <html>
    <head>
        <style>
            body {background-color: #fff; text-align: center; font-family: sans-serif;}
            img {width: 300px; border-radius: 10px; margin-top: 20px;}
        </style>
        <body>
            <h1>Taylor Swift Fan sehifesi 🎤</h1>
            <p>Bu sehife Flask ile hazirlanib!</p>
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Taylor Swift_3_-_2019_by_Glenn_Francis.jpg" alt="Taylor Swift">
        </body>
        </html>
        '''

if __name__=="__main__":
    app.run(debug=True,port=7002)