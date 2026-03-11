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
