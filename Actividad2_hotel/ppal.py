from Hotel import Hotel

mi_hotel = Hotel(100)

mi_hotel.nuevo_cliente("123456789X", "Pepito", "Piscinas")

print(mi_hotel.buscar_cliente("123456789X"))

mi_hotel.reservar_habitacion("123456789X", "05/10/2023")

