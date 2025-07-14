# Food Pantry

Food Pantry es un sistema de gestión para bancos de alimentos desarrollado con Django.  
Permite administrar beneficiarios, donaciones, entregas y el inventario de productos alimentarios.

---

## Tecnologías utilizadas

- Python 3.11+
- Django 4.x
- SQLite (modo desarrollo)
- HTML/CSS (interfaz básica del admin de Django)
- Git y GitHub

---

## Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/food_pantry.git
cd food_pantry
```

2. Crear un entorno virtual y activarlo

```bash
python3 -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instalar las dependencias

```
pip install -r requirements.txt
```

4. Aplicar migraciones

```
python manage.py migrate
```

5. Ejecutar el servidor de desarollo

```
python manage.py runserver
```

## Estructura del proyecto

```
food_pantry/
├── food_pantry/         Configuración principal de Django
├── food_pantry_app/     Lógica del sistema
├── manage.py            Archivo de control del proyecto
├── venv/                 Entorno virtual (no incluido en el repositorio)
├── requirements.txt     Lista de dependencias
└── README.md
```
## Pruebas
```
python manage.py test
```

## Equipo de desarollo

  - nombre1 - Coordinador general
  - nombre2 - Back
  - nombre3 - Front
  - nombre4 - BD y Documentacion

## Estado del proyecto
Este sistema se encuentra actualmente en desarrollo como parte de una entrega académica

## Licencia
Todos los derechos reservados. Proyecto realizado con fines educativos.
