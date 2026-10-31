
def calcular_total(precio, descuento):
    resultado = precio - (precio * (descuento / 100))
    #temporal = 500
    return resultado

def obtener_categoria(precio):
    if precio < 100:
        return "Bajo"
    elif 100 <= precio < 500:
        return "Medio"
    else:
        return "Alto"