# Proyecto-Final
Banco de Sangre
# 🩸 Sistema de Gestión para Banco de Sangre

Sistema desarrollado en Python con Tkinter para la administración de inventario, usuarios, pedidos y distribución de sangre entre sucursal principal y sucursales.

---

# 📌 Descripción General

Este proyecto fue diseñado para facilitar la gestión interna de un banco de sangre mediante una interfaz gráfica intuitiva y un sistema basado en archivos `.txt` como base de datos.

El sistema permite:

* Gestión de usuarios y administradores.
* Inicio de sesión seguro.
* Recuperación de cuentas.
* Control de inventario.
* Gestión de pedidos entre sucursales.
* Aprobación o rechazo de solicitudes.
* Envío automático de stock.
* Visualización de observaciones administrativas.
* Registro de movimientos.

---

# 🛠️ Tecnologías Utilizadas

* Python 3
* Tkinter
* OS
* Archivos TXT como almacenamiento persistente

---

# 📂 Estructura del Proyecto

```text
Banco_de_Sangre/
│
├── Sistema.py
│
├── Archivos_BD/
│   │
│   ├── Usuarios/
│   │   └── Usuarios.txt
│   │
│   ├── Sede_principal/
│   │   ├── Inventario/
│   │   └── Registro/
│   │       └── Pedidos.txt
│   │
│   └── Sucursales/
│       ├── Sucursal_1/
│       ├── Sucursal_2/
│       └── ...
```

---

# 🔐 Funcionalidades Principales

## 👤 Sistema de Usuarios

* Inicio de sesión.
* Registro de usuarios.
* Administradores y sucursales.
* Desbloqueo de usuarios.
* Recuperación de usuario y contraseña.

---

## 🩸 Gestión de Inventario

* Visualización de bolsas disponibles.
* Actualización automática de stock.
* Envío de sangre desde sede principal.
* Inventario independiente por sucursal.

---

## 📦 Sistema de Pedidos

Las sucursales pueden:

* Realizar pedidos de sangre.
* Ver historial de solicitudes.
* Consultar estado del pedido.

Los administradores pueden:

* Ver todos los pedidos.
* Aprobar solicitudes.
* Rechazar solicitudes.
* Escribir observaciones.
* Enviar automáticamente stock a sucursales.

---

## 📋 Historial y Observaciones

Cada pedido guarda:

* ID
* Fecha
* Usuario
* Sucursal
* Cantidad
* Estado
* Observaciones administrativas

---

# 🖥️ Interfaz Gráfica

El sistema usa Tkinter y cuenta con:

* Ventanas dinámicas.
* Ajuste automático de tamaño.
* Botones personalizados.
* Tablas con `Treeview`.
* Scroll automático.
* Navegación entre pantallas.

---

# 🔄 Flujo del Sistema

## Sucursal

```text
Inicio de sesión
       ↓
Realizar pedido
       ↓
Esperar aprobación
       ↓
Ver estado y observaciones
```

---

## Administrador

```text
Inicio de sesión
       ↓
Gestionar pedidos
       ↓
Aprobar/Rechazar
       ↓
Enviar stock automáticamente
```

---

# 🔒 Recuperación de Cuenta

El sistema incluye:

* Recuperación de usuario.
* Recuperación de contraseña.
* Validación mediante:

  * Nombre
  * Documento

El nombre es flexible ante:

* Mayúsculas
* Minúsculas
* Tildes
* Espacios extra

El documento mantiene validación estricta.

---

# ⚙️ Características Técnicas

## ✔️ Manejo de archivos

La información se guarda mediante archivos `.txt` estructurados.

## ✔️ Separación de funciones

El sistema está modularizado mediante funciones reutilizables.

## ✔️ Actualización automática de interfaz

Las ventanas ajustan automáticamente su tamaño según el contenido mostrado.

---

# 🚀 Cómo Ejecutar el Proyecto

## 1. Instalar Python

Descargar Python:

[Python Official Website](https://www.python.org?utm_source=chatgpt.com)

---

## 2. Ejecutar el sistema

Desde consola:

```bash
python Sistema.py
```

---

# 📌 Requisitos

* Python 3.10 o superior
* Tkinter instalado

---

# 📈 Posibles Mejoras Futuras

* Migración a SQLite/MySQL.
* Cifrado de contraseñas.
* Reportes PDF.
* Estadísticas y gráficas.
* Sistema multiusuario en red.
* Notificaciones automáticas.
* Panel administrativo avanzado.
* Control de vencimiento de sangre.

---

# 👨‍💻 Autor

Proyecto desarrollado por:

**Juan Sebastian Garzon Garzon**

---

# 📄 Licencia

Proyecto educativo y académico. Uso libre para aprendizaje y mejora del sistema.
