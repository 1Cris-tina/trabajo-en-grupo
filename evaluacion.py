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



    
#comprobacion de funcion
#if __name__ == "__main__":
#alumnos = pedir_datos ()
#print ("\nlista de los alumnos introducidos:")
#print(alumnos)

    


#JUAN
def calcular_promedio(lista_notas):
    pass

#DAVID
def evaluar_aprobado(promedio):
    pass

#MARCOS
def calculo_tasas(lista_reporte):
    pass

#DYAN
def mostrar_clasificacion(lista_alumnos):
    pass

#DIEGO
def mostrar_reporte(lista_reporte):
    pass









