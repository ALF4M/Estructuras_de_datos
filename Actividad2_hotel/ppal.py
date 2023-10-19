from Hotel import Hotel


prueba=Hotel(100)

#DEBE DE DAR TODO BIEN
#AÑADIMOS CLIENTES
prueba.nuevo_cliente('52009520B','Jose','Ventura')
prueba.nuevo_cliente('26875828Y','Armando','Paredes')
prueba.nuevo_cliente('65004204V','El','Bola')

#BUSCAMOS CLIENTE
print('BUSQUEDA CLIENTE:')
prueba.buscar_cliente('65004204V',pinta = True)

#AÑADIMOS RESERVAS
print('\n-----------------------------------------')
print('RESERVAS:')
prueba.nueva_reserva('52009520B','20/02/2024',num_dias=2)

#BUSCAMOS UNA RESERVA
print('\n-----------------------------------------')
print('BUSCAMOS RESERVA:')
prueba.buscar_reserva(1,'20/02/2024')


#DEBE DE DAR ERROR YA QUE ESTA YA RESERVADA LA HABITACION
#AÑADIMOS RESERVA
print('\n-----------------------------------------')
print('AÑADIMOS RESERVA FALLO CONTROLADO:')
prueba.nueva_reserva('26875828Y','21/02/2024',num_habitacion=1)

#CONSULTAMOS LAS RESERVAS DE UN CLIENTE EN ESPECIFICO
print('\n-----------------------------------------')
print('CONSULTAMOS RESERVAS:')
prueba.get_reservas_de_cliente('52009520B')

#ELIMINAMOS UNA RESERVA DE JOSE CON DNI 52009520B
print('\n-----------------------------------------')
print('ELIMINAMOS RESERVAS:')
prueba.cancelar_reserva(1,'21/02/2024')

#CONSULTAMOS LA RESERVA PARA VER QUE SE HA ELIMINADO
print('\n-----------------------------------------')
print('BUSCAMOS RESERVA:')
prueba.buscar_reserva(1,'21/02/2024')