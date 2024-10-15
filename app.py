"Tarea 2 Maximizador de Sumas Genéticas // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

from flask import Flask, render_template, request, redirect, flash , send_file, jsonify

app = Flask(__name__)
app.secret_key = 'ra&diegop'

# Ruta principal
@app.route('/')
def index():
    return render_template('interfaz.html')

# Ruta para procesar el formulario
@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    valores = request.form['lista']
    limite = request.form['limite']

    for x in valores:
        print(x)
    return

    return render_template('resultado.html', resultado=resultado)

# Iniciamos la plantilla web
if __name__ == '__main__':
    app.run(debug=False)