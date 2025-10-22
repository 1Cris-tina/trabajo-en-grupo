#AYYOUB
def pedir_datos():
    
    lista_alumnos = []

        #pedir el nombre
    while True:
        nombre = input ("escribe el nombre del alumno: ").strip()

        #si no se introduce nada salida del bucel
        if nombre == "":
            break

        #comprobar que solo se haya introducido letras y espacios
        if not all(c.isalpha() or c.isspace() for c in nombre):
            print ("ERROR: solo esta permitido el uso de letras y espacios. Intentalo de nuevo")
            continue
        
        #pedir las notas
        notas_str = input(f"escribe los notas del alumno {nombre} separadas por comas:")
        
        try: 
            notas =  [float (nota.strip ()) for nota in notas_str.split(",") if nota.strip() !=""]
        except ValueError:
            print ("ERROR: introduce los numeros separados por comas. intenta de nuevo")
            continue
        #valudacion de las notas que sean numeros del 1 al 10
        if not notas:
            print ("ERROR: intrdocue una nota")
            continue
        if any(n < 0 or n > 10 for n in notas):
            print ("ERROR: las notas solo pueden ser de 0 a 10.")
            continue


        #datos de los alumnos guardados
        alumno = {"nombre": nombre, "notas": notas}
        lista_alumnos.append(alumno)

    return lista_alumnos

# JUAN - Función de cálculo de promedio

def calcular_promedio(lista_notas):
    """
    Calcula el promedio de una lista de notas de un alumno.
    Parámetros:
        lista_notas (list): Lista de números (float o int) con las notas del alumno.
    Retorna:
        float: Promedio de las notas o 0 si la lista está vacía.
    """
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)


def promedio_grupo(lista_alumnos):
    """
    Calcula el promedio general del grupo a partir de la lista de alumnos.
    Parámetros:
        lista_alumnos (list): Lista de diccionarios con la estructura:
        {"nombre": str, "notas": [float, float, ...]}
    Retorna:
        float: Promedio general del grupo.
    """
    if not lista_alumnos:
        return 0

    total_promedios = 0
    for alumno in lista_alumnos:
        promedio_alumno = calcular_promedio(alumno["notas"])
        total_promedios += promedio_alumno

    return total_promedios / len(lista_alumnos)

#DAVID

def evaluar_aprobado(calcular_promedio):
    if calcular_promedio >= 5:
        return "aprobado"
    else:
        return "suspenso"

#MARCOS

def calculo_tasas_notas(lista_alumnos):
    if not lista_alumnos:
        return None, None, 0

    #BUSCAMOS LA NOTA MÁS ALTA Y EL ALUMNO QUE LA TIENE
    nota_max = max(
        ((alumno, max(alumno["notas"])) for alumno in lista_alumnos),
        key=lambda x: x[1]
    )
    #BUSCAMOS LA NOTA MÁS BAJA Y EL ALUMNO QUE LA TIENE
    nota_min = min(
        ((alumno, min(alumno["notas"])) for alumno in lista_alumnos),
        key=lambda x: x[1]
    )
    #CONTAR APROBADOS
    aprobados = sum(1 for a in lista_alumnos if a["estado"] == "Aprobado")
    #CALCULAR PORCENTAJE
    tasa_aprobados = (aprobados / len(lista_alumnos)) * 100
    #DEVUELVE RESULTADOS
    return nota_max, nota_min, tasa_aprobados

#DYAN
def mostrar_clasificacion(lista_alumnos):
    """
    Esto es un docstring en el que documentaré la función:
    Muestra la clasificación de los alumnos según su promedio.
    
    Podemos tener una lista que contenga diccionarios.
    Cada diccionario dentro de la lista tiene los datos de un alumno(nombre y promedio)

    La función ordena los alumnos basándose en el valor asociado a 'promedio' y
    muestra el ranking en pantalla.
    """
    # Ordenamos la lista de alumnos usando 'sorted(lista_alumnos)
    # key=lambda x: x['promedio'] Le dice a sorted() que utilice el valor promedio para ordenador
    # reverse=True hace que sea de mayor a menor, si fuera reverse=False(pordefecto); de menor a mayor
    lista_ordenada = sorted(lista_alumnos, key=lambda x: x['promedio'], reverse=True)

# Mostramos encabezado de la clasificación
    print("=== CLASIFICACIÓN GENERAL ===")
    
    # Enumeramos los alumnos ordenados para mostrar su posición en el ranking
    for i, alumno in enumerate(lista_ordenada, start=1):
        # Imprimimos posición, nombre y promedio con un decimal.
        # con i, indicamos en iterable que es lista_ordenada.
        # Con alumno, indicamos el diccionario
        # Con enumerate(lista_ordenada,start=1) le decimos que enumere en el ranking empezando por 1.
        # con start=1, el valor inicial del ranking.
        print(f"{i}. {alumno['nombre']} -> {alumno['promedio']:.1f}")
        # Mostramos encabezado de la clasificación
        # Muestra el i, que es la posición del alumno en el ranking
        # {alumno['nombre']} muestra el nombre del alumno, en relación al diccionario
        # {alumno['promedio']:.1f}") Muestra el promedio del alumno, pero con un formato específico (con un decimal)

#DIEGO
def mostrar_reporte(lista_reporte):
    pass

