# -*- coding: utf-8 -*-

from Cliente import Cliente
from Habitacion import Habitacion
from Reserva import Reserva

class Hotel:
    def __init__(self, num_habitaciones):
        self._num_habitaciones = num_habitaciones
        self._habitaciones = []
        self._clientes = []
        self._reservas = []

        # Constantes de error
        self.OK = 1
        self.HABITACION_NO_EXISTE = -1
        self.CLIENTE_NO_EXISTE = -2
        self.RESERVA_NO_EXISTE = -3
        self.HABITACIONES_NO_DISPONIBLES = -4
        self.CLIENTE_NO_TIENE_RESERVAS = -5
        self.FECHA_NO_DISPONIBLE = -6


        for i in range(num_habitaciones):
            self.nueva_habitacion(i)
        
    def __str__(self):
        pass

    def nuevo_cliente(self, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        self.__agregar_cliente(cliente)
    
    def __agregar_cliente(self, cliente ):
        self._clientes.append(cliente)

    def nueva_habitacion(self, num_habitacion):
        habitacion = Habitacion(num_habitacion)
        self.__agregar_habitacion(habitacion)
    
    def __agregar_habitacion(self, habitacion ):
        self._habitaciones.append(habitacion)

    def reservar_habitacion(self, dni_cliente, fecha, num_habitacion = None) -> None:
        habitacion = self.buscar_habitacion(num_habitacion) if num_habitacion else self.obtener_habitacion_disponible_en_fecha(fecha)
        
        if(habitacion and habitacion.esta_reservada(fecha)):
            self.imprime_errores(self.FECHA_NO_DISPONIBLE)
            return
        elif(cliente := self.buscar_cliente(dni_cliente)):
            reserva = Reserva(habitacion, cliente, fecha)
            self._reservas.append(reserva)
            habitacion.add_reserva(reserva)
            cliente.add_reserva(reserva)
            self.imprime_errores(self.OK)

    def get_reservas_de_cliente(self, dni):
        cliente = self.buscar_cliente(dni)
        if cliente == self.CLIENTE_NO_EXISTE:
            return self.CLIENTE_NO_EXISTE
        
        return cliente.get_reservas_de_cliente()

    def buscar_habitacion(self, num_habitacion):
        for habitacion in self._habitaciones:
            if(habitacion.get_id() == num_habitacion):
                return habitacion
        self.imprime_errores(self.HABITACION_NO_EXISTE)
    
    def buscar_cliente(self, dni) -> Cliente:
        for cliente in self._clientes:
            if(cliente.get_id() == dni):
                return cliente
        self.imprime_errores(self.CLIENTE_NO_EXISTE)

    def buscar_reserva(self, num_reserva):
        for reserva in self._reservas:
            if(reserva.get_id() == num_reserva):
                return reserva
        self.imprime_errores(self.RESERVA_NO_EXISTE)

    def imprime_errores(self, cod_error):
        errores = {self.HABITACION_NO_EXISTE: "Habitación no existente", 
                   self.CLIENTE_NO_EXISTE: "Cliente no existenete", 
                   self.RESERVA_NO_EXISTE: "Reserva no existente", 
                   self.HABITACIONES_NO_DISPONIBLES: "Todas las habitaciones ocupadas",
                   self.OK: "Todo bien", 
                   self.CLIENTE_NO_TIENE_RESERVAS: "El cliente no tiene reservas", 
                   self.FECHA_NO_DISPONIBLE: "Fecha no disponible"
                   }
        print(errores[cod_error])

    def obtener_habitacion_disponible_en_fecha(self, fecha):
        for habitacion in self._habitaciones:
            if(not habitacion.esta_reservada(fecha)):
                return habitacion
        self.imprime_errores(self.HABITACIONES_NO_DISPONIBLES)

    def cancelar_reserva(self, id_reserva):
        if self.buscar_reserva(id_reserva) != None:
            self._reservas[id_reserva] = None
            return self.OK
        self.imprime_errores(self.RESERVA_NO_EXISTE)
        return self.RESERVA_NO_EXISTE
        
    def cancelar_reserva(self, num_habitacion, dni, fecha):
        for i in range(len(self._reservas)):
            if( self._reservas[i].get_fecha == fecha and self._reservas[i].get_id_cliente == dni and self._reservas[i].get_id_habitacion == num_habitacion):
                self.imprime_errores(self.OK)
        
        return self.RESERVA_NO_EXISTE