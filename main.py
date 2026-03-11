from Funciones_Reg_Cal_Tot import registrar_venta, mostrar_total, mostrar_resumen

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
  
mostrar_resumen(Lista_ventas)
print(mostrar_total(Lista_ventas))
print("="*60)
print("~ Gracias por utilizar el programa de registro de ventas ʕ•́ᴥ•̀ʔっ")
