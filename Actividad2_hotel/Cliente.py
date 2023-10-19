# -*- coding: utf-8 -*-
import re

class Cliente:
    __LETRAS_DNI = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    def __init__(self, dni, nombre, apellido):
        self.id = dni
        self.nombre = nombre
        self.apellido = apellido
        #self.__historico_reservas = {}
    
    ###///////////////////////////###
    ###     SETTERS Y GETTERS     ###
    ###///////////////////////////###

    # DNI ---------------------------
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, nuevo_dni):
        try:
            regex_dni = re.fullmatch('^\d{8}[ABCDEFGHJKLMNPQRSTVWXYZ]$',nuevo_dni)
            letras_dni = re.match('\d{8}',nuevo_dni).group() if regex_dni else None
        except:
            raise TypeError('Introduce un DNI correcto, asegurate de que sea un string')
        else:
            if(regex_dni):
                if(Cliente.__LETRAS_DNI[int(letras_dni)%23] == nuevo_dni[-1]):
                    self.__id = nuevo_dni
                else: raise ValueError('La letra del DNI no coincide con el numero')   
            else: raise ValueError('Introduce un formato correcto de DNI: 8 Numeros y 1 Letra')
    
    # NOMBRE ------------------------
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if(isinstance(nuevo_nombre,str) and nuevo_nombre.strip() != ''):
            self.__nombre = nuevo_nombre
        else:
            raise ValueError('El nombre debe de ser un string y no debe estar vacio')

    # APELLIDO ----------------------
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        if(isinstance(nuevo_apellido,str) and nuevo_apellido.strip() != ''):
            self.__apellido = nuevo_apellido
        else:
            raise ValueError('El apellido debe de ser un string y no debe estar vacio')
    

    ###////////////////////////////###
    ###     METODOS ESPECIALES     ###
    ###////////////////////////////###

    # STRING ------------------------
    def __str__(self) -> str:
        return f"DNI: {self.id}, {self.nombre} {self.apellido}"


    ###/////////////////###
    ###     METODOS     ###
    ###/////////////////###
    
'''    
    def get_reservas_de_cliente(self):
        return self.historico_reservas

    def add_reserva(self, reserva):
        self.__historico_reservas[reserva.get_fecha()] = reserva
'''