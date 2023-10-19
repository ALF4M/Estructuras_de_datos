class HashTable:
    def __init__(self, capacidad=100):
        self.__tabla = [None] * capacidad
    

    ###////////////////////////////###
    ###     METODOS ESPECIALES     ###
    ###////////////////////////////###

    # HASH --------------------------
    def __hash(self,key):
        A = (5 ** 0.5 - 1) / 2  #(El Golden Ratio consiste en un número irracional representado por la letra griega φ (phi) o Φ (Phi))
        scaled_key = int(100 * (sum(ord(char) for char in key) * A % 1))
        return scaled_key


    ###/////////////////###
    ###     METODOS     ###
    ###/////////////////###

    # INSERTAR ----------------------
    def insertar(self, clave, valor):
        indice = self.__hash(clave)
        #print(self.__hash(clave))

        if not self.__tabla[indice]:
            self.__tabla[indice] = [(clave, valor)]
        else:
            #print(self.__tabla[indice])
            clave_repetida = [(key,value) for key,value in self.__tabla[indice] if key == clave]
            if(clave_repetida):
                self.__tabla[indice].remove(clave_repetida[0])
            
            self.__tabla[indice].append((clave,valor))

    # OBTENER -----------------------
    def obtener(self, clave):
        indice = self.__hash(clave)
        slot = self.__tabla[indice]
        if(slot):
            for key, value in slot:
                if(clave == key):
                    return value
        raise KeyError('La clave no existe')
    
    # ELIMINAR -----------------------
    def eliminar(self, clave):
        indice = self.__hash(clave)
        clave_valor = [(key,value) for key,value in self.__tabla[indice] if key == clave]
        if(clave_valor):
            self.__tabla[indice].remove(clave_valor[0])
        else:
            raise KeyError('La clave no existe')

'''
table=HashTable()
table.insertar('Hola','Quetal')
table.insertar('Adios','Quetal')
table.insertar('Prueba','Quetal')
table.insertar('Esternocleidomastoideo','Quetal')
table.insertar('mecagoenlosmuertosdelamadrequemepario','Quetal')
print(table.obtener('Prueba'))
'''

'''
table=HashTable()
table.insertar('Prueba','Adios')
table.insertar('Prueba','Quetal')
print(table.obtener('Prueba'))
'''
