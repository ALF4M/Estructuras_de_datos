# -*- coding: utf-8 -*-

class Habitacion:
    def __init__(self, num_habitacion):
        self.id = num_habitacion
        #self.__historico_reservas = {} # fecha: reserva

    
    ###///////////////////////////###
    ###     SETTERS Y GETTERS     ###
    ###///////////////////////////###

    # NUMERO HABITACION -------------
    @property
    def id(self):
        return self.__num_habitacion
    
    @id.setter
    def id(self, new_num_habitacion):
        try:
            self.id
        except:
            if(isinstance(new_num_habitacion,int)):
                self.__num_habitacion = new_num_habitacion
            else: raise TypeError('El numero de habitacion tiene que ser un numero entero')
        else: raise AttributeError('El numero de habitacion no se puede modificar')


    ###////////////////////////////###
    ###     METODOS ESPECIALES     ###
    ###////////////////////////////###

    # STRING ------------------------
    def __str__(self) -> str:
        return f"Num. habitación: {self.__num_habitacion}"
    

    ###/////////////////###
    ###     METODOS     ###
    ###/////////////////###

'''    def get_historico_reservas(self):
        return self.__historico_reservas
    
    def get_id(self):
        return self.__num_habitacion
    
    def esta_reservada(self, fecha) -> bool:
        if(fecha in self.__historico_reservas.keys()):
            return True
        return False
    
    def add_reserva(self, reserva):
        self.__historico_reservas[reserva.get_fecha()] = reserva'''