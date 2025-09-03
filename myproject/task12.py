from flask import Flask, render_template_string, url_for
app = Flask(__name__)
@app.route('/')
def index():
    mesaj = "Cappucino"
    html = '''
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title> Tek dosya Ornek</title>
        <style>
            .container {
                position: relative;
                display: inline-block;            
            }
            .yazi {
                position: absolute;
                top: 20px;
                left: 20px;
                color: white;
                font-size: 30px;
                font-weight: bold;
                text-shadow: 2px 2px 4px black;
                }
            </style>
        </head>
        <body>

        <div class="container">
            <img src="https://taplink.st/a/2/d/c/1/b3ae62.jpg?1">
            <div class="yazi">{{ mesaj }}</div>
        </div>

        </body>
        </html>
        
    '''
    return render_template_string(html, mesaj=mesaj)
if __name__=="__main__":
    app.run(debug=True)