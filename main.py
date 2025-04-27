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
  
  codigo = input("Ingrese codigo de producto: ").upper()
  while codigo not in registro:
    print("El codigo que ingreso no es correcto, intentelo nuevamente")
    codigo = input("Ingrese codigo de producto: ").upper()

  while codigo in shopping_cart:
    print("""
          El producto ya se encuentra en el carrito
          Si desea modificar la cantidad, primero elimine el producto
          y luego agreguelo nuevamente:)
    """)
    return
    

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


print(tienda())