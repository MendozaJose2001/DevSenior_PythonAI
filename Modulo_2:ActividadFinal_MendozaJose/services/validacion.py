# ./services/validacion.py

def validar_nombre(valor: str) -> str:
    if isinstance(valor, str) and valor.strip() != "":
        return valor.strip().upper()
    else:
        raise ValueError("El nombre debe ser un texto no vacio")
    
def validar_id(valor: int) -> int:
    if isinstance(valor, int) and valor > 0:
        return valor
    else:
        raise ValueError("La ID debe ser un entero positivo")
    
    
def validar_documento(valor: str) -> str:
    if isinstance(valor, str):
        
        solo_numeros = "".join(filter(str.isdigit, valor))
        
        if 6 <= len(solo_numeros) <= 10: 
            return solo_numeros
        else:
            raise ValueError("En colombia, El numero de documento debe tener de 6 a 10 digitos")  
    else:
        raise ValueError("El numero de documento debe ser una cadena de texto")
    
    
def validar_int(valor: int) -> int:
    if isinstance(valor, int) and valor > 0:
        return valor
    else:
        raise ValueError("El valor ingresado debe ser un entero positivo")
    
    