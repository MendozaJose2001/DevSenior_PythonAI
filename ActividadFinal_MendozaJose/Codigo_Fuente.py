
"""
Enunciado:
Crea un programa que lea tres números diferentes y determine si pueden formar los 
lados de un triángulo. Si es posible, indica qué tipo de triángulo es:

Equilátero (tres lados iguales)
Isósceles (dos lados iguales)
Escaleno (todos diferentes)

Competencia que evalúa:
Uso de condicionales anidados, operadores lógicos y validación de relaciones 
numéricas para clasificar casos múltiples.

"""
#----------------------
# Solicita y valida tres numeros (lados de un triangulo)
#-----------------------

def input_triangle()-> tuple[float,float,float]:
    
    a=float(input("Ingrese el primer lado del triangulo: ")) 
    b=float(input("Ingrese el segundo lado del triangulo: "))
    c=float(input("Ingrese el tercer lado del triangulo: "))
    
    return a, b, c


#-------------------------
# Validar si es posible el triangulo
#--------------------------

def possible_triangle(a:float,b:float,c:float) -> bool:
    return (c < a + b) and (b < c + a) and (a < b + c)
    
#------------------------
# Estima el tipo de triangulo
#--------------------------
def type_triangle(a:float,b:float,c:float) -> str:
    
    if a == b == c:
        return "Triángulo Equilátero"
    elif a == b or b == c or c == a:
        return "Triángulo Isósceles"
    else:
        return "Triángulo Escaleno"
        
def main() -> None:
    a,b,c = input_triangle()
    print("---------------------------------------")
    if (possible_triangle(a,b,c)):
        print(f"El Triangulo con lados {a:.2f},{b:.2f} y {c:.2f} es un {type_triangle(a,b,c)}")
    else:
        print(f"Los numeros {a:.2f},{b:.2f} y {c:.2f} no pueden formar los lados de un triángulo")
    
    
if __name__ == "__main__":
    main()
    