def tienda():
    menu()

def menu():
    while True:
        print(""""
        BIENVENIDO(A) A LA TIENDA VIRTUAL
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
            ver_catalogo()
        elif option=="2":
            agregar_producto()
        elif option=="3":
            eliminar_producto()
        elif option=="4":
            vaciar_carrito()
        elif option=="5":
            mostrar_carrito()
        elif option=="6":
            finalizar_compra()

        elif option=="7":
            print("saliendo...")
            break
        else:
            print("Ingreso una opcion incorrecta, intentelo de nuevo.")

def ver_catalogo():
    pass

def agregar_producto():
    pass

def eliminar_producto():
    pass

def vaciar_carrito():
    pass

def mostrar_carrito():
    pass

def finalizar_compra():
    pass
print(menu())