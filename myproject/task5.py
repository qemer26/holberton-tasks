from flask import Flask
app = Flask(__name__)

@app.route('/')
def basliq():
    return "Ana sehife"

@app.route('/about')
def about():
    return "Haqqimizda"

if __name__ == "__main__":
    app.run(debug=True, port=6005, host='0.0.0.0')
