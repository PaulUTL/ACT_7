from .tienda import calcular_precio, calcular_iva

def main():
    print("Bienvenido a la tienda")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        descuento = float(input("Ingrese el porcentaje de descuento: "))
        subtotal = calcular_precio(precio, descuento)
        total = calcular_iva(subtotal)
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Total con IVA: {total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
