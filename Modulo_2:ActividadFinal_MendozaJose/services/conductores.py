# ./services/conductores.py

from typing import Optional, Dict, List
from models.conductor import Conductor 


class Conductores():
    
    def __init__(self) -> None:
        self._conductores: Dict[int, Conductor] = {}
        
    def agregar_conductor(self, conductor: Conductor) -> None:
        
        if not isinstance(conductor, Conductor):
            raise ValueError("Se debe ingresar un Objeto tipo Conductor")
            
        if conductor.id_conductor in self._conductores:
            raise ValueError("El Conductor ya se encuentra registrado")
            
        self._conductores[conductor.id_conductor] = conductor 
            
        
    def buscar_conductor(self, id: int) -> Optional[Conductor]:
        return self._conductores.get(id)
    
    def eliminar_conductor(self, id: int) -> None:
        
        if id not in self._conductores:
            raise ValueError("El Conductor no se encuentra registrado")
            
        del self._conductores[id] 
        
    def listar_conductores(self) -> List[Conductor]:
        return list(self._conductores.values())
        
    def tabla_conductores(self) -> None:
        
        print(f"-----------------------\n"
            f"\n ID        Nombre      ")
        
        for conductor in self.listar_conductores():
            print(f"~ {conductor.id_conductor} | {conductor.nombre}")
            
        print("\n-------------------------")
         