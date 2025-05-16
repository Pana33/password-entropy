import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import string

colores = ["red","blue","black"]
passwords = []

def calcular_entropia(L, C):
    """Regresa los bits de la entropia segun F = L * log2(C)."""
    return L * math.log2(C)

def clasificar_caracteres(password):
    """Detecta qué tipos de caracteres contiene la contraseña para determinar C."""
    conjunto = set()

    if any(caracter.islower() for caracter in password):
        conjunto.update(string.ascii_lowercase)
    if any(caracter.isupper() for caracter in password):
        conjunto.update(string.ascii_uppercase)
    if any(caracter.isdigit() for caracter in password):
        conjunto.update(string.digits)
    if any(caracter in string.punctuation for caracter in password):
        conjunto.update(string.punctuation)
    return len(conjunto)

#Inicio del codigo, solicitando la contraseña a evaluar
def init():
    password = input("Introduce tu contraseña: ")
    longitud = len(password)
    caracteres = clasificar_caracteres(password)
    entropia = calcular_entropia(longitud, caracteres)

    print(f"\nLongitud (L): {longitud}")
    print(f"Complejidad (C): {caracteres} caracteres posibles")
    print(f"Entropía estimada: {entropia:.2f} bits")

#Evaluacion final segun la entropia recomendada
    if entropia > 75:
        print("Tu contraseña es extremadamente fuerte (entropía > 75 bits).")
    elif entropia > 60:
        print("Tu contraseña es muy fuerte fuerte (entropía > 60 bits).")
    else:
        print("Tu contraseña es débil (entropía <= 60 bits). Considera hacerla más larga o compleja.")
    #Se guarda la informacion con un maximo de 3 datos para visualizar en la grafica
    agregar_password_para_comparar(longitud=longitud,caracteres=caracteres,entropia=entropia)
    crear_grafico()

def crear_grafico():
    #Se define longitud de 1 a 24
    L_vals = np.arange(1, 25, 1)
    #Se definen caracteres de 1 a 95
    C_vals = np.arange(10, 100, 5)
    #Se configura la cuadricula de la imagen
    L_mesh, C_mesh = np.meshgrid(L_vals, C_vals)
    F_mesh = L_mesh * np.log2(C_mesh)

    #Se configura el tamaño, tipo de proyección y diseño de la imagen
    fig = plt.figure(figsize=(15, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(L_mesh, C_mesh, F_mesh, cmap='viridis')
    ax.view_init(elev=15, azim=280)
    puntos_de_comparacion(ax=ax)

    #Se configuran las etiquetas y el titulo de la imagen
    ax.set_xlabel('Longitud (L)')
    ax.set_ylabel('Complejidad (C)')
    ax.set_zlabel('Entropía (bits)')
    ax.set_title('Superficie de Entropía F(L, C)')

    #Se muestra el resultado
    plt.show()

def puntos_de_comparacion(ax):
    #se agregan puntos a la grafica para comparar los datos almacenados
    for index, password in enumerate(passwords):
        ax.scatter(password["longitud"]-2, password["caracteres"]+2, password["entropia"], color=colores[index], s=250, label=f"Contraseña {password["entropia"]:.2f} bits")
        ax.text(password["longitud"], password["caracteres"], password["entropia"], f'{password["entropia"]:.2f} bits',color=colores[index], fontsize=10)
        ax.legend()

def agregar_password_para_comparar(longitud,caracteres,entropia):
    if len(passwords) == 3:
        passwords.pop(0)
    password = {"longitud":longitud,"caracteres":caracteres,"entropia":entropia}
    passwords.append(password)

def combinaciones_seguras():
#Evaluacion de combinaciones seguras
    print("\nCombinaciones de longitud y caracteres con entropía mayor a 60:")
    for longitud in range(6, 21):
        print(f"Combinaciones con {longitud} caracteres")
        combinaciones_encontradas = 0
        for caracteres in [10, 26, 32, 36, 42, 52, 58, 62, 68, 84, 94]:
            entropia = calcular_entropia(longitud, caracteres)
            tipo_de_contrasena = ""
            if entropia > 75:
                tipo_de_contrasena = "Extremadamente fuerte"
            elif entropia > 60:
                tipo_de_contrasena = "Muy fuerte"
            if tipo_de_contrasena != "":
                combinaciones_encontradas += 1
                print(f"Caracteres = {caracteres} → entropia = {entropia:.2f} bits - Contraseña: {tipo_de_contrasena}")
        if combinaciones_encontradas == 0:
            print("No hay combinaciones seguras para esta longitud")

option = 1
while option != 3:
    try:
        print("Escribe el numero de la opcion que deseas realizar")
        print("1.- Comparar entropia de contraseñas")
        print("2.- Ver combinaciones de contraseñas seguras")
        print("3.- Salir del programa")
        option = int(input(""))
    except:
        option = 0
    if option == 1:
        init()
    elif option == 2:
        combinaciones_seguras()
    elif option == 3:
        print("Hasta luego!")