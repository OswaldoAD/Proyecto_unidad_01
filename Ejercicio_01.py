'''
Tarea 1
Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autor(es). 
Considerar que un libro puede tener varios autores.

Se solicita escribir un programa en Python que permita registrar libros. Debe utilizar: 
colecciones (listas, tuplas, etc), funciones y clases de Python.

Dicho programa debe tener un menu (a interactuar en la línea de comando) para:

Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
Opción 2: Listar libros.
Opción 3: Agregar libro.
Opción 4: Eliminar libro.
Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
Opción 6: Ordenar libros por título.
Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 
(hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.
Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
Nota: listar libros involucra: título, género, ISBN, editorial y autor(es)

'''

class libro:
    def __init__(self, id:int, titulo:str, genero:str, ISBN:int, editorial:str, autores:str) -> None:
        self._id = id
        self._titulo = titulo
        self._genero = genero
        self._ISBN = ISBN
        self._editorial = editorial
        self._autor = autores

    def __del__(self):
        return "objeto eliminado"


print("Registro y buscador de libros")
print("=============================")


print("")
print ("Opcion 1: Leer archivo de disco duro(.txt o csv)\n""Opción 2: Listar libros\n""Opción 3: Agregar libro\n"
    "Opción 4: Eliminar libro\n""Opción 5: Buscar libro por ISBN o por título\n""Opción 6: Ordenar libros por título\n"
    "Opción 7: Buscar libros por autor, editorial o género\n""Opción 8: Buscar libros por número de autores\n"
    "Opción 9: Editar o actualizar datos de un libro\n""Opción 10: Guardar libros en archivo de disco duro (.txt o csv)") 
print("")
print("Elige una opcion e ingresa su número...\n")
print("Recuerda que primero tienes que cargar un libro en la opcion 1: ")
opcion = input("")

import csv

if opcion == "1":
    ruta = input("Ingrese la ruta del archivo a cargar: ")
    nombre = input("Ingrese el nombre del archivo segun formato(nombre.csv o nombre.txt: ")
    ruta_archivo = ruta+"\\"+nombre
    f = open(ruta_archivo)
    reader =csv.reader(f)
    for row in reader:
        print (row)
    f.close()
    print("Archivo cargado correctamente...")

    inicio = True
    while inicio == True:
        print("")
        print ("Opcion 1: Leer archivo de disco duro(.txt o csv)\n""Opción 2: Listar libros\n""Opción 3: Agregar libro\n"
            "Opción 4: Eliminar libro\n""Opción 5: Buscar libro por ISBN o por título\n""Opción 6: Ordenar libros por título\n"
            "Opción 7: Buscar libros por autor, editorial o género\n""Opción 8: Buscar libros por número de autores\n"
            "Opción 9: Editar o actualizar datos de un libro\n""Opción 10: Guardar libros en archivo de disco duro (.txt o csv)\n") 
        opcion = input("Elige una opcion, ingresa su número u otro caracter para salir.\n")  

        if opcion == "2":
                    with open(ruta_archivo) as f:
                        reader =csv.reader(f)
                        titulo= []
                        for i in reader:
                            titulo.append(i)
                        titulo.pop(0)
                        for j in titulo:
                                print(f'- {j[0:]}')
                    continue