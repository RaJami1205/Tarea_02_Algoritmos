import random

"Algoritmo maximizador de sumas utilizando el enfoque genético"
registro_mejores_soluciones = []
# Función para calcular el fitness (la suma de los valores seleccionados)
def fitness(individuo, valores, limite):
    suma = sum(valores[i] for i in range(len(individuo)) if individuo[i] == 1)
    if suma >= limite:
        return 0  # Penalizar si la suma excede el límite
    return suma

# Función para generar un individuo aleatorio (solución candidata)
def generar_individuo(tamano):
    return [random.randint(0, 1) for _ in range(tamano)]

# Función de selección por torneo
def seleccion_torneo(poblacion, fitnesses, k=3):
    seleccionados = random.sample(list(zip(poblacion, fitnesses)), k)
    mejor = max(seleccionados, key=lambda x: x[1])
    return mejor[0]

# Función de cruzamiento (crossover) de dos padres
def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Función de mutación (modificar un gen aleatoriamente)
def mutar(individuo, tasa_mutacion=0.01):
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            individuo[i] = 1 - individuo[i]  # Cambiar de 0 a 1 o de 1 a 0
    return individuo

# Algoritmo genético con registro de mejores soluciones
def algoritmo_genetico(valores, limite, tamano_poblacion=30, generaciones=100, tasa_mutacion=0.01):
    # Crear la población inicial
    poblacion = [generar_individuo(len(valores)) for _ in range(tamano_poblacion)]
    
    # Inicializar variables para registrar el progreso
    mejor_fitness_historico = 0
    global registro_mejores_soluciones # Lista para almacenar cuándo cambia la mejor solución
    
    # Ejecutar por un número de generaciones
    for gen in range(generaciones):
        # Evaluar el fitness de toda la población
        fitnesses = [fitness(ind, valores, limite) for ind in poblacion]
        
        # Generar nueva población
        nueva_poblacion = []
        while len(nueva_poblacion) < tamano_poblacion:
            # Selección
            padre1 = seleccion_torneo(poblacion, fitnesses)
            padre2 = seleccion_torneo(poblacion, fitnesses)
            
            # Cruzar (crear hijos)
            hijo1, hijo2 = cruzar(padre1, padre2)
            
            # Mutación
            hijo1 = mutar(hijo1, tasa_mutacion)
            hijo2 = mutar(hijo2, tasa_mutacion)
            
            # Agregar a la nueva población
            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)
        
        # Reemplazar la población vieja por la nueva
        poblacion = nueva_poblacion[:tamano_poblacion]
        
        # Mejor individuo de esta generación
        mejor_individuo = max(poblacion, key=lambda ind: fitness(ind, valores, limite))
        mejor_fitness = fitness(mejor_individuo, valores, limite)
        
            
        # Verificar si la mejor solución ha cambiado
        if mejor_fitness > mejor_fitness_historico:
            mejor_fitness_historico = mejor_fitness
            conjunto_valores_mejor = [valores[i] for i in range(len(mejor_individuo)) if mejor_individuo[i] == 1]
            print("INSIDE IF")
            print(f"Generación {gen + 1}: Mejor Fitness: {mejor_fitness}, Conjunto de valores: {conjunto_valores_mejor}")
            # Almacenar la generación y la nueva mejor solución
            registro_mejores_soluciones.append({
                'generacion': gen + 1,
                'mejor_fitness': mejor_fitness,
                'conjunto_valores': conjunto_valores_mejor
            })
        # Mostrar el progreso del algoritmo
            print(f"Generación {gen + 1}: Mejor Fitness: {mejor_fitness}, Conjunto de valores: {conjunto_valores_mejor}")
    
    # Retornar el mejor individuo encontrado y el registro de mejores soluciones
    mejor_individuo_final = max(poblacion, key=lambda ind: fitness(ind, valores, limite))
    mejor_fitness_final = fitness(mejor_individuo_final, valores, limite)
    conjunto_valores = [valores[i] for i in range(len(mejor_individuo_final)) if mejor_individuo_final[i] == 1]

    print(registro_mejores_soluciones)
    return conjunto_valores, mejor_fitness_final, registro_mejores_soluciones
