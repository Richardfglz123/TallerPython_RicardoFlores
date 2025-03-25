if __name__ == "__main__":
    def main():
        def agregar_producto(inventario):
            nombre = input("Ingresa el nombre del producto: ").strip().lower()
            cantidad = int(input("Ingresa la cantidad: "))
            for producto in inventario:
                if producto[0] == nombre:
                    producto[1] += cantidad
                    print("✅ Producto actualizado")
                    return
            inventario.append([nombre, cantidad])
            print("✅ Producto agregado.")

        def mostrar_inventario(inventario):
            print("El inventario actual es: ")
            if not inventario:
                print("No hay existencias")
            else:
                for producto in inventario:
                    print(f"{producto[0].capitalize()} - Cantidad: {producto[1]}")

        def vender_producto(inventario):
            nombre = input("Ingresa el nombre del producto a registrar y  vneder: ").strip().lower()
            for producto in inventario:
                if producto[0] == nombre:
                    cantidad = int(input(f"Ingresa la cantidad a vender (Disponible: {producto[1]}): "))
                    if cantidad <= producto[1]:
                        producto[1] -= cantidad
                        print("Producto vendido")
                        if producto[1] == 0:
                            inventario.remove(producto)
                            print("Se agotó el producto y fue eliminado")
                        return
                    else:
                        print("No hay suficiente stock para realizar la venta")
                        return
            print("Producto no existente")

        def menu():
            inventario = []
            while True:
                print("\nMenú de opciones:")
                print("1. Agregar producto")
                print("2. Mostrar inventario")
                print("3. Vender producto")
                print("4. Salir")
                opcion = input("Selecciona una opción: ")

                if opcion == "1":
                    agregar_producto(inventario)
                elif opcion == "2":
                    mostrar_inventario(inventario)
                elif opcion == "3":
                    vender_producto(inventario)
                elif opcion == "4":
                    print("Bye")
                    break
                else:
                    print("Opción no valida")

        print("Bienvenide al sistema de inventario ")
        menu()
    main()
