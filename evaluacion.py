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
