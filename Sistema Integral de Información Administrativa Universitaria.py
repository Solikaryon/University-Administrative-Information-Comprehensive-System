import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from tkinter import PhotoImage
import re
import mysql.connector
import string
import pygame
import random
from PIL import Image, ImageTk


try:
    import tkcalendar
except ImportError:
    import subprocess
    subprocess.call(["pip", "install", "tkcalendar"])
    import tkcalendar
from tkcalendar import DateEntry

try:
    import pygame
except ImportError:
    import subprocess
    subprocess.call(["pip", "install", "pygame"])
    import pygame

try:
    import PIL
except ImportError:
    import subprocess
    subprocess.call(["pip", "install", "Pillow"])
    import PIL

usernameuser = None
useruserid = None
userprofile = None
useremail = None

# css button

def musicaparatodos():
    try:
        # Inicializar pygame
        pygame.init()

        # Cargar la canción
        #Laptop
        pygame.mixer.music.load("The Golden Touch.mp3")
        #pygame.mixer.music.load("Thhe Golden Touch.mp3") # Para el video pues no queremos que tenga musica el video a grabar

        # Reproducir la canción en loop
        pygame.mixer.music.play(-1)  # El argumento -1 indica que la canción se reproduce en un loop infinito

    except pygame.error as e:
        # Imprimir un mensaje en la consola si ocurre un error al cargar la canción
        pass


class Login:
    def __init__(self, root):
        self.root = root
        self.root.config(width=400, height=432)
        self.root.update_idletasks()
        width = 400
        height = 432
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Inicio de Sesión")
        self.root.configure(bg='#474D5C')

        self.background_image = tk.PhotoImage(file="Login.png")

        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self.root, text="Correo:", bg='black', fg='white').place(x=135, y=10)
        self.txUsuario = tk.Entry(self.root)
        self.txUsuario.place(x=200, y=10)

        tk.Label(self.root, text="Contraseña:", bg='black', fg='white').place(x=125, y=40)
        self.txContrasena = tk.Entry(self.root, show='*')
        self.txContrasena.place(x=200, y=40)

        self.img_boton = tk.PhotoImage(file="Iniciar_sesion.png")

        self.btnIniciarSesion = tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion,image=self.img_boton)
        self.btnIniciarSesion.place(x=170, y=80)

        # Establecer conexión con la base de datos
        self.conectar_a_base_de_datos()

    def conectar_a_base_de_datos(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )
        self.cursor = self.conn.cursor()

    def iniciar_sesion(self):
        usuario = self.txUsuario.get()
        contrasena = self.txContrasena.get()
        try:
            self.cursor.execute("SELECT * FROM usuarios WHERE email = %s AND Password = %s", (usuario, contrasena))
            resultado = self.cursor.fetchone()

            if resultado:
                global useruserid, usernameuser, userprofile, useremail
                useruserid = resultado[0]
                useremail = usuario
                usernameuser = resultado[1]
                userprofile = resultado[6]

                self.conn.close()
                self.cursor.close() 

                # Abrir la ventana de gestión de usuarios
                self.root.destroy()
                root = tk.Tk()
                app = option(root)
                root.mainloop()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", "Error de base de datos: " + str(err))

class option:
    def __init__(self, root):
        
        self.root = root
        self.root.config(width=850, height=500)
        width = 850
        height = 500
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Opciones")
        self.root.configure(bg='#474D5C')

        self.imagen_usuarios= tk.PhotoImage(file="Usuarios.png")
        self.imagen_preAlumnos= tk.PhotoImage(file="PreAlumnos.png")
        self.imagen_preMaestros= tk.PhotoImage(file="PreMaestros.png")
        self.imagen_materias= tk.PhotoImage(file="Materias.png")
        self.imagen_grupos= tk.PhotoImage(file="Grupos.png")
        self.imagen_horarios= tk.PhotoImage(file="Horarios.png")
        self.imagen_salon= tk.PhotoImage(file="Salon.png")
        self.imagen_carrera= tk.PhotoImage(file="Carrera.png")
        self.imagen_califiaciones= tk.PhotoImage(file="Calificaciones.png")
        self.imagen_mostrarCalifiaciones= tk.PhotoImage(file="MostrarCalificaciones.png")
        self.imagen_planeacion= tk.PhotoImage(file="Planeacion.png")
        self.imagen_dinosaurio= tk.PhotoImage(file="Dinousar.png")
        self.imagen_cambiarUsuario= tk.PhotoImage(file="CambiarUsuario.png")
        self.imagen_salir= tk.PhotoImage(file="Cancelar.png")

        self.background_image = tk.PhotoImage(file="Option.png")

        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=160, y=0, relwidth=1, relheight=1)

        tk.Label(self.root, image=self.imagen_usuarios).place(x=0, y=10)
        self.btnUsers = tk.Button(self.root, text="Usuarios", command=self.abrir_gestion_usuarios, bg='black', fg='white')
        self.btnUsers.place(x=30, y=10)

        tk.Label(self.root, image=self.imagen_preAlumnos).place(x=0, y=40)
        self.btnPreRAlumnos = tk.Button(self.root, text="Pre-registro Alumnos", command=self.abrir_gestion_PreRAlumnos, bg='black', fg='white')
        self.btnPreRAlumnos.place(x=30, y=40)

        tk.Label(self.root, image=self.imagen_preMaestros).place(x=0, y=70)
        self.btnPreRMaestros = tk.Button(self.root, text="Pre-registro Maestros", command=self.abrir_gestion_PreRMaestros, bg='black', fg='white')
        self.btnPreRMaestros.place(x=30, y=70)

        tk.Label(self.root, image=self.imagen_materias).place(x=0, y=100)
        self.btnMaterias = tk.Button(self.root, text="Materias", command=self.abrir_gestion_materias, bg='black', fg='white')
        self.btnMaterias.place(x=30, y=100)
        
        tk.Label(self.root, image=self.imagen_grupos).place(x=0, y=130)
        self.btnGrupos = tk.Button(self.root, text="Grupos", command=self.abrir_gestion_grupos, bg='black', fg='white')
        self.btnGrupos.place(x=30, y=130)

        tk.Label(self.root, image=self.imagen_horarios).place(x=0, y=160)
        self.btnHorarios = tk.Button(self.root, text="Horarios", command=self.abrir_gestion_horarios, bg='black', fg='white')
        self.btnHorarios.place(x=30, y=160)

        tk.Label(self.root, image=self.imagen_salon).place(x=0, y=190)
        self.btnSalon = tk.Button(self.root, text="Salones", command=self.abrir_gestion_salones, bg='black', fg='white')
        self.btnSalon.place(x=30, y=190)
        
        tk.Label(self.root, image=self.imagen_carrera).place(x=0, y=220)
        self.btnCarrrera = tk.Button(self.root, text="Carreras", command=self.abrir_gestion_carrera, bg='black', fg='white')
        self.btnCarrrera.place(x=30, y=220)

        tk.Label(self.root, image=self.imagen_califiaciones).place(x=0, y=250)
        self.btnCalificaciones = tk.Button(self.root, text="Calificaciones", command=self.abrir_gestion_calificaciones, bg='black', fg='white')
        self.btnCalificaciones.place(x=30, y=250)

        tk.Label(self.root, image=self.imagen_mostrarCalifiaciones).place(x=0, y=280)
        self.btnMostrarCalificaciones = tk.Button(self.root, text="Mostrar Calificaciones", command=self.abrir_gestion_MostrarCalificaciones, bg='black', fg='white')
        self.btnMostrarCalificaciones.place(x=30, y=280)

        tk.Label(self.root, image=self.imagen_planeacion).place(x=0, y=310)
        self.btnPlaneacion = tk.Button(self.root, text="Planeación", command=self.abrir_gestion_planeacion, bg='black', fg='white')
        self.btnPlaneacion.place(x=30, y=310)

        tk.Label(self.root, image=self.imagen_salir).place(x=0, y=400)
        self.btnSalir = tk.Button(self.root, text="Salir", command=self.salir, bg='black', fg='white')
        self.btnSalir.place(x=30, y=400)

        tk.Label(self.root, image=self.imagen_dinosaurio).place(x=0, y=430)
        self.btnDino = tk.Button(self.root, text="Dino", command=self.dino, bg='black', fg='white')
        self.btnDino.place(x=30, y=430)

        # Cambiar usuarios
        tk.Label(self.root, image=self.imagen_cambiarUsuario).place(x=0, y=460)
        self.btnCambiarUsuario = tk.Button(self.root, text="Cambiar Usuario", command=self.cambiar_usuario, bg='black', fg='white')
        self.btnCambiarUsuario.place(x=30, y=460)

    def abrir_gestion_usuarios(self):
        global userprofile
        if userprofile == "Admin":
            self.root.destroy()  # Cerrar la ventana de opciones
            root = tk.Tk()
            app = Usuarios(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")

    def abrir_gestion_PreRAlumnos(self):
        global userprofile
        if userprofile == "Admin":
            self.root.destroy()
            root = tk.Tk()
            app = PreRAlumnos(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")
    
    def abrir_gestion_PreRMaestros(self):
        global userprofile
        if userprofile == "Admin":
            self.root.destroy()
            root = tk.Tk()
            app = PreRMaestros(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")
    
    def abrir_gestion_materias(self):
        global userprofile
        if userprofile == "Admin" or userprofile == "Maestro":
            self.root.destroy()
            root = tk.Tk()
            app = Materias(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")
    
    def abrir_gestion_grupos(self):
        global userprofile
        if userprofile == "Admin":
            self.root.destroy()
            root = tk.Tk()
            app = Grupos(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")

    def abrir_gestion_horarios(self):
        global userprofile
        if userprofile == "Admin":
            self.root.destroy()
            root = tk.Tk()
            app = Horario(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")

    def abrir_gestion_salones(self):
        global userprofile
        if userprofile == "Admin":
            self.root.destroy()
            root = tk.Tk()
            app = Salon(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")
    
    def abrir_gestion_carrera(self):
        global userprofile
        if userprofile == "Admin":
            self.root.destroy()
            root = tk.Tk()
            app = Carrera(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")

    def abrir_gestion_calificaciones(self):
        global userprofile
        if userprofile == "Admin" or userprofile == "Maestro":
            self.root.destroy()
            root = tk.Tk()
            app = Calificaciones_Alta(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")

    def abrir_gestion_MostrarCalificaciones(self):
        global userprofile
        if userprofile == "Alumno":
            self.root.destroy()
            root = tk.Tk()
            app = Mostrar_Calificaciones(root) # Modificar
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")

    def abrir_gestion_planeacion(self):
        global userprofile
        if userprofile == "Admin":
            self.root.destroy()
            root = tk.Tk()
            app = PlaneacionSalon(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "No tienes permisos para acceder a esta opción")

    def dino(self):
        game = Game()
        game.run()

    def salir(self):
        self.root.destroy()  # Cerrar la ventana de opciones

    def cambiar_usuario(self):
        self.root.destroy()
        root = tk.Tk()
        app = Login(root)
        root.mainloop()


class Usuarios:
    def __init__(self, root):
        self.root = root
        self.root.config(width=500, height=400)
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Gestión de Usuarios")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Create users table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                NOMBRE VARCHAR(255),
                Apellido_Paterno VARCHAR(255),
                Apellido_Materno VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                PASSWORD VARCHAR(255),
                PERFIL TEXT
            );
        """)
        self.connection.commit()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        self.imagen_boton_nuevo = tk.PhotoImage(file="Nuevo.png")
        self.imagen_boton_guardar = tk.PhotoImage(file="Guardar.png")
        self.imagen_boton_editar = tk.PhotoImage(file="Editar.png")
        self.imagen_boton_cancelar = tk.PhotoImage(file="Cancelar.png")
        self.imagen_boton_eliminar = tk.PhotoImage(file="Eliminar.png")
        self.imagen_boton_buscar = tk.PhotoImage(file="Buscar.png")
        self.imagen_boton_menu = tk.PhotoImage(file="Menu.png")

        global usernameuser
        tk.Label(self.root, text="Usuario: " + usernameuser, bg='black', fg='white').place(x=10, y=240)

        tk.Label(self.root, text="Buscar ID:", bg='black', fg='white').place(x=250, y=10)
        self.txBuscar = tk.Entry(self.root)
        self.txBuscar.place(x=360, y=10)

        self.btnBuscar = tk.Button(self.root, text="Buscar", command=self.buscar_usuario, image=self.imagen_boton_buscar)
        self.btnBuscar.place(x=315, y=10)

        tk.Label(self.root, text="ID:", bg='black', fg='white').place(x=10, y=10)
        self.txId = tk.Entry(self.root, state='disabled')
        self.txId.place(x=10, y=30)

        tk.Label(self.root, text="Nombre", bg='black', fg='white').place(x=10, y=50)
        self.txNombre = tk.Entry(self.root, width=30, state='disabled')
        self.txNombre.place(x=10, y=70)

        tk.Label(self.root, text="Apellido Paterno", bg='black', fg='white').place(x=10, y=90)
        self.txApaterno = tk.Entry(self.root, width=30, state='disabled')
        self.txApaterno.place(x=10, y=110)

        tk.Label(self.root, text="Apellido Materno", bg='black', fg='white').place(x=10, y=130)
        self.txAmaterno = tk.Entry(self.root, width=30, state='disabled')
        self.txAmaterno.place(x=10, y=150)

        tk.Label(self.root, text="Email", bg='black', fg='white').place(x=10, y=170)
        self.txEmail = tk.Entry(self.root, width=30, state='disabled')
        self.txEmail.place(x=10, y=190)

        tk.Label(self.root, text="Contraseña:", bg='black', fg='white').place(x=250, y=50)
        self.txPassword = tk.Entry(self.root, show='*', state='disabled')
        self.txPassword.place(x=250, y=70)

        tk.Label(self.root, text="Perfil:", bg='black', fg='white').place(x=250, y=90)
        self.cbProfile = ttk.Combobox(self.root, state='disabled', values=["Admin", "Maestro", "Alumno", "Inactivo"])
        self.cbProfile.place(x=250, y=110)

        self.btnNuevo = tk.Button(self.root, text="Nuevo", command=self.nuevo_usuario, image=self.imagen_boton_nuevo)
        self.btnNuevo.place(x=200, y=250)

        self.btnGuardar = tk.Button(self.root, text="Guardar", state='disabled', command=self.guardar_usuario, image=self.imagen_boton_guardar)
        self.btnGuardar.place(x=226+20, y=250)

        self.btnCancelar = tk.Button(self.root, text="Cancelar", state='disabled', command=self.cancelar, image=self.imagen_boton_cancelar)
        self.btnCancelar.place(x=252+40, y=250)

        self.btnEditar = tk.Button(self.root, text="Editar", state='disabled', command=self.editar_usuario, image=self.imagen_boton_editar)
        self.btnEditar.place(x=278+60, y=250)

        self.btnEliminar = tk.Button(self.root, text="Eliminar", state='disabled', command=self.eliminar_usuario, image=self.imagen_boton_eliminar)
        self.btnEliminar.place(x=304+80, y=250)

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, image=self.imagen_boton_menu)
        self.btnMenu.place(x=330+100, y=250)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def validar_nombre(self, nombre):
        # Utilizar regex para validar que solo contiene letras y espacios
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            messagebox.showerror("Error", "Nombre solo debe contener letras y espacios")
            return False
        return True

    def validar_usuario(self, usuario):
        # Utilizar regex para validar que solo contiene letras, números y espacios
        if not re.match(r'^[a-zA-Z0-9 ]+$', usuario):
            messagebox.showerror("Error", "Usuario solo debe contener letras, números y espacios")
            return False
        return True

    def validar_contrasena(self, contrasena):
        # Utilizar regex para validar que no contiene espacios
        if ' ' in contrasena:
            messagebox.showerror("Error", "Contraseña no debe contener espacios")
            return False
        if (len(contrasena) < 6):
            messagebox.showerror("Error", "Contraseña debe tener mínimo 6 caracteres de extensión")
            return False
        if not any(c in string.ascii_uppercase for c in contrasena):
            messagebox.showerror("Error", "Contraseña debe contener al menos una mayúscula")
            return False
        if not any(c in string.ascii_lowercase for c in contrasena):
            messagebox.showerror("Error", "Contraseña debe contener al menos una minúscula")
            return False
        if not any(c in string.digits for c in contrasena):
            messagebox.showerror("Error", "Contraseña debe contener al menos un número")
            return False
        return True
    
    #def validar_email(email):
    #    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) is not None

    def validar_email(self, email):
        # Expresión regular para validar el formato del correo electrónico
        patron_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(patron_email, email):
            # Verificar que no haya espacios en el correo
            if ' ' in email:
                messagebox.showerror("Error", "Error: El correo no debe contener espacios")
                return False
            return True
        else:
            messagebox.showerror("Error", "Correo electrónico inválido")
            return False

    def validar_perfil(self, perfil):
        # Validar que el perfil sea "Admin", "Maestro" o "Alumno
        opciones_perfil = ["Admin", "Maestro", "Alumno"]
        if perfil not in opciones_perfil:
            messagebox.showerror("Error", "El perfil debe ser Admin o Maestro o Alumno")
            return False
        return True

    def id_existe(self, user_id):
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID debe ser un número entero")
            return False

        # Consultar si el ID ya existe en la base de datos
        self.cursor.execute("SELECT * FROM usuarios WHERE ID = %s", (user_id,))
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False
        
    def buscar_usuario(self):
        id_buscar = self.txBuscar.get()

        # Consultar el usuario por ID en la base de datos
        self.cursor.execute("SELECT * FROM usuarios WHERE ID = %s", (id_buscar,))
        usuario = self.cursor.fetchone()

        if usuario:
            # Mostrar los datos en la interfaz gráfica
            self.txId.config(state='normal')
            self.txNombre.config(state='normal')
            self.txApaterno.config(state='normal')
            self.txAmaterno.config(state='normal')
            self.txEmail.config(state='normal')
            self.txPassword.config(state='normal')
            self.cbProfile.config(state='readonly')

            self.txId.delete(0, tk.END)
            self.txNombre.delete(0, tk.END)
            self.txApaterno.delete(0, tk.END)
            self.txAmaterno.delete(0, tk.END)
            self.txEmail.delete(0, tk.END)
            self.txPassword.delete(0, tk.END)
            self.cbProfile.set('')

            self.txId.insert(tk.END, usuario[0])
            self.txNombre.insert(tk.END, usuario[1])
            self.txApaterno.insert(tk.END, usuario[2])
            self.txAmaterno.insert(tk.END, usuario[3])
            self.txEmail.insert(tk.END, usuario[4])
            self.txPassword.insert(tk.END, usuario[5])
            self.cbProfile.set(usuario[6])

            self.btnEditar.config(state='normal')
            self.btnEliminar.config(state='normal')
            self.txId.config(state='disabled')
            self.txBuscar.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def nuevo_usuario(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.txNombre.config(state='normal')
        self.txApaterno.config(state='normal')
        self.txAmaterno.config(state='normal')
        self.txEmail.config(state='normal')
        self.txPassword.config(state='normal')
        self.cbProfile.config(state='readonly')
        self.cursor.execute("SELECT MAX(ID) FROM usuarios")
        max_id = self.cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1
        self.txId.delete(0, tk.END)
        self.txId.insert(tk.END, new_id)
        self.txId.config(state='disabled')
        self.btnNuevo.config(state='disabled')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def guardar_usuario(self):
        user_id = self.txId.get()
        nombre = self.txNombre.get()
        apellido_Paterno = self.txApaterno.get()
        apellido_Materno = self.txAmaterno.get()
        email = self.txEmail.get()
        password = self.txPassword.get()
        profile = self.cbProfile.get()

        opciones_profile = ["Admin", "Maestro", "Alumno"]

        if not user_id or not nombre or not apellido_Paterno or not apellido_Materno or not email or not password or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Admin, Maestro o Alumno")

        elif not self.validar_nombre(nombre) or not self.validar_nombre(apellido_Paterno) or not self.validar_nombre(apellido_Materno) or not self.validar_contrasena(password) or not self.validar_perfil(profile) or not self.validar_email(email):
            pass  # Handle validation errors as needed
        else:
            # Insertar el nuevo usuario en la base de datos
            self.cursor.execute("INSERT INTO usuarios (NOMBRE, Apellido_Paterno, Apellido_Materno, email, PASSWORD, PERFIL) VALUES (%s, %s, %s, %s, %s, %s)",
                               (nombre, apellido_Paterno, apellido_Materno, email, password, profile))
            self.connection.commit()

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.btnGuardar.config(state='disabled')
            self.btnCancelar.config(state='disabled')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')
            messagebox.showinfo("Éxito", "Usuario guardado correctamente")

    def cancelar(self):
        self.limpiar()
        self.btnNuevo.config(state='normal')

    def editar_usuario(self):
        user_id = self.txId.get()
        nombre = self.txNombre.get()
        apellido_Paterno = self.txApaterno.get()
        apellido_Materno = self.txAmaterno.get()
        email = self.txEmail.get()
        password = self.txPassword.get()
        profile = self.cbProfile.get()

        opciones_profile = ["Admin", "Maestro", "Alumno"]

        if not user_id or not nombre or not apellido_Paterno or not apellido_Materno or not email or not password or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Admin, Maestro o Alumno")
        elif not self.validar_nombre(nombre) or not self.validar_nombre(apellido_Paterno) or not self.validar_nombre(apellido_Materno) or not self.validar_contrasena(password) or not self.validar_perfil(profile) or not self.validar_email(email):
            pass  # Handle validation errors as needed
        else:
            # Actualizar el usuario en la base de datos
            self.cursor.execute("UPDATE usuarios SET NOMBRE=%s, Apellido_Paterno=%s, Apellido_Materno=%s, email=%s, PASSWORD=%s, PERFIL=%s WHERE ID=%s",
                               (nombre, apellido_Paterno, apellido_Materno, email, password, profile, user_id))
            self.connection.commit()

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def eliminar_usuario(self):
        id_eliminar = self.txId.get()
        self.limpiar()

        # Actualizar el perfil a "Inactivo" en lugar de eliminar físicamente
        self.cursor.execute("UPDATE usuarios SET Perfil=%s WHERE ID=%s", ("Inactivo", id_eliminar))
        self.connection.commit()

        self.btnNuevo.config(state='normal')

    def limpiar(self):
        self.txId.config(state='normal')
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txApaterno.delete(0, tk.END)
        self.txAmaterno.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)
        self.txPassword.delete(0, tk.END)
        self.cbProfile.set('')
        self.txId.config(state='disabled')
        self.txNombre.config(state='disabled')
        self.txApaterno.config(state='disabled')
        self.txAmaterno.config(state='disabled')
        self.txEmail.config(state='disabled')
        self.txPassword.config(state='disabled')
        self.cbProfile.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

# ------------------------------- Fin de la clase Usuarios -----------------------------------

# ------------------------------- Pre-registro de alumnos -----------------------------------

class PreRAlumnos:
    def __init__(self, root):
        self.root = root
        self.root.config(width=500, height=400)
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Pre-registro de Alumnos")
        self.root.configure(bg='#474D5C')


        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Create users table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS preregistro (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                IDUsuario INT,
                NOMBRE VARCHAR(255),
                Apellido_Paterno VARCHAR(255),
                Apellido_Materno VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                PERFIL TEXT,
                FechaDeNacimiento DATE,
                Carrera VARCHAR(255),
                Materia VARCHAR(255)
            );
        """)
        self.connection.commit()

        self.validar_contenido()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        global usernameuser
        self.imagen_boton_nuevo = tk.PhotoImage(file="Nuevo.png")
        self.imagen_boton_guardar = tk.PhotoImage(file="Guardar.png")
        self.imagen_boton_editar = tk.PhotoImage(file="Editar.png")
        self.imagen_boton_cancelar = tk.PhotoImage(file="Cancelar.png")
        self.imagen_boton_eliminar = tk.PhotoImage(file="Eliminar.png")
        self.imagen_boton_buscar = tk.PhotoImage(file="Buscar.png")
        self.imagen_boton_menu = tk.PhotoImage(file="Menu.png")
        tk.Label(self.root, text="Usuario: " + usernameuser, bg='black', fg='white').place(x=10, y=270)

        tk.Label(self.root, text="Buscar ID:", bg='black', fg='white').place(x=250, y=10)
        self.txBuscar = tk.Entry(self.root)
        self.txBuscar.place(x=360, y=10)

        self.btnBuscar = tk.Button(self.root, text="Buscar", command=self.buscar_usuario, image=self.imagen_boton_buscar)
        self.btnBuscar.place(x=315, y=10)

        tk.Label(self.root, text="ID:", bg='black', fg='white').place(x=10, y=10)
        self.txId = tk.Entry(self.root, state='disabled')
        self.txId.place(x=10, y=30)

        tk.Label(self.root, text="ID Alumno", bg='black', fg='white').place(x=10, y=50)
        # Cambiar los valores de la lista según los ID de los usuarios de la tabla de usuarios :)
        self.cursor.execute("SELECT ID FROM usuarios WHERE PERFIL = 'Alumno';")
        Datos= self.cursor.fetchall()

        self.cbIdAlumno = ttk.Combobox(self.root, state='disabled', values=Datos)
        self.cbIdAlumno.bind("<<ComboboxSelected>>", self.actualizar_id_part)
        self.cbIdAlumno.place(x=10, y=70)

        tk.Label(self.root, text="Nombre", bg='black', fg='white').place(x=10, y=90)
        self.txNombre = tk.Entry(self.root, width=30, state='disabled')
        self.txNombre.place(x=10, y=110)

        tk.Label(self.root, text="Apellido Paterno", bg='black', fg='white').place(x=10, y=130)
        self.txApaterno = tk.Entry(self.root, width=30, state='disabled')
        self.txApaterno.place(x=10, y=150)

        tk.Label(self.root, text="Apellido Materno", bg='black', fg='white').place(x=10, y=170)
        self.txAmaterno = tk.Entry(self.root, width=30, state='disabled')
        self.txAmaterno.place(x=10, y=190)

        tk.Label(self.root, text="Email", bg='black', fg='white').place(x=10, y=210)
        self.txEmail = tk.Entry(self.root, width=30, state='disabled')
        self.txEmail.place(x=10, y=230)

        tk.Label(self.root, text="Perfil:", bg='black', fg='white').place(x=250, y=50)
        self.cbProfile = ttk.Combobox(self.root, state='disabled', values=["Activo", "Inactivo"])
        self.cbProfile.place(x=250, y=70)

        tk.Label(self.root, text="Fecha de Nacimiento", bg='black', fg='white').place(x=250, y=90)
        self.txFechaNacimiento = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2, state="disabled", date_pattern="dd/mm/yyyy")
        self.txFechaNacimiento.place(x=250, y=110)

        tk.Label(self.root, text="Carrera", bg='black', fg='white').place(x=250, y=130)
        self.cursor.execute("SELECT NombreCarrera FROM carrera where perfil = 'Activo'")
        Carrera=self.cursor.fetchall()
        if len(Carrera)>=1:
            self.cbCarrera = ttk.Combobox(self.root, state='disabled', values=Carrera)
        else:
            self.cbCarrera = ttk.Combobox(self.root, state='disabled', values=[])
        self.cbCarrera.place(x=250, y=150)
        
        self.cbCarrera.bind("<<ComboboxSelected>>", self.CambiarGrupo)


        tk.Label(self.root, text="Grupo", bg='black', fg='white').place(x=250, y=170)
        self.cbMateria = ttk.Combobox(self.root, state='disabled', values=[])
        self.cbMateria.place(x=250, y=190)


        self.btnNuevo = tk.Button(self.root, text="Nuevo", command=self.nuevo_usuario, image=self.imagen_boton_nuevo)
        self.btnNuevo.place(x=200, y=250)

        self.btnGuardar = tk.Button(self.root, text="Guardar", state='disabled', command=self.guardar_usuario, image=self.imagen_boton_guardar)
        self.btnGuardar.place(x=226+20, y=250)

        self.btnCancelar = tk.Button(self.root, text="Cancelar", state='disabled', command=self.cancelar, image=self.imagen_boton_cancelar)
        self.btnCancelar.place(x=252+40, y=250)

        self.btnEditar = tk.Button(self.root, text="Editar", state='disabled', command=self.editar_usuario, image=self.imagen_boton_editar)
        self.btnEditar.place(x=278+60, y=250)

        self.btnEliminar = tk.Button(self.root, text="Eliminar", state='disabled', command=self.eliminar_usuario, image=self.imagen_boton_eliminar)
        self.btnEliminar.place(x=304+80, y=250)

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, image=self.imagen_boton_menu)
        self.btnMenu.place(x=330+100, y=250)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    
    def validar_contenido(self):
        self.cursor.execute("SELECT NombreCarrera FROM carrera where perfil = 'Activo' ")
        self.DCarrera = self.cursor.fetchall()

        self.cursor.execute("SELECT ID FROM usuarios WHERE PERFIL = 'Alumno' ")
        self.DAlumnos= self.cursor.fetchall()

        self.cursor.execute("SELECT NombrGrupo FROM grupo where perfil = 'Activo' ")
        DGrupo= self.cursor.fetchall()

        if len(self.DCarrera) == 0 or len(self.DAlumnos)==0 or len(DGrupo)==0:
            messagebox.showinfo("Advertencia", "La tabla está vacía. Primero debe registrar contenido.")
            self.abrir_menu()
        
    def actualizar_id_part(self, event):
        
        ID= self.cbIdAlumno.get()
        self.cursor.execute("SELECT NOMBRE, Apellido_Paterno, Apellido_Materno, email FROM usuarios WHERE ID = '"+ID+"';")
        Datos= self.cursor.fetchall()


        self.txNombre.config(state='normal')
        self.txApaterno.config(state='normal')
        self.txAmaterno.config(state='normal')
        self.txEmail.config(state='normal')

        self.txNombre.delete(0, tk.END)
        self.txApaterno.delete(0, tk.END)
        self.txAmaterno.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)
        
        self.txNombre.insert(tk.END, Datos[0][0])
        self.txApaterno.insert(tk.END, Datos[0][1])
        self.txAmaterno.insert(tk.END, Datos[0][2])
        self.txEmail.insert(tk.END, Datos[0][3])
       
        self.txNombre.config(state='disabled')
        self.txApaterno.config(state='disabled')
        self.txAmaterno.config(state='disabled')
        self.txEmail.config(state='disabled')

        self.btnEditar.config(state='normal')
        self.btnEliminar.config(state='normal')
        self.txId.config(state='disabled')
        self.txBuscar.delete(0, tk.END)

    def id_existe(self, user_id):
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID debe ser un número entero")
            return False

        # Consultar si el ID ya existe en la base de datos
        self.cursor.execute("SELECT * FROM preregistro WHERE ID = %s", (user_id,))
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False

    def validar_fecha_nacimiento(self, fecha_nacimiento):
        try:
            VNace = fecha_nacimiento.strftime("%d/%m/%Y")
        except:
            try:
                fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            except:
                messagebox.showerror("Error", "La Fecha debe seguir el formato DD/MM/YYYY")
                return False
                
        fecha_actual = datetime.now()
        
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        
        if edad < 18:
            messagebox.showerror("Error", "La persona debe ser mayor de edad.")
            return False
        
        return True

    def validar_correo_existente(self, email):
        # Verificar si el correo electrónico ya existe en la base de datos
        self.cursor.execute("SELECT COUNT(*) FROM preregistro WHERE email = %s", (email,))
        count = self.cursor.fetchone()[0]
        if count > 0:
            messagebox.showerror("Error", "No puedes registrar al alumno a diferentes grupos o al mismo dos veces")
            return True
        return False

    def CambiarGrupo(self, event):
        Carrera=self.cbCarrera.get()
        
        self.cursor.execute("SELECT NombrGrupo FROM grupo where perfil = 'Activo' and Carrera='"+Carrera+"'")
        Grupo=self.cursor.fetchall()
        if len(Grupo)>=1:
            self.cbMateria.config(values=Grupo)
        else:
            self.cbMateria.config(values=[]) 

    def buscar_usuario(self):
        id_buscar = self.txBuscar.get()

        # Consultar el preregistro por ID en la base de datos
        self.cursor.execute("SELECT * FROM preregistro WHERE ID = %s", (id_buscar,))
        usuario = self.cursor.fetchone()

        if usuario:
            # Mostrar los datos en la interfaz gráfica
            self.txId.config(state='normal')
            self.cbIdAlumno.config(state='readonly')
            self.txNombre.config(state='normal')
            self.txApaterno.config(state='normal')
            self.txAmaterno.config(state='normal')
            self.txEmail.config(state='normal')
            self.cbProfile.config(state='readonly')
            self.txFechaNacimiento.config(state='normal')
            self.cbCarrera.config(state='readonly')
            self.cbMateria.config(state='readonly')

            self.txId.delete(0, tk.END)
            self.cbIdAlumno.set('')
            self.txNombre.delete(0, tk.END)
            self.txApaterno.delete(0, tk.END)
            self.txAmaterno.delete(0, tk.END)
            self.txEmail.delete(0, tk.END)
            self.cbProfile.set('')
            self.txFechaNacimiento.delete(0, tk.END)
            self.cbCarrera.set('')
            self.cbMateria.set('')

            self.txId.insert(tk.END, usuario[0])
            self.cbIdAlumno.set(usuario[1])
            self.txNombre.insert(tk.END, usuario[2])
            self.txApaterno.insert(tk.END, usuario[3])
            self.txAmaterno.insert(tk.END, usuario[4])
            self.txEmail.insert(tk.END, usuario[5])
            self.cbProfile.set(usuario[6])
            self.txFechaNacimiento.insert(0, usuario[7].strftime("%d/%m/%Y"))
            self.cbCarrera.set(usuario[8])
            self.cbMateria.set(usuario[9])
            self.CambiarGrupo("a")

            
            self.btnEditar.config(state='normal')
            self.btnEliminar.config(state='normal')
            self.txId.config(state='disabled')
            self.txBuscar.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def nuevo_usuario(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.cbIdAlumno.config(state='readonly')
        self.txNombre.config(state='normal')
        self.txApaterno.config(state='normal')
        self.txAmaterno.config(state='normal')
        self.txEmail.config(state='normal')
        self.cbProfile.config(state='readonly')
        self.txFechaNacimiento.config(state='normal')
        self.cbCarrera.config(state='readonly')
        self.cbMateria.config(state='readonly')
        self.cursor.execute("SELECT MAX(ID) FROM preregistro")
        max_id = self.cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1
        self.txId.delete(0, tk.END)
        self.txId.insert(tk.END, new_id)
        self.txId.config(state='disabled')
        self.btnNuevo.config(state='disabled')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def guardar_usuario(self):
        user_id = self.txId.get()
        id_alumno = self.cbIdAlumno.get()
        nombre = self.txNombre.get()
        apellido_Paterno = self.txApaterno.get()
        apellido_Materno = self.txAmaterno.get()
        email = self.txEmail.get()
        profile = self.cbProfile.get()
        fecha_nacimiento = self.txFechaNacimiento.get()  # Formato recibido: 'DD/MM/YYYY'
        carrera = self.cbCarrera.get()
        materia = self.cbMateria.get()

        # Convertir fecha de 'DD/MM/YYYY' a 'YYYY-MM-DD'
        

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not nombre or not apellido_Paterno or not apellido_Materno or not email or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser activo o inactivo")

        elif not self.validar_fecha_nacimiento(fecha_nacimiento):
            pass
        elif self.validar_correo_existente(email):
            pass
        else:
            # Insertar el nuevo usuario en la base de datos
            fecha_nacimiento_formato_sql = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").strftime("%Y-%m-%d")
            self.cursor.execute("INSERT INTO preregistro (IDUsuario, NOMBRE, Apellido_Paterno, Apellido_Materno, email, PERFIL, FechaDeNacimiento, Carrera, Materia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                 (id_alumno, nombre, apellido_Paterno, apellido_Materno, email, profile, fecha_nacimiento_formato_sql, carrera, materia))
            self.connection.commit()

            # Actualizar el número de cupos disponibles en el grupo correspondiente
            self.cursor.execute("UPDATE grupo SET MaxNumAlumnos = MaxNumAlumnos - 1 WHERE NombrGrupo = %s", (materia,))
            self.connection.commit()

            # Verificar si el grupo se quedó sin cupos
            self.cursor.execute("SELECT MaxNumAlumnos FROM grupo WHERE NombrGrupo = %s", (materia,))
            max_num_alumnos = self.cursor.fetchone()[0]
            if max_num_alumnos == 0:
                messagebox.showerror("Error", "Ya no quedan cupos disponibles en este grupo")
            else:
                self.limpiar()
                self.btnNuevo.config(state='normal')
                self.btnGuardar.config(state='disabled')
                self.btnCancelar.config(state='disabled')
                self.txId.config(state='normal')
                self.txId.delete(0, tk.END)
                self.txId.config(state='disabled')
                messagebox.showinfo("Éxito", "Usuario guardado correctamente")

    def cancelar(self):
        self.limpiar()
        self.btnNuevo.config(state='normal')

    def editar_usuario(self):
        user_id = self.txId.get()
        id_alumno = self.cbIdAlumno.get()
        nombre = self.txNombre.get()
        apellido_Paterno = self.txApaterno.get()
        apellido_Materno = self.txAmaterno.get()
        email = self.txEmail.get()
        profile = self.cbProfile.get()
        fecha_nacimiento = self.txFechaNacimiento.get()
        carrera = self.cbCarrera.get()
        materia = self.cbMateria.get()

        opciones_profile = ["Activo", "Inactivo"]
        
        


        if not user_id or not nombre or not apellido_Paterno or not apellido_Materno or not email or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser activo o inactivo")
        elif not self.validar_fecha_nacimiento(fecha_nacimiento):
            pass
        else:
            # Actualizar el usuario en la base de datos
            fecha_nacimiento_formato_sql = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").strftime("%Y-%m-%d")
            self.cursor.execute("UPDATE preregistro SET IDUsuario=%s, NOMBRE=%s, Apellido_Paterno=%s, Apellido_Materno=%s, email=%s, PERFIL=%s, FechaDeNacimiento=%s, Carrera=%s, Materia=%s WHERE ID=%s;",
                               (id_alumno, nombre, apellido_Paterno, apellido_Materno, email, profile, fecha_nacimiento_formato_sql, carrera, materia, user_id))
            self.connection.commit()

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def eliminar_usuario(self):
        id_eliminar = self.txId.get()
        self.limpiar()

        # Actualizar el perfil a "Inactivo" en lugar de eliminar físicamente
        self.cursor.execute("UPDATE preregistro SET Perfil=%s WHERE ID=%s", ("Inactivo", id_eliminar))
        self.connection.commit()

        self.btnNuevo.config(state='normal')

    def limpiar(self):
        self.txId.config(state='normal')
        self.txId.delete(0, tk.END)
        self.cbIdAlumno.set('')
        self.txNombre.delete(0, tk.END)
        self.txApaterno.delete(0, tk.END)
        self.txAmaterno.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)
        self.cbProfile.set('')
        self.txFechaNacimiento.delete(0, tk.END)
        self.cbCarrera.set('')
        self.cbMateria.set('')
        self.txId.config(state='disabled')
        self.cbIdAlumno.config(state='disabled')
        self.txNombre.config(state='disabled')
        self.txApaterno.config(state='disabled')
        self.txAmaterno.config(state='disabled')
        self.txEmail.config(state='disabled')
        self.cbProfile.config(state='disabled')
        self.txFechaNacimiento.config(state='disabled')
        self.cbCarrera.config(state='disabled')
        self.cbMateria.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

# ------------------------------- Fin Pre-registro de alumnos -----------------------------------

class PreRMaestros:
    def __init__(self, root):
        self.root = root
        self.root.config(width=500, height=400)
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Pre-registro de Maestros")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Create users table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS premaestros (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                IDUsuario INT,
                NOMBRE VARCHAR(255),
                Apellido_Paterno VARCHAR(255),
                Apellido_Materno VARCHAR(255),
                email VARCHAR(255),
                PERFIL TEXT,
                carrera VARCHAR(255),
                materia VARCHAR(255),
                gradoEstudios VARCHAR(255)
            );
        """)
        self.connection.commit()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        global usernameuser
        self.imagen_boton_nuevo = tk.PhotoImage(file="Nuevo.png")
        self.imagen_boton_guardar = tk.PhotoImage(file="Guardar.png")
        self.imagen_boton_editar = tk.PhotoImage(file="Editar.png")
        self.imagen_boton_cancelar = tk.PhotoImage(file="Cancelar.png")
        self.imagen_boton_eliminar = tk.PhotoImage(file="Eliminar.png")
        self.imagen_boton_buscar = tk.PhotoImage(file="Buscar.png")
        self.imagen_boton_menu = tk.PhotoImage(file="Menu.png")
        tk.Label(self.root, text="Usuario: " + usernameuser, bg='black', fg='white').place(x=10, y=270)

        tk.Label(self.root, text="Buscar ID:", bg='black', fg='white').place(x=250, y=10)
        self.txBuscar = tk.Entry(self.root)
        self.txBuscar.place(x=360, y=10)

        self.btnBuscar = tk.Button(self.root, text="Buscar", command=self.buscar_usuario, image=self.imagen_boton_buscar)
        self.btnBuscar.place(x=315, y=10)

        tk.Label(self.root, text="ID:", bg='black', fg='white').place(x=10, y=10)
        self.txId = tk.Entry(self.root, state='disabled')
        self.txId.place(x=10, y=30)

        tk.Label(self.root, text="ID Maestro", bg='black', fg='white').place(x=10, y=50)
        # Cambiar los valores de la lista según los ID de los usuarios de la tabla de usuarios :)
        self.cursor.execute("SELECT ID FROM usuarios WHERE PERFIL = 'Maestro';")
        Datos= self.cursor.fetchall()

        self.cbIdMaestro = ttk.Combobox(self.root, state='disabled', values=Datos)
        self.cbIdMaestro.bind("<<ComboboxSelected>>", self.actualizar_id_part)
        self.cbIdMaestro.place(x=10, y=70)

        tk.Label(self.root, text="Nombre", bg='black', fg='white').place(x=10, y=90)
        self.txNombre = tk.Entry(self.root, width=30, state='disabled')
        self.txNombre.place(x=10, y=110)

        tk.Label(self.root, text="Apellido Paterno", bg='black', fg='white').place(x=10, y=130)
        self.txApaterno = tk.Entry(self.root, width=30, state='disabled')
        self.txApaterno.place(x=10, y=150)

        tk.Label(self.root, text="Apellido Materno", bg='black', fg='white').place(x=10, y=170)
        self.txAmaterno = tk.Entry(self.root, width=30, state='disabled')
        self.txAmaterno.place(x=10, y=190)

        tk.Label(self.root, text="Email", bg='black', fg='white').place(x=10, y=210)
        self.txEmail = tk.Entry(self.root, width=30, state='disabled')
        self.txEmail.place(x=10, y=230)

        tk.Label(self.root, text="Perfil:", bg='black', fg='white').place(x=250, y=50)
        self.cbProfile = ttk.Combobox(self.root, state='disabled', values=["Activo", "Inactivo"])
        self.cbProfile.place(x=250, y=70)
        # Modificar los valores de las listas según las carreras y materias de la base de datos :)
        
        tk.Label(self.root, text="Carrera", bg='black', fg='white').place(x=250, y=90)
        
        self.cursor.execute("SELECT NombreCarrera FROM carrera where perfil = 'Activo'")
        Carrera=self.cursor.fetchall()
        if len(Carrera)>=1:
            self.cbCarrera = ttk.Combobox(self.root, state='disabled', values=Carrera)
        else:
            self.cbCarrera = ttk.Combobox(self.root, state='disabled', values=[])
        self.cbCarrera.place(x=250, y=110)

        self.cbCarrera.bind("<<ComboboxSelected>>", self.CambiarMaterias)

        tk.Label(self.root, text="Materia", bg='black', fg='white').place(x=250, y=130)

        self.cbMateria = ttk.Combobox(self.root, state='disabled', values=[])
        self.cbMateria.place(x=250, y=150)

        tk.Label(self.root, text="Grado de Estudios", bg='black', fg='white').place(x=250, y=170)
        self.cbGradoEstudios = ttk.Combobox(self.root, state='disabled', values=["Licenciatura", "Maestría", "Doctorado"])
        self.cbGradoEstudios.place(x=250, y=190)

        self.btnNuevo = tk.Button(self.root, text="Nuevo", command=self.nuevo_usuario, image=self.imagen_boton_nuevo)
        self.btnNuevo.place(x=200, y=250)

        self.btnGuardar = tk.Button(self.root, text="Guardar", state='disabled', command=self.guardar_usuario, image=self.imagen_boton_guardar)
        self.btnGuardar.place(x=226+20, y=250)

        self.btnCancelar = tk.Button(self.root, text="Cancelar", state='disabled', command=self.cancelar, image=self.imagen_boton_cancelar)
        self.btnCancelar.place(x=252+40, y=250)

        self.btnEditar = tk.Button(self.root, text="Editar", state='disabled', command=self.editar_usuario, image=self.imagen_boton_editar)
        self.btnEditar.place(x=278+60, y=250)

        self.btnEliminar = tk.Button(self.root, text="Eliminar", state='disabled', command=self.eliminar_usuario, image=self.imagen_boton_eliminar)
        self.btnEliminar.place(x=304+80, y=250)

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, image=self.imagen_boton_menu)
        self.btnMenu.place(x=330+100, y=250)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()
        
    def actualizar_id_part(self, event):
        
        ID= self.cbIdMaestro.get()
        self.cursor.execute("SELECT NOMBRE, Apellido_Paterno, Apellido_Materno, email FROM usuarios WHERE ID = %s", (ID,))
        Datos= self.cursor.fetchall()

        self.txNombre.config(state='normal')
        self.txApaterno.config(state='normal')
        self.txAmaterno.config(state='normal')
        self.txEmail.config(state='normal')

        self.txNombre.delete(0, tk.END)
        self.txApaterno.delete(0, tk.END)
        self.txAmaterno.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)
        
        self.txNombre.insert(tk.END, Datos[0][0])
        self.txApaterno.insert(tk.END, Datos[0][1])
        self.txAmaterno.insert(tk.END, Datos[0][2])
        self.txEmail.insert(tk.END, Datos[0][3])
       
        self.txNombre.config(state='disabled')
        self.txApaterno.config(state='disabled')
        self.txAmaterno.config(state='disabled')
        self.txEmail.config(state='disabled')

        self.btnEditar.config(state='normal')
        self.btnEliminar.config(state='normal')
        self.txId.config(state='disabled')
        self.txBuscar.delete(0, tk.END)

    def id_existe(self, user_id):
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID debe ser un número entero")
            return False

        # Consultar si el ID ya existe en la base de datos
        self.cursor.execute("SELECT * FROM premaestros WHERE ID = %s", (user_id,))
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False
    
    def CambiarMaterias(self, event):
        Carrera=self.cbCarrera.get()
        
        self.cursor.execute("SELECT Asignatura FROM materias where perfil = 'Activo' and Carrera='"+Carrera+"'")
        Materia=self.cursor.fetchall()
        if len(Materia)>=1:
            self.cbMateria.config(values=Materia)
        else:
            self.cbMateria.config(values=[])

    def buscar_usuario(self):
        id_buscar = self.txBuscar.get()

        # Consultar el preregistro por ID en la base de datos
        self.cursor.execute("SELECT * FROM premaestros WHERE ID = %s", (id_buscar,))
        usuario = self.cursor.fetchone()

        if usuario:
            # Mostrar los datos en la interfaz gráfica
            self.txId.config(state='normal')
            self.cbIdMaestro.config(state='readonly')
            self.txNombre.config(state='normal')
            self.txApaterno.config(state='normal')
            self.txAmaterno.config(state='normal')
            self.txEmail.config(state='normal')
            self.cbProfile.config(state='readonly')
            self.cbCarrera.config(state='readonly')
            self.cbMateria.config(state='readonly')
            self.cbGradoEstudios.config(state='readonly')

            self.txId.delete(0, tk.END)
            self.cbIdMaestro.set('')
            self.txNombre.delete(0, tk.END)
            self.txApaterno.delete(0, tk.END)
            self.txAmaterno.delete(0, tk.END)
            self.txEmail.delete(0, tk.END)
            self.cbProfile.set('')
            self.cbCarrera.set('')
            self.cbMateria.set('')
            self.cbGradoEstudios.set('')

            self.txId.insert(tk.END, usuario[0])
            self.cbIdMaestro.set(usuario[1])
            self.txNombre.insert(tk.END, usuario[2])
            self.txApaterno.insert(tk.END, usuario[3])
            self.txAmaterno.insert(tk.END, usuario[4])
            self.txEmail.insert(tk.END, usuario[5])
            self.cbProfile.set(usuario[6])
            self.cbCarrera.set(usuario[7])
            self.cbMateria.set(usuario[8])
            self.cbGradoEstudios.set(usuario[9])

            
            self.btnEditar.config(state='normal')
            self.btnEliminar.config(state='normal')
            self.txId.config(state='disabled')
            self.txBuscar.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def nuevo_usuario(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.cbIdMaestro.config(state='readonly')
        self.txNombre.config(state='normal')
        self.txApaterno.config(state='normal')
        self.txAmaterno.config(state='normal')
        self.txEmail.config(state='normal')
        self.cbProfile.config(state='readonly')
        self.cbCarrera.config(state='readonly')
        self.cbMateria.config(state='readonly')
        self.cbGradoEstudios.config(state='readonly')
        self.cursor.execute("SELECT MAX(ID) FROM premaestros")
        max_id = self.cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1
        self.txId.delete(0, tk.END)
        self.txId.insert(tk.END, new_id)
        self.txId.config(state='disabled')
        self.btnNuevo.config(state='disabled')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def validar_perfil(self, perfil):
        # Validar que el perfil sea activo o inactivo
        opciones_perfil = ["Activo", "Inactivo"]
        if perfil not in opciones_perfil:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
            return False
        return True
    
    def validar_nombre(self, nombre):
        # Utilizar regex para validar que solo contiene letras y espacios
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            messagebox.showerror("Error", "Nombre solo debe contener letras y espacios")
            return False
        return True

    def validar_usuario(self, usuario):
        # Utilizar regex para validar que solo contiene letras, números y espacios
        if not re.match(r'^[a-zA-Z0-9 ]+$', usuario):
            messagebox.showerror("Error", "Usuario solo debe contener letras, números y espacios")
            return False
        return True

    def guardar_usuario(self):
        user_id = self.txId.get()
        id_Maestro = self.cbIdMaestro.get()
        nombre = self.txNombre.get()
        apellido_Paterno = self.txApaterno.get()
        apellido_Materno = self.txAmaterno.get()
        email = self.txEmail.get()
        profile = self.cbProfile.get()
        carrera = self.cbCarrera.get()
        materia = self.cbMateria.get()
        gradoEstudios = self.cbGradoEstudios.get()
    
        # Convertir fecha de 'DD/MM/YYYY' a 'YYYY-MM-DD'
    
        opciones_profile = ["Activo", "Inactivo"]
        opciones_gradoEstudios = ["Licenciatura", "Maestría", "Doctorado"]
    
        if not user_id or not nombre or not apellido_Paterno or not apellido_Materno or not email or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
        elif gradoEstudios not in opciones_gradoEstudios:
            messagebox.showerror("Error", "El grado de estudios debe ser Licenciatura, Maestría o Doctorado")

        elif not self.validar_nombre(profile) or not self.validar_nombre(carrera) or not self.validar_usuario(materia) or not self.validar_usuario(materia):
            pass
        else:
            # Insertar el nuevo usuario en la base de datos
            self.cursor.execute("INSERT INTO premaestros (IDUsuario, NOMBRE, Apellido_Paterno, Apellido_Materno, email, PERFIL, Carrera, Materia, GradoEstudios) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (id_Maestro, nombre, apellido_Paterno, apellido_Materno, email, profile, carrera, materia, gradoEstudios))
            self.connection.commit()
            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.btnGuardar.config(state='disabled')
            self.btnCancelar.config(state='disabled')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')
            messagebox.showinfo("Éxito", "Usuario guardado correctamente")


    def cancelar(self):
        self.limpiar()
        self.btnNuevo.config(state='normal')

    def editar_usuario(self):
        user_id = self.txId.get()
        id_Maestro = self.cbIdMaestro.get()
        nombre = self.txNombre.get()
        apellido_Paterno = self.txApaterno.get()
        apellido_Materno = self.txAmaterno.get()
        email = self.txEmail.get()
        profile = self.cbProfile.get()
        carrera = self.cbCarrera.get()
        materia = self.cbMateria.get()
        gradoEstudios = self.cbGradoEstudios.get()

        opciones_profile = ["Activo", "Inactivo"]
        opciones_gradoEstudios = ["Licenciatura", "Maestría", "Doctorado"]

        if not user_id or not nombre or not apellido_Paterno or not apellido_Materno or not email or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
        elif gradoEstudios not in opciones_gradoEstudios:
            messagebox.showerror("Error", "El grado de estudios debe ser Licenciatura, Maestría o Doctorado")

        elif not self.validar_nombre(profile) or not self.validar_nombre(carrera) or not self.validar_usuario(materia) or not self.validar_usuario(materia):
            pass
        else:
            # Actualizar el usuario en la base de datos
            self.cursor.execute("UPDATE premaestros SET IDUsuario=%s NOMBRE=%s, Apellido_Paterno=%s, Apellido_Materno=%s, email=%s, PERFIL=%s, Carrera=%s, Materia=%s GradoEstudios=%s WHERE ID=%s",
                               (id_Maestro, nombre, apellido_Paterno, apellido_Materno, email, profile, carrera, materia, user_id, gradoEstudios))
            self.connection.commit()

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def eliminar_usuario(self):
        id_eliminar = self.txId.get()
        self.limpiar()

        # Actualizar el perfil a "Inactivo" en lugar de eliminar físicamente
        self.cursor.execute("UPDATE premaestros SET Perfil=%s WHERE ID=%s", ("Inactivo", id_eliminar))
        self.connection.commit()

        self.btnNuevo.config(state='normal')

    def limpiar(self):
        self.txId.config(state='normal')
        self.txId.delete(0, tk.END)
        self.cbIdMaestro.set('')
        self.txNombre.delete(0, tk.END)
        self.txApaterno.delete(0, tk.END)
        self.txAmaterno.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)
        self.cbProfile.set('')
        self.cbCarrera.set('')
        self.cbMateria.set('')
        self.cbGradoEstudios.set('')
        self.txId.config(state='disabled')
        self.cbIdMaestro.config(state='disabled')
        self.txNombre.config(state='disabled')
        self.txApaterno.config(state='disabled')
        self.txAmaterno.config(state='disabled')
        self.txEmail.config(state='disabled')
        self.cbProfile.config(state='disabled')
        self.cbCarrera.config(state='disabled')
        self.cbMateria.config(state='disabled')
        self.cbGradoEstudios.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

    # FALTA CALIFICACIONES

# ------------------------------- Fin Pre-registro de Maestros -----------------------------------

# ------------------------------- Pre-registro de Materias -----------------------------------

class Materias:
    def __init__(self, root):
        self.root = root
        self.root.config(width=500, height=400)
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Materias")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Create users table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS materias (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Asignatura VARCHAR(255),
                Creditos INT,
                Semestre INT,
                Carrera VARCHAR(255),
                PERFIL TEXT,
                Horario VARCHAR(255),
                Dia VARCHAR(255)
            );
        """)
        self.connection.commit()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        global usernameuser
        self.imagen_boton_nuevo = tk.PhotoImage(file="Nuevo.png")
        self.imagen_boton_guardar = tk.PhotoImage(file="Guardar.png")
        self.imagen_boton_editar = tk.PhotoImage(file="Editar.png")
        self.imagen_boton_cancelar = tk.PhotoImage(file="Cancelar.png")
        self.imagen_boton_eliminar = tk.PhotoImage(file="Eliminar.png")
        self.imagen_boton_buscar = tk.PhotoImage(file="Buscar.png")
        self.imagen_boton_menu = tk.PhotoImage(file="Menu.png")
        tk.Label(self.root, text="Usuario: " + usernameuser, bg='black', fg='white').place(x=10, y=240)

        tk.Label(self.root, text="Buscar ID:", bg='black', fg='white').place(x=250, y=10)
        self.txBuscar = tk.Entry(self.root)
        self.txBuscar.place(x=360, y=10)

        self.btnBuscar = tk.Button(self.root, text="Buscar", command=self.buscar_usuario, image=self.imagen_boton_buscar)
        self.btnBuscar.place(x=315, y=10)

        tk.Label(self.root, text="ID:", bg='black', fg='white').place(x=10, y=10)
        self.txId = tk.Entry(self.root, state='disabled')
        self.txId.place(x=10, y=30)

        tk.Label(self.root, text="Asignatura", bg='black', fg='white').place(x=10, y=50)
        self.txAsignatura = tk.Entry(self.root, width=30, state='disabled')
        self.txAsignatura.place(x=10, y=70)

        tk.Label(self.root, text="Creditos", bg='black', fg='white').place(x=10, y=90)
        self.intCreditos = tk.Entry(self.root, width=30, state='disabled')
        self.intCreditos.place(x=10, y=110)

        tk.Label(self.root, text="Semestre", bg='black', fg='white').place(x=10, y=130)
        self.intSemestre = tk.Entry(self.root, width=30, state='disabled')
        self.intSemestre.place(x=10, y=150)

        tk.Label(self.root, text="Carrera", bg='black', fg='white').place(x=250, y=50)
        self.cursor.execute("SELECT NombreCarrera FROM carrera where perfil = 'Activo'")
        Carrera=self.cursor.fetchall()
        if len(Carrera)>=1:
            self.cbCarrera = ttk.Combobox(self.root, state='disabled', values=Carrera)
        else:
            self.cbCarrera = ttk.Combobox(self.root, state='disabled', values=[])
        self.cbCarrera.place(x=250, y=70)
        

        tk.Label(self.root, text="Perfil:", bg='black', fg='white').place(x=10, y=170)
        self.cbProfile = ttk.Combobox(self.root, state='disabled', values=["Activo", "Inactivo"])
        self.cbProfile.place(x=10, y=190)

        # Cambiar los valores de la tabla de horarios :)
        tk.Label(self.root, text="Horario", bg='black', fg='white').place(x=250, y=90)
        self.cursor.execute("SELECT Hora, Horafin, Turno FROM horario where perfil = 'Activo'")
        Horario=self.cursor.fetchall()
        if len(Horario)>=1:
            self.timeHorario = ttk.Combobox(self.root, state='disabled', values=Horario)
        else:
            self.timeHorario = ttk.Combobox(self.root, state='disabled', values=[])
        self.timeHorario.place(x=250, y=110)

        tk.Label(self.root, text="Dia", bg='black', fg='white').place(x=250, y=130)
        self.cbDia = ttk.Combobox(self.root, state='disabled', values=["L,M,I,J,V", "L,M,I,V", "M,I,J,V", "L,M,I", "M,I,J", "I,J,V", "L,M", "M,I", "I,J", "J,V", "L", "M", "I", "J", "V"])
        self.cbDia.place(x=250, y=150)

        self.btnNuevo = tk.Button(self.root, text="Nuevo", command=self.nuevo_usuario, image=self.imagen_boton_nuevo)
        self.btnNuevo.place(x=200, y=250)

        self.btnGuardar = tk.Button(self.root, text="Guardar", state='disabled', command=self.guardar_usuario, image=self.imagen_boton_guardar)
        self.btnGuardar.place(x=226+20, y=250)

        self.btnCancelar = tk.Button(self.root, text="Cancelar", state='disabled', command=self.cancelar, image=self.imagen_boton_cancelar)
        self.btnCancelar.place(x=252+40, y=250)

        self.btnEditar = tk.Button(self.root, text="Editar", state='disabled', command=self.editar_usuario, image=self.imagen_boton_editar)
        self.btnEditar.place(x=278+60, y=250)

        self.btnEliminar = tk.Button(self.root, text="Eliminar", state='disabled', command=self.eliminar_usuario, image=self.imagen_boton_eliminar)
        self.btnEliminar.place(x=304+80, y=250)

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, image=self.imagen_boton_menu)
        self.btnMenu.place(x=330+100, y=250)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def validar_nombre(self, nombre):
        # Utilizar regex para validar que solo contiene letras y espacios
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            messagebox.showerror("Error", "Nombre solo debe contener letras y espacios")
            return False
        return True

    def CambiarMaterias(self, event):
        Carrera=self.cbCarrera.get()
        
        self.cursor.execute("SELECT Asignatura FROM materias where perfil = 'Activo' and Carrera='"+Carrera+"'")
        Materia=self.cursor.fetchall()
        if len(Materia)>=1:
            self.cbCarrera.config(values=Materia)
        else:
            self.cbCarrera.config(values=[])
    

    def validar_usuario(self, usuario):
        # Utilizar regex para validar que solo contiene letras, números y espacios
        if not re.match(r'^[a-zA-Z0-9 ]+$', usuario):
            messagebox.showerror("Error", "Usuario solo debe contener letras, números y espacios")
            return False
        return True

    def validar_perfil(self, perfil):
        # Validar que el perfil sea activo o inactivo
        opciones_perfil = ["Activo", "Inactivo"]
        if perfil not in opciones_perfil:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
            return False
        return True

    def id_existe(self, user_id):
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID debe ser un número entero")
            return False

        # Consultar si el ID ya existe en la base de datos
        self.cursor.execute("SELECT * FROM materias WHERE ID = %s", (user_id,))
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False
        
    def validar_enteros(self, x):
        # Utilizar regex para validar que solo contiene números enteros
        if not re.match(r'^\d+$', x):
            messagebox.showerror("Error", "El Creditos y semestre solo deben contener números enteros")
            return False
        return True
            
    def buscar_usuario(self):
        id_buscar = self.txBuscar.get()

        # Consultar el usuario por ID en la base de datos
        self.cursor.execute("SELECT * FROM materias WHERE ID = %s", (id_buscar,))
        usuario = self.cursor.fetchone()

        if usuario:
            # Mostrar los datos en la interfaz gráfica
            self.txId.config(state='normal')
            self.txAsignatura.config(state='normal')
            self.intCreditos.config(state='normal')
            self.intSemestre.config(state='normal')
            self.cbCarrera.config(state='readonly')
            self.cbProfile.config(state='readonly')
            self.timeHorario.config(state='readonly')
            self.cbDia.config(state='readonly')

            self.txId.delete(0, tk.END)
            self.txAsignatura.delete(0, tk.END)
            self.intCreditos.delete(0, tk.END)
            self.intSemestre.delete(0, tk.END)
            self.cbCarrera.set('')
            self.cbProfile.set('')
            self.timeHorario.set('')
            self.cbDia.set('')

            self.txId.insert(tk.END, usuario[0])
            self.txAsignatura.insert(tk.END, usuario[1])
            self.intCreditos.insert(tk.END, usuario[2])
            self.intSemestre.insert(tk.END, usuario[3])
            self.cbCarrera.set(usuario[4])
            self.cbProfile.set(usuario[5])
            self.timeHorario.set(usuario[6])
            self.cbDia.set(usuario[7])

            self.btnEditar.config(state='normal')
            self.btnEliminar.config(state='normal')
            self.txId.config(state='disabled')
            self.txBuscar.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def nuevo_usuario(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.txAsignatura.config(state='normal')
        self.intCreditos.config(state='normal')
        self.intSemestre.config(state='normal')
        self.cbCarrera.config(state='readonly')
        self.cbProfile.config(state='readonly')
        self.timeHorario.config(state='readonly')
        self.cbDia.config(state='readonly')
        self.cursor.execute("SELECT MAX(ID) FROM materias")
        max_id = self.cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1
        self.txId.delete(0, tk.END)
        self.txId.insert(tk.END, new_id)
        self.txId.config(state='disabled')
        self.btnNuevo.config(state='disabled')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def guardar_usuario(self):
        user_id = self.txId.get()
        asignatura = self.txAsignatura.get()
        creditos = self.intCreditos.get()
        semestre = self.intSemestre.get()
        carrera = self.cbCarrera.get()
        profile = self.cbProfile.get()
        horario = self.timeHorario.get()
        dia = self.cbDia.get()

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not asignatura or not creditos or not semestre or not carrera or not profile or not horario or not dia:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")

        elif not self.validar_enteros(creditos) or not self.validar_enteros(semestre):
            pass
        elif not self.validar_usuario(asignatura) or not self.validar_nombre(carrera):
            pass  # Handle validation errors as needed
        else:
            # Verificar que la carrera sea diferente BORRAR EN CASO DE NO FUNCIONAR
            self.cursor.execute("SELECT * FROM materias WHERE Carrera=%s and Horario=%s", (carrera, horario))
            existing_materia_same_career = self.cursor.fetchall()
            if existing_materia_same_career:
                messagebox.showerror("Error", "Ya existe una materia con el mismo horario y carrera")
            else:
                # Insertar el nuevo usuario en la base de datos
                self.cursor.execute("INSERT INTO materias (Asignatura, Creditos, Semestre, Carrera, PERFIL, Horario, Dia) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                    (asignatura, creditos, semestre, carrera, profile, horario, dia))
                self.connection.commit()
                messagebox.showinfo("Éxito", "Usuario guardado correctamente")

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.btnGuardar.config(state='disabled')
            self.btnCancelar.config(state='disabled')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def cancelar(self):
        self.limpiar()
        self.btnNuevo.config(state='normal')

    def editar_usuario(self):
        user_id = self.txId.get()
        asignatura = self.txAsignatura.get()
        creditos = self.intCreditos.get()
        semestre = self.intSemestre.get()
        carrera = self.cbCarrera.get()
        profile = self.cbProfile.get()
        horario = self.timeHorario.get()
        dia = self.cbDia.get()

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not asignatura or not creditos or not semestre or not carrera or not profile or not horario or not dia:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")

        elif not self.validar_enteros(creditos) or not self.validar_enteros(semestre):
            pass
        elif not self.validar_usuario(asignatura) or not self.validar_nombre(carrera):
            pass  # Handle validation errors as needed
        else:
            # Verificar que la carrera sea diferente BORRAR EN CASO DE NO FUNCIONAR
            self.cursor.execute("SELECT * FROM materias WHERE Carrera=%s and Horario=%s", (carrera, horario))
            existing_materia_same_career = self.cursor.fetchall()
            if existing_materia_same_career:
                messagebox.showerror("Error", "Ya existe una materia con el mismo horario y carrera")
            else:
                # Actualizar el usuario en la base de datos
                self.cursor.execute("UPDATE materias SET Asignatura=%s, Creditos=%s, Semestre=%s, Carrera=%s, PERFIL=%s, Horario=%s, Dia=%s WHERE ID=%s",
                                    (asignatura, creditos, semestre, carrera, profile, horario, dia, user_id))
                self.connection.commit()

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def eliminar_usuario(self):
        id_eliminar = self.txId.get()
        self.limpiar()

        # Actualizar el perfil a "Inactivo" en lugar de eliminar físicamente
        self.cursor.execute("UPDATE materias SET Perfil=%s WHERE ID=%s", ("Inactivo", id_eliminar))
        self.connection.commit()

        self.btnNuevo.config(state='normal')

    def limpiar(self):
        self.txId.config(state='normal')
        self.txId.delete(0, tk.END)
        self.txAsignatura.delete(0, tk.END)
        self.intCreditos.delete(0, tk.END)
        self.intSemestre.delete(0, tk.END)
        self.cbCarrera.set('')
        self.cbProfile.set('')
        self.timeHorario.set('')
        self.cbDia.set('')
        self.txId.config(state='disabled')
        self.txAsignatura.config(state='disabled')
        self.intCreditos.config(state='disabled')
        self.intSemestre.config(state='disabled')
        self.cbCarrera.config(state='disabled')
        self.cbProfile.config(state='disabled')
        self.timeHorario.config(state='disabled')
        self.cbDia.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

# ------------------------------- Fin Pre-registro de Materias -----------------------------------

# ------------------------------- Pre-registro de Grupos -----------------------------------

class Grupos:
    def __init__(self, root):
        self.root = root
        self.root.config(width=500, height=400)
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Grupos")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # ALTER TABLE grupo DROP COLUMN Horario, DROP COLUMN Dia;
        # Create users table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS grupo (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                NombrGrupo VARCHAR(255),
                Fecha DATE,
                Carrera varchar(255), 
                Materia VARCHAR(1024),
                Maestro VARCHAR(255),
                Salon VARCHAR(50),
                Semestre INT,
                MaxNumAlumnos INT,
                Perfil TEXT,
                IDMaestro INT
            );
        """)
        self.connection.commit()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        global usernameuser
        self.imagen_boton_nuevo = tk.PhotoImage(file="Nuevo.png")
        self.imagen_boton_guardar = tk.PhotoImage(file="Guardar.png")
        self.imagen_boton_editar = tk.PhotoImage(file="Editar.png")
        self.imagen_boton_cancelar = tk.PhotoImage(file="Cancelar.png")
        self.imagen_boton_eliminar = tk.PhotoImage(file="Eliminar.png")
        self.imagen_boton_buscar = tk.PhotoImage(file="Buscar.png")
        self.imagen_boton_menu = tk.PhotoImage(file="Menu.png")
        tk.Label(self.root, text="Usuario: " + usernameuser, bg='black', fg='white').place(x=10, y=260)

        tk.Label(self.root, text="Buscar ID:", bg='black', fg='white').place(x=250, y=10)
        self.txBuscar = tk.Entry(self.root)
        self.txBuscar.place(x=360, y=10)

        self.btnBuscar = tk.Button(self.root, text="Buscar", command=self.buscar_usuario, image=self.imagen_boton_buscar)
        self.btnBuscar.place(x=315, y=10)

        tk.Label(self.root, text="ID:", bg='black', fg='white').place(x=10, y=10)
        self.txId = tk.Entry(self.root, state='disabled')
        self.txId.place(x=10, y=30)

        tk.Label(self.root, text="Nombre del Grupo", bg='black', fg='white').place(x=10, y=50)
        self.txNombre = tk.Entry(self.root, width=30, state='disabled')
        self.txNombre.place(x=10, y=70)

        tk.Label(self.root, text="Fecha", bg='black', fg='white').place(x=10, y=90)
        self.txFecha = DateEntry(self.root, width=12, background='black', foreground='white', borderwidth=2, state="disabled", date_pattern="dd/mm/yyyy")
        self.txFecha.place(x=10, y=110)

        # Cambiar los valores de la tabla de carrera :)
        tk.Label(self.root, text="Carrera", bg='black', fg='white').place(x=10, y=130)
        self.cursor.execute("SELECT NombreCarrera FROM carrera where perfil = 'Activo'")
        Carrera=self.cursor.fetchall()
        if len(Carrera)>=1:
            self.cbCarrera = ttk.Combobox(self.root, state='disabled', values=Carrera)
        else:
            self.cbCarrera = ttk.Combobox(self.root, state='disabled', values=[])
        self.cbCarrera.place(x=10, y=150)
        
        self.cbCarrera.bind("<<ComboboxSelected>>", self.CambiarMaterias)

        # Cambiar los valores de la tabla de materias :)
        tk.Label(self.root, text="Materia", bg='black', fg='white').place(x=10, y=170)
        
        self.cbMateria = ttk.Combobox(self.root, state='disabled', values=[])
        self.cbMateria.place(x=10, y=190)
        
        self.cbMateria.bind("<<ComboboxSelected>>", self.CambiarMaestros)

        # Cambiar los valores de la tabla de maestros :)
        tk.Label(self.root, text="Maestros", bg='black', fg='white').place(x=10, y=210)
        
        self.cbMaestro = ttk.Combobox(self.root, state='disabled', values=[])
        self.cbMaestro.place(x=10, y=230)
        
        # Cambiar los valores de la tabla de salones :)
        tk.Label(self.root, text="Salones", bg='black', fg='white').place(x=250, y=50)
        self.cursor.execute("SELECT Nombre, Edificio FROM salon where perfil = 'Activo'")
        Salon=self.cursor.fetchall()
        if len(Salon)>=1:
            self.txSalon = ttk.Combobox(self.root, state='disabled', values=Salon)
        else:
            self.txSalon = ttk.Combobox(self.root, state='disabled', values=[])
        self.txSalon.place(x=250, y=70)

        tk.Label(self.root, text="Semestre", bg='black', fg='white').place(x=250, y=90)
        self.cursor.execute("SELECT NumSemestre FROM carrera where perfil = 'Activo'")
        Semestre=self.cursor.fetchall()
        if len(Semestre)>=1:
            self.txSemestre = ttk.Combobox(self.root, state='disabled', values=Semestre)
        else:
            self.txSemestre = ttk.Combobox(self.root, state='disabled', values=[])
        self.txSemestre.place(x=250, y=110)

        tk.Label(self.root, text="Max Num Alumnos", bg='black', fg='white').place(x=250, y=130)
        self.txMaxNumAlumnos = tk.Entry(self.root, width=30, state='disabled')
        self.txMaxNumAlumnos.place(x=250, y=150)

        tk.Label(self.root, text="Perfil:", bg='black', fg='white').place(x=250, y=170)
        self.cbProfile = ttk.Combobox(self.root, state='disabled', values=["Activo", "Inactivo"])
        self.cbProfile.place(x=250, y=190)

        self.btnNuevo = tk.Button(self.root, text="Nuevo", command=self.nuevo_usuario, image=self.imagen_boton_nuevo)
        self.btnNuevo.place(x=200, y=250+50)

        self.btnGuardar = tk.Button(self.root, text="Guardar", state='disabled', command=self.guardar_usuario, image=self.imagen_boton_guardar)
        self.btnGuardar.place(x=226+20, y=250+50)

        self.btnCancelar = tk.Button(self.root, text="Cancelar", state='disabled', command=self.cancelar, image=self.imagen_boton_cancelar)
        self.btnCancelar.place(x=252+40, y=250+50)

        self.btnEditar = tk.Button(self.root, text="Editar", state='disabled', command=self.editar_usuario, image=self.imagen_boton_editar)
        self.btnEditar.place(x=278+60, y=250+50)

        self.btnEliminar = tk.Button(self.root, text="Eliminar", state='disabled', command=self.eliminar_usuario, image=self.imagen_boton_eliminar)
        self.btnEliminar.place(x=304+80, y=250+50)

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, image=self.imagen_boton_menu)
        self.btnMenu.place(x=330+100, y=250+50)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def validar_nombre(self, nombre):
        # Utilizar regex para validar que solo contiene letras, números y espacios
        if not re.match(r'^[a-zA-Z0-9 ]+$', nombre):
            messagebox.showerror("Error", "Usuario solo debe contener letras, números y espacios")
            return False
        return True
    
    def validar_nombre_grupo(self, nombre):
        # Utilizar regex para validar que solo contiene letras, números y espacios
        if not re.match(r'^[a-zA-Z0-9 ]+$', nombre):
            messagebox.showerror("Error", "El nolmbre del grupo solo debe contener letras, números y espacios")
            return False
        return True

    def validar_max_num_alumnos(self, numero):
        if int(numero) > 13:
            messagebox.showerror("Error", "El número de alumnos debe ser, como límite, de 13.")
            return False
        return True

    def CambiarMaterias(self, event):
        Carrera=self.cbCarrera.get()
        
        self.cursor.execute("SELECT Asignatura FROM materias where perfil = 'Activo' and Carrera='"+Carrera+"'")
        Materia=self.cursor.fetchall()
        if len(Materia)>=1:
            self.cbMateria.config(values=Materia)
        else:
            self.cbMateria.config(values=[])

        self.cbMaestro.config(values=[])
    

    def CambiarMaestros(self, event):
        Materia=self.cbMateria.get()
        
        self.cursor.execute("SELECT Nombre, IDUsuario FROM premaestros where perfil = 'Activo' and materia='"+Materia+"'")
        self.Maestro=self.cursor.fetchall()
        Maestro=[]
        for dates in self.Maestro:
            Maestro.append(dates[0])
        if len(Maestro)>=1:
            self.cbMaestro.config(values=Maestro)
        else:
            self.cbMaestro.config(values=[])
            
            
    def validar_perfil(self, perfil):
        # Validar que el perfil sea activo o inactivo
        opciones_perfil = ["Activo", "Inactivo"]
        if perfil not in opciones_perfil:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
            return False
        return True

    def validar_fecha_nacimiento(self, fecha_nacimiento):
        # Convertir la fecha de nacimiento en un objeto datetime
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        
        # Obtener la fecha actual
        fecha_actual = datetime.now()
        
        # Verificar si la fecha de nacimiento es posterior a la fecha actual
        if fecha_nacimiento > fecha_actual:
            messagebox.showerror("Error", "La fecha de creacion no puede ser posterior a la fecha actual.")
            return False
        
        return True


    def id_existe(self, user_id):
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID debe ser un número entero")
            return False

        # Consultar si el ID ya existe en la base de datos
        self.cursor.execute("SELECT * FROM grupo WHERE ID = %s", (user_id,))
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False
        
    def buscar_usuario(self):
        id_buscar = self.txBuscar.get()

        # Consultar el usuario por ID en la base de datos
        self.cursor.execute("SELECT * FROM grupo WHERE ID = %s", (id_buscar,))
        usuario = self.cursor.fetchone()

        if usuario:
            # Mostrar los datos en la interfaz gráfica
            self.txId.config(state='normal')
            self.txNombre.config(state='normal')
            self.txFecha.config(state='normal')
            self.cbCarrera.config(state='readonly')
            self.cbMateria.config(state='readonly')
            self.cbMaestro.config(state='readonly')
            self.txSalon.config(state='normal')
            self.txSemestre.config(state='normal')
            self.txMaxNumAlumnos.config(state='normal')
            self.cbProfile.config(state='readonly')

            self.txId.delete(0, tk.END)
            self.txNombre.delete(0, tk.END)
            self.txFecha.delete(0, tk.END)
            self.cbCarrera.set('')
            self.cbMateria.set('')
            self.cbMaestro.set('')
            self.txSalon.delete(0, tk.END)
            self.txSemestre.delete(0, tk.END)
            self.txMaxNumAlumnos.delete(0, tk.END)
            self.cbProfile.set('')

            self.txId.insert(tk.END, usuario[0])
            self.txNombre.insert(tk.END, usuario[1])
            self.txFecha.set_date(usuario[2])
            self.cbCarrera.set(usuario[3])
            self.cbMateria.set(usuario[4])
            self.cbMaestro.set(usuario[5])
            self.txSalon.insert(tk.END, usuario[6])
            self.txSemestre.insert(tk.END, usuario[7])
            self.txMaxNumAlumnos.insert(tk.END, usuario[8])
            self.cbProfile.set(usuario[9])

            self.btnEditar.config(state='normal')
            self.btnEliminar.config(state='normal')
            self.txId.config(state='disabled')
            self.txBuscar.delete(0, tk.END)
            self.CambiarMaterias("a")    
            self.CambiarMaestros("a")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def nuevo_usuario(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.txNombre.config(state='normal')
        self.txFecha.config(state='normal')
        self.cbCarrera.config(state='readonly')
        self.cbMateria.config(state='readonly')
        self.cbMaestro.config(state='readonly')
        self.txSalon.config(state='normal')
        self.txSemestre.config(state='normal')
        self.txMaxNumAlumnos.config(state='normal')
        self.cbProfile.config(state='readonly')
        self.cursor.execute("SELECT MAX(ID) FROM grupo")
        max_id = self.cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1
        self.txId.delete(0, tk.END)
        self.txId.insert(tk.END, new_id)
        self.txId.config(state='disabled')
        self.btnNuevo.config(state='disabled')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def guardar_usuario(self):
        user_id = self.txId.get()
        nombre = self.txNombre.get()
        fecha = self.txFecha.get()
        carrera = self.cbCarrera.get()
        materia = self.cbMateria.get()
        maestro = self.cbMaestro.get()
        salon = self.txSalon.get()
        semestre = self.txSemestre.get()
        max_num_alumnos = self.txMaxNumAlumnos.get()
        profile = self.cbProfile.get()
        id_maestro = self.cbMaestro.current()
        id_maestro = self.Maestro[id_maestro][1]

        opciones_profile = ["Activo", "Inactivo"]

        fecha_formato_sql = datetime.strptime(fecha, "%d/%m/%Y").strftime("%Y-%m-%d")
        # Verificar que sean diferentes salones BORRAR EN CASO DE NO FUNCIONAR
        self.cursor.execute("SELECT * FROM grupo WHERE Salon=%s", (salon,))
        existing_group_same_room = self.cursor.fetchall()

        if not user_id or not nombre or not fecha or not carrera or not materia or not maestro or not salon or not semestre or not max_num_alumnos or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
            pass
        elif not self.validar_nombre(nombre):
            pass  # Handle validation errors as needed
        elif not self.validar_nombre_grupo(nombre):
            pass
        elif not self.validar_max_num_alumnos(max_num_alumnos):
            pass
        elif not self.validar_fecha_nacimiento(fecha):
            return  # Detener el proceso si la validación de la fecha de nacimiento falla
        else:
            # Consultar si ya existe un registro con los mismos datos (excepto ID)
            self.cursor.execute("SELECT * FROM grupo WHERE Fecha=%s AND Carrera=%s AND Salon=%s AND Semestre=%s AND MaxNumAlumnos=%s AND Perfil=%s",
                                (fecha_formato_sql, carrera, salon, semestre, max_num_alumnos, profile))
            existing_group = self.cursor.fetchone()

            if existing_group:
                # Si existe un grupo con los mismos datos (excepto ID), actualizamos materia y maestro
                existing_materias = existing_group[4].split(', ')
                existing_maestros = existing_group[5].split(', ')

                if materia not in existing_materias:
                    existing_materias.append(materia)
                if maestro not in existing_maestros:
                    existing_maestros.append(maestro)

                new_materias = ', '.join(existing_materias)
                new_maestros = ', '.join(existing_maestros)

                self.cursor.execute("UPDATE grupo SET Materia=%s, Maestro=%s WHERE ID=%s",
                                    (new_materias, new_maestros, existing_group[0]))
                self.connection.commit()
                messagebox.showinfo("Éxito", "Grupo actualizado correctamente")
            elif existing_group_same_room:
                messagebox.showerror("Error", "Ya existe un grupo con el mismo salón")
            else:
                # Insertamos un nuevo grupo
                self.cursor.execute("INSERT INTO grupo (NombrGrupo, Fecha, Carrera, Materia, Maestro, Salon, Semestre, MaxNumAlumnos, Perfil, IDMaestro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                    (nombre, fecha_formato_sql, carrera, materia, maestro, salon, semestre, max_num_alumnos, profile, id_maestro))
                self.connection.commit()
                messagebox.showinfo("Éxito", "Grupo guardado correctamente")
            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.btnGuardar.config(state='disabled')
            self.btnCancelar.config(state='disabled')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def cancelar(self):
        self.limpiar()
        self.btnNuevo.config(state='normal')

    def editar_usuario(self):
        user_id = self.txId.get()
        nombre = self.txNombre.get()
        fecha = self.txFecha.get()
        carrera = self.cbCarrera.get()
        materia = self.cbMateria.get()
        maestro = self.cbMaestro.get()
        salon = self.txSalon.get()
        semestre = self.txSemestre.get()
        max_num_alumnos = self.txMaxNumAlumnos.get()
        profile = self.cbProfile.get()
        id_maestro = self.cbMaestro.current()
        id_maestro = self.Maestro[id_maestro][1]

        opciones_profile = ["Activo", "Inactivo"]
        fecha_formato_sql = datetime.strptime(fecha, "%d/%m/%Y").strftime("%Y-%m-%d")

        # Verificar que sean diferentes salones BORRAR EN CASO DE NO FUNCIONAR
        self.cursor.execute("SELECT * FROM grupo WHERE Salon=%s", (salon,))
        existing_group_same_room = self.cursor.fetchall()

        if not user_id or not nombre or not fecha or not carrera or not materia or not maestro or not salon or not semestre or not max_num_alumnos or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
        elif not self.validar_nombre(nombre) or not self.validar_nombre_grupo(nombre) or not self.validar_max_num_alumnos(max_num_alumnos) or not self.validar_fecha_nacimiento(fecha):
            return  # Terminar la edición si alguna validación falla
        else:
            # Consultar si el grupo ya existe para solo actualizar materias y maestros
            self.cursor.execute("SELECT Materia, Maestro FROM grupo WHERE ID=%s", (user_id,))
            grupo_existente = self.cursor.fetchone()

            if grupo_existente:
                materias_existentes, maestros_existentes = grupo_existente
                materias_lista = materias_existentes.split(', ')
                maestros_lista = maestros_existentes.split(', ')

                if materia not in materias_lista:
                    materias_lista.append(materia)
                if maestro not in maestros_lista:
                    maestros_lista.append(maestro)

                materias_actualizadas = ', '.join(materias_lista)
                maestros_actualizados = ', '.join(maestros_lista)

                # Actualizar el grupo con las nuevas listas de materias y maestros
                self.cursor.execute("UPDATE grupo SET NombrGrupo=%s, Fecha=%s, Carrera=%s, Materia=%s, Maestro=%s, Salon=%s, Semestre=%s, MaxNumAlumnos=%s, Perfil=%s, IDMaestro=%s WHERE ID=%s",
                                    (nombre, fecha_formato_sql, carrera, materias_actualizadas, maestros_actualizados, salon, semestre, max_num_alumnos, profile, id_maestro, user_id))
                self.connection.commit()
                messagebox.showinfo("Éxito", "Grupo actualizado correctamente con nuevas materias y maestros")
            elif existing_group_same_room:
                messagebox.showerror("Error", "Ya existe un grupo con el mismo salón")
            else:
                messagebox.showerror("Error", "No se encontró el grupo para actualizar")

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def eliminar_usuario(self):
        id_eliminar = self.txId.get()
        self.limpiar()

        # Actualizar el perfil a "Inactivo" en lugar de eliminar físicamente
        self.cursor.execute("UPDATE grupo SET Perfil=%s WHERE ID=%s", ("Inactivo", id_eliminar))
        self.connection.commit()

        self.btnNuevo.config(state='normal')

    def limpiar(self):
        self.txId.config(state='normal')
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txFecha.delete(0, tk.END)
        self.cbCarrera.set('')
        self.cbMateria.set('')
        self.cbMaestro.set('')
        self.txSalon.delete(0, tk.END)
        self.txSemestre.delete(0, tk.END)
        self.txMaxNumAlumnos.delete(0, tk.END)
        self.cbProfile.set('')
        self.Maestro=[]
        self.txId.config(state='disabled')
        self.txNombre.config(state='disabled')
        self.txFecha.config(state='disabled')
        self.cbCarrera.config(state='disabled')
        self.cbMateria.config(state='disabled')
        self.cbMaestro.config(state='disabled')
        self.txSalon.config(state='disabled')
        self.cbProfile.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

# ------------------------------- Fin Pre-registro de Grupos -----------------------------------

# ------------------------------- Horario -----------------------------------
class Horario:
    def __init__(self, root):
        self.root = root
        self.root.config(width=500, height=400)
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Horario")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # ALTER TABLE horario ADD COLUMN Horario TIME, ADD COLUMN Dia VARCHAR(255);
        # Create users table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS horario (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Turno VARCHAR(255),
                Hora TIME,
                HoraFin TIME,
                PERFIL TEXT
            );
        """)
        self.connection.commit()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        global usernameuser
        self.imagen_boton_nuevo = tk.PhotoImage(file="Nuevo.png")
        self.imagen_boton_guardar = tk.PhotoImage(file="Guardar.png")
        self.imagen_boton_editar = tk.PhotoImage(file="Editar.png")
        self.imagen_boton_cancelar = tk.PhotoImage(file="Cancelar.png")
        self.imagen_boton_eliminar = tk.PhotoImage(file="Eliminar.png")
        self.imagen_boton_buscar = tk.PhotoImage(file="Buscar.png")
        self.imagen_boton_menu = tk.PhotoImage(file="Menu.png")
        tk.Label(self.root, text="Usuario: " + usernameuser, bg='black', fg='white').place(x=10, y=240)

        tk.Label(self.root, text="Buscar ID:", bg='black', fg='white').place(x=250, y=10)
        self.txBuscar = tk.Entry(self.root)
        self.txBuscar.place(x=360, y=10)

        self.btnBuscar = tk.Button(self.root, text="Buscar", command=self.buscar_usuario, image=self.imagen_boton_buscar)
        self.btnBuscar.place(x=315, y=10)

        tk.Label(self.root, text="ID:", bg='black', fg='white').place(x=10, y=10)
        self.txId = tk.Entry(self.root, state='disabled')
        self.txId.place(x=10, y=30)

        tk.Label(self.root, text="Turno", bg='black', fg='white').place(x=10, y=50)
        self.cbTurno = ttk.Combobox(self.root, state='disabled', values=["Matutino", "Vespertino"])
        self.cbTurno.place(x=10, y=70)

        tk.Label(self.root, text="Hora", bg='black', fg='white').place(x=10, y=90)
        self.timeHora = tk.Entry(self.root, width=30, state='disabled')
        self.timeHora.place(x=10, y=110)

        tk.Label(self.root, text="Hora Fin", bg='black', fg='white').place(x=10, y=130)
        self.timeHoraFin = tk.Entry(self.root, width=30, state='disabled')
        self.timeHoraFin.place(x=10, y=150)

        tk.Label(self.root, text="Perfil:", bg='black', fg='white').place(x=250, y=130)
        self.cbProfile = ttk.Combobox(self.root, state='disabled', values=["Activo", "Inactivo"])
        self.cbProfile.place(x=250, y=150)
        
        self.btnNuevo = tk.Button(self.root, text="Nuevo", command=self.nuevo_usuario, image=self.imagen_boton_nuevo)
        self.btnNuevo.place(x=200, y=250)

        self.btnGuardar = tk.Button(self.root, text="Guardar", state='disabled', command=self.guardar_usuario, image=self.imagen_boton_guardar)
        self.btnGuardar.place(x=226+20, y=250)

        self.btnCancelar = tk.Button(self.root, text="Cancelar", state='disabled', command=self.cancelar, image=self.imagen_boton_cancelar)
        self.btnCancelar.place(x=252+40, y=250)

        self.btnEditar = tk.Button(self.root, text="Editar", state='disabled', command=self.editar_usuario, image=self.imagen_boton_editar)
        self.btnEditar.place(x=278+60, y=250)

        self.btnEliminar = tk.Button(self.root, text="Eliminar", state='disabled', command=self.eliminar_usuario, image=self.imagen_boton_eliminar)
        self.btnEliminar.place(x=304+80, y=250)

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, image=self.imagen_boton_menu)
        self.btnMenu.place(x=330+100, y=250)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def validar_nombre(self, nombre):
        # Utilizar regex para validar que solo contiene letras y espacios
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            messagebox.showerror("Error", "Nombre solo debe contener letras y espacios")
            return False
        return True

    def validar_perfil(self, perfil):
        # Validar que el perfil sea activo o inactivo
        opciones_perfil = ["Activo", "Inactivo"]
        if perfil not in opciones_perfil:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
            return False
        return True

    def id_existe(self, user_id):
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID debe ser un número entero")
            return False

        # Consultar si el ID ya existe en la base de datos
        self.cursor.execute("SELECT * FROM horario WHERE ID = %s", (user_id,))
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False
        
    def buscar_usuario(self):
        id_buscar = self.txBuscar.get()

        # Consultar el usuario por ID en la base de datos
        self.cursor.execute("SELECT * FROM horario WHERE ID = %s", (id_buscar,))
        usuario = self.cursor.fetchone()

        if usuario:
            # Mostrar los datos en la interfaz gráfica
            self.txId.config(state='normal')
            self.cbTurno.config(state='readonly')
            self.timeHora.config(state='normal')
            self.timeHoraFin.config(state='normal')
            self.cbProfile.config(state='readonly')

            self.txId.delete(0, tk.END)
            self.cbTurno.set('')
            self.timeHora.delete(0, tk.END)
            self.cbProfile.set('')
            self.timeHoraFin.delete(0, tk.END)

            self.txId.insert(tk.END, usuario[0])
            self.cbTurno.set(usuario[1])
            self.timeHora.insert(tk.END, usuario[2])
            self.cbProfile.set(usuario[3])
            self.timeHoraFin.insert(tk.END, usuario[4])


            self.btnEditar.config(state='normal')
            self.btnEliminar.config(state='normal')
            self.txId.config(state='disabled')
            self.txBuscar.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def nuevo_usuario(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.cbTurno.config(state='readonly')
        self.timeHora.config(state='normal')
        self.timeHoraFin.config(state='normal')
        self.cbProfile.config(state='readonly')
        self.cursor.execute("SELECT MAX(ID) FROM horario")
        max_id = self.cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1
        self.txId.delete(0, tk.END)
        self.txId.insert(tk.END, new_id)
        self.txId.config(state='disabled')
        self.btnNuevo.config(state='disabled')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def guardar_usuario(self):
        user_id = self.txId.get()
        turno = self.cbTurno.get()
        hora = self.timeHora.get()
        horafin = self.timeHoraFin.get()
        profile = self.cbProfile.get()

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not turno or not hora or not profile or not horafin:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")

        elif not self.validar_nombre(turno):
            pass  # Handle validation errors as needed
        else:
            # Validar formato de hora y límite máximo
            if not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?$', hora) and not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?$', horafin):
                messagebox.showerror("Error", "Formato de hora incorrecto (HH:MM[:SS])")
            elif hora > "17:00:00" and horafin > "17:00:00":
                messagebox.showerror("Error", "La hora no puede ser mayor a 17:00:00 (5:00 PM)")
            elif horafin < hora:
                messagebox.showerror("Error", "La hora final no puede ser menor a la hora de inicio")
            elif hora < "07:00:00" and horafin < "07:00:00":
                messagebox.showerror("Error", "La hora no puede ser menor a 07:00:00 (7:00 AM)")
            else:
                # Insertar el nuevo usuario en la base de datos
                self.cursor.execute("INSERT INTO horario (Turno, Hora, PERFIL, Horafin) VALUES (%s, %s, %s, %s)",
                                    (turno, hora, profile, horafin))
                self.connection.commit()

                self.limpiar()
                self.btnNuevo.config(state='normal')
                self.btnGuardar.config(state='disabled')
                self.btnCancelar.config(state='disabled')
                self.txId.config(state='normal')
                self.txId.delete(0, tk.END)
                self.txId.config(state='disabled')
                messagebox.showinfo("Éxito", "Usuario guardado correctamente")

    def cancelar(self):
        self.limpiar()
        self.btnNuevo.config(state='normal')

    def editar_usuario(self):
        user_id = self.txId.get()
        turno = self.cbTurno.get()
        hora = self.timeHora.get()
        horafin = self.timeHoraFin.get()
        profile = self.cbProfile.get()

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not turno or not hora or not profile or not horafin:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")

        elif not self.validar_nombre(turno):
            pass  # Handle validation errors as needed
        else:
            # Validar formato de hora y límite máximo
            if not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?$', hora) and not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?$', horafin):
                messagebox.showerror("Error", "Formato de hora incorrecto (HH:MM[:SS])")
            elif hora > "15:00:00" and horafin > "15:00:00":
                messagebox.showerror("Error", "La hora no puede ser mayor a 15:00:00")
            elif horafin < hora:
                messagebox.showerror("Error", "La hora final no puede ser menor a la hora de inicio")
            else:
                # Actualizar el usuario en la base de datos
                self.cursor.execute("UPDATE horario SET Turno=%s, Hora=%s, PERFIL=%s, Horafin=%s WHERE ID=%s",
                                    (turno, hora, profile, horafin, user_id))
                self.connection.commit()

                self.limpiar()
                self.btnNuevo.config(state='normal')
                self.txId.config(state='normal')
                self.txId.delete(0, tk.END)
                self.txId.config(state='disabled')

    def eliminar_usuario(self):
        id_eliminar = self.txId.get()
        self.limpiar()

        # Actualizar el perfil a "Inactivo" en lugar de eliminar físicamente
        self.cursor.execute("UPDATE horario SET Perfil=%s WHERE ID=%s", ("Inactivo", id_eliminar))
        self.connection.commit()

        self.btnNuevo.config(state='normal')

    def limpiar(self):
        self.txId.config(state='normal')
        self.txId.delete(0, tk.END)
        self.cbTurno.set('')
        self.timeHora.delete(0, tk.END)
        self.timeHoraFin.delete(0, tk.END)
        self.cbProfile.set('')
        self.txId.config(state='disabled')
        self.cbTurno.config(state='disabled')
        self.timeHora.config(state='disabled')
        self.timeHoraFin.config(state='disabled')
        self.cbProfile.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

# ------------------------------- Fin Horario -----------------------------------

# ------------------------------- Salon -----------------------------------

class Salon:
    def __init__(self, root):
        self.root = root
        self.root.config(width=500, height=400)
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Salon")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Create users table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS salon (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR(255),
                Edificio VARCHAR(255),
                PERFIL TEXT
            );
        """)
        self.connection.commit()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        global usernameuser
        self.imagen_boton_nuevo = tk.PhotoImage(file="Nuevo.png")
        self.imagen_boton_guardar = tk.PhotoImage(file="Guardar.png")
        self.imagen_boton_editar = tk.PhotoImage(file="Editar.png")
        self.imagen_boton_cancelar = tk.PhotoImage(file="Cancelar.png")
        self.imagen_boton_eliminar = tk.PhotoImage(file="Eliminar.png")
        self.imagen_boton_buscar = tk.PhotoImage(file="Buscar.png")
        self.imagen_boton_menu = tk.PhotoImage(file="Menu.png")
        tk.Label(self.root, text="Usuario: " + usernameuser, bg='black', fg='white').place(x=10, y=240)

        tk.Label(self.root, text="Buscar ID:", bg='black', fg='white').place(x=250, y=10)
        self.txBuscar = tk.Entry(self.root)
        self.txBuscar.place(x=360, y=10)

        self.btnBuscar = tk.Button(self.root, text="Buscar", command=self.buscar_usuario, image=self.imagen_boton_buscar)
        self.btnBuscar.place(x=315, y=10)

        tk.Label(self.root, text="ID:", bg='black', fg='white').place(x=10, y=10)
        self.txId = tk.Entry(self.root, state='disabled')
        self.txId.place(x=10, y=30)

        tk.Label(self.root, text="Nombre", bg='black', fg='white').place(x=10, y=50)
        self.txNombre = tk.Entry(self.root, width=30, state='disabled')
        self.txNombre.place(x=10, y=70)

        tk.Label(self.root, text="Edificio", bg='black', fg='white').place(x=10, y=90)
        self.cbEdificio = ttk.Combobox(self.root, state='disabled', values=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
        self.cbEdificio.place(x=10, y=110)

        tk.Label(self.root, text="Perfil:", bg='black', fg='white').place(x=250, y=130)
        self.cbProfile = ttk.Combobox(self.root, state='disabled', values=["Activo", "Inactivo"])
        self.cbProfile.place(x=250, y=150)
        
        self.btnNuevo = tk.Button(self.root, text="Nuevo", command=self.nuevo_usuario, image=self.imagen_boton_nuevo)
        self.btnNuevo.place(x=200, y=250)

        self.btnGuardar = tk.Button(self.root, text="Guardar", state='disabled', command=self.guardar_usuario, image=self.imagen_boton_guardar)
        self.btnGuardar.place(x=226+20, y=250)

        self.btnCancelar = tk.Button(self.root, text="Cancelar", state='disabled', command=self.cancelar, image=self.imagen_boton_cancelar)
        self.btnCancelar.place(x=252+40, y=250)

        self.btnEditar = tk.Button(self.root, text="Editar", state='disabled', command=self.editar_usuario, image=self.imagen_boton_editar)
        self.btnEditar.place(x=278+60, y=250)

        self.btnEliminar = tk.Button(self.root, text="Eliminar", state='disabled', command=self.eliminar_usuario, image=self.imagen_boton_eliminar)
        self.btnEliminar.place(x=304+80, y=250)

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, image=self.imagen_boton_menu)
        self.btnMenu.place(x=330+100, y=250)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def validar_nombre(self, nombre):
        # Utilizar regex para validar que solo contiene letras, números y espacios
        if not re.match(r'^[a-zA-Z0-9 ]+$', nombre):
            messagebox.showerror("Error", "Usuario solo debe contener letras, números y espacios")
            return False
        return True

    def validar_perfil(self, perfil):
        # Validar que el perfil sea activo o inactivo
        opciones_perfil = ["Activo", "Inactivo"]
        if perfil not in opciones_perfil:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
            return False
        return True

    def id_existe(self, user_id):
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID debe ser un número entero")
            return False

        # Consultar si el ID ya existe en la base de datos
        self.cursor.execute("SELECT * FROM salon WHERE ID = %s", (user_id,))
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False
        
    def buscar_usuario(self):
        id_buscar = self.txBuscar.get()

        # Consultar el usuario por ID en la base de datos
        self.cursor.execute("SELECT * FROM salon WHERE ID = %s", (id_buscar,))
        usuario = self.cursor.fetchone()

        if usuario:
            # Mostrar los datos en la interfaz gráfica
            self.txId.config(state='normal')
            self.txNombre.config(state='normal')
            self.cbEdificio.config(state='readonly')
            self.cbProfile.config(state='readonly')

            self.txId.delete(0, tk.END)
            self.txNombre.delete(0, tk.END)
            self.cbEdificio.set('')
            self.cbProfile.set('')

            self.txId.insert(tk.END, usuario[0])
            self.txNombre.insert(tk.END, usuario[1])
            self.cbEdificio.set(usuario[2])
            self.cbProfile.set(usuario[3])

            self.btnEditar.config(state='normal')
            self.btnEliminar.config(state='normal')
            self.txId.config(state='disabled')
            self.txBuscar.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def nuevo_usuario(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.txNombre.config(state='normal')
        self.cbEdificio.config(state='readonly')
        self.cbProfile.config(state='readonly')
        self.cursor.execute("SELECT MAX(ID) FROM salon")
        max_id = self.cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1
        self.txId.delete(0, tk.END)
        self.txId.insert(tk.END, new_id)
        self.txId.config(state='disabled')
        self.btnNuevo.config(state='disabled')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def guardar_usuario(self):
        user_id = self.txId.get()
        nombre = self.txNombre.get()
        edificio = self.cbEdificio.get()
        profile = self.cbProfile.get()

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not nombre or not edificio or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")

        elif not self.validar_nombre(nombre):
            pass  # Handle validation errors as needed
        else:
            # Insertar el nuevo usuario en la base de datos
            self.cursor.execute("INSERT INTO salon (Nombre, Edificio, PERFIL) VALUES (%s, %s, %s)",
                                (nombre, edificio, profile))
            self.connection.commit()
            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.btnGuardar.config(state='disabled')
            self.btnCancelar.config(state='disabled')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')
            messagebox.showinfo("Éxito", "Usuario guardado correctamente")

    def cancelar(self):
        self.limpiar()
        self.btnNuevo.config(state='normal')

    def editar_usuario(self):
        user_id = self.txId.get()
        nombre = self.txNombre.get()
        edificio = self.cbEdificio.get()
        profile = self.cbProfile.get()

        opciones_profile = ["Activo", "Inactivo"]
        
        if not user_id or not nombre or not edificio or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
        elif not self.validar_nombre(nombre):
            pass  # Handle validation errors as needed
        else:
            # Actualizar el usuario en la base de datos
            self.cursor.execute("UPDATE salon SET Nombre=%s, Edificio=%s, PERFIL=%s WHERE ID=%s",
                                (nombre, edificio, profile, user_id))
            self.connection.commit()

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def eliminar_usuario(self):
        id_eliminar = self.txId.get()
        self.limpiar()

        # Actualizar el perfil a "Inactivo" en lugar de eliminar físicamente
        self.cursor.execute("UPDATE salon SET Perfil=%s WHERE ID=%s", ("Inactivo", id_eliminar))
        self.connection.commit()

        self.btnNuevo.config(state='normal')

    def limpiar(self):
        self.txId.config(state='normal')
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.cbEdificio.set('')
        self.cbProfile.set('')
        self.txId.config(state='disabled')
        self.txNombre.config(state='disabled')
        self.cbEdificio.config(state='disabled')
        self.cbProfile.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

# ------------------------------- Fin Salon -----------------------------------

# ------------------------------- Carrera -----------------------------------

class Carrera:
    def __init__(self, root):
        self.root = root
        self.root.config(width=500, height=400)
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Carrera")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Create users table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS carrera (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                NombreCarrera VARCHAR(255),
                NumSemestre INT,                
                PERFIL TEXT
            );
        """)
        self.connection.commit()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        global usernameuser
        self.imagen_boton_nuevo = tk.PhotoImage(file="Nuevo.png")
        self.imagen_boton_guardar = tk.PhotoImage(file="Guardar.png")
        self.imagen_boton_editar = tk.PhotoImage(file="Editar.png")
        self.imagen_boton_cancelar = tk.PhotoImage(file="Cancelar.png")
        self.imagen_boton_eliminar = tk.PhotoImage(file="Eliminar.png")
        self.imagen_boton_buscar = tk.PhotoImage(file="Buscar.png")
        self.imagen_boton_menu = tk.PhotoImage(file="Menu.png")
        tk.Label(self.root, text="Usuario: " + usernameuser, bg='black', fg='white').place(x=10, y=240)

        tk.Label(self.root, text="Buscar ID:", bg='black', fg='white').place(x=250, y=10)
        self.txBuscar = tk.Entry(self.root)
        self.txBuscar.place(x=360, y=10)

        self.btnBuscar = tk.Button(self.root, text="Buscar", command=self.buscar_usuario, image=self.imagen_boton_buscar)
        self.btnBuscar.place(x=315, y=10)

        tk.Label(self.root, text="ID:", bg='black', fg='white').place(x=10, y=10)
        self.txId = tk.Entry(self.root, state='disabled')
        self.txId.place(x=10, y=30)

        tk.Label(self.root, text="Nombre de la carrera", bg='black', fg='white').place(x=10, y=50)
        self.txNombre = tk.Entry(self.root, width=30, state='disabled')
        self.txNombre.place(x=10, y=70)

        tk.Label(self.root, text="Número de Semestres", bg='black', fg='white').place(x=10, y=90)
        self.intNumSemestre = tk.Entry(self.root, width=30, state='disabled')
        self.intNumSemestre.place(x=10, y=110)

        tk.Label(self.root, text="Perfil:", bg='black', fg='white').place(x=250, y=130)
        self.cbProfile = ttk.Combobox(self.root, state='disabled', values=["Activo", "Inactivo"])
        self.cbProfile.place(x=250, y=150)
        
        self.btnNuevo = tk.Button(self.root, text="Nuevo", command=self.nuevo_usuario, image=self.imagen_boton_nuevo)
        self.btnNuevo.place(x=200, y=250)

        self.btnGuardar = tk.Button(self.root, text="Guardar", state='disabled', command=self.guardar_usuario, image=self.imagen_boton_guardar)
        self.btnGuardar.place(x=226+20, y=250)

        self.btnCancelar = tk.Button(self.root, text="Cancelar", state='disabled', command=self.cancelar, image=self.imagen_boton_cancelar)
        self.btnCancelar.place(x=252+40, y=250)

        self.btnEditar = tk.Button(self.root, text="Editar", state='disabled', command=self.editar_usuario, image=self.imagen_boton_editar)
        self.btnEditar.place(x=278+60, y=250)

        self.btnEliminar = tk.Button(self.root, text="Eliminar", state='disabled', command=self.eliminar_usuario, image=self.imagen_boton_eliminar)
        self.btnEliminar.place(x=304+80, y=250)

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, image=self.imagen_boton_menu)
        self.btnMenu.place(x=330+100, y=250)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def validar_nombre(self, nombre):
        # Utilizar regex para validar que solo contiene letras, números y espacios
        if not re.match(r'^[a-zA-Z0-9 ]+$', nombre):
            messagebox.showerror("Error", "Usuario solo debe contener letras, números y espacios")
            return False
        return True

    def validar_perfil(self, perfil):
        # Validar que el perfil sea activo o inactivo
        opciones_perfil = ["Activo", "Inactivo"]
        if perfil not in opciones_perfil:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
            return False
        return True

    def id_existe(self, user_id):
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID debe ser un número entero")
            return False

        # Consultar si el ID ya existe en la base de datos
        self.cursor.execute("SELECT * FROM carrera WHERE ID = %s", (user_id,))
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False
        
    def validar_enteros(self, x):
        # Utilizar regex para validar que solo contiene números enteros
        if not re.match(r'^\d+$', x):
            messagebox.showerror("Error", "Los numeros de semestre solo deben contener números enteros")
            return False
        return True
        
    def buscar_usuario(self):
        id_buscar = self.txBuscar.get()

        # Consultar el usuario por ID en la base de datos
        self.cursor.execute("SELECT * FROM carrera WHERE ID = %s", (id_buscar,))
        usuario = self.cursor.fetchone()

        if usuario:
            # Mostrar los datos en la interfaz gráfica
            self.txId.config(state='normal')
            self.txNombre.config(state='normal')
            self.intNumSemestre.config(state='normal')
            self.cbProfile.config(state='normal')

            self.txId.delete(0, tk.END)
            self.txNombre.delete(0, tk.END)
            self.intNumSemestre.delete(0, tk.END)
            self.cbProfile.set('')

            self.txId.insert(tk.END, usuario[0])
            self.txNombre.insert(tk.END, usuario[1])
            self.intNumSemestre.insert(tk.END, usuario[2])
            self.cbProfile.set(usuario[3])

            self.btnEditar.config(state='normal')
            self.btnEliminar.config(state='normal')
            self.txId.config(state='disabled')
            self.txBuscar.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def nuevo_usuario(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.txNombre.config(state='normal')
        self.intNumSemestre.config(state='normal')
        self.cbProfile.config(state='normal')
        self.cursor.execute("SELECT MAX(ID) FROM carrera")
        max_id = self.cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1
        self.txId.delete(0, tk.END)
        self.txId.insert(tk.END, new_id)
        self.txId.config(state='disabled')
        self.btnNuevo.config(state='disabled')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def guardar_usuario(self):
        user_id = self.txId.get()
        nombre = self.txNombre.get()
        numsemestre = self.intNumSemestre.get()
        profile = self.cbProfile.get()

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not nombre or not numsemestre or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")

        elif not self.validar_nombre(nombre):
            pass 
        elif not self.validar_enteros(numsemestre):
            pass
        else:
            # Insertar el nuevo usuario en la base de datos
            self.cursor.execute("INSERT INTO carrera (NombreCarrera, NumSemestre, PERFIL) VALUES (%s, %s, %s)",
                                (nombre, numsemestre, profile))
            self.connection.commit()
            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.btnGuardar.config(state='disabled')
            self.btnCancelar.config(state='disabled')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')
            messagebox.showinfo("Éxito", "Usuario guardado correctamente")

    def cancelar(self):
        self.limpiar()
        self.btnNuevo.config(state='normal')

    def editar_usuario(self):
        user_id = self.txId.get()
        nombre = self.txNombre.get()
        numsemestre = self.intNumSemestre.get()
        profile = self.cbProfile.get()

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not nombre or not numsemestre or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
        elif not self.validar_nombre(nombre):
            pass 
        elif not self.validar_enteros(numsemestre):
            pass
        else:
            # Actualizar el usuario en la base de datos
            self.cursor.execute("UPDATE carrera SET NombreCarrera=%s, NumSemestre=%s, PERFIL=%s WHERE ID=%s",
                                (nombre, numsemestre, profile, user_id))
            self.connection.commit()

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def eliminar_usuario(self):
        id_eliminar = self.txId.get()
        self.limpiar()

        # Actualizar el perfil a "Inactivo" en lugar de eliminar físicamente
        self.cursor.execute("UPDATE carrera SET Perfil=%s WHERE ID=%s", ("Inactivo", id_eliminar))
        self.connection.commit()

        self.btnNuevo.config(state='normal')

    def limpiar(self):
        self.txId.config(state='normal')
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.intNumSemestre.delete(0, tk.END)
        self.cbProfile.set('')
        self.txId.config(state='disabled')
        self.txNombre.config(state='disabled')
        self.intNumSemestre.config(state='disabled')
        self.cbProfile.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

# ------------------------------- Fin Carrera -----------------------------------

# ------------------------------- Calificaciones Alta -----------------------------------
class Calificaciones_Alta:
    def __init__(self, root):
        self.root = root
        self.root.config(width=500, height=400)
        width = 500
        height = 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Calificaciones Alta")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Create users table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS calificaciones_alta (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                NombreCarrera VARCHAR(255),
                NombreMateria VARCHAR(255),
                NombreAlumno VARCHAR(255),
                Calificacion FLOAT,
                PERFIL TEXT,
                email VARCHAR(255)
            );
        """)
        self.connection.commit()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        global usernameuser, useruserid, userprofile
        self.imagen_boton_nuevo = tk.PhotoImage(file="Nuevo.png")
        self.imagen_boton_guardar = tk.PhotoImage(file="Guardar.png")
        self.imagen_boton_editar = tk.PhotoImage(file="Editar.png")
        self.imagen_boton_cancelar = tk.PhotoImage(file="Cancelar.png")
        self.imagen_boton_eliminar = tk.PhotoImage(file="Eliminar.png")
        self.imagen_boton_buscar = tk.PhotoImage(file="Buscar.png")
        self.imagen_boton_menu = tk.PhotoImage(file="Menu.png")
        tk.Label(self.root, text="Usuario: " + usernameuser, bg='black', fg='white').place(x=10, y=260)

        tk.Label(self.root, text="Buscar ID:", bg='black', fg='white').place(x=250, y=10)
        self.txBuscar = tk.Entry(self.root)
        self.txBuscar.place(x=360, y=10)

        self.btnBuscar = tk.Button(self.root, text="Buscar", command=self.buscar_usuario, image=self.imagen_boton_buscar)
        self.btnBuscar.place(x=315, y=10)

        tk.Label(self.root, text="ID:", bg='black', fg='white').place(x=10, y=10)
        self.txId = tk.Entry(self.root, state='disabled')
        self.txId.place(x=10, y=30)

        # Modificar para que funcione en base a la tabla de carreras
        tk.Label(self.root, text="Escoja carrera", bg='black', fg='white').place(x=10, y=50)
        
        if userprofile=="Admin":
            self.cursor.execute("SELECT DISTINCT carrera FROM premaestros where PERFIL = 'Activo'") 
        else:
            self.cursor.execute("SELECT DISTINCT carrera FROM premaestros where IDUsuario = "+str(useruserid)+" and PERFIL = 'Activo'") 

        Carrera=self.cursor.fetchall()
        
        if len(Carrera)>=1:
            self.txNombreCarrera = ttk.Combobox(self.root, state='disabled', values=Carrera)
        else:
            self.txNombreCarrera = ttk.Combobox(self.root, state='disabled', values=[])
        self.txNombreCarrera.place(x=10, y=70)

        self.txNombreCarrera.bind("<<ComboboxSelected>>", self.CambiarMaterias)   

        # Modificar para que funcione en base a la tabla de materias
        tk.Label(self.root, text="Escoja materia", bg='black', fg='white').place(x=10, y=90)
        

        self.txNombreMateria = ttk.Combobox(self.root, state='disabled', values=[])
        self.txNombreMateria.place(x=10, y=110)

        self.txNombreMateria.bind("<<ComboboxSelected>>", self.CambiarAlumnos)  

        # Modificar para que funcione en base a la tabla de alumnos       
        tk.Label(self.root, text="Escoja alumno", bg='black', fg='white').place(x=10, y=130)
        
        self.txNombreAlumno = ttk.Combobox(self.root, state='disabled', values=[])
        self.txNombreAlumno.place(x=10, y=150)

        tk.Label(self.root, text="Calificación", bg='black', fg='white').place(x=10, y=170)
        self.floatCalificacion = tk.Entry(self.root, width=30, state='disabled')
        self.floatCalificacion.place(x=10, y=190)

        tk.Label(self.root, text="Perfil:", bg='black', fg='white').place(x=10, y=210)
        self.cbProfile = ttk.Combobox(self.root, state='disabled', values=["Activo", "Inactivo"])
        self.cbProfile.place(x=10, y=230)
        
        self.btnNuevo = tk.Button(self.root, text="Nuevo", command=self.nuevo_usuario, image=self.imagen_boton_nuevo)
        self.btnNuevo.place(x=200, y=250)

        self.btnGuardar = tk.Button(self.root, text="Guardar", state='disabled', command=self.guardar_usuario, image=self.imagen_boton_guardar)
        self.btnGuardar.place(x=226+20, y=250)

        self.btnCancelar = tk.Button(self.root, text="Cancelar", state='disabled', command=self.cancelar, image=self.imagen_boton_cancelar)
        self.btnCancelar.place(x=252+40, y=250)

        self.btnEditar = tk.Button(self.root, text="Editar", state='disabled', command=self.editar_usuario, image=self.imagen_boton_editar)
        self.btnEditar.place(x=278+60, y=250)

        self.btnEliminar = tk.Button(self.root, text="Eliminar", state='disabled', command=self.eliminar_usuario, image=self.imagen_boton_eliminar)
        self.btnEliminar.place(x=304+80, y=250)

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, image=self.imagen_boton_menu)
        self.btnMenu.place(x=330+100, y=250)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def validar_nombre(self, nombre):
        # Utilizar regex para validar que solo contiene letras, números y espacios
        if not re.match(r'^[a-zA-Z0-9 ]+$', nombre):
            messagebox.showerror("Error", "Usuario solo debe contener letras, numeros y espacios")
            return False
        return True

    def validar_perfil(self, perfil):
        # Validar que el perfil sea activo o inactivo
        opciones_perfil = ["Activo", "Inactivo"]
        if perfil not in opciones_perfil:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")
            return False
        return True

    def CambiarMaterias(self, event):
        Carrera=self.txNombreCarrera.get()

        if userprofile=="Admin":
            self.cursor.execute("SELECT DISTINCT materia FROM premaestros where PERFIL = 'Activo' and Carrera='"+Carrera+"'") 
        else:
            self.cursor.execute("SELECT DISTINCT materia FROM premaestros where PERFIL = 'Activo' and Carrera='"+Carrera+"'"+" and IDUsuario = '"+str(useruserid)+"'") 
            
        Materia=self.cursor.fetchall()
        
        if len(Materia)>=1:
            self.txNombreMateria.config(values=Materia)
        else:
            self.txNombreMateria.config(values=[])

        #self.txNombreAlumno.config(state='normal')
        #self.txNombreAlumno.delete(0, tk.END)
        #self.txNombreAlumno.config(state='readonly')
        self.txNombreAlumno.config(values=[])


    def CambiarAlumnos(self, event):


        Carrera=self.txNombreCarrera.get()
        Materia=self.txNombreMateria.get()
        
        if userprofile=="Admin":
            self.cursor.execute("SELECT NombrGrupo FROM grupo where perfil = 'Activo' and Carrera='"+Carrera+"'"+" and Materia='"+Materia+"' ")
        else:
            self.cursor.execute("SELECT NombrGrupo FROM grupo where perfil = 'Activo' and Carrera='"+Carrera+"'"+" and Materia='"+Materia+"' and IDMaestro = '"+str(useruserid)+"'")
        
        Grupo=self.cursor.fetchall()

        if len(Grupo)>=1:

            self.cursor.execute("SELECT NOMBRE, Apellido_Paterno, Apellido_Materno, email FROM preregistro where Materia = '"+Grupo[0][0]+"'")
            Alumn=self.cursor.fetchall()
            
            self.Emails=[]
            Alumnos=[]
            for dates in Alumn:
                self.Emails.append(dates[3])
                Alumnos.append(dates[0]+" "+ dates[1]+ " "+ dates[2])

            self.txNombreAlumno.config(values=Alumnos)

        else:
            self.txNombreAlumno.config(values=[])
    
    def id_existe(self, user_id):
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID debe ser un numero entero")
            return False

        # Consultar si el ID ya existe en la base de datos
        self.cursor.execute("SELECT * FROM calificaciones_alta WHERE ID = %s", (user_id,))
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False

    def validar_flotante(self, flotante):
        # Utilizar regex para validar que solo contiene números flotantes
        if not re.match(r'^-?\d+(?:\.\d+)?$', flotante):
            messagebox.showerror("Error", "La calificación debe ser un número flotante")
            return False
        return True

        
    def buscar_usuario(self):
        id_buscar = self.txBuscar.get()

        # Consultar el usuario por ID en la base de datos
        self.cursor.execute("SELECT * FROM calificaciones_alta WHERE ID = %s", (id_buscar,))
        usuario = self.cursor.fetchone()

        if usuario:
            # Mostrar los datos en la interfaz gráfica
            self.txId.config(state='normal')
            self.txNombreCarrera.config(state='normal')
            self.txNombreMateria.config(state='normal')
            self.txNombreAlumno.config(state='normal')
            self.floatCalificacion.config(state='normal')
            self.cbProfile.config(state='normal')

            self.txId.delete(0, tk.END)
            self.txNombreCarrera.delete(0, tk.END)
            self.txNombreMateria.delete(0, tk.END)
            self.txNombreAlumno.delete(0, tk.END)
            self.floatCalificacion.delete(0, tk.END)
            self.cbProfile.set('')

            self.txId.insert(tk.END, usuario[0])
            self.txNombreCarrera.insert(tk.END, usuario[1])
            self.txNombreMateria.insert(tk.END, usuario[2])
            self.txNombreAlumno.insert(tk.END, usuario[3])
            self.floatCalificacion.insert(tk.END, usuario[4])
            self.cbProfile.set(usuario[5])

            self.btnEditar.config(state='normal')
            self.btnEliminar.config(state='normal')
            self.txId.config(state='disabled')
            self.txBuscar.delete(0, tk.END)

            self.CambiarMaterias("a")
            self.CambiarAlumnos("a")
            
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def nuevo_usuario(self):
        self.limpiar()
        self.txId.config(state='normal')
        self.txNombreAlumno.config(state='normal')
        self.txNombreCarrera.config(state='normal')
        self.txNombreMateria.config(state='normal')
        self.floatCalificacion.config(state='normal')
        self.cbProfile.config(state='normal')
        self.cursor.execute("SELECT MAX(ID) FROM calificaciones_alta")
        max_id = self.cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1
        self.txId.delete(0, tk.END)
        self.txId.insert(tk.END, new_id)
        self.txId.config(state='disabled')
        self.btnNuevo.config(state='disabled')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def guardar_usuario(self):
        user_id = self.txId.get()
        nombre_carrera = self.txNombreCarrera.get()
        nombre_materia = self.txNombreMateria.get()
        nombre_alumno = self.txNombreAlumno.get()
        calificacion = self.floatCalificacion.get()
        profile = self.cbProfile.get()

        Email=self.Emails[self.txNombreAlumno.current()]

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not nombre_carrera or not nombre_materia or not nombre_alumno or not calificacion or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser Activo o Inactivo")

        elif not self.validar_flotante(calificacion):
            pass
        else:
            # Insertar el nuevo usuario en la base de datos
            self.cursor.execute("INSERT INTO calificaciones_alta (NombreCarrera, NombreMateria, NombreAlumno, Calificacion, PERFIL, email) VALUES (%s, %s, %s, %s, %s, %s)",
                                (nombre_carrera, nombre_materia, nombre_alumno, calificacion, profile, Email))
            self.connection.commit()
            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.btnGuardar.config(state='disabled')
            self.btnCancelar.config(state='disabled')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')
            messagebox.showinfo("Éxito", "Usuario guardado correctamente")

    def cancelar(self):
        self.limpiar()
        self.btnNuevo.config(state='normal')

    def editar_usuario(self):
        user_id = self.txId.get()
        nombre_carrera = self.txNombreCarrera.get()
        nombre_materia = self.txNombreMateria.get()
        nombre_alumno = self.txNombreAlumno.get()
        calificacion = self.floatCalificacion.get()
        profile = self.cbProfile.get()

        opciones_profile = ["Activo", "Inactivo"]

        if not user_id or not nombre_carrera or not nombre_materia or not nombre_alumno or not calificacion or not profile:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
        elif profile not in opciones_profile:
            messagebox.showerror("Error", "El perfil debe ser activo o inactivo")
        else:
            # Actualizar el usuario en la base de datos
            self.cursor.execute("UPDATE calificaciones_alta SET NombreCarrera=%s, NombreMateria=%s, NombreAlumno=%s, Calificacion=%s, PERFIL=%s WHERE ID=%s",
                                (nombre_carrera, nombre_materia, nombre_alumno, calificacion, profile, user_id))
            self.connection.commit()

            self.limpiar()
            self.btnNuevo.config(state='normal')
            self.txId.config(state='normal')
            self.txId.delete(0, tk.END)
            self.txId.config(state='disabled')

    def eliminar_usuario(self):
        id_eliminar = self.txId.get()
        self.limpiar()

        # Actualizar el perfil a "Inactivo" en lugar de eliminar físicamente
        self.cursor.execute("UPDATE calificaciones_alta SET Perfil=%s WHERE ID=%s", ("Inactivo", id_eliminar))
        self.connection.commit()

        self.btnNuevo.config(state='normal')

    def limpiar(self):
        self.txId.config(state='normal')
        self.txId.delete(0, tk.END)
        self.txNombreCarrera.delete(0, tk.END)
        self.txNombreMateria.delete(0, tk.END)
        self.txNombreAlumno.delete(0, tk.END)
        self.floatCalificacion.delete(0, tk.END)
        self.cbProfile.set('')
        self.txId.config(state='disabled')
        self.txNombreAlumno.config(state='disabled')
        self.txNombreCarrera.config(state='disabled')
        self.txNombreMateria.config(state='disabled')
        self.floatCalificacion.config(state='disabled')
        self.cbProfile.config(state='disabled')
        self.btnEditar.config(state='disabled')
        self.btnEliminar.config(state='disabled')

    #validaciones
    
    def validar_calificacion(self):
        calificacion = self.floatCalificacion.get()
        if (not calificacion.isdigit()):
            messagebox.showerror("Error", "La calificación debe ser un número")
        else:
            if (calificacion > 100) or (calificacion < 0):
                messagebox.showerror("Error", "La calificación debe ser un número entre 0 y 100")
            else:
                messagebox.showinfo("Aceptado", "La calificación fue guardada exitosamente")

# ------------------------------- Fin Calificaciones -----------------------------------

# ------------------------------- Visualizar calificación alumno -----------------------------------

class Mostrar_Calificaciones:
    def __init__(self, root):
        self.root = root
        self.root.config(width=800, height=600)
        width = 800
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Calificaciones")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Header
        global usernameuser
        tk.Label(self.root, text="Calificaciones", bg='black', fg='white', font=("Arial", 16)).pack(pady=10)

        # Frame to hold repair data
        frame = tk.Frame(self.root, bg='black')
        frame.pack(pady=20)

        # Create Treeview widget
        self.tree = ttk.Treeview(frame, columns=('Nombre Materia', 'Calificación'))
        self.tree.heading('Nombre Materia', text='Nombre Materia')
        self.tree.heading('Calificación', text='Calificación')
        self.tree.pack()

        # Populate Treeview with grades data
        self.populate_treeview()

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, bg='black')
        self.btnMenu.place(x=10, y=10)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def populate_treeview(self):
        # Clear existing items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve grades data from the database for the current user
        global useremail
        self.cursor.execute("SELECT NombreMateria, Calificacion FROM calificaciones_alta WHERE email = %s", (usernameuser,))
        grades = self.cursor.fetchall()

        # If no grades found for the current user, display a message
        if not grades:
            self.tree.insert('', 'end', text="No tienes calificaciones", values=("", ""))
        else:
            # Insert grades data into the Treeview
            for grade in grades:
                self.tree.insert('', 'end', text="", values=(grade[0], grade[1]))

# ------------------------------- Fin Visualizar calificación alumno -----------------------------------

# ------------------------------- Mostrar Alumnos -----------------------------------

class PlaneacionSalon:
    def __init__(self, root):
        self.root = root
        self.root.config(width=800, height=600)
        width = 800
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Planeación")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Widgets
        self.create_widgets()

    def create_widgets(self):

        self.cursor.execute("SELECT ID,Nombre, Edificio FROM salon")

        tk.Label(self.root, text="Salones Disponibles", bg='black', fg='white', font=("Arial", 24)).place(x=250,y=30)
        
        Frames=[]
        c=0
        Separacion=0
        Altura=0
        for dates in self.cursor.fetchall():
            Frames.append([tk.Frame(self.root, bg='Black'),dates[1],dates[2]])
            Frames[c][0].config(width=120, height=120)
            Frames[c][0].place(x=80+Separacion*130,y=120+Altura*130)
            tk.Label(Frames[c][0], text="Edificio: "+dates[2], bg='Black', fg='white', font=("Arial", 9)).place(x=30,y=35)
            tk.Label(Frames[c][0], text="Salòn: "+dates[1], bg='Black', fg='white', font=("Arial", 9)).place(x=30,y=55)
            Frames[c][0].bind("<Button-1>", lambda event, dato=dates: self.MostrarAlumnos(event, dato[1]+" "+dato[2]))
            Separacion+=1
            
            c+=1
            if c%5==0:
                Altura+=1
                Separacion=0

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, bg='black', fg='white')
        self.btnMenu.place(x=10, y=10)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def MostrarAlumnos(self, event, Datos):

        self.root.destroy()
        root = tk.Tk()
        app = PlaneacionGrupos(root,Datos)
        root.mainloop()

    def populate_treeview(self):
        # Clear existing items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve data from the 'grupo' table
        self.cursor.execute("SELECT * FROM grupo")
        self.data = self.cursor.fetchall()

        # If no data found in the 'grupo' table, display a message
        if not self.data:
            self.tree.insert('', 'end', text="No hay datos en la tabla", values=("", "", "", "", "", "", "", "", "", "", "", ""))
        else:
            # Insert data into the Treeview
            for row in self.data:
                self.tree.insert('', 'end', text=row[0], values=row[1:])

class PlaneacionGrupos:
    def __init__(self, root, salon):
        self.root = root
        self.root.config(width=800, height=600)
        width = 800
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Planeación")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Widgets
        self.salon=salon
        self.create_widgets()

    def create_widgets(self):
        # Header
        tk.Label(self.root, text="Planeación", bg='black', fg='white', font=("Arial", 16)).pack(pady=10)

        # Frame to hold data
        frame = tk.Frame(self.root, bg='black')
        frame.pack(pady=20)

        # Create Treeview widget
        self.tree = ttk.Treeview(frame, columns=('ID', 'NombreGrupo', 'Fecha', 'Carrera', 'Materia', 'Maestro', 'Salon', 'Horario', 'Semestre', 'MaxNumAlumnos', 'Perfil', 'IDMaestro'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('ID', text='Nombre Grupo')  # Asignar la columna '#0' a 'ID'
        self.tree.heading('NombreGrupo', text='Fecha')
        self.tree.heading('Fecha', text='Carrera')
        self.tree.heading('Carrera', text='Materia')
        self.tree.heading('Materia', text='Maestro')
        self.tree.heading('Maestro', text='Salon')
        self.tree.heading('Salon', text='Semestre')
        self.tree.heading('Horario', text='MaxNumAlumnos')
        self.tree.heading('Semestre', text='Perfil')
        self.tree.heading('MaxNumAlumnos', text='IDMaestro')

        # Agregar la barra de desplazamiento horizontal
        xscrollbar = ttk.Scrollbar(frame, orient='horizontal', command=self.tree.xview)
        xscrollbar.pack(side='bottom', fill='x')
        self.tree.configure(xscrollcommand=xscrollbar.set)

        self.tree.pack()

        self.tree.bind("<<TreeviewSelect>>", self.MostrarAlumnos)
        # Populate Treeview with data from 'grupo' table
        self.populate_treeview()

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, bg='black', fg='white')
        self.btnMenu.place(x=10, y=10)



    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def MostrarAlumnos(self, event):
        
        Iteam= int(self.tree.selection()[0][1:])-1
        datos=[]
        datos.append(self.data[Iteam][1])
        datos.append(self.data[Iteam][3])
        datos.append(self.data[Iteam][4])
        self.root.destroy()
        root = tk.Tk()
        app = PlaneacionHorario(root,datos)
        root.mainloop()

    def populate_treeview(self):
        # Clear existing items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve data from the 'grupo' table
        self.cursor.execute("SELECT * FROM grupo where Salon = '"+self.salon+"'")
        self.data = self.cursor.fetchall()

        # If no data found in the 'grupo' table, display a message
        if not self.data:
            self.tree.insert('', 'end', text="No hay datos en la tabla", values=("", "", "", "", "", "", "", "", "", "", "", ""))
        else:
            # Insert data into the Treeview
            for row in self.data:
                self.tree.insert('', 'end', text=row[0], values=row[1:])

class PlaneacionHorario:
    def __init__(self, root, datos):
        self.root = root
        self.root.config(width=800, height=600)
        width = 800
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Planeación")
        self.root.configure(bg='#474D5C')

        # Database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        self.datos=datos
        self.create_widgets()

    def create_widgets(self):

        dias_semana = [" ","Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        for i, dia in enumerate(dias_semana):
            tk.Label(self.root, text=dia, width=15).place(x=10+(i*120), y=20)

        for hora in range(7, 18):
            tk.Label(self.root, text=f"{hora:02}:00 - {hora+1:02}:00", width=15, pady=9).place(x=10, y=4+((hora-6)*38))

        self.Horario=[]
        Materias= self.datos[2].split(',')
        for dates in Materias:
            self.cursor.execute("SELECT Horario, Dia FROM materias where Asignatura = '"+dates+"' and Carrera = '"+self.datos[1]+"'")
            Consulta=self.cursor.fetchall()
            for Info in Consulta:
                self.Horario.append([Info[0],Info[1],dates])

        Colores=["#FF5733", "#1ABC9C", "#3498DB", "#8E44AD", "#E74C3C", "#FFC300", "#2ECC71", "#FF5733", "#F39C12", "#34495E"]

        SepaDia=1
        Dias= []
        FramesHorario=[]
        c=0
        for dates in self.Horario:

            Dias= dates[1].split(',')

            for dia in Dias:
                if dia=="L":
                    SepaDia=2
                elif dia=="M":
                    SepaDia=3
                elif dia=="I":
                    SepaDia=4
                elif dia=="J":
                    SepaDia=5
                elif dia=="V":
                    SepaDia=6

                Horas= dates[0].split(' ')

                Inicio = int(Horas[1][:1])
                if Inicio==1:
                    Inicio= int(Horas[1][:2])
                
                Fin= int(Horas[0][:1])

                if Fin==1:
                    Fin= int(Horas[0][:2])

                HorasDeClase= Inicio-Fin
                rand=Colores[random.randint(0, 9)]
                FramesHorario.append([tk.Frame(self.root, bg=rand),"Hola"])
                FramesHorario[c][0].config(width=115, height=38 * HorasDeClase + (HorasDeClase - 1))

                tk.Label(FramesHorario[c][0], text=" "+dates[2], bg=rand, fg='Black', font=("Arial Black", 9, "bold")).place(x=15,y=30)

                FramesHorario[c][0].place(x=2+((SepaDia-1)*120+5), y=4+((Fin-6)*38))
                FramesHorario[c][0].bind("<Button-1>", lambda event, dato=self.datos[0]: self.MostrarAlumnos(event, dato))
                c+=1

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, bg='black', fg='white')
        self.btnMenu.place(x=10, y=480)



    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()
            
    def MostrarAlumnos(self, event, Datos):

        self.root.destroy()
        root = tk.Tk()
        app = PlaneacionAlumnos(root,Datos)
        root.mainloop()
        

class PlaneacionAlumnos:
    def __init__(self, root, Grupo):
        self.root = root
        self.root.config(width=800, height=600)
        width = 800
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.title("Planeación")
        self.root.configure(bg='#474D5C')

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LFMB",
            database="proyect"
        )

        self.cursor = self.connection.cursor()

        # Widgets
        print(Grupo)
        self.cursor.execute("SELECT * FROM preregistro where perfil = 'Activo' and materia='"+Grupo+"'")
        self.data = self.cursor.fetchall()

        self.create_widgets()

    
    def create_widgets(self):
        # Header
        tk.Label(self.root, text="Planeación", bg='black', fg='gold', font=("Arial", 16)).pack(pady=10)

        # Frame to hold data
        frame = tk.Frame(self.root, bg='black')
        frame.pack(pady=20)

        # Create Treeview widget
        self.tree = ttk.Treeview(frame, columns=('ID', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'email', 'PERFIL', 'FechaDeNacimiento', 'Carrera', 'Materia'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('ID', text='IDUsuario')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Apellido_Paterno', text='Apellido_Paterno')
        self.tree.heading('Carrera', text='Carrera')
        self.tree.heading('Apellido_Materno', text='Apellido_Materno')
        self.tree.heading('email', text='email')
        self.tree.heading('PERFIL', text='PERFIL')
        self.tree.heading('FechaDeNacimiento', text='FechaDeNacimiento')
        self.tree.heading('Carrera', text='Carrera')
        self.tree.heading('Materia', text='Materia')

        xscrollbar = ttk.Scrollbar(frame, orient='horizontal', command=self.tree.xview)
        xscrollbar.pack(side='bottom', fill='x')
        self.tree.configure(xscrollcommand=xscrollbar.set)
        self.tree.pack()

        # Populate Treeview with data from 'grupo' table
        self.populate_treeview()

        self.btnMenu = tk.Button(self.root, text="Menú", command=self.abrir_menu, bg='black', fg='white')
        self.btnMenu.place(x=10, y=10)

    def abrir_menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = option(root)
        root.mainloop()

    def populate_treeview(self):
        # Clear existing items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve data from the 'grupo' table
        
        

        # If no data found in the 'grupo' table, display a message
        if not self.data:
            self.tree.insert('', 'end', text="No hay datos en la tabla", values=("", "", "", "", "", "", "", "", "", "", "", ""))
        else:
            # Insert data into the Treeview
            for row in self.data:
                self.tree.insert('', 'end', text=row[0], values=row[1:])


# ------------------------------- Fin Planeacion ----------------------------------

# ------------------------------- Extra: Dinosauro :) -----------------------------------
class Dinosaur:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 300
        self.DINO_WIDTH = 20  # Dinosaurio más delgado
        self.DINO_HEIGHT = 40  # Dinosaurio más delgado
        self.GRAVITY = 1
        self.dino_image1 = pygame.image.load("Dinosaurio.png")
        self.dino_image2 = pygame.image.load("Dinosaurio2.png")
        self.current_dino_image = self.dino_image1
        self.image_timer = 0
        self.image_switch_time = 15  # Switch image every 30 frames
        
        self.x = 50
        self.y = self.SCREEN_HEIGHT - self.DINO_HEIGHT - 10
        self.velocity = 0
        self.jump_strength = -20
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity = self.jump_strength
            self.is_jumping = True

    def update(self):
        self.velocity += self.GRAVITY
        self.y += self.velocity

        if self.y >= self.SCREEN_HEIGHT - self.DINO_HEIGHT - 10:
            self.y = self.SCREEN_HEIGHT - self.DINO_HEIGHT - 10
            self.velocity = 0
            self.is_jumping = False

        # Increment the image timer
        self.image_timer += 1
        # Check if it's time to switch the image
        if self.image_timer >= self.image_switch_time:
            self.image_timer = 0
            # Toggle between the two images
            if self.current_dino_image == self.dino_image1:
                self.current_dino_image = self.dino_image2
            else:
                self.current_dino_image = self.dino_image1

    def draw(self, screen):
        screen.blit(self.current_dino_image, (self.x, self.y))

class Game:
    def __init__(self):
        pygame.init()
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 300
        self.clock = pygame.time.Clock()
        self.dinosaur = Dinosaur()
        self.obstacles = []
        self.spawn_timer = 0

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Dinosaur Game")

        self.score = 0  # Inicializa el contador de puntuación

        self.game_over = False

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        self.dinosaur.jump()

            self.screen.fill(self.WHITE)

            self.spawn_obstacles()
            self.move_obstacles()
            self.handle_collisions()

            self.dinosaur.update()
            self.dinosaur.draw(self.screen)

            # Mostrar puntuación en la pantalla
            self.draw_score()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        musicaparatodos()

    def spawn_obstacles(self):
        self.spawn_timer += 1
        if self.spawn_timer == 7:  # Obstáculos aún más seguidos
            self.spawn_timer = 0
            if random.randint(1, 15) == 1:
                self.obstacles.append(Obstacle())

    def move_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.move()
            obstacle.draw(self.screen)

    def handle_collisions(self):
        dino_rect = pygame.Rect(self.dinosaur.x, self.dinosaur.y, self.dinosaur.DINO_WIDTH, self.dinosaur.DINO_HEIGHT)
        for obstacle in self.obstacles:
            obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
            if dino_rect.colliderect(obstacle_rect):
                messagebox.showinfo("Game Over!", "Game Over! tu puntuación fue: " + str(self.score))
                self.game_over = True
            elif obstacle.x + obstacle.width < self.dinosaur.x:
                # Si el dinosaurio pasa un obstáculo, aumenta la puntuación
                self.increase_score()
                self.obstacles.remove(obstacle)

    def draw_score(self):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, self.BLACK)
        self.screen.blit(score_text, (10, 10))

    def increase_score(self):
        self.score += 1

class Obstacle:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 300
        self.width = 20
        self.height = 40
        self.x = self.SCREEN_WIDTH
        self.y = self.SCREEN_HEIGHT - self.height - 10
        self.speed = 5
        self.obstacle_image = pygame.image.load("Obstaculo.png")

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        screen.blit(self.obstacle_image, (self.x, self.y))

# ------------------------------- Fin Extra: Dinosauro :) -----------------------------------

if __name__ == "__main__":
    musicaparatodos()
    root = tk.Tk()
    login = Login(root)
    # Database connection
    login.connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="LFMB",
        database="proyect"
    )
    login.cursor = login.connection.cursor()
    root.mainloop()


