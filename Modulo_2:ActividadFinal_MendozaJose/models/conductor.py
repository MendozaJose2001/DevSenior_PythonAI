# ./models/conductor.py

from services.validacion import validar_nombre, validar_id, validar_documento

class Conductor():
    
    def __init__(self, nombre: str, id_conductor: int, documento: str, licencia: str) -> None:
        self.nombre = nombre
        self.id_conductor = id_conductor
        self.documento = documento
        self.licencia = licencia
        
    @property
    def nombre(self) -> str: return self._nombre
    
    @property
    def id_conductor(self) -> int: return self._id_conductor
    
    @property
    def documento(self) -> str: return self._documento
    
    @property
    def licencia(self) -> str: return self._licencia
    
    @nombre.setter
    def nombre(self, valor: str) -> None: self._nombre = validar_nombre(valor)
        
    @id_conductor.setter
    def id_conductor(self, valor: int) -> None: self._id_conductor = validar_id(valor)
    
    @documento.setter
    def documento(self, valor: str) -> None: self._documento = validar_documento(valor)
    
    """
    En colombia, y muchos otros paises, el numero del documento identificacion (cedula)
    es el mismo numero de licencia de conducir.
    """
    @licencia.setter
    def licencia(self, valor: str) -> None: self._licencia = validar_documento(valor) 
    
    
    def __str__(self) -> str:
        return(f"\n --- Resumen de Conductor --- \n"
               f"~ Nombre: {self.nombre} \n"
               f"~ ID: {self.id_conductor} \n"
               f"~ Documento: {self.documento} \n"
               f"~ Licencia: {self.licencia} \n"
               f"----------------------------- \n")
    