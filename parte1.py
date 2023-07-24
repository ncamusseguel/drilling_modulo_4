from clases import Vehiculo,Automovil

instancias = []

n = int(input("Cuantos vehiculos ingresan: "))

for i in range(n):
    print(f"Datos del automovil {i+1}")
    marca = input("Inserte la marca del Automovil: ")
    modelo = input("Inserte el modelo: ")
    nruedas = int(input("Inserte numero de ruedas: "))
    velocidad = int(input("Inserte velocidad en km/h: "))
    cilindraje = int(input("Inserte cilindraje en cc: "))
    print("")
    auto = Automovil(marca,modelo,nruedas,velocidad,cilindraje)
    instancias.append(auto)

print("Imprimiendo por pantalla los vehiculos: ")



for index,item in enumerate(instancias):
    print(f"Datos del automovil {index + 1} : Marca{item.marca}, Modelo {item.modelo}, {item.nruedas} ruedas, {item.velocidad} km/h, {item.cilindraje} cc")