# -*- coding: utf-8 -*-
import ClasesObjeto as objVC
def alquilarArticulo(nom,lista):
    for art in lista:
        if art.titulo == nom:
            res = art.alquiler()
            if (res == 1):
                print "Se ha alquilado "+art.__str__()
            else:
                print "No se ha podido alquilar "+art.__str__()
def devolverArticulo(nom,lista):
    for art in lista:
        if art.titulo == nom:
            res = art.devolver()
            if (res == 1):
                print "Se ha devuelto "+art.__str__()
            else:
                print "No se ha podido devolver "+art.__str__()
def imprimirLista(lista):
    for obj in lista:
        obj.mostrarDatos()  
def main():
    obj1 = objVC.Pelicula("ESDLA", "3€", True, "Ficcion", "2000", "P.Jackson")
    obj2 = objVC.Pelicula("Titanic","3€", False, "Drama", "1997", "James Cameron")
    obj3 = objVC.Pelicula("Skyfall", "3€",False,"Acción", "2012", "Sam Mendes" )
    obj4 = objVC.Videojuego("Call Of Duty Black Ops III"," 5€", True, "18", "PS4")
    obj5 = objVC.Videojuego("Super Mario Bros", "4€",False, "3", "3DS")
    obj6 = objVC.Videojuego("Just Dance 2016", "4€",True, "3", "WII")
    lista = [obj1,obj2,obj3,obj4,obj5,obj6]
    imprimirLista(lista)
    print " * * * Se abre el videoclub * * * "
    alquilarArticulo("ESDLA", lista)
    alquilarArticulo("Titanic", lista)
    devolverArticulo("Skyfall", lista)
    devolverArticulo("Call Of Duty Black Ops III", lista)
    alquilarArticulo("Super Mario Bros", lista)
    devolverArticulo("Just Dance 2016", lista)
    print " * * * Se cierra el videoclub * * * "
    imprimirLista(lista)
main()


        



