

seguir = "S"

while seguir == "S":

    # Contadores
    pikachu = 0
    otaku = 0
    pulpo = 0
    anguila = 0

    subtotal = 0
    descuento = 0
    total = 0

    opcion = 0

    # MENÚ DE PEDIDOS

    while opcion != 5:

        print("\n==================== MENU SUSHI ====================")
        print("1. Pikachu Roll $4500")
        print("2. Otaku Roll $5000")
        print("3. Pulpo Venenoso Roll $5200")
        print("4. Anguila Eléctrica Roll $4800")
        print("5. Terminar pedido")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            pikachu = pikachu + 1
            subtotal = subtotal + 4500
            print("Pikachu Roll agregado")

        elif opcion == 2:
            otaku = otaku + 1
            subtotal = subtotal + 5000
            print("Otaku Roll agregado")

        elif opcion == 3:
            pulpo = pulpo + 1
            subtotal = subtotal + 5200
            print("Pulpo Venenoso Roll agregado")

        elif opcion == 4:
            anguila = anguila + 1
            subtotal = subtotal + 4800
            print("Anguila Eléctrica Roll agregado")

        elif opcion == 5:
            print("Pedido finalizado")

        else:
            print("Opción no válida")

    # CÓDIGO DE DESCUENTO    

    codigo = input("\nIngrese código de descuento o X para continuar: ")

    while codigo != "soyotaku" and codigo != "X":

        print("Código no válido")
        codigo = input("Ingrese código nuevamente o X para continuar: ")

    if codigo == "soyotaku":
        descuento = subtotal * 0.10

    total = subtotal - descuento

    # DETALLE DEL PEDIDO

    total_productos = pikachu + otaku + pulpo + anguila

    print("\n==============================")
    print("TOTAL PRODUCTOS:", total_productos)
    print("==============================")

    print("Pikachu Roll :", pikachu)
    print("Otaku Roll :", otaku)
    print("Pulpo Venenoso Roll :", pulpo)
    print("Anguila Eléctrica Roll :", anguila)

    print("==============================")
    print("Subtotal por pagar: $", subtotal)
    print("Descuento por código: $", int(descuento))
    print("TOTAL: $", int(total))


    # NUEVO PEDIDO

    seguir = input("\n¿Desea realizar otro pedido? (S/N): ").upper()

print("Programa terminado")