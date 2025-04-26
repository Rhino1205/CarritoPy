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
            finalizar_compra()

        elif option=="7":
            print("saliendo...")
            break
        else:
            print("Ingreso una opcion incorrecta, intentelo de nuevo.")

def ver_catalogo(registro):
    max_nombre = max(len(registro[producto]['nombre']) for producto in registro)
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
  print(shopping_cart)

def eliminar_producto(shopping_cart):
    codigo_a_eliminar = input("Ingrese el codigo del producto que desea eliminar: ").upper()
    del(shopping_cart[codigo_a_eliminar])
    

def vaciar_carrito(shopping_cart):
    shopping_cart.clear()

    print(shopping_cart)

def mostrar_carrito(shopping_cart):
    pass

def finalizar_compra():
    pass
print(tienda())