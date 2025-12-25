# Sistema de Gestión de Vehículos y Conductores

Sistema de gestión para **Transporte Seguro S.A.** que digitaliza la operación básica de la empresa, permitiendo gestionar conductores, vehículos y sus relaciones de manera eficiente.

## 📋 Descripción

Sistema orientado a objetos que implementa la gestión completa de:
- **Conductores**: Registro con validación de datos (nombre, documento, licencia)
- **Vehículos**: Tres tipos (Moto, Carro, Camión) con características diferenciadas
- **Relaciones**: Asignación de conductores a vehículos
- **Operaciones**: Inicio de jornadas de trabajo y verificación de requisitos

## 🏗️ Arquitectura

El sistema implementa principios de POO:

- **Abstracción**: Clase abstracta `Vehiculo` con métodos abstractos
- **Encapsulación**: Atributos privados con properties y validación
- **Herencia**: Subclases `Moto`, `Carro`, `Camión` especializadas
- **Polimorfismo**: Métodos `mover()` y `requisitos()` con comportamiento diferenciado
- **Composición**: Cada vehículo contiene un `Motor`
- **Agregación**: Vehículos pueden existir sin conductor asignado
- **Interfaces**: `Movible` como contrato para objetos móviles

## 📁 Estructura del Proyecto

```
.
├── models/
│   ├── __init__.py
│   ├── conductor.py      # Clase Conductor
│   ├── motor.py          # Clase Motor (composición)
│   ├── movible.py        # Interfaz Movible
│   └── vehiculo.py       # Clase abstracta Vehiculo + subclases
├── services/
│   ├── __init__.py
│   ├── conductores.py    # Gestión CRUD de conductores
│   ├── validacion.py     # Funciones de validación
│   └── vehiculos.py      # Gestión CRUD de vehículos
├── main.py               # Programa principal con tests
├── .gitignore
└── README.md
```

## 🚀 Características

### Gestión de Conductores
- Registro con validación de datos
- Búsqueda por ID
- Eliminación de registros
- Listado completo

### Gestión de Vehículos
- Tres tipos: Moto, Carro, Camión
- Motor integrado (composición)
- Asignación/desasignación de conductores
- Verificación de requisitos específicos:
  - **Moto**: Casco obligatorio
  - **Carro**: Revisión técnico-mecánica vigente
  - **Camión**: Planilla de carga y peso máximo

### Operaciones
- Inicio de jornada de trabajo (polimorfismo)
- Validación de datos en tiempo real
- Manejo de excepciones

## 💻 Requisitos

- Python 3.10 o superior
- No requiere dependencias externas

## 🔧 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/MendozaJose2001/DevSenior_PythonAI.git

# Navegar al directorio
cd ./DevSenior_PythonAI/Modulo_2:ActividadFinal_MendozaJose

# Ejecutar el programa
python3 main.py
```

## 🧪 Tests

El archivo `main.py` incluye pruebas exhaustivas:

```bash
python3 main.py
```

**Pruebas incluidas:**
- CRUD de conductores (crear, buscar, eliminar, listar)
- CRUD de vehículos (crear, buscar, eliminar, listar)
- Asignación y desasignación de conductores
- Inicio de jornadas de trabajo (polimorfismo)
- Verificación de requisitos diferenciados

## 📝 Validaciones

El sistema valida automáticamente:

- **Nombre**: Texto no vacío
- **ID**: Entero positivo único
- **Documento**: 6-10 dígitos numéricos (formato colombiano)
- **Licencia**: 6-10 dígitos numéricos
- **Conductor**: Instancia válida de `Conductor` o `None`
- **Vehículo**: Instancia válida de `Vehiculo`

## 👤 Autor

Mendoza Arango, Jose Daniel

## Fecha

Diciembre 2025

---

**Nota**: Este programa forma parte de la Actividad Final del Módulo 2, demostrando la comprensión de conceptos fundamentales de Programación Orientada a Objetos. 
