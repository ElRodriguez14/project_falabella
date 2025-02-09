# 🏗️ Prueba Técnica Ingeniero de Desarrollo

## 📌 Falabella Colombia

### 📋 Descripción
La empresa **Rios del Desierto SAS** necesita una herramienta para el equipo de SAC que permita consultar la información de un cliente ingresando únicamente su número de documento. Esto reducirá los tiempos de respuesta en llamadas de soporte y permitirá fidelizar a los mejores clientes.

---

## 📌 Requerimientos

1. **Modelo de Datos**
   - Crear una base de datos con la información de los clientes, incluyendo:
     - Tipo de documento
     - Número de documento
     - Nombre
     - Apellido
     - Correo
     - Teléfono
   - Crear una relación con las compras de cada cliente.

2. **Frontend**
   - Una página web básica con un formulario para buscar clientes por tipo y número de documento.

3. **API Backend**
   - Un servicio REST para consultar la información de los clientes.
   - La base de datos debe ser SQLite.

4. **Exportación de Datos**
   - Permitir exportar la información del cliente en formato CSV, Excel o TXT.

5. **Fidelización de Clientes**
   - Generar un reporte en Excel con clientes que superen los **5.000.000 COP** en compras en el último mes.

---

## 🚀 Instalación y Configuración

### 🔹 Prerrequisitos

- Python 3.10+
- Virtualenv (opcional, pero recomendado)
- Django

### 🔹 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/proyecto-clientes.git
cd proyecto-clientes

# Crear y activar un entorno virtual (opcional)
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 🔹 Migraciones y Base de Datos

```bash
# Crear las migraciones
django-admin migrate
```

### 🔹 Ejecutar el Servidor

```bash
python manage.py runserver
```

---

## 📡 API Endpoints

| Método | Endpoint                | Descripción                 |
|--------|-------------------------|-----------------------------|
| GET    | /api/clientes/{id}/     | Obtener cliente por ID      |
| GET    | /api/compras/{id}/      | Obtener compras de cliente  |
| GET    | /api/exportar/{id}/     | Exportar datos del cliente  |
| GET    | /api/reporte/           | Generar reporte de clientes |

---

## 📦 Entregables

✅ Guía de implementación 📖  
✅ Código en GIT 📂  
✅ Documentación técnica 📝  
✅ Video explicativo 🎥  
✅ Base de datos con datos de prueba 📊  

---

## 👨‍💻 Tecnologías Utilizadas

- Python 🐍
- Django 🕸️
- SQLite 🗄️
- Pandas 📊
- Django REST Framework 🔗

---

## 📧 Contacto

Si tienes alguna duda o sugerencia, puedes contactarme.

