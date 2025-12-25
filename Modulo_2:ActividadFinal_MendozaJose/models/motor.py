# ./models/motor.py

from services.validacion import validar_int

class Motor():
    
    def __init__(self, cilindros: int, hp: int) -> None:
        self.cilindros = cilindros
        self.hp = hp
        
    @property
    def cilindros(self) -> int: return self._cilindros
    
    @property
    def hp(self) -> int: return self._hp
    
    @cilindros.setter
    def cilindros(self, valor: int) -> None: self._cilindros = validar_int(valor)
    
    @hp.setter
    def hp(self, valor: int) -> None: self._hp = validar_int(valor)
        
    def __str__(self) -> str:
        return ("\n ---Parametros del Motor--- \n" 
                f"~ Cilindros = {self.cilindros} \n" 
                f"~ HP = {self.hp} \n"
                f"------------------------- \n")


