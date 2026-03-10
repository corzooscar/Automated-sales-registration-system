# Automated-sales-registration-system



Lista_ventas = []

def registrar_venta():
    print("="*60)
    Producto = input("Ingrese el producto que desea comprar: ")
    Precio = float(input("Ingrese el precio del producto: "))
    Cantidad = int(input("Ingrese la cantidad de productos que desea comprar: "))
    Total = Precio * Cantidad
    return {"Producto": Producto, "Precio": Precio, "Cantidad": Cantidad, "Total": Total}

Deseo = input("Desea registrar una venta? s/n: ").lower()
while Deseo == "s": 
    venta = registrar_venta()
    Lista_ventas.append(venta)
    print(f"""{"="*60}
Producto: {Lista_ventas[-1]['Producto']} 
Precio: {Lista_ventas[-1]['Precio']}
Cantidad: {Lista_ventas[-1]['Cantidad']} 
SubTotal: {Lista_ventas[-1]['Total']}
""")
    Deseo = input("Desea registrar otra venta? s/n: ").lower()

print("\n")
print("-"*60)
print("RESUMEN DE VENTAS DEL DÍA")
print("-"*60)
for venta in Lista_ventas:
    print(f"""El total a pagar por {venta['Cantidad']} {venta['Producto']}(s) es: ${venta['Total']:.2f}
""")
print
print("Gracias por utilizar el programa de registro de ventas.")
