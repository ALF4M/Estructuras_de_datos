# -*- coding: utf-8 -*-

from Cliente import Cliente
from Habitacion import Habitacion
from Reserva import Reserva
from HashTable import HashTable

class Hotel:
    def __init__(self, num_habitaciones):
        self.__habitaciones = []
        self.__clientes = HashTable()
        self.__reservas = HashTable()

        for i in range(num_habitaciones):
            self.nueva_habitacion(i+1)

        # Constantes de error
        self.OK = 1
        self.HABITACION_NO_EXISTE = -1
        self.CLIENTE_NO_EXISTE = -2
        self.RESERVA_NO_EXISTE = -3
        self.HABITACIONES_NO_DISPONIBLES = -4
        self.CLIENTE_NO_TIENE_RESERVAS = -5
        self.FECHA_NO_DISPONIBLE = -6
        
    def __str__(self):
        pass

    ###/////////////////###
    ###     METODOS     ###
    ###/////////////////###

    # CLIENTE -----------------------
    def nuevo_cliente(self, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        self.__agregar_cliente(cliente)
    
    def __agregar_cliente(self, cliente):
        self.__clientes.insertar(cliente.id,(cliente,[]))
    
    def buscar_cliente(self, dni, pinta= False) -> Cliente:
        try:
            cliente = self.__clientes.obtener(dni)
        except:
            self.imprime_errores(self.CLIENTE_NO_EXISTE)
        else:
            print(cliente[0]) if pinta else None
            return cliente[0]


    # HABITACION --------------------
    def nueva_habitacion(self, num_habitacion):
        habitacion = Habitacion(num_habitacion)
        self.__agregar_habitacion(habitacion)
    
    def __agregar_habitacion(self, habitacion ):
        self.__habitaciones.append(habitacion)
    
    def buscar_habitacion(self, num_habitacion):
        for habitacion in self.__habitaciones:
            if(habitacion.id == num_habitacion):
                return habitacion
        self.imprime_errores(self.HABITACION_NO_EXISTE)
    
    def habitacion_reservada(self,habitacion,fecha):
        try:
            self.__reservas.obtener(f'{habitacion.id}:{fecha}')
            return True
        except:
            return False
    
    def obtener_habitacion_disponible_en_fecha(self, fecha):
        for habitacion in self.__habitaciones:
            if(not self.habitacion_reservada(habitacion,fecha)):
                return habitacion
        self.imprime_errores(self.HABITACIONES_NO_DISPONIBLES)

    
    # RESERVA -----------------------
    def nueva_reserva(self, dni_cliente, fecha, num_dias=1, num_habitacion = None) -> None:
        fecha = list(map(lambda x: int(x),fecha.split('/')))
        fechas = []
        for dia in range(1,num_dias+1):
            if(fecha[0]+dia > 31):
                fecha[0] = 1
                fecha[1] += 1
            else:
                if(dia != 1):fecha[0] += 1
            
            if(fecha[1] > 12):
                fecha[1] = 1
                fecha[2] += 1

            fechas.append(f'{fecha[0] if fecha[0] > 9 else f"0{fecha[0]}"}/{fecha[1] if fecha[1] > 9 else f"0{fecha[1]}"}/{fecha[2]}')
        print(fechas)
        for fecha in fechas:
            habitacion = self.buscar_habitacion(num_habitacion) if num_habitacion else self.obtener_habitacion_disponible_en_fecha(fecha)
            
            if(habitacion and self.habitacion_reservada(habitacion,fecha)):
                self.imprime_errores(self.FECHA_NO_DISPONIBLE)
                return
            elif(cliente := self.buscar_cliente(dni_cliente)):
                reserva = Reserva(habitacion.id, cliente.id, fecha)
                self.__reservas.insertar(reserva.id,(habitacion.id, fecha, cliente.nombre))
                self.__clientes.insertar(dni_cliente,(cliente,self.__clientes.obtener(dni_cliente)[1]+[reserva]))
                self.imprime_errores(self.OK)
    
    def buscar_reserva(self, num_habitacion,fecha):
        try:
            reserva = self.__reservas.obtener(f'{num_habitacion}:{fecha}')
        except:
            self.imprime_errores(self.RESERVA_NO_EXISTE)
        else:
            print(reserva)
    
    def cancelar_reserva(self, num_habitacion, fecha):
        try:
            self.__reservas.eliminar(f'{num_habitacion}:{fecha}')
        except:
            self.imprime_errores(self.RESERVA_NO_EXISTE)
        else:
            self.imprime_errores(self.OK)


    # MIXTOS ------------------------
    def get_reservas_de_cliente(self, dni):
        try:
            cliente = self.__clientes.obtener(dni)
        except:
            self.imprime_errores(self.CLIENTE_NO_EXISTE)
        else:
            for reserva in cliente[1]:
                print(reserva)


    # ERRORES -----------------------
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