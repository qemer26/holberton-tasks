from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/merhaba')
def merhaba():
    return jsonify({"mesaj": "Merhaba, Flask API!"})

if __name__ == '__main__':
    app.run(debug=True)
