import controlador
import os 

      
os.system('cls')

while True:
    print("\n+-------------------------------------------+")
    print("|         DISQUERÍA FORMOSA MUSICAL         |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n") 
    print("1 - ALTA DE UN ÁLBUM" + "    2 - MODIFICACION DE UN ÁLBUM" + "   3 - BAJA DE UN ÁLBUM \n")
    print("4 - LISTADO DE ÁLBUMES POR ARTISTAS")
    print("5 - LISTADO DE ÁLBUMES POR GÉNERO MUSICAL")
    print("6 - BÚSQUEDA POR NOMBRE DE ÁLBUM")
    print("7 - INSERTAR INTERPRETE " + " 8 - LISTAR INTERPRETES")
    print("9 - SALIR")
    print("\n")
    opcion = str(input("Ingrese su opción: "))

    if opcion == "1":
        controlador.InsertarAlbum()
    elif opcion == "2":
        controlador.ModificarUnAlbum()
    elif opcion == "3":
        controlador.BorrarUnAlbum()
    elif opcion == "4":
        controlador.ListarAlbumesPorArtistas()
    elif opcion == "5":
        controlador.ListarAlbumesPorGenero()
    elif opcion == "6":
        controlador.BusquedaPorNombreAlbum()
    elif opcion == "7":
        controlador.InsertarInterprete() 
    elif opcion == "8":
        controlador.ListarInterpretes()   
    elif opcion == "9":
        break
    else:
        print("¡Opción incorrecta!")
