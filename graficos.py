import matplotlib.pyplot as plt


def armar_grafico_f1(filas, columnas, posicion, fechas, datos, formato, etiqueta_y):
    plt.subplot(filas, columnas, posicion)  # 1 fila, 2 columnas, posición 2
    plt.plot(fechas, datos, formato) # graficamos función y2
    plt.xlabel("Fecha")
    plt.ylabel(etiqueta_y)
    plt.xticks(fechas[::60])
    plt.grid(axis="y")


def armar_grafico_f2(filas, columnas, posicion, fechas, datos, pais1, pais2, etiqueta_y):
    plt.subplot(filas, columnas, posicion)  # 1 fila, 2 columnas, posición 2
    plt.plot(fechas, datos[0], 'b-', label=pais1)
    plt.plot(fechas, datos[1], 'r-.', label=pais2)
    plt.xlabel("Fecha")
    plt.ylabel(etiqueta_y)
    plt.legend()
    plt.xticks(fechas[::30], rotation=60)
    plt.grid(axis="y")


def armar_grafico_f3(df, paises):
    x = df["date"]
    for pais in paises:
        y = df["total_cases"].where(df['location'] == pais)
        plt.semilogy(x, y, label=pais) 
    plt.title("Curvas Logarítmicas por pais")
    plt.ylabel("Casos")
    plt.xlabel("Fecha")
    plt.legend()
    plt.xticks(x[::30], rotation=60)
    plt.grid(axis="y")
    plt.savefig("Logaritmicas_por_pais")


