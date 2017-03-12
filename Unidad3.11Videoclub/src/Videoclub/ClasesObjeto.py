# -*- coding: utf-8 -*-
'''
Created on 26 ene. 2017

@author: 21542295
'''

class ObjetoVC(object):
    '''
    classdocs
    '''


    def __init__(self, titulo,precioAlq,estaAlquilado):
        '''
        Constructor
        '''
        self.titulo = titulo
        self.precioAlq = precioAlq
        self.estaAlquilado = estaAlquilado
    def alquiler(self):
        if(self.estaAlquilado):
            res = 0
        else:
            self.estaAlquilado=True
            res = 1
        return res
    def devolver(self):
        if(self.estaAlquilado):
            self.estaAlquilado=False
            res = 1
        else:
            res=0
        return res
    def mostrarDatos(self):
        print self



class Pelicula(ObjetoVC):
    '''
    classdocs
    '''
    def __init__(self, titulo, precioAlq, estaAlquilado, genero, ano, director):
        ObjetoVC.__init__(self, titulo, precioAlq, estaAlquilado)
        '''
        Constructor
        '''
        self.genero = genero
        self.ano = ano
        self.director = director
    def __str__(self):
        if(self.estaAlquilado):
            al = "Esta en alquiler "
        else:
            al = "No esta en alquiler"
        return "Pelicula "+self.titulo+" "+self.precioAlq+" "+al+" "+self.genero+" "+self.ano+" "+self.director
        
        
class Videojuego(ObjetoVC):
    '''
    classdocs
    '''
    def __init__(self, titulo, precioAlq, estaAlquilado, codPegi,plataforma):
        ObjetoVC.__init__(self, titulo, precioAlq, estaAlquilado)
        '''
        Constructor
        '''
        self.codPegi = codPegi
        self.plataforma = plataforma    
        
    def __str__(self):
        if(self.estaAlquilado):
            al = "Esta en alquiler "
        else:
            al = "No esta en alquiler"
        return "Videojuego "+self.titulo+" "+self.precioAlq+" "+al+" "+self.codPegi+" "+self.plataforma
    
    
    
    
            