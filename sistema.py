from usuario import Usuario
from imprimir import Imprimir

class Sistema:

    def __init__(self):
        self.lista_usuarios = []
        self.imprimir = Imprimir()
        self.archivo_usuarios = "usuarios.txt"
        self.archivo_grupos = "grupos.txt"
        self.usuario_actual = None
        #self.leer_usuarios_desde_archivo(self.archivo_usuarios)
        #self.leer_grupos_desde_archivo(self.archivo_grupos)

    def guardar_en_archivo(self, usuario, nombre_archivo):
        with open(nombre_archivo, "a") as archivo:
            archivo.write(usuario.obtener_info() + "\n")

    def leer_usuarios_desde_archivo(self, nombre_archivo):
        usuarios = []

        try:
            with open(nombre_archivo, "r") as archivo:
                lineas = archivo.readlines()

                for linea in lineas:
                    nombre_inicio = linea.find("Nombre:")
                    contrasena_inicio = linea.find("Contraseña:")
                    monto_inicio = linea.find("Monto:")
                    grupos_inicio = linea.find("Grupos:")

                    if nombre_inicio != -1 and contrasena_inicio != -1 and monto_inicio != -1:
                        nombre = linea[nombre_inicio + len("Nombre:"):contrasena_inicio].strip()
                        contrasena = linea[contrasena_inicio + len("Contraseña:"):monto_inicio].strip()
                        monto_str = linea[monto_inicio + len("Monto:"):grupos_inicio].strip()
                        grupos_str = linea[grupos_inicio + len("Grupos:"):].strip()

                        try:
                            monto = int(monto_str)
                        except ValueError:
                            print(f"Error al convertir monto a entero en la línea: {linea}")
                            continue

                        grupos = [grupo.strip() for grupo in grupos_str.split(',')]
                        usuarios.append(Usuario(nombre, contrasena, monto))

        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
        except Exception as e:
            print(f"Error al leer usuarios desde el archivo: {e}")

        return usuarios

    def iniciar_sesion(self):
        nombre = input("Ingrese su nombre: ")
        contrasena = input("Ingrese su contraseña: ")

        usuarios = self.leer_usuarios_desde_archivo(self.archivo_usuarios)

        print('<<------------------------>>')

        for usuario_actual in usuarios:
            if usuario_actual.nombre == nombre and usuario_actual.contraseña == contrasena:
                print(f"Inicio de sesión exitoso. Hola, {nombre}!")
                self.usuario_actual = usuario_actual
                print('<<------------------------>>')
                return

        print("Inicio de sesión fallido. Verifique sus credenciales.")
        print('<<------------------------>>')

    def arrancamos(self):

        print(self.lista_usuarios)

        salir = False

        while not salir:
            valido = False

            print(self.usuario_actual)
            if self.usuario_actual is not None:
                print(self.usuario_actual.Grupos)

            while not valido:
                self.imprimir.menu()

                resp = int(input('R/= '))

                if 0 < resp <= 12:
                    valido = True
                else:
                    print('<------- Respuesta inválida, por favor intente de nuevo -------->')

            if resp == 1:
                self.iniciar_sesion()

            if resp == 2:
                self.cerrar_sesion()

            if resp == 3:
                nombre = input("Ingrese su nombre: ")
                monto = 0
                try:
                    monto = int(input("Ingrese su Monto: "))
                except ValueError:
                    print("El monto debe ser un número entero.")
                    continue

                contrasena = input("Ingrese su contraseña: ")

                nuevo_usuario = Usuario(nombre, contrasena, monto)
                self.guardar_en_archivo(nuevo_usuario, self.archivo_usuarios)

            if resp==4:

                print(self.usuario_actual)

                self.unirse_a_grupo()

            if resp==5:

                self.crear_grupo()