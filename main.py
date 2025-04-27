import datetime


def tienda():
    print("      BIENVENIDO(A) A LA TIENDA VIRTUAL")
    catalogo = {
    "A001": {"nombre": "Camiseta Deportiva", "precio": 19.99},
    "A002": {"nombre": "Auriculares Bluetooth", "precio": 49.99},
    "A003": {"nombre": "Zapatillas Running", "precio": 69.99},
    "A004": {"nombre": "Mochila Deportiva", "precio": 39.99},
    "A005": {"nombre": "Smartphone X500", "precio": 499.99},
    "A006": {"nombre": "Reloj Inteligente", "precio": 99.99},
    "A007": {"nombre": "Taza de Cerámica", "precio": 9.99},
    "A008": {"nombre": "Lámpara LED", "precio": 29.99}
}
    carrito = {}

    menu(catalogo,carrito)

def menu(registro,shopping_cart):
    while True:
        print("""
        1. Ver catálogo
        2. Agregar producto al carrito
        3. Eliminar producto del carrito
        4. Vaciar carrito
        5. Mostrar carrito
        6. Finalizar compra
        7. Salir
        """)
        option=input("Ingrese una opcion: ")

        if option=="1":
            ver_catalogo(registro)
        elif option=="2":
            agregar_producto(registro,shopping_cart)
        elif option=="3":
            eliminar_producto(shopping_cart)
        elif option=="4":
            vaciar_carrito(shopping_cart)
        elif option=="5":
            mostrar_carrito(shopping_cart)
        elif option=="6":
            finalizar_compra(shopping_cart)

        elif option=="7":
            print("Hasta pronto")
            break
        else:
            print("Ingreso una opcion incorrecta, intentelo de nuevo.")

def ver_catalogo(registro):
    max_nombre = max(len(registro[producto]['nombre']) for producto in registro)
    print("Catalogo de productos:")
    for producto in registro:
        nombre = registro[producto]['nombre']
        precio = registro[producto]['precio']
        espacios = max_nombre-len(nombre)
        print(f" {producto} | {nombre}{" "*espacios} | {precio}")
    

def agregar_producto(registro,shopping_cart):
   print("""
    Ingrese el numero de operaciones que desea realizar.
    Si durante el proceso cambia de opinion sobre la cantidad
    de operaciones ingrese la letra m para agregar hasta la 
    ultima operacion añadida y luego salir al menu
    """)
   while True:
    try:
        numero_operaciones = int(input("Numero de operaciones: "))
        if numero_operaciones<0:
           print("Ingrese un numero mayor a cero")
        else:
           break

    except ValueError as e:
      print(f"Ingrese un numero valido, error: {e}")
      

   for i in range(numero_operaciones):
    codigo = input(f"Ingrese el codigo de producto {i + 1}: ").upper()
    if codigo == "M":
      return
    
    while codigo not in registro:
      print("El codigo que ingreso no es correcto, intentelo nuevamente")
      codigo = input(f"Ingrese el codigo de producto {i + 1}: ").upper()

    while codigo in shopping_cart:
      print("""
            El producto ya se encuentra en el carrito
            Si desea modificar la cantidad, primero salga
            al menu, escoja la opcion eliminar producto
            y luego agreguelo nuevamente:)
      """)
      codigo = input(f"Ingrese el codigo de producto {i + 1}: ").upper()

    cantidad=int(input("Ingresa cantidad: "))
    
    while cantidad <=0:
      print("Ingreso una cantidad invalida, intentelo nuevamente")
      cantidad=int(input("Ingresa cantidad: "))
  
    shopping_cart[codigo]={"nombre":registro[codigo]["nombre"] , "precio":registro[codigo]["precio"] , "cantidad":cantidad}
    print("Producto agregado al carrito") 

def eliminar_producto(shopping_cart):
    codigo_a_eliminar = input("Ingrese el codigo del producto que desea eliminar: ").upper()
    
    while codigo_a_eliminar not in shopping_cart:
        print("""
              si se trato de un error ingrese la tecla m para volver al menu,
              si no es un error ingrese un codigo valido del producto que desea eliminar
               """)
        codigo_a_eliminar = input("Ingrese el codigo del producto que desea eliminar: ").upper()
        if codigo_a_eliminar == "M":
            return
    del(shopping_cart[codigo_a_eliminar])
    

def vaciar_carrito(shopping_cart):
    shopping_cart.clear()

def mostrar_carrito(shopping_cart):
    print("Tu carrito: ")

    max_nombre = max(len(shopping_cart[producto]['nombre']) for producto in shopping_cart)
    for producto in shopping_cart:
        nombre = shopping_cart[producto]['nombre']
        precio = float(shopping_cart[producto]['precio'])
        cantidad = int(shopping_cart[producto]['cantidad'])
        total_por_producto = round(precio*cantidad,2)
        espacios = max_nombre - len(nombre)
        print(f"  - {nombre}{" "*espacios} (x{cantidad}) -> {total_por_producto}")

def finalizar_compra(shopping_cart):
    print("Resumen de compra: ")
    max_nombre = max(len(shopping_cart[producto]['nombre']) for producto in shopping_cart)
    precio_total = 0
    for producto in shopping_cart:
        nombre = shopping_cart[producto]['nombre']
        precio = float(shopping_cart[producto]['precio'])
        cantidad = int(shopping_cart[producto]['cantidad'])
        total_por_producto = round(precio*cantidad,2)
        espacios = max_nombre - len(nombre)
        print(f" {nombre}{" "*espacios} (x{cantidad}) -> {total_por_producto}")
        precio_total += total_por_producto
    
    print(f"Total a pagar {precio_total}")
    guardar_historial_compras_txt(shopping_cart, precio_total)

def guardar_historial_compras_txt(shopping_cart, precio_total):
    
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_archivo = "historial_compras.txt"

    with open(nombre_archivo, mode='a') as archivo:
        archivo.write(f"Fecha: {fecha_actual}\n")
        archivo.write(f"Productos comprados:\n")
        
        for producto in shopping_cart:
            nombre = shopping_cart[producto]["nombre"]
            cantidad = shopping_cart[producto]["cantidad"]
            precio = shopping_cart[producto]["precio"]
            total_producto = round(precio * cantidad, 2)
            archivo.write(f"  - {nombre} (x{cantidad}) -> {total_producto}\n")
        
        archivo.write(f"Total de la compra: {precio_total}\n")
        archivo.write("-" * 40 + "\n")

    print("Historial de compra guardado exitosamente.")



print(tienda())