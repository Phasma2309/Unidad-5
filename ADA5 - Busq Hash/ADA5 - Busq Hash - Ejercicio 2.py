def contar_frecuencia_palabras(texto):
    palabras = texto.split()
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

texto = "Hola mundo hola estudiantes del mundo"
frecuencia_palabras = contar_frecuencia_palabras(texto)

for palabra, frecuencia in frecuencia_palabras.items():
    print(f"La palabra '{palabra}' aparece {frecuencia} veces.")
