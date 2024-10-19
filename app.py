import json
import os
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
    ruta_static = os.path.join('static', 'resultados.json')

    if request.method == 'POST':
        # Limpiar el archivo resultados.json solo si es un POST
        with open(ruta_static, 'w') as json_file:
            json_file.write('')  # Esto deja el archivo vacío

        # Procesar la lista y el límite
        valores = request.form['lista'].split(',')
        valores = [int(valor.strip()) for valor in valores]  # Convertir cada valor a entero
        limite = int(request.form['limite'])  # Convertir el límite a entero

        # Ejecutar el algoritmo genético y obtener las tres variables
        mejor_solucion, mejor_fitness, registro_mejores_soluciones = algoritmo_genetico(valores, limite)

        data = {
            'mejor_solucion': mejor_solucion,
            'mejor_fitness': mejor_fitness,
            'registro_mejores_soluciones': registro_mejores_soluciones
        }

        # Guardar los resultados en el archivo
        with open(ruta_static, 'w') as json_file:
            json.dump(data, json_file)

    return render_template('interfaz.html')

# Iniciamos la plantilla web
if __name__ == '__main__':
    app.run(debug=False)