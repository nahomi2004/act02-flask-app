# render_template_string se usa para renderizar una plantilla HTML escrita directamente como un string
from flask import Flask, render_template_string

import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Leer el contenido
    r = requests.get('https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt')
    
    # Compruebo que lo lea bien
    # print(r.text)
    
    # Leer y quitar los espacios ("Enters")
    lines = r.text.strip().split('\n')
    
    # Separo los encabezados
    headers = lines[0].split('|')
    
    # Filtro y busco los IDs que empiecen con 3, 4, 5 o 7 
    data = [] # Array vacio donde voy a guardar los datos
    
    for line in lines[1:]:
        fields = line.split('|')
        if fields[0].startswith(('3', '4', '5', '7')):
            data.append(fields)
    
    # Creo el HTML
    html_template = """
    <html>
        <head>
            <title>Personas filtradas</title>
            <style>
                table { border-collapse: collapse; width: 80%; margin: 20px auto; }
                th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h2 style="text-align:center;">Personas con ID que comienza en 3, 4, 5 o 7</h2>
            <table>
                <thead>
                    <tr>{% for h in headers %}<th>{{ h }}</th>{% endfor %}</tr>
                </thead>
                <tbody>
                    {% for row in data %}
                        <tr>{% for cell in row %}<td>{{ cell }}</td>{% endfor %}</tr>
                    {% endfor %}
                </tbody>
            </table>
        </body>
    </html>
    """

    return render_template_string(html_template, headers=headers, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)