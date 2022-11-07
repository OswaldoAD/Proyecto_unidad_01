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
def fun_1(archicsv):
    with open (archicsv) as f:
            
            lis_id=[]
            lis_titulo=[]
            lis_genero=[]
            lis_isbn=[]
            lis_editorial=[]
            lis_autor=[]
            prueba=[]
            reader=csv.reader(f)
            
            for j in reader:
                id_5,titulo_5,genero_5,isbn_5,editorial_5,autor_5 = j
                lis_id.append(id_5)
                lis_titulo.append(titulo_5)
                lis_genero.append(genero_5)
                lis_isbn.append(isbn_5)
                lis_editorial.append(editorial_5)
                lis_autor.append(autor_5)
            lis_id.pop(0)
            lis_titulo.pop(0)
            lis_genero.pop(0)
            lis_isbn.pop(0)
            lis_editorial.pop(0)
            lis_autor.pop(0)
            return lis_id, lis_titulo,lis_genero,lis_isbn,lis_editorial,lis_autor

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
            
        
        elif opcion == "3":
            id =  input("Ingrese id: ")
            titulo = input("Ingrese el título: ")
            genero = input("Ingrese el genero: ")
            isbn = input ("Ingrese el ISBN: ")
            editorial = input("Ingrese la editorial: ")
            autores = input ("Ingrese el autor(nombre,apellidos): ")
            datos=[id,titulo,genero,isbn,editorial,autores]

            with open(ruta_archivo,'a',newline ='') as f:
                archivo = csv.writer(f, delimiter=',')
                archivo.writerow(datos)
                f.close()
            continue

        elif opcion == "4":
            with open(ruta_archivo) as f:
                archivo =csv.reader(f)
                datos =[]
                for i in archivo:
                    datos.append(i)
                for j in datos:
                    print(f'- {datos.index(j)} - {j[1]}')
                f.close()
            
            eliminar = int(input("Ingrese el numero que le corresponde al libro, para eliminar: "))
            datos.pop(eliminar)
            print(datos)
            
            for i in datos[0:1]:
                libro = []
                for j in i:
                    libro.append(j)
                with open(ruta_archivo,'w',newline ='') as f:
                    archivo = csv.writer(f,delimiter=',')
                    archivo.writerow(libro)
                    f.close()
            for i in datos[1:]:
                libro=[]
                for j in i:
                    libro.append(j)
                with open(ruta_archivo,'a',newline ='') as f:
                    archivo = csv.writer(f,delimiter=',')
                    archivo.writerow(libro)
                    f.close()
            continue
        
        elif opcion == "5":
            print("\nPrefieres buscar el libro por ISBN o por titulo?")
            var_5_pala1=str(input("Ingresar ISBN o Titulo:"))
            var_5_pala2=var_5_pala1.lower()
            while var_5_pala2 not in ("isbn".lower(), "titulo".lower()):
                var_5_pala1=str(input("Solo puedes ingresar ISBN o Titulo:"))
                var_5_pala2=var_5_pala1.lower()

            if var_5_pala2 =="isbn":
                pola=fun_1(ruta_archivo)
                isbn_5=[ int(p) for p in pola[3] if p!="larry.ñp"]
                prueba_5=[]
                for i in range(len(isbn_5)):
                    if isbn_5[i] not in prueba_5:
                        prueba_5.append(isbn_5[i])
                print(f"Como ayuda te mostramos todos los ISBN{prueba_5}")
                n_is=int(input("Ingresar numero de ISBN:"))
                for k in isbn_5:
                    if k==n_is:
                        pos_5=isbn_5.index(k)
                        print(f"Id:{pola[0][pos_5]},Titulo:{pola[1][pos_5]},Genero:{pola[2][pos_5]},Editorial:{pola[4][pos_5]},Autor:{pola[5][pos_5]}")
                        isbn_5[pos_5]=str("Nada")

            elif var_5_pala2 =="titulo":
                pola=fun_1(ruta_archivo)
                isbn_5=[ str(p) for p in pola[1] if p!=" "]
                prueba_5=[]
                for i in range(len(isbn_5)):
                    if isbn_5[i] not in prueba_5:
                        prueba_5.append(isbn_5[i])
                print(f"Como ayuda te mostramos todos los titulos{prueba_5}")
                n_is=str(input("Ingresar titulo:"))
                for k in isbn_5:
                    if k==n_is:
                        pos_5=isbn_5.index(k)
                        print(f"Id:{pola[0][pos_5]},Genero:{pola[2][pos_5]},ISBN::{pola[3][pos_5]},Editorial:{pola[4][pos_5]},Autor:{pola[5][pos_5]}")
                        isbn_5[pos_5]=str("Nada")
            continue

        elif opcion == "6":
            file = open(ruta_archivo)
            def list_to_dict(list):
                return {"id":list[0], "titulo":list[1], "genero":list[2], "ISBN":list[3], "autor(es)":list[4]}
            list = []
            for line in file.readlines():
                arr=line.replace("\n", "").split(",")
                dict=list_to_dict(arr)
                list.append(dict)
            list.pop(0)

            list=sorted(list,key=lambda x: x["titulo"])
            for dict in list:
                print(dict)

            continue

        elif opcion == "7":
            print("\nPrefieres buscar el libro por autor, editorial o genero?")
            var_6_pala1=str(input("Ingrese autor, editorial o genero:"))
            var_6_pala2=var_6_pala1.lower()
            while var_6_pala2 not in ("genero".lower(), "editorial".lower(),"autor".lower()):
                var_6_pala1=str(input("Solo puedes ingresar ISBN o Titulo:"))
                var_6_pala2=var_6_pala1.lower()
            if var_6_pala2 =="genero":
                polo=fun_1(ruta_archivo)
                isbn_n_7=[ str(p) for p in polo[2] if p!=" "]
                prueba_7=[]
                for i in range(len(isbn_n_7)):
                    if isbn_n_7[i] not in prueba_7:
                        prueba_7.append(isbn_n_7[i])
                print(f"Como ayuda te mostramos todos los generos: {prueba_7}")
                n_is_7=str(input("Ingresar genero:"))
                for k in isbn_n_7:
                    if k==n_is_7:
                        pos_7=isbn_n_7.index(k)
                        print(f"Id:{polo[0][pos_7]},Titulo:{polo[1][pos_7]},ISBN:{polo[3][pos_7]},Editorial:{polo[4][pos_7]},Autor:{polo[5][pos_7]}")
                        isbn_n_7[pos_7]=str("Nada")
            elif var_6_pala2 =="editorial":
                polo=fun_1(ruta_archivo)
                isbn_n_7=[ str(p) for p in polo[4] if p!=" "]
                prueba_7=[]
                for i in range(len(isbn_n_7)):
                    if isbn_n_7[i] not in prueba_7:
                        prueba_7.append(isbn_n_7[i])
                print(f"Como ayuda te mostramos todos las editoriales: {prueba_7}")
                n_is_7=str(input("Ingresar editorial:"))
                for k in isbn_n_7:
                    if k==n_is_7:
                        pos_7=isbn_n_7.index(k)
                        print(f"Id:{polo[0][pos_7]},Titulo:{polo[1][pos_7]},Genero:{polo[2][pos_7]},ISBN:{polo[3][pos_7]},Autor:{polo[5][pos_7]}")
                        isbn_n_7[pos_7]=str("Nada")
            elif var_6_pala2 =="autor":
                polo=fun_1(ruta_archivo)
                isbn_n_7=[ str(p) for p in polo[5] if p!=" "]
                prueba_7=[]
                for i in range(len(isbn_n_7)):
                    if isbn_n_7[i] not in prueba_7:
                        prueba_7.append(isbn_n_7[i])
                print(f"Como ayuda te mostramos todos los autores o autores: {prueba_7}")
                n_is_7=str(input("Ingresar autor:"))
                for k in isbn_n_7:
                    if k==n_is_7:
                        pos_7=isbn_n_7.index(k)
                        print(f"Id:{polo[0][pos_7]},Titulo:{polo[1][pos_7]},Genero:{polo[2][pos_7]},ISBN:{polo[3][pos_7]},Editorial:{polo[4][pos_7]}")
                        isbn_n_7[pos_7]=str("Nada")
                        
        elif opcion == "8":
            with open(ruta_archivo)as f:
                archivo = csv.reader(f)
                datos= []
                for i in archivo:
                    datos.append(i)

            numero_autores = input("Ingresa el numero de autores: ")
            
            if numero_autores == "3":
                for j in datos:
                    count = 0
                    if j[5].count(",")==2:
                        print(j)
                        count+=1
                if count == 0:
                    print("No se encontro resultados.")
            elif numero_autores == "2":
                for j in datos:
                    count = 0
                    if j[5].count(",")==1: 
                        print(j)
                        count+=1
                if count == 0:
                    print("No se encontro resultados.")

            elif numero_autores == "1":
                for j in datos[1:]:
                    if j[5].count(",")==0: 
                        print(j)

        elif opcion == "9":
            with open(ruta_archivo) as f:
                archivo =csv.reader(f)
                datos =[]
                for i in archivo:
                    datos.append(i)
                
                for j in datos:
                    print(f'- {datos.index(j)} - {j[1]}')
        
                modificar = int(input("Ingrese el numero del libro a modificar: "))

                for cabecera in datos[0]:
                    print(f'- {datos[0].index(cabecera)} - {cabecera}')

                modificar_2 = int(input(f'Ingrese el numero del parametro a modificar: '))

                cambio = input("Ingrese la modificacion : ")
                datos [modificar][modificar_2]= cambio

                print(f'El cambio se realizo con exito: \n {datos[modificar]}')
                
                for i in datos[0:1]:
                    libro = []
                    for j in i:
                        libro.append(j)
                    with open(ruta_archivo,'w',newline ='') as f:
                        archivo = csv.writer(f,delimiter=',')
                        archivo.writerow(libro)
                        f.close()
                for i in datos[1:]:
                    libro=[]
                    for j in i:
                        libro.append(j)
                    with open(ruta_archivo,'a',newline ='') as f:
                        archivo = csv.writer(f,delimiter=',')
                        archivo.writerow(libro)
                        f.close()
        
        elif opcion == "10":
            nombre_archivo= input("Ingrese el nombre del archivo nuevo (nombre.csv o nombre.txt): ")
            with open(ruta_archivo) as f:
                archivo =csv.reader(f)
                datos =[]
                for i in archivo:
                    datos.append(i)
                for j in datos:
                    print(f'- {datos.index(j)} - {j[1]}')
                f.close()

            control = True    
            while control == True:
                
                indice = int(input("Ingrese el numero que le corresponde al libro, para guardar o 0 para acabar: "))
                if indice == 0:
                    break
                else:
                    with open(nombre_archivo,'a',newline ='') as f:
                        archivo = csv.writer(f,delimiter=',')
                        archivo.writerow(datos[indice])

        else:
            break