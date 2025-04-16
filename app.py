from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")
    return f'¡Hola, Loja! <br> Fecha: <b>{fecha_formateada}</b> <br> Me gusta mucho el chocolate uwu'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)