"""Al final de un curso se desea saber cual ha sido el alumno con la mejor nota promedio. Se sabe que
este año entraron 75 alumnos y que todos tienen 3 asignaturas. Dar el nombre y la nota media."""
import operator                                                                                      #importa operator para poder usar mi funcion operator para hacer operaciones con los datos de mi diccionario
base = {}                                                                                           # Cargo mi base
ciclo = True                                                                                              #Cargamos el ciclo con True
while ciclo == True:                                                                                       # Creamos un bucle mientras ciclo sea True
    print("------------Alumnos y promedios------------")                                                 # Mi menú
    print("1. Digite esta opcion para almacenar Nombre del alumno con sus respectivas notas:")
    print("2. Digite esta opcion para saber la lista de alumnos")
    print("3. Digite esta opcion para saber el el primero puesto y su promedio:")
    print("4. Digite para salir\n")

    opc = input("Ingrese la opción a elegir:\n")                                                    #Cargo la opcion a elegir

    if opc == "1":                                                                              # si digita 1
        nombre = input("Ingrese nombre del alumno >> ")                                         #Digito las 3 notas
        nota1 = int(input("Ingrese primera nota >> "))
        nota2 = int(input("Ingrese segunda nota >> "))
        nota3 = int(input("Ingrese tercera nota >> "))
        prom= (nota1 + nota2 + nota3)/ 3                                                        # saco el promedio de las 3 notas
        prom1= "{:.2f}".format(prom)
        base[nombre] = prom1                                                                   #Se guarda en la base el nombre y el promedio calculado
        print("Se ha almacenado las notas del alumno correctamente\n")

    elif opc == "2":                                                                              # Si digita 2
        print("----------------")
        
        for keys, values in base.items():
            print(keys,">>",values)                                                                # Muestro mi base ordenadamente en vertical

    elif opc=="3":                                                                              # Si digito 3
        print("----------------")
        print("El mejor alumno es:\n")

                                                                                                # Me demoré mucho en aplicar esta función xD 
        max_key = max(base.items(), key=operator.itemgetter(1))[0]                              # Guardo en max_key el mayor promedio de mi base 
        print(max_key)                                                                  # Imprimo el mayor promedio


        datos = base.get(max_key, "No se encontraron Resultados")                             # guardo el nombre del de mayor promedio

        print(datos)                                                                           # imprimo los datos del primer puesto



    elif opc =="4":                                                                               # termino el ciclo
        ciclo== False

    else:                                                                              # Lo mando a digitar nuevamente porque se equivocó seguramente 
        print("Opcion Ingresada Incorrecta")

    print()