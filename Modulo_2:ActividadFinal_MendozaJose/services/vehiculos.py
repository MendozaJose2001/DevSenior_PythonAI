# ./services/vehiculos.py

from typing import Optional, Dict, List
from models.vehiculo import Vehiculo 
from .validacion import validar_id
from .conductores import Conductores

class Vehiculos():
    
    def __init__(self) -> None:
        self._vehiculos: Dict[int, Vehiculo] = {}
        
    def agregar_vehiculo(self, vehiculo: Vehiculo) -> None:
        
        if not isinstance(vehiculo, Vehiculo):
            raise ValueError("Se debe ingresar un Objeto tipo Vehiculo")
            
        if vehiculo.id_vehiculo in self._vehiculos:
            raise ValueError("El Vehiculo ya se encuentra registrado")
            
        self._vehiculos[vehiculo.id_vehiculo] = vehiculo 
            
        
    def buscar_vehiculo(self, id: int) -> Optional[Vehiculo]:        
        return self._vehiculos.get(id)
        
    def modificar_vehiculo(self, 
                           conductores: Conductores,
                           id_vehiculo: int, 
                           id_conductor: Optional[int] = None) -> None:
        
        if not isinstance(conductores, Conductores):
            raise ValueError("Base de Datos no es del tipo Conductores")
            
        vehiculo = self.buscar_vehiculo(id_vehiculo)
        
        if vehiculo is None: 
            raise ValueError(f"El vehiculo {id_vehiculo} no esta registrado")
        
        if id_conductor is None:
            vehiculo.conductor = None 
        else:
            conductor = conductores.buscar_conductor(id_conductor)
            
            if conductor is None: 
                raise ValueError(f"El conductor {id_conductor} no esta registrado en la base de datos")
        
            vehiculo.conductor = conductor

        self._vehiculos[id_vehiculo] = vehiculo
            
    def eliminar_vehiculo(self, id: int) -> None:
        
        if id not in self._vehiculos:
            raise ValueError("El vehiculo no se encuentra registrado")
            
        del self._vehiculos[id] 
            
    def listar_vehiculos(self) -> List[Vehiculo]:
        return list(self._vehiculos.values())
        
    def tabla_vehiculos(self) -> None:
        
        
        print(f"------Tabla de Vehiculos-----\n"
            f"\n ID        Conductor      ")
        
        for vehiculo in self.listar_vehiculos():
            conductor = vehiculo.conductor.nombre if vehiculo.conductor else "Sin conductor asignado"
            print(f"~ {vehiculo.id_vehiculo} | {conductor}")
            
        print("\n-----------------------------")
            