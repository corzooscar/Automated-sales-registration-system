from Funciones_Reg_Cal import registrar_venta
Lista_ventas = []

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
