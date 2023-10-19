# -*- coding: utf-8 -*-

class Reserva:
    def __init__(self, habitacion, cliente, fecha):
        self.__fecha = fecha
        self.__id_cliente = cliente
        self.__id_habitacion = habitacion
    
    ###///////////////////////////###
    ###     SETTERS Y GETTERS     ###
    ###///////////////////////////###

    # ID ----------------------------
    @property
    def id(self):
        return f"{self.habitacion}:{self.fecha}"

    # NUMERO HABITACION -------------
    @property
    def habitacion(self):
        return self.__id_habitacion

    # CLIENTE -----------------------
    @property
    def cliente(self):
        return self.__id_cliente

    # FECHA -------------------------
    @property
    def fecha(self):
        return self.__fecha

    ###////////////////////////////###
    ###     METODOS ESPECIALES     ###
    ###////////////////////////////###

    # STRING ------------------------
    def __str__(self) -> str:
        return f'RESERVA: {self.id}, CLIENTE:{self.cliente}'
    
    
'''
    r = Reserva(12,'asdkj','10/04/2002',4)
    print(r.id)
'''