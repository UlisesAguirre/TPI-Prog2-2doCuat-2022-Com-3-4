from os import system
import sqlite3
import time

class ProgramaPrincipal:

    def menu(self):
        while True:
            system("cls")
            print("Menu de opciones Concesionaria")
            print("-------------------------------")
            print("1- Cargar automovil")
            print("2- Modificar precio automovil")
            print("3- Eliminar automovil")
            print("4- Cargar disponibilidad automovil")
            print("5- Listado automoviles\n")
            print("6- Ingresar al menú motocicletas")
            print("\n0- Salir\n")
            try:
                nro = int(input("Por favor ingrese un número: "))
            
            
                system("cls")
                if nro == 1:
                    marca = input("Por favor ingrese la marca del automovil: ")
                    modelo = input("Por favor ingrese el modelo del automovil: ")
                    precio = input("Por favor ingrese el precio del automovil: $")
                    cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                    nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                    nuevo_automovil.cargar_automovil()
                if nro == 2:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    precio = input("Por favor ingrese el nuevo precio: $")
                    automovil_a_modificar=Automovil(marca,modelo,precio)
                    automovil_a_modificar.modificar_automoviles()
                if nro == 3:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    automovil_a_modificar=Automovil(marca,modelo)
                    automovil_a_modificar.eliminar_automoviles()
                if nro == 4:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    automovil_a_modificar=Automovil(marca,modelo)
                    automovil_a_modificar.modificar_cantidad()
                if nro == 5:
                    programa.listado_automoviles()
                if nro == 6:
                    programa.subMenu()
                if nro == 0:
                    break
                if nro < 0 or nro > 6:
                    print("Opcion ingresada no valida... ")

                aux = input("\nPresione enter para continuar...")


            except:
                system("cls")
                print("ERROR: Intente nuevamente...")
                time.sleep(2)
                

        print("¡Gracias por utilizar nuestro programa!\n")
        time.sleep(2)

    def subMenu(self):
        while True:
            system("cls")
            print("MENU MOTOCICLETAS:")
            print("-------------------")
            print("1- Cargar motocicleta\n2- Modificar precio motocicleta\n3- Eliminar motocicleta")
            print("4- Actualizar precios motocicletas")
            print("5- Mostrar registro de motocicletas anteriores a una fecha en especifico")
            print("6- Mostrar registro(historico) de motocicletas anteriores a una fecha en especifico")
            print("\n0- Volver al menú principal\n")
            op = int(input("Por favor ingrese un número: "))
            system("cls")

            if op == 1:
                marca = input("Por favor ingrese la marca de la motocicleta: ")
                modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                cilindrada = input("Por favor ingrese la cilindrada de la motocicleta: ")
                color = input("Por favor ingrese el color de la motocicleta: ")
                precio = input("Por favor ingrese el precio de la motocicleta: $")
                nueva_moto = motocicletas(marca,modelo,cilindrada,color,precio)
                nueva_moto.cargar_motocicleta()
            if op == 2:
                marca = input("Por favor ingrese la marca de la motocicleta: ")
                modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                precio = input("Por favor ingrese el nuevo precio: $")
                cilindrada = ""
                color = ""
                nueva_moto = motocicletas(marca,modelo, cilindrada, color, precio)
                nueva_moto.modificar_motocicleta()
            if op == 3:
                marca = input("Por favor ingrese la marca de la motocicleta: ")
                modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                nueva_moto = motocicletas(marca,modelo)
                nueva_moto.eliminar_motocicleta()
            if op == 4:
                    porcentaje = int(input("Ingrese el porcentaje de aumento: "))
                    programa.actualizar_precios(porcentaje)
            if op == 5:
                    fecha = input("Ingrese fecha (formato AAAA-MM-DD):")
                    programa.consultar_motocicletas(fecha)
            if op == 6:
                    fecha = input("Ingrese fecha (formato AAAA-MM-DD):")
                    programa.consultar_historico_motocicletas(fecha)
            if op == 0:
                print("Volviendo al menú principal...")
                break
            if op < 0 or op > 6:
                print("Opcion ingresada no valida... ")

            
            aux = input("\nPresione enter para continuar...")

    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    def crearTablaMotocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_MOTOCICLETAS") #BORRO LA TABLA DE HISTORICOS_MOTOCICLETAS Y LA CREO
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),cilindrada VARCHAR(30),color VARCHAR(30),precio INTEGER NOT NULL,fechaUltimoPrecio DATETIME)")
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),cilindrada VARCHAR(30),color VARCHAR(30),precio INTEGER NOT NULL,fechaUltimoPrecio DATETIME DEFAULT CURRENT_TIMESTAMP)")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    def actualizarHistoricoMotocicletas(self):
        conexion = Conexiones()
        conexion.abrirConexion()    
        conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
        motocicletas = conexion.miCursor.fetchall()


        for i in motocicletas:
            moto = i
            marca = moto[1]
            modelo = moto[2]
            cilindrada = moto[3]
            color = moto [4]
            precio = moto [5]
            fechaUltimoPrecio = moto [6]
            conexion.miCursor.execute("INSERT INTO HISTORICO_MOTOCICLETAS(marca,modelo,cilindrada,color,precio,fechaUltimoPrecio) VALUES('{}', '{}','{}','{}','{}','{}')".format(marca,modelo,cilindrada,color,precio,fechaUltimoPrecio))
            conexion.miConexion.commit()
     
        conexion.cerrarConexion()

    def listado_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            datos = conexion.miCursor.fetchall()

            print("LISTADO DE AUTOMOVILES:\nID\tMARCA\tMODELO\tPRECIO\tUNIDADES DISPONIBLES")
            print("----------------------------------------------------")

            for i in datos:
                auto = i
                print(f'{auto[0]}\t{auto[1]}\t{auto[2]}\t${auto[3]}\t{auto[4]}')

                # Forma diferente de mostrar el listado:
                # print(f'\nID: {auto[0]}\tMARCA: {auto[1]}\tMODELO: {auto[2]}\tPRECIO: ${auto[3]}\tUNIDADES DISPONIBLES: {auto[4]}')    
        except:
            print('Error al mostrar el listado')
        finally:
            conexion.cerrarConexion()

    def actualizar_precios(self, porcentaje):
        programa.actualizarHistoricoMotocicletas()

        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT id_moto,precio FROM MOTOCICLETAS")
            motocicletas = conexion.miCursor.fetchall()

            for i in motocicletas:
                motos = i
                id = motos[0]
                precio =motos[1]
                precio = precio + (precio*(porcentaje/100))
                conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio='{}', fechaUltimoPrecio = CURRENT_TIMESTAMP where id_moto='{}'  ".format(precio, id))
                conexion.miConexion.commit()
            
            print("\nPrecios actualizados correctamente")

        except:
            print("Error: No se pudo actualizar los precios")
        finally:
            conexion.cerrarConexion()

    def consultar_motocicletas(self, fecha):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:                        
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS WHERE fechaUltimoPrecio <= '{}' ".format(fecha))
            fechas = conexion.miCursor.fetchall()

            print("LISTADO DE MOTOCICLETAS:\nID\tMARCA\tMODELO\tCILINDRADA\tCOLOR\tPRECIO\tFECHA")
            print("---------------------------------------------------------------")
            for i in fechas:
                moto = i
                print(f'{moto[0]}\t{moto[1]}\t{moto[2]}\t{moto[3]}\t\t{moto[4]}\t${moto[5]}\t{moto[6]}')
        except:
            print("Error al consultar datos")
    
    def consultar_historico_motocicletas(self, fecha):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:                        
            conexion.miCursor.execute("SELECT * FROM HISTORICO_MOTOCICLETAS WHERE fechaUltimoPrecio <= '{}' ".format(fecha))
            fechas = conexion.miCursor.fetchall()

            print("HISTORICO DE MOTOCICLETAS:\nID\tMARCA\tMODELO\tCILINDRADA\tCOLOR\tPRECIO\tFECHA")
            print("------------------------------------------------------")
            for i in fechas:
                moto = i
                print(f'{moto[0]}\t{moto[1]}\t{moto[2]}\t{moto[3]}\t{moto[4]}\t${moto[5]}\t{moto[6]}')
        except:
            print("Error al consultar datos")

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio= precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        print("\n---------------------------------\n")
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()

    
    
    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        print("\n---------------------------------\n")
        try:
            conexion.miCursor.execute("SELECT marca FROM AUTOMOVILES")
            marca = str(conexion.miCursor.fetchall())

            conexion.miCursor.execute("SELECT modelo FROM AUTOMOVILES")
            modelo = str(conexion.miCursor.fetchall())

            if modelo.find(self.modelo) != -1 and marca.find(self.marca) != -1:
                conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
                conexion.miConexion.commit()
                print("Automovil modificado correctamente")
            else:
                print("Modelo no encontrado")

        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
        
    def modificar_cantidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT marca,modelo,cantidadDisponibles FROM AUTOMOVILES")
            datos = conexion.miCursor.fetchall()
            
            validacion = False

            for i in datos:
                auto = i
                if auto[0] == self.marca and auto[1] == self.modelo:
                    cantidadDisponible = auto[2] + 1
                    conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles='{}' where marca='{}' and modelo='{}' ".format(cantidadDisponible,self.marca,self.modelo))
                    conexion.miConexion.commit()
                    print("Automovil modificado correctamente")
                    validacion = True
            if validacion == False:
                print("Modelo no encontrado")
                    

        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()

    def eliminar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        print("\n---------------------------------\n")
        try:
            conexion.miCursor.execute("SELECT marca FROM AUTOMOVILES")
            marca = str(conexion.miCursor.fetchall())

            conexion.miCursor.execute("SELECT modelo FROM AUTOMOVILES")
            modelo = str(conexion.miCursor.fetchall())

            if modelo.find(self.modelo) != -1 and marca.find(self.marca) != -1:
                conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
                conexion.miConexion.commit()
                print("Automovil eliminado correctamente")
            else:
                print("Modelo no encontrado")

        except:
            print('Error al eliminar un automovil')
        finally:
            conexion.cerrarConexion()  


class motocicletas:
    def __init__(self, marca, modelo, cilindrada = None,color = None,precio=None, fechaUltimoPrecio= None):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.color = color
        self.fechaUltimoPrecio = fechaUltimoPrecio
        self.precio= precio
    
    def cargar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()

        try:
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS(marca,modelo,cilindrada,color,precio) VALUES('{}', '{}','{}','{}','{}')".format(self.marca, self.modelo, self.cilindrada, self.color, self.precio))
            conexion.miConexion.commit()

            print("\nMotocicleta cargada correctamente")
        except:
            pass
        finally:
            conexion.cerrarConexion()

    def modificar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        print("\n---------------------------------\n")
        try:
            conexion.miCursor.execute("SELECT marca FROM MOTOCICLETAS")
            marca = str(conexion.miCursor.fetchall())

            conexion.miCursor.execute("SELECT modelo FROM MOTOCICLETAS")
            modelo = str(conexion.miCursor.fetchall())

            if modelo.find(self.modelo) != -1 and marca.find(self.marca) != -1:
                conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio='{}', fechaUltimoPrecio = CURRENT_TIMESTAMP where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
                conexion.miConexion.commit()
                print("Motocicleta modificada correctamente")
            else:
                print("Modelo no encontrado")

        except:
            print('Error al actualizar la motocicleta')
        finally:
            conexion.cerrarConexion()  


    def eliminar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        print("\n---------------------------------\n")
        try:
            conexion.miCursor.execute("SELECT marca FROM MOTOCICLETAS")
            marca = str(conexion.miCursor.fetchall())

            conexion.miCursor.execute("SELECT modelo FROM MOTOCICLETAS")
            modelo = str(conexion.miCursor.fetchall())

            if modelo.find(self.modelo) != -1 and marca.find(self.marca) != -1:
                conexion.miCursor.execute("DELETE FROM MOTOCICLETAS where marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
                conexion.miConexion.commit()
                print("Motocicleta eliminada correctamente")
            else:
                print("Modelo no encontrado")

        except:
            print('Error al eliminar la motocicleta')
        finally:
            conexion.cerrarConexion()  
    
    

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   

programa = ProgramaPrincipal()
programa.crearTablas()
programa.crearTablaMotocicleta()


##<--------SE DEJAN CARGADOS 3 AUTOMOVILES Y 3 MOTOCICLETAS PARA FACILITAR EL TESTEO DE LAS OPCIONES DEL MENU------>

#Creo los AUTOMOVILES 

auto1 = Automovil("ford","fiesta",100000,10)
auto2 = Automovil("ford","ka",200000,20)
auto3 = Automovil("fiat","uno",300000,30)

#Creo las MOTOCICLETAS

moto1 = motocicletas("honda", "titan", "150cc","roja",100000)
moto2 = motocicletas("honda", "wave", "110cc","negra",300000)
moto3 = motocicletas("yamaha", "fz", "150cc","azul",200000)


            
#Cargamos las motocicletas a la base de datos
moto1.cargar_motocicleta()
moto2.cargar_motocicleta()
moto3.cargar_motocicleta()

#Cargamos los automoviles a la base de datos
auto1.cargar_automovil()
auto2.cargar_automovil()
auto3.cargar_automovil()


programa.menu()