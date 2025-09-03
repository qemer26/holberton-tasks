from flask import Flask
app = Flask(__name__)
@app.route('/')

def start():
    return '''
    <h2>KODY.AZ Flask</h2><p>Bu ilk basliq sehifedir</p>
    <a href="/about">About page</a>

'''
def About():
    return '''
    <h2>About Flask</h2><p>Bu about sehifesidir</p>
    <a href="/">Main page</a>
'''

if __name__=="__main__":
    app.run(debug=True)