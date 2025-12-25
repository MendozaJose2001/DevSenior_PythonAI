from services.conductores import Conductores
from services.vehiculos import Vehiculos
from models.conductor import Conductor
from models.vehiculo import Moto, Camion, Carro

def poblar_conductores(conductores: Conductores) -> None:
    
    C = [Conductor("AAA",1,"111111","111111"),
        Conductor("BBB",2,"222222","21-13-11#2"),
        Conductor("CCC",3,"45746801","Hola2356222o"),
        Conductor("DDD",4,"121424124","13224241"),
        Conductor("EEE",5,"5667777","wrwr2223211")]
    
    for conductor in C:
        conductores.agregar_conductor(conductor)
    
def poblar_vehiculos(vehiculos: Vehiculos) -> None:
    
    V = [Moto(1),Carro(2),Camion(3),Moto(4),Carro(5)]
    
    for vehiculo in V:
        vehiculos.agregar_vehiculo(vehiculo)
            
def prueba_CRUD_conductores(conductores: Conductores) -> None:

    print(f"\n <<<< Prueba de CRUD para Conductores >>>>\n")
    print(f"\nTest 1: Agregar Conductores\n")
    
    poblar_conductores(conductores)
    conductores.tabla_conductores()
    
    print(f"\nTest 2: Buscar conductor (ID = 1)\n")
    
    conductor = conductores.buscar_conductor(id=1)
    print(conductor)
    
    print(f"\nTest 3: Eliminar conductor (ID = 1)\n")
    
    conductores.eliminar_conductor(id=1)
    conductores.tabla_conductores()
    
    print(f"\n <<<< Fin de la Prueba de CRUD >>>>\n")
    
def prueba_CRUD_vehiculos(vehiculos: Vehiculos, conductores: Conductores) -> None:
    
    print(f"\n <<<< Prueba de CRUD para Vehiculos >>>>\n")
    print(f"\nTest 1: Agregar Vehiculos\n")
    
    poblar_vehiculos(vehiculos)
    vehiculos.tabla_vehiculos()
    
    print(f"\nTest 2: Buscar vehiculo (ID = 2)\n")
    
    vehiculo_moto = vehiculos.buscar_vehiculo(id=1)
    print(vehiculo_moto)
    
    print(f"\nTest 3: Eliminar vehiculo (ID = 1)\n")
    
    vehiculos.eliminar_vehiculo(id=1)
    vehiculos.tabla_vehiculos()
    
    print(f"\nTest 4: Asociar conductores a vehiculo\n")
    
    for i in range(2,6):
        vehiculos.modificar_vehiculo(conductores,id_vehiculo=i,id_conductor=i)
    vehiculos.tabla_vehiculos()
    
    print(f"\nTest 5: Desasociar conductor de vehiculo (ID = 5)\n")
    
    vehiculos.modificar_vehiculo(conductores,id_vehiculo=5)
    vehiculos.tabla_vehiculos()
    
    print(f"\n <<<< Fin de la Prueba de CRUD >>>>\n")
    
def prueba_reglas_interfaz_vehiculos(vehiculos: Vehiculos) -> None:
    # Prueba de Interfaz
    
    print(f"\n <<<< Prueba de Interfaz: Vehiculos >>>>\n") 
    
    for vehiculo in vehiculos.listar_vehiculos():
        vehiculo.mover()
        
    print(f"\n <<<< Prueba de Reglas Diferenciadas: Vehiculos >>>>\n") 
    
    for vehiculo in vehiculos.listar_vehiculos():
        vehiculo.requisitos()
        
    print(f"\n <<<< Fin de Pruebas >>>>\n")
    
def main():
    
    #------------------------------ 
    # Iniciar base de datos
    #------------------------------
    conductores = Conductores()
    vehiculos = Vehiculos()
    
    #------------------------------ 
    # Prueba funciones CRUDS
    #------------------------------
    
    prueba_CRUD_conductores(conductores)
    
    prueba_CRUD_vehiculos(vehiculos, conductores)
    
    # ------------------------------
    # Prueba de Metodos de Vehiculos
    # ------------------------------
    
    prueba_reglas_interfaz_vehiculos(vehiculos)
    
if __name__ == "__main__": main()



