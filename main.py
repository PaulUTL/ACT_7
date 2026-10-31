from tienda import calcular_iva, calcular_precio


def main():
    precio = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))

    try:
        precio_con_descuento = calcular_precio(precio, descuento)
        precio_final = calcular_iva(precio_con_descuento)

        print(f"Precio con descuento: {precio_con_descuento:.2f}")
        print(f"Precio final con IVA: {precio_final:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()