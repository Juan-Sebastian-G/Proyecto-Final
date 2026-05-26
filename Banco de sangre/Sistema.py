# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Librerias 

import os
import tkinter as tk
from tkinter import ttk
from datetime import datetime

########################################################################################################################################################################################################################

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Creacion y inicio de base de datos
def crear_estructura_bd():
    base_dir = "Archivos_BD"

    # Crear carpeta principal
    os.makedirs(base_dir, exist_ok=True)

    # =========================
    # 📁 Sucursales
    # =========================
    sucursales_dir = os.path.join(base_dir, "Sucursales")
    os.makedirs(sucursales_dir, exist_ok=True)

    sucursales = ["Sucursal_A.txt", "Sucursal_B.txt", "Sucursal_C.txt", "Sucursal_D.txt"]

    for sucursal in sucursales:
        path = os.path.join(sucursales_dir, sucursal)
        open(path, "a").close()  # crea si no existe

    # =========================
    # 📁 Sede principal
    # =========================
    sede_dir = os.path.join(base_dir, "Sede_principal")
    os.makedirs(sede_dir, exist_ok=True)

    # Inventario
    inventario_path = os.path.join(sede_dir, "Inventario.txt")
    open(inventario_path, "a").close()

    # =========================
    # 📁 Registro
    # =========================
    registro_dir = os.path.join(sede_dir, "Registro")
    os.makedirs(registro_dir, exist_ok=True)

    archivos_registro = ["Vencidos.txt", "Enviados.txt", "Pedidos.txt"]

    for archivo in archivos_registro:
        path = os.path.join(registro_dir, archivo)
        open(path, "a").close()

    # =========================
    # 📁 Usuarios
    # =========================
    usuarios_dir = os.path.join(sede_dir, "Usuarios")
    os.makedirs(usuarios_dir, exist_ok=True)

    archivos_usuarios = ["Otros.txt", "Admins.txt"]

    for archivo in archivos_usuarios:
        path = os.path.join(usuarios_dir, archivo)
        open(path, "a").close()

    print("✅ Estructura de base de datos creada correctamente.")


def inicializar_datos():
    base_dir = "Archivos_BD"
    sede_dir = os.path.join(base_dir, "Sede_principal")

    inventario_path = os.path.join(sede_dir, "Inventario.txt")
    admins_path = os.path.join(sede_dir, "Usuarios", "Admins.txt")

    # =========================
    # 📦 Inicializar Inventario
    # =========================
    if os.path.getsize(inventario_path) == 0:
        with open(inventario_path, "w") as f:
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            
            for i in range(60):
                f.write(f"Unidad_{i+1}, FechaIngreso:{fecha_actual}, Estado:Disponible\n")

        print("✅ Inventario inicial creado con 60 unidades.")

    else:
        print("ℹ️ Inventario ya existente.")

    # =========================
    # 👤 Inicializar Admin
    # =========================
    if os.path.getsize(admins_path) == 0:
        with open(admins_path, "w") as f:
            f.write("Nombre:Juan Sebastian\n")
            f.write("Apellido:Garzon Garzon\n")
            f.write("Usuario:TheBossBoss\n")
            f.write("Documento:1020304050\n")
            f.write("Rol:Principal_Admin\n")
            f.write("Estado:Activo\n")
            f.write("----------------------\n")

        print("✅ Administrador por defecto creado.")

    else:
        print("ℹ️ Administradores ya existentes.")


########################################################################################################################################################################################################################


        

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Validaciones
def validar_cedula(cedula):
    return cedula.isdigit() and len(cedula) >= 8 and len(cedula) <= 10


def validar_nombre(texto):
    return all(c.isalpha() or c.isspace() for c in texto)


def validar_usuario(usuario):
    return 7 <= len(usuario) <= 12


def usuario_existe(usuario, ruta_admins, ruta_otros):
    usuario = usuario.lower()

    for ruta in [ruta_admins, ruta_otros]:
        with open(ruta, "r") as f:
            for linea in f:
                if linea.lower().startswith("usuario:"):
                    existente = linea.strip().split(":")[1].lower()
                    if usuario == existente:
                        return True
    return False

########################################################################################################################################################################################################################




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// USUARIOS (login, registro)

def registrar_usuario():
    base = "Archivos_BD/Sede_principal/Usuarios"
    otros_path = os.path.join(base, "Otros.txt")
    admins_path = os.path.join(base, "Admins.txt")

    while True:
        cedula = input("Ingrese cédula: ")
        if not validar_cedula(cedula):
            print("❌ Cédula inválida (debe tener 10 dígitos).")
            continue
        break

    while True:
        nombre = input("Nombres: ")
        apellido = input("Apellidos: ")

        if not validar_nombre(nombre) or not validar_nombre(apellido):
            print("❌ Solo letras permitidas.")
            continue
        break

    while True:
        usuario = input("Nombre de usuario: ")

        if not validar_usuario(usuario):
            print("❌ Debe tener entre 7 y 12 caracteres.")
            continue

        if usuario_existe(usuario, admins_path, otros_path):
            print("❌ Usuario ya existe.")
            continue

        break

    with open(otros_path, "a") as f:
        f.write(f"Nombre:{nombre}\n")
        f.write(f"Apellido:{apellido}\n")
        f.write(f"Usuario:{usuario}\n")
        f.write(f"Documento:{cedula}\n")
        f.write("Rol:Usuario\n")
        f.write("Estado:Activo\n")
        f.write("----------------------\n")

    print("✅ Usuario registrado correctamente.")


def registrar_admin():
    base = "Archivos_BD/Sede_principal/Usuarios"
    admins_path = os.path.join(base, "Admins.txt")
    otros_path = os.path.join(base, "Otros.txt")

    codigo_principal = "1020304050"

    while True:
        cedula = input("Ingrese cédula: ")
        if not validar_cedula(cedula):
            print("❌ Cédula inválida.")
            continue
        break

    while True:
        nombre = input("Nombres: ")
        apellido = input("Apellidos: ")

        if not validar_nombre(nombre) or not validar_nombre(apellido):
            print("❌ Solo letras permitidas.")
            continue
        break

    while True:
        usuario = input("Nombre de usuario: ")

        if not validar_usuario(usuario):
            print("❌ Debe tener entre 7 y 12 caracteres.")
            continue

        if usuario_existe(usuario, admins_path, otros_path):
            print("❌ Usuario ya existe.")
            continue

        break

    # 🔐 Verificación (2 intentos)
    for intento in range(2):
        codigo = input("Ingrese código de administrador: ")

        if codigo == codigo_principal:
            with open(admins_path, "a") as f:
                f.write(f"Nombre:{nombre}\n")
                f.write(f"Apellido:{apellido}\n")
                f.write(f"Usuario:{usuario}\n")
                f.write(f"Documento:{cedula}\n")
                f.write("Rol:Admin\n")
                f.write("Estado:Activo\n")
                f.write("----------------------\n")

            print("✅ Administrador registrado.")
            return

        else:
            print("❌ Código incorrecto.")

    print("⛔ Registro cancelado.")



def cargar_usuarios(ruta):
    usuarios = []
    if not os.path.exists(ruta): return usuarios
    
    with open(ruta, "r") as f:
        usuario_actual = {}
        for linea in f:
            linea = linea.strip()
            # Esto reconoce el separador aunque tenga 22 o 26 guiones
            if linea.startswith("---"):
                if usuario_actual:
                    usuarios.append(usuario_actual)
                    usuario_actual = {}
            else:
                if ":" in linea:
                    # El .strip() aquí es VITAL: limpia espacios en la clave y el valor
                    clave, valor = linea.split(":", 1)
                    usuario_actual[clave.strip()] = valor.strip()
    return usuarios


def guardar_usuarios(ruta, usuarios):
    with open(ruta, "w") as f:
        for u in usuarios:
            for k, v in u.items():
                f.write(f"{k}:{v}\n")
            f.write("----------------------\n")



def login_sistema(usuario_input, password_input):
    u_input = usuario_input.strip().lower()
    p_input = password_input.strip()

    if not u_input or not p_input:
        return "vacio", None

    base = "Archivos_BD/Sede_principal/Usuarios"
    admins = cargar_usuarios(os.path.join(base, "Admins.txt"))
    otros = cargar_usuarios(os.path.join(base, "Otros.txt"))
    # =========================
    # 🔐 Buscar en admins
    # =========================
    for user in admins:
            # Comparamos ignorando mayúsculas y espacios
        if user.get("Usuario", "").lower() == u_input and user.get("Documento") == p_input:
             if user.get("Estado") == "Bloqueado":
                 return "bloqueado", None
             if user.get("Rol") == "Principal_Admin":
                 return "Principal_Admin", user
             else:
                 return "admin", user

    # =========================
    # 👤 Buscar en usuarios
    # =========================
    for user in otros:
        if user.get("Usuario", "").lower() == u_input and user.get("Documento") == p_input:
            if user.get("Estado") == "Bloqueado":
                return "bloqueado", None
            return "usuario", user

    # =========================
    # ❌ No encontrado
    # =========================
    return None, None




########################################################################################################################################################################################################################

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// INVENTARIO / PEDIDOS

def obtener_stock(ruta):
    with open(ruta, "r") as f:
        primera = f.readline().strip()

        if primera.startswith("Stock:"):
            return int(primera.split(":")[1])

    return 0


def actualizar_stock(ruta, nuevo_stock):
    with open(ruta, "r") as f:
        lineas = f.readlines()

    lineas[0] = f"Stock:{nuevo_stock}\n"

    with open(ruta, "w") as f:
        f.writelines(lineas)

def cargar_pedidos(ruta):
    pedidos = []
    actual = {}

    with open(ruta, "r") as f:
        for linea in f:
            linea = linea.strip()

            if linea == "----------------------":
                if actual:
                    pedidos.append(actual)
                    actual = {}
            else:
                if ":" in linea:
                    clave, valor = linea.split(":", 1)
                    actual[clave] = valor

    return pedidos


def guardar_pedidos(ruta, pedidos):
    with open(ruta, "w") as f:
        for p in pedidos:
            for k, v in p.items():
                f.write(f"{k}:{v}\n")
            f.write("----------------------\n")

def aprobar_pedido(pedido):
    sucursal = pedido["Sucursal"]
    cantidad = int(pedido["Cantidad"])

    enviar_automatico(sucursal, cantidad)




########################################################################################################################################################################################################################

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Registro y revicion de pedidodo


def registrar_movimiento(ruta, usuario, accion):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(ruta, "a") as f:
        f.write(f"{fecha} | Usuario:{usuario} | Acción:{accion}\n")


def retirar_sangre(sucursal, usuario):
    ruta = f"Archivos_BD/Sucursales/{sucursal}.txt"

    stock = obtener_stock(ruta)

    if stock <= 0:
        print("❌ No hay unidades disponibles.")
        return

    stock -= 1
    actualizar_stock(ruta, stock)
    registrar_movimiento(ruta, usuario, "Retiro")

    print(f"✅ Retiro realizado. Stock actual: {stock}")

    # 🔥 Verificar mínimo
    if stock <= 3:
        print("⚠️ Stock bajo, enviando unidades automáticamente...")
        enviar_automatico(sucursal, 5)



def enviar_automatico(sucursal, cantidad):
    inventario_path = "Archivos_BD/Sede_principal/Inventario.txt"
    enviados_path = "Archivos_BD/Sede_principal/Registro/Enviados.txt"
    sucursal_path = f"Archivos_BD/Sucursales/{sucursal}.txt"

    # Leer inventario
    with open(inventario_path, "r") as f:
        lineas = f.readlines()

    disponibles = [l for l in lineas if "Disponible" in l]

    if len(disponibles) < cantidad:
        print("❌ No hay suficiente inventario en sede.")
        return

    # Quitar del inventario
    disponibles_restantes = disponibles[cantidad:]

    otras_lineas = [
        l for l in lineas
        if "Disponible" not in l
    ]

    nuevas_lineas = otras_lineas + disponibles_restantes

    with open(inventario_path, "w") as f:
        f.writelines(nuevas_lineas)

    # Sumar a sucursal
    stock = obtener_stock(sucursal_path)
    stock += cantidad
    actualizar_stock(sucursal_path, stock)

    # Registrar envío
    from datetime import datetime
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(enviados_path, "a") as f:
        f.write(f"{fecha} | Sucursal:{sucursal} | Cantidad:{cantidad} | Tipo:Automático\n")

    print(f"🚚 Envío automático realizado a {sucursal}")


def inicializar_sucursales():
    sucursales = ["Sucursal_A", "Sucursal_B", "Sucursal_C", "Sucursal_D"]

    for s in sucursales:
        ruta = f"Archivos_BD/Sucursales/{s}.txt"

        if os.path.getsize(ruta) == 0:
            with open(ruta, "w") as f:
                f.write("Stock:10\n")
                f.write("----------------------\n")


def generar_id_pedido(ruta):
    if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
        return 1

    ultimo_id = 0

    with open(ruta, "r") as f:
        for linea in f:
            if linea.startswith("ID:"):
                ultimo_id = int(linea.split(":")[1])

    return ultimo_id + 1


def crear_pedido(sucursal, usuario):
    ruta = "Archivos_BD/Sede_principal/Registro/Pedidos.txt"

    while True:
        try:
            cantidad = int(input("Cantidad a pedir: "))
            if cantidad <= 0:
                raise ValueError
            break
        except:
            print("❌ Cantidad inválida.")

    pedido_id = generar_id_pedido(ruta)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(ruta, "a") as f:
        f.write(f"ID:{pedido_id}\n")
        f.write(f"Fecha:{fecha}\n")
        f.write(f"Sucursal:{sucursal}\n")
        f.write(f"Usuario:{usuario}\n")
        f.write(f"Cantidad:{cantidad}\n")
        f.write("Estado:Pendiente\n")
        f.write("Observacion:\n")
        f.write("----------------------\n")

    print("✅ Pedido registrado correctamente.")



def procesar_pedidos():
    ruta = "Archivos_BD/Sede_principal/Registro/Pedidos.txt"
    pedidos = cargar_pedidos(ruta)

    pendientes = [p for p in pedidos if p.get("Estado") == "Pendiente"]

    if not pendientes:
        print("✅ No hay pedidos pendientes.")
        return

    for p in pendientes:
        print(f"\nID: {p['ID']}")
        print(f"Sucursal: {p['Sucursal']}")
        print(f"Usuario: {p['Usuario']}")
        print(f"Cantidad: {p['Cantidad']}")

        decision = input("Aprobar (s/n): ").lower()

        if decision == "s":
            aprobar_pedido(p)
            p["Estado"] = "Aprobado"
        else:
            p["Estado"] = "Rechazado"

    guardar_pedidos(ruta, pedidos)



def verificar_vencimientos():
    inventario_path = "Archivos_BD/Sede_principal/Inventario.txt"
    vencidos_path = "Archivos_BD/Sede_principal/Registro/Vencidos.txt"

    nuevas_lineas = []
    vencidas = []

    with open(inventario_path, "r") as f:
        lineas = f.readlines()

    for linea in lineas:
        try:
            partes = linea.strip().split(", ")
            unidad = partes[0]

            fecha_str = partes[1].split(":")[1]
            fecha_ingreso = datetime.strptime(fecha_str, "%Y-%m-%d")

            dias = (datetime.now() - fecha_ingreso).days

            if dias >= 42:
                vencidas.append((unidad, fecha_str))
            else:
                nuevas_lineas.append(linea)

        except:
            # Si algo falla, dejamos la línea intacta
            nuevas_lineas.append(linea)

    # 🔄 Actualizar inventario (sin vencidas)
    with open(inventario_path, "w") as f:
        f.writelines(nuevas_lineas)

    # 📝 Registrar vencidas
    if vencidas:
        with open(vencidos_path, "a") as f:
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")

            for unidad, fecha_ingreso in vencidas:
                f.write(f"{fecha_actual} | {unidad} | Ingreso:{fecha_ingreso} | Estado:Vencido\n")

        print(f"⚠️ {len(vencidas)} unidades vencidas eliminadas.")
    else:
        print("✅ No hay unidades vencidas.")

########################################################################################################################################################################################################################


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Intereccion de usuario admin.

def buscar_usuario(usuario, ruta):
    usuarios = cargar_usuarios(ruta)

    for u in usuarios:
        if u.get("Usuario", "").lower() == usuario.lower():
            return u

    return None


def bloquear_usuario():
    base = "Archivos_BD/Sede_principal/Usuarios"
    otros_path = os.path.join(base, "Otros.txt")

    usuario = input("Usuario a bloquear: ")

    usuarios = cargar_usuarios(otros_path)
    encontrado = False


    for u in usuarios:
        if u.get("Usuario", "").lower() == usuario.lower():

            if u.get("Rol") == "Principal_Admin":
                print("❌ No puedes bloquear al Administrador Principal")
                return



            
            u["Estado"] = "Bloqueado"
            encontrado = True
            print("🔒 Usuario bloqueado.")
            break

    if not encontrado:
        print("❌ Usuario no encontrado.")
        return

    guardar_usuarios(otros_path, usuarios)  # reutilizamos función



def desbloquear_usuario():
    base = "Archivos_BD/Sede_principal/Usuarios"
    otros_path = os.path.join(base, "Otros.txt")

    usuario = input("Usuario a desbloquear: ")

    usuarios = cargar_usuarios(otros_path)
    encontrado = False


    for u in usuarios:
        if u.get("Usuario", "").lower() == usuario.lower():
            u["Estado"] = "Activo"
            encontrado = True
            print("🔓 Usuario desbloqueado.")
            break

    if not encontrado:
        print("❌ Usuario no encontrado.")
        return

    guardar_usuarios(otros_path, usuarios)



def eliminar_usuario_logica(username):
    """
    Busca y elimina un usuario en Admins.txt o Otros.txt.
    Retorna el estado del proceso para que la UI decida qué mostrar.
    """
    base = "Archivos_BD/Sede_principal/Usuarios"
    rutas = ["Admins.txt", "Otros.txt"]
    eliminado_global = False

    for archivo in rutas:
        path = os.path.join(base, archivo)
        usuarios = cargar_usuarios(path)

        nuevos = []
        for u in usuarios:
            if u.get("Usuario", "").lower() == username.lower():
                if u.get("Rol") == "Principal_Admin":
                    return "no_eliminar"  # Protección para el Super Admin
                eliminado_global = True
                # Al NO agregarlo a la lista 'nuevos', se borra del archivo
            else:
                nuevos.append(u)

        if eliminado_global:
            guardar_usuarios(path, nuevos)
            return "ok"

    return "no_encontrado"

def listar_usuarios(mostrar_password=False):
    base = "Archivos_BD/Sede_principal/Usuarios"
    admins = cargar_usuarios(os.path.join(base, "Admins.txt"))
    otros = cargar_usuarios(os.path.join(base, "Otros.txt"))

    todos = admins + otros

    resultado = []
    for u in todos:
        info = f"{u['Usuario']} ({u['Rol']}) - {u['Estado']}"
        
        if mostrar_password:
            info += f" | Documento: {u['Documento']}"
        
        resultado.append(info)

    return resultado
########################################################################################################################################################################################################################






# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// TKINTER (Interfaz)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Interfaz de usuario


def ui_ver_pedidos(ventana, datos):

    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    crear_label(
        ventana.frame_central,
        "MIS PEDIDOS",
        titulo=True
    ).pack(pady=15)

    tabla_frame = tk.Frame(
        ventana.frame_central,
        bg=COLORES_FONDO[0]
    )

    tabla_frame.pack(
        pady=10,
        fill="both",
        expand=True
    )

    columnas = (
        "id",
        "fecha",
        "cantidad",
        "estado",
        "observacion"
    )

    tabla = ttk.Treeview(
        tabla_frame,
        columns=columnas,
        show="headings",
        height=10
    )

    tabla.heading("id", text="ID")
    tabla.heading("fecha", text="Fecha")
    tabla.heading("cantidad", text="Cantidad")
    tabla.heading("estado", text="Estado")
    tabla.heading("observacion", text="Observación")

    tabla.column("id", width=50, anchor="center")
    tabla.column("fecha", width=130, anchor="center")
    tabla.column("cantidad", width=80, anchor="center")
    tabla.column("estado", width=100, anchor="center")
    tabla.column("observacion", width=250, anchor="center")

    scrollbar = ttk.Scrollbar(
        tabla_frame,
        orient="vertical",
        command=tabla.yview
    )

    tabla.configure(
        yscrollcommand=scrollbar.set
    )

    tabla.pack(side="left", fill="both", expand=True)

    scrollbar.pack(side="right", fill="y")

    ruta = "Archivos_BD/Sede_principal/Registro/Pedidos.txt"

    pedidos = cargar_pedidos(ruta)

    for p in pedidos:

        if p.get("Usuario") == datos["Usuario"]:

            tabla.insert(
                "",
                "end",
                values=(
                    p.get("ID"),
                    p.get("Fecha"),
                    p.get("Cantidad"),
                    p.get("Estado"),
                    p.get("Observacion")
                )
            )
    

    crear_boton(
        ventana.frame_central,
        "Atrás",
        lambda: pantalla_usuario(ventana, datos)
    ).pack(pady=15)


def pantalla_usuario(ventana, datos):

    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    nombre = datos.get("Nombre", "Usuario")
    usuario = datos.get("Usuario", "")

    crear_label(
        ventana.frame_central,
        f"Bienvenido\n{nombre}",
        titulo=True
    ).pack(pady=30)

    crear_label(
        ventana.frame_central,
        "Seleccione una opción del menú",
        titulo=False
    ).pack(pady=5)

    # =====================================================
    # RETIRAR SANGRE
    # =====================================================

    def ui_retirar():

        limpiar_pantalla(ventana)
        ventana.update_idletasks()
        ventana.geometry("")

        crear_label(
            ventana.frame_central,
            "RETIRAR SANGRE",
            titulo=True
        ).pack(pady=15)

        crear_label(
            ventana.frame_central,
            "Ingrese la sucursal donde desea retirar sangre",
            titulo=False
        ).pack(pady=5)

        crear_label(
            ventana.frame_central,
            "Ejemplo: Sucursal_A",
            titulo=False
        ).pack(pady=2)

        entry_sucursal = tk.Entry(
            ventana.frame_central,
            font=("Arial", 12),
            width=30
        )

        entry_sucursal.pack(pady=10)

        label_msg = tk.Label(
            ventana.frame_central,
            text="",
            bg=COLORES_FONDO[0],
            font=("Arial", 11)
        )

        label_msg.pack(pady=10)

        def ejecutar():

            sucursal = entry_sucursal.get().strip()

            sucursales_validas = [
                "Sucursal_A",
                "Sucursal_B",
                "Sucursal_C",
                "Sucursal_D"
            ]

            if not sucursal:

                label_msg.config(
                    text="⚠️ Debe ingresar una sucursal",
                    fg="orange"
                )

                return

            if sucursal not in sucursales_validas:

                label_msg.config(
                    text="❌ Sucursal no válida",
                    fg="red"
                )

                return

            ruta = f"Archivos_BD/Sucursales/{sucursal}.txt"

            stock_actual = obtener_stock(ruta)

            if stock_actual <= 0:

                label_msg.config(
                    text="❌ No hay unidades disponibles",
                    fg="red"
                )

                return

            retirar_sangre(sucursal, usuario)

            nuevo_stock = obtener_stock(ruta)

            label_msg.config(
                text=f"✅ Retiro realizado correctamente\nStock restante: {nuevo_stock}",
                fg="green"
            )

        crear_boton(
            ventana.frame_central,
            "Confirmar retiro",
            ejecutar
        ).pack(pady=10)

        crear_boton(
            ventana.frame_central,
            "Atrás",
            lambda: pantalla_usuario(ventana, datos)
        ).pack(pady=10)

    # =====================================================
    # CREAR PEDIDO
    # =====================================================

    def ui_pedido():

        limpiar_pantalla(ventana)
        ventana.update_idletasks()
        ventana.geometry("")

        crear_label(
            ventana.frame_central,
            "CREAR PEDIDO",
            titulo=True
        ).pack(pady=15)

        # =========================
        # SUCURSAL
        # =========================

        crear_label(
            ventana.frame_central,
            "Sucursal destino",
            titulo=False
        ).pack()

        crear_label(
            ventana.frame_central,
            "Ejemplo: Sucursal_A",
            titulo=False
        ).pack()

        entry_sucursal = tk.Entry(
            ventana.frame_central,
            font=("Arial", 12),
            width=30
        )

        entry_sucursal.pack(pady=10)

        # =========================
        # CANTIDAD
        # =========================

        crear_label(
            ventana.frame_central,
            "Cantidad de unidades",
            titulo=False
        ).pack()

        crear_label(
            ventana.frame_central,
            "Ingrese solo números",
            titulo=False
        ).pack()

        entry_cantidad = tk.Entry(
            ventana.frame_central,
            font=("Arial", 12),
            width=30
        )

        entry_cantidad.pack(pady=10)

        label_msg = tk.Label(
            ventana.frame_central,
            text="",
            bg=COLORES_FONDO[0],
            font=("Arial", 11)
        )

        label_msg.pack(pady=10)

        def ejecutar():

            sucursal = entry_sucursal.get().strip()

            sucursales_validas = [
                "Sucursal_A",
                "Sucursal_B",
                "Sucursal_C",
                "Sucursal_D"
            ]

            if sucursal not in sucursales_validas:

                label_msg.config(
                    text="❌ Sucursal inválida",
                    fg="red"
                )

                return

            try:

                cantidad = int(entry_cantidad.get())

                if cantidad <= 0:
                    raise ValueError

            except:

                label_msg.config(
                    text="❌ Cantidad inválida",
                    fg="red"
                )

                return

            ruta = "Archivos_BD/Sede_principal/Registro/Pedidos.txt"

            pedido_id = generar_id_pedido(ruta)

            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

            with open(ruta, "a") as f:

                f.write(f"ID:{pedido_id}\n")
                f.write(f"Fecha:{fecha}\n")
                f.write(f"Sucursal:{sucursal}\n")
                f.write(f"Usuario:{usuario}\n")
                f.write(f"Cantidad:{cantidad}\n")
                f.write("Estado:Pendiente\n")
                f.write("Observacion:\n")
                f.write("----------------------\n")

            label_msg.config(
                text=(
                    f"✅ Pedido registrado correctamente\n\n"
                    f"ID Pedido: {pedido_id}\n"
                    f"Sucursal: {sucursal}\n"
                    f"Cantidad: {cantidad}\n"
                    f"Estado: Pendiente"
                ),
                fg="green"
            )

        crear_boton(
            ventana.frame_central,
            "Registrar pedido",
            ejecutar
        ).pack(pady=10)

        crear_boton(
            ventana.frame_central,
            "Atrás",
            lambda: pantalla_usuario(ventana, datos)
        ).pack(pady=10)

    # =====================================================
    # VER STOCK
    # =====================================================

    def ui_stock():

        limpiar_pantalla(ventana)
        ventana.update_idletasks()
        ventana.geometry("")

        crear_label(
            ventana.frame_central,
            "STOCK DE SUCURSALES",
            titulo=True
        ).pack(pady=15)

        sucursales = [
            "Sucursal_A",
            "Sucursal_B",
            "Sucursal_C",
            "Sucursal_D"
        ]

        for s in sucursales:

            ruta = f"Archivos_BD/Sucursales/{s}.txt"

            stock = obtener_stock(ruta)

            crear_label(
                ventana.frame_central,
                f"{s} → {stock} unidades"
            ).pack(pady=3)

        crear_boton(
            ventana.frame_central,
            "Atrás",
            lambda: pantalla_usuario(ventana, datos)
        ).pack(pady=20)

    

    # =====================================================
    # BOTONES PRINCIPALES
    # =====================================================

    crear_boton(
        ventana.frame_central,
        "Retirar sangre",
        ui_retirar
    ).pack(pady=10)

    crear_boton(
        ventana.frame_central,
        "Crear pedido",
        ui_pedido
    ).pack(pady=10)

    crear_boton(
        ventana.frame_central,
        "Ver stock sucursales",
        ui_stock
    ).pack(pady=10)

    crear_boton(
        
        ventana.frame_central,
        "Ver estado de pedidos",
        lambda: ui_ver_pedidos(ventana, datos)
    ).pack(pady=10)

    

    crear_boton(
        ventana.frame_central,
        "Cerrar sesión",
        lambda: menu_principal(ventana),
        color="#D9534F"
    ).pack(pady=20)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Variables//colores


#Fondo degradado

COLORES_FONDO = [
    "#F0F9FF",  # 0 - Azul blanquecino muy suave
    "#E2F4FF",  # 1
    "#D4EEFF",  # 2
    "#C4E7FF",  # 3
    "#B2DFFF",  # 4
    "#A1D7FF",  # 5 (Pico de intensidad: Azul cielo pastel suave)
    "#B2DFFF",  # 4
    "#C4E7FF",  # 3
    "#D4EEFF",  # 2
    "#E2F4FF",  # 1
    "#F0F9FF",  # 0 - Cierre de ciclo suave
]
#Botones
COLOR_BOTON = "#7EBDFC"
COLOR_HOVER = "#5A9BDB"

#Texto
COLOR_TEXTO = "#2E2E2E"

# Tamaños
ANCHO_BOTON = 35
ALTO_BOTON = 2
FUENTE_NORMAL = ("Arial", 15)
FUENTE_TITULO = ("Arial", 25, "bold")



def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def interpolate(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def crear_ventana():
    ventana = tk.Tk()

    ventana.title("Sistema Banco de Sangre")
    ventana.geometry("700x500")
    ventana.minsize(500, 400)

    canvas = tk.Canvas(ventana, highlightthickness=0)
    canvas.place(relwidth=1, relheight=1)

    offset = 0

    def dibujar_fondo():
        nonlocal offset

        canvas.delete("fondo")

        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()

        secciones = 60
        altura_seccion = alto / secciones

        colores_rgb = [hex_to_rgb(c) for c in COLORES_FONDO]

        for i in range(secciones):
            t = ((i + offset) % secciones) / secciones * (len(colores_rgb) - 1)
            idx = int(t)
            local_t = t - idx

            if idx >= len(colores_rgb) - 1:
                color = colores_rgb[-1]
            else:
                color = interpolate(colores_rgb[idx], colores_rgb[idx + 1], local_t)

            color_hex = rgb_to_hex(color)

            canvas.create_rectangle(
                0, i * altura_seccion,
                ancho, (i + 1) * altura_seccion,
                fill=color_hex,
                outline="",
                tags="fondo"
            )

        offset = (offset + 1) % secciones

        ventana.after(30, dibujar_fondo)

    dibujar_fondo()

    ventana.main_frame = canvas

    return ventana


def limpiar_pantalla(ventana):

    for widget in ventana.main_frame.winfo_children():
        widget.destroy()

    # Frame central
    frame_central = tk.Frame(
        ventana.main_frame,
        bg=COLORES_FONDO[0]
    )

    frame_central.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    ventana.frame_central = frame_central


def crear_boton(parent, texto, comando=None, color=COLOR_BOTON, fg="white"):

    boton = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=color,
        fg=fg,
        activebackground=COLOR_HOVER,
        activeforeground="white",
        font=("Arial", 13, "bold"),
        width=40,   # +40% aprox
        height=3,   # +40% aprox
        bd=0,
        cursor="hand2"
    )

    # Hover manual
    boton.bind(
        "<Enter>",
        lambda e: boton.config(bg=COLOR_HOVER)
    )

    boton.bind(
        "<Leave>",
        lambda e: boton.config(bg=color)
    )

    return boton

def crear_label(parent, texto, titulo=False):

    fuente = FUENTE_TITULO if titulo else FUENTE_NORMAL

    label = tk.Label(
        parent,
        text=texto,
        bg=COLORES_FONDO[0],
        fg=COLOR_TEXTO,
        font=fuente
    )

    return label

def menu_principal(ventana):

    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    crear_label(
        ventana.frame_central,
        "BANCO DE SANGRE",
        titulo=True
    ).pack(pady=25)

    crear_boton(
        ventana.frame_central,
        "Iniciar sesión",
        lambda: pantalla_login(ventana)
    ).pack(pady=10)

    crear_boton(
        ventana.frame_central,
        "Registrar nuevo usuario",
        lambda: pantalla_registro(ventana)
    ).pack(pady=10)

    crear_boton(
        ventana.frame_central,
        "Salir",
        ventana.destroy,
        color="#D9534F"
    ).pack(pady=10)


def ver_inventario_ui(ventana, datos):
    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    # Título de la pantalla
    crear_label(ventana.frame_central, "INVENTARIO DE SEDE PRINCIPAL", titulo=True).pack(pady=10)

    # 📦 CONTENEDOR DE LA TABLA (Frame interno para agrupar tabla + scrollbar)
    tabla_frame = tk.Frame(ventana.frame_central, bg=COLORES_FONDO[0])
    tabla_frame.pack(pady=10, fill="both", expand=True)

    # Configuración del estilo para que se adapte a tu paleta azulada
    estilo = ttk.Style()  # <- CORREGIDO: Era tk.Scale() por error
    estilo.theme_use("clam")
    estilo.configure("Treeview", 
                     background="#FFFFFF", 
                     foreground=COLOR_TEXTO, 
                     rowheight=25, 
                     fieldbackground="#FFFFFF",
                     font=("Arial", 11))
    estilo.configure("Treeview.Heading", 
                     background=COLOR_BOTON, 
                     foreground="white", 
                     font=("Arial", 11, "bold"))
    estilo.map("Treeview", background=[("selected", COLOR_HOVER)])

    # Definición de Columnas de la Tabla
    columnas = ("unidad", "fecha", "estado")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=10)
    
    # Encabezados
    tabla.heading("unidad", text="📦 Unidad / Componente")
    tabla.heading("fecha", text="📅 Fecha de Ingreso")
    tabla.heading("estado", text="🟢 Estado")

    # Dimensiones y alineación de columnas
    tabla.column("unidad", width=180, anchor="center")
    tabla.column("fecha", width=150, anchor="center")
    tabla.column("estado", width=130, anchor="center")

    # 📜 BARRA DE DESPLAZAMIENTO (Scrollbar) Lateral
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    
    # Empaquetado de la tabla y su scrollbar
    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # LECTURA Y PROCESAMIENTO DE DATOS
    ruta = "Archivos_BD/Sede_principal/Inventario.txt"
    if os.path.exists(ruta):
        with open(ruta, "r") as f:
            for linea in f:
                linea = linea.strip()
                if not linea: continue
                try:
                    partes = linea.split(", ")
                    unidad = partes[0].replace("_", " ") 
                    fecha = partes[1].split(":")[1]
                    estado = partes[2].split(":")[1]
                    
                    # Insertar fila en la tabla
                    tabla.insert("", "end", values=(unidad, fecha, estado))
                except:
                    tabla.insert("", "end", values=(linea, "---", "---"))

    # Botón de regreso
    crear_boton(ventana.frame_central, "Atrás", lambda: pantalla_admin(ventana, datos)).pack(pady=15)


def eliminar_usuario_ui(ventana):
    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    crear_label(ventana.frame_central, "ELIMINAR USUARIO DEL SISTEMA", titulo=True).pack(pady=15)
    crear_label(ventana.frame_central, "⚠️ ¡Atención! Esta acción es irreversible.\nIngrese el nombre de usuario exacto que desea borrar", titulo=False).pack(pady=5)

    entry_usuario = tk.Entry(ventana.frame_central, font=("Arial", 12), width=30, justify="center")
    entry_usuario.pack(pady=15)
    entry_usuario.focus() 

    label_mensaje = tk.Label(
        ventana.frame_central,
        text="",
        bg=COLORES_FONDO[0],
        font=("Arial", 11, "bold")
    )
    label_mensaje.pack(pady=10)

    def ejecutar_eliminacion():
        usuario_a_borrar = entry_usuario.get().strip()

        if not usuario_a_borrar:
            label_mensaje.config(text="⚠️ Por favor, escribe un nombre de usuario.", fg="orange")
            return

        resultado = eliminar_usuario_logica(usuario_a_borrar)

        if resultado == "ok":
            label_mensaje.config(text=f"✅ El usuario '{usuario_a_borrar}' fue eliminado con éxito.", fg="green")
            entry_usuario.delete(0, tk.END) 
        elif resultado == "no_eliminar":
            label_mensaje.config(text="⛔ Acción denegada: No se puede eliminar al Administrador Principal.", fg="red")
        elif resultado == "no_encontrado":
            label_mensaje.config(text=f"❌ El usuario '{usuario_a_borrar}' no existe en la base de datos.", fg="red")

    crear_boton(ventana.frame_central, "Confirmar Eliminación", ejecutar_eliminacion, color="#D9534F").pack(pady=8)
    crear_boton(ventana.frame_central, "Atrás", lambda: pantalla_admin(ventana, {"Rol": "Principal_Admin"})).pack(pady=8)


def bloquear_usuario_ui(ventana):
    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    crear_label(ventana.frame_central, "Bloquear usuario", titulo=True).pack(pady=10)

    entry = tk.Entry(ventana.frame_central)
    entry.pack(pady=5)

    label_msg = tk.Label(ventana.frame_central, text="", bg=COLORES_FONDO[0])
    label_msg.pack()

    def ejecutar():
        usuario = entry.get().strip()

        if not usuario:
            label_msg.config(text="Ingrese usuario", fg="orange")
            return

        base = "Archivos_BD/Sede_principal/Usuarios"
        otros_path = os.path.join(base, "Otros.txt")
        usuarios = cargar_usuarios(otros_path)

        for u in usuarios:
            if u.get("Usuario", "").lower() == usuario.lower():
                if u.get("Rol") == "Principal_Admin":
                    label_msg.config(text="No se puede bloquear al principal", fg="red")
                    return

                u["Estado"] = "Bloqueado"
                guardar_usuarios(otros_path, usuarios)
                label_msg.config(text="Usuario bloqueado", fg="green")
                return

        label_msg.config(text="No encontrado", fg="red")

    crear_boton(ventana.frame_central, "Bloquear", ejecutar).pack(pady=10)
    crear_boton(ventana.frame_central, "Atrás", lambda: pantalla_admin(ventana, {"Rol": "Admin"})).pack(pady=10)


def desbloquear_usuario_ui(ventana):
    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("") 

    crear_label(ventana.frame_central, "DESBLOQUEAR USUARIO", titulo=True).pack(pady=15)
    crear_label(ventana.frame_central, "Ingrese el nombre de usuario", titulo=False).pack(pady=5)

    entry = tk.Entry(ventana.frame_central, font=("Arial", 12), width=30)
    entry.pack(pady=10)

    label_mensaje = tk.Label(ventana.frame_central, text="", bg=COLORES_FONDO[0], font=("Arial", 11))
    label_mensaje.pack(pady=10)

    def ejecutar():
        usuario = entry.get().strip()

        if not usuario:
            label_mensaje.config(text="⚠️ Ingrese un usuario", fg="orange")
            return

        base = "Archivos_BD/Sede_principal/Usuarios"
        otros_path = os.path.join(base, "Otros.txt")
        usuarios = cargar_usuarios(otros_path)

        for u in usuarios:
            if u.get("Usuario", "").lower() == usuario.lower():
                if u.get("Estado") == "Activo":
                    label_mensaje.config(text="ℹ️ El usuario ya está activo", fg="blue")
                    return

                u["Estado"] = "Activo"
                guardar_usuarios(otros_path, usuarios)
                label_mensaje.config(text="✅ Usuario desbloqueado correctamente", fg="green")
                return

        label_mensaje.config(text="❌ Usuario no encontrado", fg="red")

    crear_boton(ventana.frame_central, "Desbloquear", ejecutar).pack(pady=10)
    crear_boton(ventana.frame_central, "Atrás", lambda: pantalla_admin(ventana, {"Rol": "Admin"})).pack(pady=10)


def ver_usuarios_ui(ventana, es_super):
    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    crear_label(ventana.frame_central, "CONTROL DE USUARIOS Y ROLES", titulo=True).pack(pady=10)

    tabla_frame = tk.Frame(ventana.frame_central, bg=COLORES_FONDO[0])
    tabla_frame.pack(pady=10, fill="both", expand=True)

    if es_super:
        columnas = ("usuario", "rol", "estado", "documento")
    else:
        columnas = ("usuario", "rol", "estado")

    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=10)
    
    tabla.heading("usuario", text="👤 Nombre de Usuario")
    tabla.heading("rol", text="🛡️ Rol asignado")
    tabla.heading("estado", text="⚡ Estado de cuenta")
    
    tabla.column("usuario", width=150, anchor="w")
    tabla.column("rol", width=120, anchor="center")
    tabla.column("estado", width=110, anchor="center")

    if es_super:
        tabla.heading("documento", text="🪪 Documento (Contraseña)")
        tabla.column("documento", width=150, anchor="center")

    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    
    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    base = "Archivos_BD/Sede_principal/Usuarios"
    admins = cargar_usuarios(os.path.join(base, "Admins.txt"))
    otros = cargar_usuarios(os.path.join(base, "Otros.txt"))
    todos_los_usuarios = admins + otros

    for u in todos_los_usuarios:
        user_val = u.get("Usuario", "N/A")
        rol_val = u.get("Rol", "N/A").replace("_", " ")
        estado_val = u.get("Estado", "N/A")
        
        if estado_val == "Bloqueado":
            estado_val = "🔒 Bloqueado"
        elif estado_val == "Activo":
            estado_val = "✅ Activo"

        if es_super:
            doc_val = u.get("Documento", "N/A")
            tabla.insert("", "end", values=(user_val, rol_val, estado_val, doc_val))
        else:
            tabla.insert("", "end", values=(user_val, rol_val, estado_val))

    crear_boton(ventana.frame_central, "Atrás",
                 lambda: pantalla_admin(
                     ventana,
                     {"Rol": "Principal_Admin" if es_super else "Admin"}
                 )).pack(pady=15)


def ver_pedidos_ui(ventana, datos):

    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    crear_label(
        ventana.frame_central,
        "GESTIÓN DE PEDIDOS",
        titulo=True
    ).pack(pady=10)

    # =====================================================
    # FRAME TABLA
    # =====================================================

    tabla_frame = tk.Frame(
        ventana.frame_central,
        bg=COLORES_FONDO[0]
    )

    tabla_frame.pack(
        pady=10,
        fill="both",
        expand=True
    )

    columnas = (
        "id",
        "fecha",
        "sucursal",
        "usuario",
        "cantidad",
        "estado"
    )

    tabla = ttk.Treeview(
        tabla_frame,
        columns=columnas,
        show="headings",
        height=10
    )

    # Encabezados
    tabla.heading("id", text="ID")
    tabla.heading("fecha", text="Fecha")
    tabla.heading("sucursal", text="Sucursal")
    tabla.heading("usuario", text="Usuario")
    tabla.heading("cantidad", text="Cantidad")
    tabla.heading("estado", text="Estado")

    # Tamaños
    tabla.column("id", width=50, anchor="center")
    tabla.column("fecha", width=120, anchor="center")
    tabla.column("sucursal", width=100, anchor="center")
    tabla.column("usuario", width=100, anchor="center")
    tabla.column("cantidad", width=80, anchor="center")
    tabla.column("estado", width=100, anchor="center")

    scrollbar = ttk.Scrollbar(
        tabla_frame,
        orient="vertical",
        command=tabla.yview
    )

    tabla.configure(
        yscrollcommand=scrollbar.set
    )

    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # =====================================================
    # CARGAR PEDIDOS
    # =====================================================

    ruta = "Archivos_BD/Sede_principal/Registro/Pedidos.txt"

    pedidos = cargar_pedidos(ruta)

    def cargar_tabla():

        tabla.delete(*tabla.get_children())

        pedidos_actualizados = cargar_pedidos(ruta)

        for p in pedidos_actualizados:

            tabla.insert(
                "",
                "end",
                values=(
                    p.get("ID"),
                    p.get("Fecha"),
                    p.get("Sucursal"),
                    p.get("Usuario"),
                    p.get("Cantidad"),
                    p.get("Estado")
                )
            )

    cargar_tabla()

    # =====================================================
    # OBSERVACIONES
    # =====================================================

    crear_label(
        ventana.frame_central,
        "Observaciones"
    ).pack(pady=5)

    entry_observacion = tk.Entry(
        ventana.frame_central,
        width=60,
        font=("Arial", 11)
    )

    entry_observacion.pack(pady=5)


    observacion_actual = tk.StringVar()

    def confirmar_observacion():

        texto = entry_observacion.get().strip()

        if not texto:

            label_msg.config(
                text="⚠️ Escriba una observación",
                fg="orange"
            )

            return

        observacion_actual.set(texto)

        label_msg.config(
            text="✅ Observación confirmada",
            fg="green"
        )

    crear_boton(
        ventana.frame_central,
        "Confirmar observación",
        confirmar_observacion,
        color="#5BC0DE"
    ).pack(pady=5)


    

    label_msg = tk.Label(
        ventana.frame_central,
        text="",
        bg=COLORES_FONDO[0],
        font=("Arial", 11)
    )

    label_msg.pack(pady=5)

    # =====================================================
    # APROBAR PEDIDO
    # =====================================================

    def aprobar():

        seleccionado = tabla.selection()

        if not seleccionado:
            label_msg.config(
                text="⚠️ Seleccione un pedido",
                fg="orange"
            )
            return

        item = tabla.item(seleccionado)

        pedido_id = item["values"][0]

        pedidos = cargar_pedidos(ruta)

        for p in pedidos:

            if str(p.get("ID")) == str(pedido_id):

                if p.get("Estado") != "Pendiente":

                    label_msg.config(
                        text="❌ Este pedido ya fue procesado",
                        fg="red"
                    )

                    return

                observacion = observacion_actual.get()

                p["Estado"] = "Aprobado"
                p["Observacion"] = observacion

                aprobar_pedido(p)

                guardar_pedidos(ruta, pedidos)

                label_msg.config(
                    text="✅ Pedido aprobado",
                    fg="green"
                )

                cargar_tabla()

                return

    # =====================================================
    # RECHAZAR PEDIDO
    # =====================================================

    def rechazar():

        seleccionado = tabla.selection()

        if not seleccionado:

            label_msg.config(
                text="⚠️ Seleccione un pedido",
                fg="orange"
            )

            return

        item = tabla.item(seleccionado)

        pedido_id = item["values"][0]

        pedidos = cargar_pedidos(ruta)

        for p in pedidos:

            if str(p.get("ID")) == str(pedido_id):

                if p.get("Estado") != "Pendiente":

                    label_msg.config(
                        text="❌ Este pedido ya fue procesado",
                        fg="red"
                    )

                    return

                observacion = observacion_actual.get()

                p["Estado"] = "Rechazado"
                p["Observacion"] = observacion

                guardar_pedidos(ruta, pedidos)

                label_msg.config(
                    text="❌ Pedido rechazado",
                    fg="red"
                )

                cargar_tabla()

                return

    # =====================================================
    # BOTONES
    # =====================================================

    frame_botones = tk.Frame(
        ventana.frame_central,
        bg=COLORES_FONDO[0]
    )

    frame_botones.pack(pady=10)

    crear_boton(
        frame_botones,
        "Aprobar Pedido",
        aprobar,
        color="#5CB85C"
    ).pack(side="left", padx=10)

    crear_boton(
        frame_botones,
        "Rechazar Pedido",
        rechazar,
        color="#D9534F"
    ).pack(side="left", padx=10)

    crear_boton(
        ventana.frame_central,
        "Atrás",
        lambda: pantalla_admin(ventana, datos)
    ).pack(pady=10)



def pantalla_admin(ventana, datos):
    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    es_super = datos.get("Rol") == "Principal_Admin"

    crear_label(
        ventana.frame_central,
        f"Bienvenido al Panel\n de Administrador",
        titulo=True
    ).pack(pady=50)

    crear_boton(
        ventana.frame_central,
        "Ver Inventario",
        lambda: ver_inventario_ui(ventana, datos)  
    ).pack(pady=8)

    crear_boton(
        ventana.frame_central,
        "Gestionar Pedidos",
        lambda: ver_pedidos_ui(ventana, datos)
    ).pack(pady=8)

    crear_boton(
        ventana.frame_central,
        "Ver Usuarios",
        lambda: ver_usuarios_ui(ventana, es_super)
    ).pack(pady=8)

    crear_boton(
        ventana.frame_central,
        "Bloquear Usuario",
        lambda: bloquear_usuario_ui(ventana)
    ).pack(pady=8)

    crear_boton(
        ventana.frame_central,
        "Desbloquear Usuario",
        lambda: desbloquear_usuario_ui(ventana)
    ).pack(pady=8)

    if es_super:
        crear_boton(
            ventana.frame_central,
            "Eliminar Usuario",
            lambda: eliminar_usuario_ui(ventana)
        ).pack(pady=8)

    crear_boton(
        ventana.frame_central,
        "Cerrar sesión",
        lambda: menu_principal(ventana),
        color="#D9534F"
    ).pack(pady=15)

def pantalla_login(ventana):

    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    crear_label(
        ventana.frame_central,
        "INICIAR SESIÓN",
        titulo=True
    ).pack(pady=20)

    crear_label(
        ventana.frame_central,
        "Usuario"
    ).pack()

    entry_usuario = tk.Entry(
        ventana.frame_central,
        font=("Arial", 12),
        width=30
    )
    entry_usuario.pack(pady=5)

    crear_label(
        ventana.frame_central,
        "Contraseña"
    ).pack()

    entry_password = tk.Entry(
        ventana.frame_central,
        show="*",
        font=("Arial", 12),
        width=30
    )
    entry_password.pack(pady=5)

    label_mensaje = crear_label(
        ventana.frame_central,
        ""
    )

    label_mensaje.pack(pady=10)

    def intentar_login():

        usuario = entry_usuario.get()
        password = entry_password.get()

        rol, datos = login_sistema(usuario, password)

        if rol == "admin" or rol == "Principal_Admin":
            pantalla_admin(ventana, datos)

        elif rol == "usuario":
            pantalla_usuario(ventana, datos)

        elif rol == "bloqueado":
            label_mensaje.config(
                text="⛔ Usuario bloqueado",
                fg="red"
            )

        elif rol == "vacio":
            label_mensaje.config(
                text="⚠️ Complete todos los campos",
                fg="orange"
            )

        else:
            label_mensaje.config(
                text="❌ Datos incorrectos",
                fg="red"
            )

    crear_boton(
        ventana.frame_central,
        "Ingresar",
        intentar_login
    ).pack(pady=10)

    crear_boton(
        ventana.frame_central,
        "Olvidé mi usuario o contraseña",
        lambda: recuperar_cuenta_ui(ventana),
        color="#F0C040"
    ).pack(pady=8)

    

    crear_boton(
        ventana.frame_central,
        "Atrás",
        lambda: menu_principal(ventana)
    ).pack(pady=10)


def recuperar_cuenta_ui(ventana):

    limpiar_pantalla(ventana)

    crear_label(
        ventana.frame_central,
        "RECUPERAR CUENTA",
        titulo=True
    ).pack(pady=15)

    crear_label(
        ventana.frame_central,
        "Nombre completo"
    ).pack(pady=5)

    entry_nombre = tk.Entry(
        ventana.frame_central,
        font=("Arial", 11),
        width=35
    )

    entry_nombre.pack(pady=5)

    crear_label(
        ventana.frame_central,
        "Número de documento"
    ).pack(pady=5)

    entry_documento = tk.Entry(
        ventana.frame_central,
        font=("Arial", 11),
        width=35
    )

    entry_documento.pack(pady=5)

    resultado = tk.Label(
        ventana.frame_central,
        text="",
        bg=COLORES_FONDO[0],
        font=("Arial", 11)
    )

    resultado.pack(pady=10)

    def recuperar():

        nombre = entry_nombre.get().strip().lower()
        documento = entry_documento.get().strip()

        ruta = "Archivos_BD/Usuarios/Usuarios.txt"

        if not os.path.exists(ruta):

            resultado.config(
                text="❌ Base de datos no encontrada",
                fg="red"
            )

            return

        with open(ruta, "r", encoding="utf-8") as f:

            contenido = f.read().split("--------------------")

        for bloque in contenido:

            lineas = bloque.strip().split("\n")

            datos = {}

            for linea in lineas:

                if ":" in linea:

                    clave, valor = linea.split(":", 1)

                    datos[clave.strip()] = valor.strip()

            nombre_bd = datos.get("Nombre", "").lower()
            documento_bd = datos.get("Documento", "")

            if nombre == nombre_bd and documento == documento_bd:

                resultado.config(
                    text=(
                        f"✅ Usuario encontrado\n\n"
                        f"Usuario: {datos.get('Usuario')}\n"
                        f"Contraseña: {datos.get('Contraseña')}"
                    ),
                    fg="green"
                )

                return

        resultado.config(
            text="❌ Datos incorrectos",
            fg="red"
        )

    crear_boton(
        ventana.frame_central,
        "Recuperar cuenta",
        recuperar,
        color="#5CB85C"
    ).pack(pady=10)

    crear_boton(
        ventana.frame_central,
        "Atrás",
        lambda: pantalla_login(ventana)
    ).pack(pady=10)


def pantalla_registro(ventana):
    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    crear_label(ventana.frame_central, "INICIAR SESIÓN", titulo=True).pack(pady=20)


    crear_boton(
        ventana.frame_central,
        "Nuevo Administrador",
        lambda: registro_admin_ui(ventana)
    ).pack(pady=10)

    crear_boton(
        ventana.frame_central,
        "Nuevo Usuario de sucursal",
        lambda: registro_usuario_ui(ventana)
    ).pack(pady=10)

    crear_boton(
        ventana.frame_central,
        "Atrás",
        lambda: menu_principal(ventana)
    ).pack(pady=10)



def registro_admin_ui(ventana):
    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    
    crear_label(ventana.frame_central, "Registrar Administrador", titulo=True).pack(pady=10)
    crear_label(ventana.frame_central, "Su numero de documento se guardara \n omo contraseña por defecto.", titulo=False).pack(pady=10)

    crear_label(ventana.frame_central, "Cedula", titulo=False).pack(pady=10)
    entry_cedula = tk.Entry(ventana.frame_central)
    entry_cedula.pack()
#False
    crear_label(ventana.frame_central, "Nombres", titulo=False).pack(pady=10)
    entry_nombre = tk.Entry(ventana.frame_central)
    entry_nombre.pack()

    crear_label(ventana.frame_central, "Apellidos", titulo=False).pack(pady=10)
    entry_apellido = tk.Entry(ventana.frame_central)
    entry_apellido.pack()

    crear_label(ventana.frame_central, "Usuario", titulo=False).pack(pady=10)
    entry_usuario = tk.Entry(ventana.frame_central)
    entry_usuario.pack()

    crear_label(ventana.frame_central, "Codigo de Administrador", titulo=False).pack(pady=10)
    entry_codigo = tk.Entry(ventana.frame_central)
    entry_codigo.pack()

    label_mensaje = tk.Label(ventana.frame_central, text="", wraplength=400) # wraplength para que el texto largo no se corte.
    label_mensaje.pack(pady=5)

    def registrar():
        cedula = entry_cedula.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        usuario = entry_usuario.get()
        codigo = entry_codigo.get()

        base = "Archivos_BD/Sede_principal/Usuarios"
        admins_path = os.path.join(base, "Admins.txt")
        otros_path = os.path.join(base, "Otros.txt")

        codigo_principal = "1020304050"

        if not validar_cedula(cedula):
            label_mensaje.config(text="Cedula invalida, recuerde que son 10 digitos numericos sin espacios ni simbolos.", fg="red")
            print("❌ Cédula inválida")
            return

        if not validar_nombre(nombre) or not validar_nombre(apellido):
            label_mensaje.config(text="Nombre o apellido invalido.", fg="red")
            print("❌ Nombre inválido")
            return

        if not validar_usuario(usuario):
            label_mensaje.config(text="Usuario invalido, intente denuevo. Recuerde que debe contener entre 7 y 12 digitos.", fg="orange")
            print("❌ Usuario inválido")
            return

        if usuario_existe(usuario, admins_path, otros_path):
            label_mensaje.config(text="Usuario ya existe.", fg="orange")
            print("❌ Usuario ya existe")
            return

        if codigo != codigo_principal:
            label_mensaje.config(text="Por favor ingrese el codigo de administración.", fg="orange")
            print("❌ Código incorrecto")
            return

        with open(admins_path, "a") as f:
            f.write(f"Nombre:{nombre}\n")
            f.write(f"Apellido:{apellido}\n")
            f.write(f"Usuario:{usuario}\n")
            f.write(f"Documento:{cedula}\n")
            f.write("Rol:Admin\n")
            f.write("Estado:Activo\n")
            f.write("----------------------\n")

        print("✅ Admin registrado")
        label_mensaje.config(text="✅ Admin registrado", fg="green")

    crear_boton(ventana.frame_central, "Registrar", lambda: registrar()).pack(pady=10)

    crear_boton(ventana.frame_central, "Atrás",
        lambda: pantalla_registro(ventana)).pack(pady=10)



def registro_usuario_ui(ventana):
    limpiar_pantalla(ventana)
    ventana.update_idletasks()
    ventana.geometry("")

    crear_label(ventana.frame_central, "Registrar Usuario", titulo=True).pack(pady=10)
    crear_label(ventana.frame_central, "Su numero de documento se guardara como contraseña por defecto.", titulo=False).pack(pady=10)

    crear_label(ventana.frame_central, "Cédula", titulo=False).pack()
    entry_cedula = tk.Entry(ventana.frame_central)
    entry_cedula.pack(pady=5)

    crear_label(ventana.frame_central, "Nombres", titulo=False).pack()
    entry_nombre = tk.Entry(ventana.frame_central)
    entry_nombre.pack(pady=5)

    crear_label(ventana.frame_central, "Apellidos", titulo=False).pack()
    entry_apellido = tk.Entry(ventana.frame_central)
    entry_apellido.pack(pady=5)

    crear_label(ventana.frame_central, "Usuario", titulo=False).pack()
    entry_usuario = tk.Entry(ventana.frame_central)
    entry_usuario.pack(pady=5)

    label_mensaje = tk.Label(ventana.frame_central, text="", wraplength=400)
    label_mensaje.pack(pady=5)

    def registrar():
        cedula = entry_cedula.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        usuario = entry_usuario.get()

        base = "Archivos_BD/Sede_principal/Usuarios"
        admins_path = os.path.join(base, "Admins.txt")
        otros_path = os.path.join(base, "Otros.txt")

        if not validar_cedula(cedula):
            label_mensaje.config(text="Cedula invalida, recuerde que son 10 digitos numericos sin espacios ni simbolos.", fg="red")
            print("❌ Cédula inválida")
            return

        if not validar_nombre(nombre) or not validar_nombre(apellido):
            label_mensaje.config(text="Nombre o apellido invalido.", fg="red")
            print("❌ Nombre inválido")
            return

        if not validar_usuario(usuario):
            label_mensaje.config(text="Usuario invalido, intente denuevo. Recuerde que debe contener entre 7 y 12 digitos.", fg="orange")
            print("❌ Usuario inválido")
            return

        if usuario_existe(usuario, admins_path, otros_path):
            label_mensaje.config(text="Usuario ya existe.", fg="orange")
            print("❌ Usuario ya existe")
            return

        with open(otros_path, "a") as f:
            f.write(f"Nombre:{nombre}\n")
            f.write(f"Apellido:{apellido}\n")
            f.write(f"Usuario:{usuario}\n")
            f.write(f"Documento:{cedula}\n")
            f.write("Rol:Usuario\n")
            f.write("Estado:Activo\n")
            f.write("----------------------\n")

        print("✅ Usuario registrado")
        label_mensaje.config(text="✅ Usuario registrado", fg="green")

    crear_boton(ventana.frame_central, "Registrar", lambda: registrar()).pack(pady=10)
    crear_boton(ventana.frame_central, "Atrás", lambda: pantalla_registro(ventana)).pack(pady=10)

########################################################################################################################################################################################################################








# Ejecutar
if __name__ == "__main__":
    crear_estructura_bd()
    inicializar_datos()
    inicializar_sucursales()
    verificar_vencimientos()

    ventana = crear_ventana()
    menu_principal(ventana)
    ventana.mainloop()


