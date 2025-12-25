from services.conductores import Conductores
from services.vehiculos import Vehiculos
from models.conductor import Conductor
from models.vehiculo import Moto, Camion, Carro

def main():
    
    C = [Conductor("AAA",1,"111111","111111"),
        Conductor("BBB",2,"222222","21-13-11#2"),
        Conductor("CCC",3,"45746801","Hola2356222o")]
    
    V = [Moto(11),Carro(22),Camion(33)]
    
    conductores = Conductores()
    vehiculos = Vehiculos()
    
    for conductor in C:
        conductores.agregar_conductor(conductor)
        
    
    
    for vehiculo in V:
        vehiculos.agregar_vehiculo(vehiculo)
        
        
    conductores.tabla_conductores()
    vehiculos.tabla_vehiculos()
    
    vehiculos.modificar_vehiculo(conductores, 11, 1)
    
    vehiculos.tabla_vehiculos()
    
    vehiculos.modificar_vehiculo(conductores, 11)
    
    vehiculos.tabla_vehiculos()
    
if __name__ == "__main__": main()



