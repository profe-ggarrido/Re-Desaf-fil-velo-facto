precios = {'Notebook': 700000, 'Teclado': 25000, 'Mouse': 12000, 'Monitor': 250000, 'Escritorio': 135000, 'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral, modo=None):
    if modo == 'menor':
        filtro = [(k, v) for k, v in diccionario.items() if v <= umbral]
    elif modo == 'mayor':
        filtro = [(k, v) for k, v in diccionario.items() if v > umbral]
    else:
        filtro = [(k, v) for k, v in diccionario.items() if v > umbral]
    filtro.sort(key=lambda x: x[1])
    return filtro

def formatear_salida(resultado):
    salida = []
    for clave, valor in resultado:
        valor_formateado = "${:,.0f}".format(valor)
        salida.append(f"{clave}: {valor_formateado}")
    return salida

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python filtro.py <umbral> [<menor|mayor>]")
        sys.exit(1)
    umbral = int(sys.argv[1])
    modo = sys.argv[2] if len(sys.argv) > 2 else None
    if modo and modo != 'menor' and modo != 'mayor':
        print("El modo debe ser 'menor' o 'mayor'")
        sys.exit(1)
    print("\033[42m*********************************************************************\033[0m")
    if modo == 'menor':
        print(f"elementos cuyo precio es \033[1migual o menor al umbral de ${umbral:,.0f}\033[0m")
    elif modo == 'mayor':
        print(f"elementos cuyo precio es MAYOR al umbral de ${umbral:,.0f}")
    else:
        print(f"elementos cuyo precio es MAYOR al umbral de ${umbral:,.0f}")
    resultado = filtrar(precios, umbral, modo)
    salida_formateada = formatear_salida(resultado)
    print("\n".join(salida_formateada))
    print("\033[41m*********************************************************************\033[0m")