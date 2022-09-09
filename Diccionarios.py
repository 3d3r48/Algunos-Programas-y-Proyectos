"""
Ejercicio 1
===========

Realizar un programa utilizando cada una de las relaciones entre clases comentando la utilidad de su uso

a)  Planteo del problema:
    Un banco nos pide que realicemos un sistema en donde el administrador del banco puede registrar tanto a clientes como trabajadores.
    cada usuario estara asociado solo a una cuenta, y esta cuenta será generada al registrarlo.
    El numero de esa cuenta sera su DNI (una C al inicio si es cliente, y una T al inicio si es Trabajador), y tendrá un monto inciial de 0

"""

from os import system

class Cuenta:
    def __init__(self, numero_cuenta, saldo_inicial):
        self.saldo = saldo_inicial
        self.numero_cuenta = numero_cuenta


class Persona:
    """
    Clase que define datos principales de los clientes y trabajadores
    """
    def __init__(self, fullname, dni, cuenta):  # agregando clase Cuenta
        self.fullname = fullname
        self.dni = dni
        self.cuenta = cuenta

class Cliente(Persona):
    """
    Esta clase hereda de la clase Persona
    """
    def __init__(self, fullname, dni, cuenta):
        super().__init__(fullname, dni, cuenta)

class Trabajador(Persona):
    """
    Esta clase hereda de la clase Persona
    """
    def __init__(self, fullname, dni, cuenta):
        super().__init__(fullname, dni, cuenta)

class Banco:
    """
    El banco esta compuesto por sus clientes y sus trabajadores      Es decir aqui se aplica la composicion
    """
    def __init__(self):
        self.clientes = []
        self.trabajadores = []

    """ 
    Aqui la herencia multinivel 
    """
    def ver_trabajadores(self):
        for trabajador in self.trabajadores:
            print("Nombre >>", trabajador.fullname)

    def ver_clientes(self):
        for cliente in self.clientes:
            print("Nombres >>", cliente.fullname)

    def anadir_cliente(self, cliente):
        self.clientes.append(cliente)

    def anadir_trabajador(self, trabajador):
        self.trabajadores.append(trabajador)


banco = Banco()
salir  = False

print("----------------------------------------")  # Mi interfaz de usuario
print("Menu de opciones")
print("Autor: Eder Huillca Ayma")
print("Bienvenidos :)")
print("Hoy es 26 de Febrero del 2022.")
print("Programa que usa la herencia multiple , agregación y compoosición.")
print("----------------------------------------")
print("--- Pulse una tecla para continuar")
input()
while not salir:
    system("cls")
    print("Bienvenido al Sistema")
    print("1. Registrar")
    print("2. Mostrar todos los usuarios")
    print("3. Salir")
    opc = input("Ingrese la opcion a elegir >> ")
    if opc == "1":
        dni = input("Ingrese el dni de la persona >> ")
        fullname = input("Ingrese nombres y apellidos de la persona >> ")
        tipo = input("Ingrese 'T' si es trabajador o 'C' si es cliente >> ")
        if tipo.lower() == "t":
            trabajador = Trabajador(fullname, dni, Cuenta("t"+dni, 0)) # agregando cuenta
            banco.anadir_trabajador(trabajador)
            print("Trabajador correctamente registrado")
        elif tipo.lower() == "c":
            cliente = Cliente(fullname, dni, Cuenta("c"+dni, 0)) # agregando cuenta
            banco.anadir_cliente(cliente)
            print("Cliente correctamente registrado")
        else:
            print("Opcion ingresada no valida")

    elif opc == "2":
        print("Trabajadores")
        banco.ver_trabajadores()
        print()
        print("Clientes")
        banco.ver_clientes()

    elif opc == "3":
        print("Gracias por usar este programa!")
        salir = True



    else:
        print("Opcion ingresada no valida")

    input("\nPresione enter para continuar ...")