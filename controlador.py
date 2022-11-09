import datos
import os #limpiar consola

def ListarAlbumesPorArtistas():
    os.system('cls')
    obj = datos.Datos()
    listado = obj.ListarAlbumes()
    
    print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
    for album in listado:
        print(' ',album[0],"\t",album[1],"\t\t",str(album[2])+' '+str(album[3]),"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
    input("\n Presione ENTER para continuar")



def ListarAlbumesPorGenero():
    os.system('cls')
    obj = datos.Datos()
    listado = obj.ListarPorGenero()

    print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
    for album in listado:
        print(' ',album[0],"\t",album[1],"\t\t",str(album[2])+' '+str(album[3]),"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
    input("\n Presione ENTER para continuar")




def BusquedaPorNombreAlbum():
    nombre_busqueda = str(input("\nIngrese el nombre del Album a Buscar: "))

    obj = datos.Datos()
    listado = obj.BusquedaNombreAlbum(nombre_busqueda)

    if listado == []:
        os.system('cls')
        print("No se encontraron registros.")
        input("\n Presione ENTER para continuar")
    else:
        print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
        for album in listado:
            print(' ',album[0],"\t",album[1],"\t\t",str(album[2])+' '+str(album[3]),"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
        input("\n Presione ENTER para continuar")





def ListarAlbumesPorID():
    obj = datos.Datos()
    listado = obj.ListarAlbumesPorID()

    print("\n|ID |COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
    for album in listado:
        print(' ',album[0],"\t",album[1],"\t\t",str(album[2])+' '+str(album[3]),"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8]," ",album[9])






#-----------------------------------------------------------------------------------------------
#Listados de tablas individuales:
#-----------------------------------------------------------------------------------------------


def ListarInterpretes():
    print("\n Listado de Interpretes\n")
    obj = datos.Datos()
    listado = obj.ListarInterprete()

    print("\n|ID |          NOMBRE              |       APELLIDO             |   NACIONALIDAD   |     FOTO    |")
    for interprete in listado:
        print(' ',interprete[0],"\t",interprete[1],"\t\t",str(interprete[2]), str(interprete[3]),interprete[4])


def ListarGeneros():
    print("\n Listado de Generos\n")
    obj = datos.Datos()
    listado = obj.ListarGenero()

    print("\n|ID |   NOMBRE   | ")
    for genero in listado:
        print(' ',genero[0],"\t",genero[1])

def ListarFormatos():
    print("\n Listado de Formatos\n")
    obj = datos.Datos()
    listado = obj.ListarFormato()

    print("\n|ID |     TIPO   | ")
    for formato in listado:
        print(' ',formato[0],"\t",formato[1])

def ListarDiscograficas():
    print("\n Listado de Discográficas\n")
    obj = datos.Datos()
    listado = obj.ListarDiscografica()

    print("\n| ID |    NOMBRE   | ")
    for discografica in listado:
        print(' ',discografica[0],"\t",discografica[1])

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------


def InsertarAlbum():
    cod_album = str(input("\nIngrese el código del nuevo Álbum: "))
    nombre = input("Ingrese el nombre del álbum: ")
    
    print("\nIntérpretes Disponibles:")
    ListarInterpretes()
    id_interprete = int(input("\nIngrese el ID del Intérprete: "))
    

    print("\nListado de Géneros Musicales:")

    obj = datos.Datos()
    listado = obj.ListarGenero()
    for g in listado:
        print(g)

    id_genero = int(input("\nIngrese el ID del Género: "))
    cant_temas = int(input("\nIngrese la cantidad de temas: "))

    print("\nListado de Discográfica:")

    obj = datos.Datos()
    listado = obj.ListarDiscografica()

    for d in listado:
        print(d)

    id_discografica = int(input("\nIngrese el ID de la discografica: "))

    print("\nListado de Formatos de Audio:")

    obj = datos.Datos()
    listado = obj.ListarFormato()
 
    for f in listado:
        print(f)
        
    id_formato = int(input("\nIngrese el ID del formato: "))
    fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento (aaaa-mm-dd): ")
    precio = float(input("\nIngrese el precio: "))
    cantidad = int(input("\nIngrese cantidad disponible de este álbum: "))
    caratula = input("\nIngrese la dirección web de la Carátula: ")

    #Luego de preguntar se crea el objeto con los datos recolectados:
    nuevoAlbum = datos.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
    
    preg = input("Desea cargar el album? S/N: ")
    if preg.lower() == "s": 
        obj = datos.Datos()
        obj.InsertarAlbum(nuevoAlbum) #Se envia el objeto.

        print("\n Carga realizada.")

    input("\n Presione ENTER para continuar")


#-----------------------------------------------------------------------------------------------

def BorrarUnAlbum():
    print("LISTA DE ALBUMS POR ID:")
    ListarAlbumesPorID()
    elegido = ""
    elegido = input("\nIndique el ID del Album a ELIMINAR según su elección de la lista: ")

    if elegido =="\n" or elegido == None or elegido == "":
        print("Debe elegir una opcion..")
        BorrarUnAlbum()
    else: 
        preg = input("\nDesea ELIMINAR el album? con ID " + elegido + "  ? S/N: ")
        if preg.lower() == "s": 
            obj = datos.Datos()
            obj.BorrarAlbum(elegido)
        else:
            print("Cancelado borrar Album.")


#-----------------------------------------------------------------------------------------------

def ModificarUnAlbum(): 

    print("LISTA DE ALBUMS POR ID, ELIJA CUAL DESEA MODIFICAR:")
    ListarAlbumesPorID()
    elegido = input("\nIndique el ID del Album a MODIFICAR según su elección de la lista: ")
    preg = input("\nDesea MODIFICAR el album? con ID " + elegido + "  ? s/n ") #se elige el id album
    if preg.lower() == "s":
        ModificacionAlbumPasos(elegido) #se envia al cuestionario el id album
    else:
        print("Cancelado modificar Album.")

    
def ModificacionAlbumPasos(id_album): #Cuestionario
    id_album = id_album
    #variables reseteadas
    cod_album, nombre, id_interprete, id_genero, cant_temas, id_discografica, id_formato, fec_lanzamiento, precio, cantidad, caratula = "","","","","","","","","","",""
    obj = datos.Datos()
    listado = obj.BuscarUnAlbumPorSuID(id_album)
    for album in listado: #la clase album se llena con los datos del id de Album de la tabla al inicializarse
        AlbumDataBD = datos.Album(album[0],album[1],album[2],album[3],album[4],album[5],album[6],album[7],album[8],album[9],album[10],album[11])
        print(AlbumDataBD)

    #se almacenan en variables temporales los valores nuevos
    cod_album = input("\nIndique nuevo codigo del Album (no es el ID, puede ser Alfanumérico) (ENTER para omitir):  ")
    if cod_album != "": #si dimos enter y dejamos vacia la variable entonces asignamos el valor con el setter del objeto Album
        AlbumDataBD.setCod_album(cod_album)
    else:    
        cod_album = AlbumDataBD.getCod_album()

    nombre =  input("\nIndique nuevo nombre (ENTER para omitir):  ")
    if nombre != "": 
        AlbumDataBD.setNombre(nombre)
    else:    
        nombre = AlbumDataBD.getNombre()

    ListarInterpretes()      #mostramos tablas para ver el id
    id_interprete =  input("\nIndique nuevo ID de interprete (ENTER para omitir):  ")
    if id_interprete != "": 
        AlbumDataBD.setId_interprete(id_interprete)
    else:
        id_interprete = AlbumDataBD.getId_interprete()

    ListarGeneros()          #mostramos tablas para ver el id
    id_genero =  input("\nIndique nuevo ID de género (ENTER para omitir):  ")
    if id_genero != "": 
        AlbumDataBD.setId_genero(id_genero)
    else:
        id_genero = AlbumDataBD.getId_genero()

    cant_temas = input("\nIndique cantidad de canciones que tiene el Album (ENTER para omitir):  ")
    if cant_temas != "": 
        AlbumDataBD.setCant_temas(cant_temas)
    else:
        cant_temas = AlbumDataBD.getCant_temas()

    ListarDiscograficas()    #mostramos tablas para ver el id
    id_discografica =  input("\nIndique nuevo ID de Discográfica (ENTER para omitir):  ")
    if id_discografica != "": 
        AlbumDataBD.setId_discografica(id_discografica)
    else:
        id_discografica = AlbumDataBD.getId_discografica()

    ListarFormatos()          #mostramos tablas para ver el id  
    id_formato =  input("\nIndique nuevo ID de Formato (ENTER para omitir):  ")  
    if id_formato != "": 
        AlbumDataBD.setId_formato(id_formato)
    else:
        id_formato = AlbumDataBD.getId_formato()

    #datos que no requieren ver tablas:
    fec_lanzamiento = input("\nIndique fecha de lanzamiento AAAA-MM-DD, (ENTER para omitir):  ")
    if fec_lanzamiento != "": 
        AlbumDataBD.setFec_lanzamiento(fec_lanzamiento)
    else:
        fec_lanzamiento = AlbumDataBD.getFec_lanzamiento()

    precio =  input("\nIndique precio (ENTER para omitir):  ")
    if precio != "": 
        AlbumDataBD.setPrecio(precio)
    else:
        precio = AlbumDataBD.getPrecio()

    cantidad =  input("\nIndique cantidad de unidades del Album (ENTER para omitir):  ")
    if cantidad != "": 
        AlbumDataBD.setCantidad(cantidad)
    else:
        cantidad = AlbumDataBD.getCantidad()

    caratula =  input("\nIndique un link a la imagen de la carátula (ENTER para omitir):  ")
    if caratula != "": 
        AlbumDataBD.setCaratula(caratula)   
    else:
        caratula = AlbumDataBD.getCaratula()

    #Resumen de los cambios segun cuestionario:
    print("\nResumen de MODIFICACIONES al Album antes de su carga:")
    print("------------------------------")
    print("ID SELECCIONADA ------> " + str(id_album))
    print("Codigo del Album    : " + str(cod_album))
    print("ID Interprete       : " + str(id_interprete))
    print("ID Género           : " + str(id_genero))
    print("Cantidad temas      : " + str(cant_temas))
    print("ID Discografica     : " + str(id_discografica))
    print("ID Formato          : " + str(id_formato))
    print("Fecha de Lanzamiento: " + str(fec_lanzamiento))
    print("Precio              : " + str(precio))
    print("Cantidad            : " + str(cantidad))
    print("Caratula            : " + str(caratula))

    preg = input("\nDesea MODIFICAR el album? con ID " + id_album + "? s/n: ")
    if preg.lower() == "s":
        AlbumDataBD = datos.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
        obj = datos.Datos()
        obj.ModificarAlbum(AlbumDataBD,id_album) #Se envia el objeto.
        print("Album Modificado.")       
    else:
        print("Cancelado Modificar")
#-----------------------------------------------------------------------------------------------


def InsertarInterprete():
    print("\nEstá por agregar un interprete:\n ")
    nombre = input("\n Ingrese Nombre Artista: ")
    apellido =  input("\n Ingrese Apellido Artista: ")
    nacionalidad = input("\n Ingrese Nacionalidad Artista: ")
    
    foto = input("\n Ingrese Link de la Foto del Artista: ")
    preg = input("Desea agregarlo? S/N:" )
    if preg.lower() == "s":
        obj = datos.Datos()
        obj.CargarInterprete(nombre,apellido,nacionalidad,foto)
    else:
        print("\n Se cancelo la carga de Interprete.." )
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    #   self.data = (album.getCod_album(),
    #     album.getNombre(),
    #     album.getId_interprete(),
    #     album.getId_genero(),
    #     album.getCant_temas(),
    #     album.getId_discografica(),
    #     album.getId_formato(),
    #     album.getFec_lanzamiento(),
    #     album.getPrecio(),
    #     album.getCantidad(),
    #     album.getCaratula())
