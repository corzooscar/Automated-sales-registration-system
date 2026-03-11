#Funciones para el registro de ventas
conteo = 0

def registrar_venta():
    global conteo
    conteo += 1
    print(f"\n========================Producto #{conteo}=========================")
    Producto = input("~ Nombre del producto: ")
    Precio = float(input("~ Precio Unitario: $"))
    Cantidad = int(input("~ Cantidad vendida: "))
    Total = Precio * Cantidad
    return {"Producto": Producto, "Precio": Precio, "Cantidad": Cantidad, "Total": Total}


#Funcion para mostrar el total a pagar por cada venta registrada
def mostrar_total(Lista_ventas):
    Total_venta = sum(venta['Total'] for venta in Lista_ventas)
    return f"— Total Recaudado: ${Total_venta:.2f}"

#Función para mostrar el resumen de ventas del día
def mostrar_resumen(Lista_ventas):
    print(f"""{"="*60}
{"RESUMEN DE VENTAS DEL DÍA".center(60) }
{"="*60}""")
    for venta in Lista_ventas:
        print(f"""— Producto: {venta['Producto']} 
  Precio U: ${venta['Precio']:.2f}        
  Cantidad: {venta['Cantidad']}  
  Subtotal: ${venta['Total']:.2f}
  -------------------------------""")
