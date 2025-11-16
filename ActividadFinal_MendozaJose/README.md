# Clasificador de Triángulos

## Descripción del Programa

Este programa determina si tres números pueden formar los lados de un triángulo y, en caso afirmativo, clasifica el tipo de triángulo según sus características geométricas.

## Propósito

El objetivo es aplicar conceptos fundamentales de programación en Python para resolver un problema matemático que involucra:
- Validación de condiciones geométricas (desigualdad triangular)
- Clasificación mediante condicionales anidados
- Modularización del código mediante funciones
- Buenas prácticas de programación

## Funcionalidad

El programa solicita al usuario tres valores numéricos que representan los lados de un potencial triángulo y realiza las siguientes operaciones:

1. **Validación de existencia**: Verifica que los tres números cumplan con la desigualdad triangular (la suma de dos lados debe ser mayor que el tercer lado)
2. **Clasificación**: Si es posible formar un triángulo, determina su tipo:
   - **Equilátero**: Los tres lados son iguales
   - **Isósceles**: Dos lados son iguales
   - **Escaleno**: Todos los lados son diferentes

## Estructura del Código

El programa está organizado en cuatro funciones principales:

### `input_triangle() -> tuple[float, float, float]`
Solicita al usuario los tres valores correspondientes a los lados del triángulo y los retorna como una tupla de números flotantes.

### `possible_triangle(a: float, b: float, c: float) -> bool`
Valida si los tres números pueden formar un triángulo aplicando la desigualdad triangular. Retorna `True` si es posible, `False` en caso contrario.

### `type_triangle(a: float, b: float, c: float) -> str`
Clasifica el tipo de triángulo comparando la igualdad entre sus lados. Retorna una cadena descriptiva del tipo de triángulo.

### `main() -> None`
Función principal que coordina el flujo del programa: obtiene los datos, valida la posibilidad del triángulo y muestra el resultado formateado.

## Buenas Prácticas Aplicadas

- **Modularidad**: El código está dividido en funciones específicas con responsabilidades únicas
- **Nombres descriptivos**: Variables y funciones con nombres claros que indican su propósito
- **Type hints**: Anotaciones de tipo para mayor claridad y mantenibilidad
- **Formateo de salida**: Uso de f-strings con formato de precisión para una presentación profesional
- **Estructura clara**: Uso del patrón `if __name__ == "__main__"` para ejecución controlada

## Posibles Mejoras

Una mejora identificada para versiones futuras del programa sería:

**Validación de entrada numérica**: Agregar un bucle `while` dentro de la función `input_triangle()` para validar que el usuario ingrese valores mayores a cero, ya que un lado de un triángulo no puede tener longitud negativa o nula. Esto mejoraría la robustez del programa y la experiencia del usuario.

Ejemplo de implementación:
```python
def input_triangle() -> tuple[float, float, float]:
    while True:
        a = float(input("Ingrese el primer lado del triángulo: "))
        if a > 0:
            break
        print("Error: El valor debe ser mayor a cero")
    # Similar para b y c
```

## Video Explicativo

**Enlace al video**: https://youtu.be/En8fFSiTfEI

**Duración**: 4:30 minutos

## Autor

Mendoza Arango, Jose Daniel

## Fecha

Noviembre 2025

---

**Nota**: Este programa forma parte de la Actividad Final del Módulo 1, demostrando la comprensión de conceptos fundamentales de Python como funciones, condicionales y buenas prácticas de programación.