from Funciones_Reg_Cal_Tot import registrar_venta

Lista_ventas = []

print(f"""╔═══════════════════════════════════════════════════════════╗
                🏦 SALES REGISTRATION SYSTEM 🏦
╚═══════════════════════════════════════════════════════════╝""")
Deseo = input("~ Desea registrar una venta? s/n: ").lower()
while Deseo == "s": 
    venta = registrar_venta()
    Lista_ventas.append(venta)
    print(f"""{"-"*60} 
 ~ SubTotal: ${Lista_ventas[-1]['Total']} | Producto: {Lista_ventas[-1]['Producto']} 
{"="*60}
""")
    Deseo = input("~ Desea registrar otra venta? s/n: ").lower()

print(f"""{"="*60}
{"RESUMEN DE VENTAS DEL DÍA".center(60) }
{"="*60}""")
for venta in Lista_ventas:
    print(f"""— Producto: {venta['Producto']} 
  Precio U: ${venta['Precio']:.2f}        
  Cantidad: {venta['Cantidad']}  
  Subtotal: ${venta['Total']:.2f}
  -------------------------------""")
print(f"— Total Recaudado: ${sum(venta['Total'] for venta in Lista_ventas):.2f}")
print("="*60)
print("~ Gracias por utilizar el programa de registro de ventas ʕ•́ᴥ•̀ʔっ")
