import os
import time 
from Lista import listaSimple

Ordenes = listaSimple()

def Menu():
    print('')
    print('1. Agregar orden.')
    print('2. Entregar orden.')
    print('3. Mostrar ordenes.')
    print('4. Datos del estudiante.')
    print('5. Salir.')
    print('')

    opcion = input('Ingrese un número del menú.')
    if opcion == '1':
        limpiarConsola()
        agregarOrden()
    elif opcion == '2':
        limpiarConsola()
        sacarOrden()
    elif opcion == '3':
        limpiarConsola()
        mostrarOrden()
    elif opcion == '4':
        limpiarConsola()
        informacionEstudiante()
    elif opcion == '5':
        limpiarConsola()
        print('Esperamos vuelvas pronto..!')
        exit()
    else:
        limpiarConsola()
        input('\nIngrese una opción válida. Presione Enter para continuar.\n')
        limpiarConsola()
        Menu()

'''-----------------------PARA LA PIZZA-----------------------'''
def agregarOrden():
    opcionPedir = str(input('\nIngrese la pizza que desea.\n'))
    if opcionPedir == "":
       limpiarConsola()
       Menu()
    Ordenes.Agregar(opcionPedir)
    limpiarConsola()

    opcionPedir2 = str(input('\n¿Desea agregar otra orden? Presione Enter para continuar.\nDe lo contrario presione cualquier tecla para regresar al Menu.\n'))
    if opcionPedir2 != "":
        limpiarConsola()
        Menu()
    else:
        limpiarConsola()
        agregarOrden()

def sacarOrden():
    if Ordenes.vacio():
        input('\nNo hay ordens pendientes. Presione Enter para regresar al Menú.\n')
        limpiarConsola()
        Menu()
    ordenx = Ordenes.Retirar()
    input('Pizza de ' + str(ordenx.item) + ' entregada. Presione Enter para regresar al Menú.\n')
    limpiarConsola()
    Menu()

def mostrarOrden():
    if Ordenes.vacio():
        input('\nNo hay ordens pendientes. Presione Enter para regresar al Menú.\n')
        limpiarConsola()
        Menu()
    x = Ordenes.enviarCola()
    size = 1
    for i in x:
        size += 1
        print(str(size)+'. Oden: Pizza de ' + str(i.item))
    input('\nPresione Enter para regresal al Menú.')
    limpiarConsola()
    Menu()


'''-----------------------PARA EL TIEMPO-----------------------'''


def informacionEstudiante():
    print('') 
    print('Christian Alessander Blanco González.')
    print('202000173.')
    print('Introducción a la Programación y Computación.')
    print('Seccion D.')
    print('4to. Semestre.')
    print('')
    input('Presione Enter para regresar la Menú')
    limpiarConsola()
    Menu()

def limpiarConsola():    
    comando = 'clear'
    if os.name in ('nt', 'dos'):
        comando = 'cls'
    os.system(comando)

Menu()

