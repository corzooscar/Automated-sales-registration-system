#Funciones para el registro de ventas

def registrar_venta():
    print("="*60)
    Producto = input("Ingrese el producto que desea comprar: ")
    Precio = float(input("Ingrese el precio del producto: "))
    Cantidad = int(input("Ingrese la cantidad de productos que desea comprar: "))
    Total = Precio * Cantidad
    return {"Producto": Producto, "Precio": Precio, "Cantidad": Cantidad, "Total": Total}

#Funcion para mostrar el total a pagar por cada venta registrada
