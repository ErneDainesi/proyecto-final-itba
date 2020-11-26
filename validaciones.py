def pedir_fecha(fechas, mensaje):
    fecha = input(mensaje)
    while fecha not in fechas:
        print("Fecha invalida")
        print("Recuerde formato aaaa-mm-dd")
        fecha = input("Insertar fecha nuevamente: ")
    return fecha


def input_pais(df1):
    """"Funcion que permite al usuario ingresar el pais con el que desea trabajar y devuelve la variable pais"""
    pais = input("Pais que desea analizar: ")
    all_paises = df1["location"].tolist()
    while pais not in all_paises:
        print("Pais inexistente")
        pais = input("Pais que desea analizar: ")
    return pais


def pedir_opcion():
    opcion_elegida = int(
        input("Ingrese la opcion que desee realizar (1, 2 o 3): "))
    while opcion_elegida < 1 or opcion_elegida > 3:  #Validar opcion ingresada esta dentro de rango
        opcion_elegida = int(
            input(
                "Error, vuelva a ingresar la opcion que desee realizar (1, 2 o 3): "
            ))
    return opcion_elegida
