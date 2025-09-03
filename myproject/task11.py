from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def ana_sehife():
    melumatlar = [
        {"ad": "Qemer", "yas": 18, "olke": "Koreya"},
        {"ad": "Sevinc", "yas": 19, "olke": "Almaniya"},
        {"ad": "Feruz", "yas": 21, "olke": "Amerika"},
    ]

    html = '''
    <h1>İstifadəçi Siyahısı</h1>
    <p>Aşağıda istifadəçilərin məlumatları verilmişdir:</p>

    <table border="1" cellpadding="5">
        <tr>
            <th>Ad</th>
            <th>Yaş</th>
            <th>Ölkə</th>
        </tr>
        {% for istifadeci in melumatlar %}
        <tr>
            <td>{{ istifadeci.ad }}</td>
            <td>{{ istifadeci.yas }}</td>
            <td>{{ istifadeci.olke }}</td>
        </tr>
        {% endfor %}
    </table>
    '''

    return render_template_string(html, melumatlar=melumatlar)

if __name__ == '__main__':
    app.run(debug=True)

     