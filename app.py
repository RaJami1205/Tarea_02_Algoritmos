"Tarea 2 Maximizador de Sumas Genéticas // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

from flask import Flask, render_template, request
from suma_genetica import algoritmo_genetico

app = Flask(__name__)
app.secret_key = 'ra&diegop'

# Ruta principal
@app.route('/')
def index():
    return render_template('interfaz.html')

# Ruta para procesar el formulario
@app.route('/interfaz', methods=['GET', 'POST'])
def ejecutar():
    valores = request.form['lista'].split(',')
    valores = [int(valor.strip()) for valor in valores]  # Convertir cada valor a entero
    limite = int(request.form['limite'])  # Convertir el límite a entero

    suma_maxima = algoritmo_genetico(valores, limite)

    print(suma_maxima)
    
    return render_template('interfaz.html')

# Iniciamos la plantilla web
if __name__ == '__main__':
    app.run(debug=False)