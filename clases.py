import csv

class Vehiculo():
    def _init_(self, marca, modelo, nruedas):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas

    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv","a", newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print("No existe el archivo vehiculos.csv")
        except Exception as  e:
            print("Error reportado", e)

    def leer_datos_csv(self):
        try:  
            with open("vehiculos.csv","r") as archivo:
                #datos = [(self.__class__, self.__dict__)]
                vehiculos = csv.reader(archivo)
                print(f"Lista de Vehiculos {type(self).__name__}")

                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item[0]:
                        print(item[1])
                print("")

                    


        except FileNotFoundError:
            print("No existe el archivo vehiculos.csv")
        except Exception as  e:
            print("Error reportado", e)             

            

    def _str_ (self):
        return f"Marca {self.marca},Modelo {self.modelo}, {self.nruedas} ruedas"

class  Automovil(Vehiculo): 
    def _init_(self, marca, modelo, nruedas, velocidad, cilindraje ):
        super()._init_(marca, modelo, nruedas) 
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def _str_ (self):
        return Vehiculo._str_(self) + f" {self.velocidad} km/h, {self.cilindraje} cc"    
    
class Particular(Automovil):
    def _init_(self, marca, modelo, nruedas, velocidad, cilindraje, npuesto):
        super()._init_(marca, modelo, nruedas, velocidad, cilindraje) 
        self.npuesto = npuesto

    def get_npuesto(self):
        return self.npuesto

    def set_npuesto(self,npuesto_new):
        self.npuesto = npuesto_new

    def _str_ (self):
        return Automovil._str_(self) + f" Puestos: {self.npuesto}"     
    
class Carga(Automovil):
    def _init_(self, marca, modelo, nruedas, velocidad, cilindraje, carga):
        super()._init_(marca, modelo, nruedas, velocidad, cilindraje) 
        self.carga = carga

    
    def _str_ (self):
        return Automovil._str_(self) + f" Carga: {self.carga} kg"

class  Bicicleta(Vehiculo): 
    def _init_(self, marca, modelo, nruedas, tipo ):
        super()._init_(marca, modelo, nruedas) 
        self.tipo = tipo
        

    def _str_ (self):
        return Vehiculo._str_(self) + f" Tipo:{self.tipo} " 


class Motocicleta(Bicicleta):
    def _init_(self, marca, modelo, nruedas, tipo, nradio, cuadro, motor ):
        super()._init_(marca, modelo, nruedas, tipo) 
        self.nradio = nradio
        self.cuadro = cuadro
        self.motor = motor

    
    def _str_ (self):
        return Bicicleta._str_(self) + f" Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nradio}"
    
          

      