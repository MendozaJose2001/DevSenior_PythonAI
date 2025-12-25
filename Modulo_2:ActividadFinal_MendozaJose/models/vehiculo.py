# ./models/vehiculo.py

from abc import ABC, abstractmethod
from typing import Optional
from services.validacion import validar_id
from .motor import Motor
from .conductor import Conductor
from .movible import Movible


class Vehiculo(ABC):
        
    def __init__(self, id_vehiculo: int) -> None:
        self.id_vehiculo = id_vehiculo
        self.conductor = None
        
    @property
    def id_vehiculo(self) -> int: return self._id_vehiculo
    
    @property
    def conductor(self) -> Optional[Conductor]: return self._conductor
    
    @id_vehiculo.setter
    def id_vehiculo(self, valor: int) -> None: self._id_vehiculo = validar_id(valor)   
    
    @conductor.setter
    def conductor(self, valor: Optional[Conductor]) -> None:
        if valor is None:
            self._conductor = valor
        elif isinstance(valor, Conductor): 
            self._conductor = valor
        else:
            raise ValueError("Se debe ingresar un Objeto tipo Conductor o None")
 
            
    @abstractmethod
    def requisitos(self) -> None:
        pass
    
    @abstractmethod
    def tipo_vehiculo(self) -> str:
        pass
    
    def __str__(self) -> str:
        
        conductor_id = self.conductor.id_conductor if self.conductor else "Sin conductor asignado"
            
        return(f"\n ------ Resumen de Vehiculo ------ \n"
            f"~ ID: {self.id_vehiculo} \n"
            f"~ Tipo: {self.tipo_vehiculo()} \n"
            f"~ Conductor: {conductor_id} \n"
            f"~ Motor: {self.motor.hp} HP y {self.motor.cilindros} Cilindros \n"
            "-----------------------------------")
        
class Moto(Vehiculo, Movible):
    
    def __init__(self, id_vehiculo: int) -> None:
        super().__init__(id_vehiculo)
        self._motor = Motor(1, 50)
        
    @property
    def motor(self) -> Motor: return self._motor
    
    def mover(self) -> None:
        if self.conductor:
            print(f"\nNoticia: La moto {self.id_vehiculo} ha iniciado su jornada de trabajo!\n")
        else:
            print(f"\nNoticia: La moto {self.id_vehiculo} no tiene conductor asignado!\n")
        
    def requisitos(self) -> None:
        print(f"\n ------ Requisitos: Moto ------ \n"
              f" 1) Casco obligatorio \n"
              f" -------------------------------\n")
        
    def tipo_vehiculo(self) -> str:
        return "Moto"
    
        
class Carro(Vehiculo, Movible):
    
    def __init__(self, id_vehiculo: int) -> None:
        super().__init__(id_vehiculo)
        self._motor = Motor(4, 1000)
        
    @property
    def motor(self) -> Motor: return self._motor
    
    def mover(self) -> None:
        if self.conductor:
            print(f"\nNoticia: El carro {self.id_vehiculo} ha iniciado su jornada de trabajo!\n")
        else:
            print(f"\nNoticia: El carro {self.id_vehiculo} no tiene conductor asignado!\n")
        
    def requisitos(self) -> None:
        print(f"\n ------ Requisitos: Carro ------ \n"
              f" 1) Revisión técnico-mecánica vigente \n"
              f" -------------------------------\n")
        
    def tipo_vehiculo(self) -> str:
        return "Carro"
    
class Camion(Vehiculo, Movible):
    def __init__(self, id_vehiculo: int) -> None:
        super().__init__(id_vehiculo)
        self._motor = Motor(10, 15000)
        
    @property
    def motor(self) -> Motor: return self._motor
    
    def mover(self) -> None:
        if self.conductor:
            print(f"\nNoticia: El camión {self.id_vehiculo} ha iniciado su jornada de trabajo!\n")
        else:
            print(f"\nNoticia: El camión  {self.id_vehiculo} no tiene conductor asignado!\n")
        
    def requisitos(self) -> None:
        print(f"\n ------ Requisitos: Camión ------ \n"
              f" 1) planilla de carga \n"
              f" 2) máximo peso permitido \n"
              f" -------------------------------\n")
        
    def tipo_vehiculo(self) -> str:
        return "Camión"