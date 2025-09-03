from flask import Flask, jsonify, render_template_string
app = Flask(__name__)
@app.route('/')
def home():
    return render_template_string('''
    <h1>Salam, bu sayt hissesdir</h1>
    <p>Melumatlari gormek ucun <a href="/api/user">Buraya klikle</a>.</p>
    ''')
@app.route('/api/user')
def user():
    return jsonify({
        "ad": "Qemer",
        "yas": 18,
        "soyad": "Qehremanova"
    })
    
if __name__=="__main__":
    app.run(debug=True, port=5005, host="0.0.0.0")