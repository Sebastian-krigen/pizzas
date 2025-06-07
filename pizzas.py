import os

catalogo_pizzas = []
pedidos_realizados = []

while True:
    
    os.system('cls'  ,os.name == 'nt'  'clear')
    os.system('cls'  ,os.name == 'nt'  'clear')

    print("🍕 Sistema de Gestión de Pedidos de Pizzería 🍕")
    print("-" * 40)
    print("1. Registrar nueva pizza")
    print("2. Ver catálogo de pizzas")
    print("3. Realizar un pedido")
    print("4. Ver pedidos realizados")
    print("5. Salir del sistema")
    print("-" * 40)

    opcion_menu = 0
    while True:
        try:
            opcion_menu = int(input("Ingrese su opción: "))
            if 1 <= opcion_menu <= 5:
                break
            else:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
    if opcion_menu == 1:
        os.system('cls'  ,os.name == 'nt' , 'clear')
        print("--- Registrar Nueva Pizza ---")
        codigo = input("Ingrese el código de la pizza: ").strip().upper()
        
        codigo_duplicado = False
        for pizza in catalogo_pizzas:
            if pizza['codigo'] == codigo:
                print(f"Error: Ya existe una pizza con el código '{codigo}'.")
                codigo_duplicado = True
                break
        
        if not codigo_duplicado:
            nombre = input("Ingrese el nombre de la pizza: ").strip().capitalize()
            tipo_masa = input("Ingrese el tipo de masa (ej. delgada, gruesa): ").strip().capitalize()
            
            precio_unitario = 0.0
            while True:
                try:
                    precio_unitario = float(input("Ingrese el precio unitario de la pizza: "))
                    if precio_unitario <= 0:
                        print("El precio debe ser mayor que cero.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número para el precio.")

            stock_disponible = 0
            while True:
                try:
                    stock_disponible = int(input("Ingrese el stock disponible: "))
                    if stock_disponible < 0:
                        print("El stock no puede ser negativo.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para el stock.")

            nueva_pizza = {
                'codigo': codigo,
                'nombre': nombre,
                'tipo_masa': tipo_masa,
                'precio_unitario': precio_unitario,
                'stock_disponible': stock_disponible
            }
            catalogo_pizzas.append(nueva_pizza)
            print(f"\nPizza '{nombre}' registrada exitosamente.")
        
        input("Presione Enter para continuar...")
    elif opcion_menu == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Catálogo de Pizzas ---")
        if not catalogo_pizzas:
            print("El catálogo de pizzas está vacío.")
        else:
            for pizza in catalogo_pizzas:
                print(f"Código: {pizza['codigo']}")
                print(f"Nombre: {pizza['nombre']}")
                print(f"Tipo de Masa: {pizza['tipo_masa']}")
                print(f"Precio: ${pizza['precio_unitario']:.2f}")
                print(f"Stock: {pizza['stock_disponible']}")
                print("-" * 20)
        input("Presione Enter para continuar...")
    elif opcion_menu == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Realizar un Pedido ---")
        if not catalogo_pizzas:
            print("No hay pizzas disponibles en el catálogo para realizar un pedido.")
            input("Presione Enter para continuar...")
            continue

        nombre_cliente = input("Ingrese el nombre del cliente: ").strip().capitalize()
    
        print("\nCatálogo de Pizzas Disponibles:")
        for i, pizza in enumerate(catalogo_pizzas):
            print(f"{i+1}. {pizza['nombre']} (Código: {pizza['codigo']}) - ${pizza['precio_unitario']:.2f} - Stock: {pizza['stock_disponible']}")
        print("-" * 40)

        pizza_seleccionada = None
        while pizza_seleccionada is None:
            try:
                opcion_pizza = int(input("Ingrese el número de la pizza deseada: "))
                if 1 <= opcion_pizza <= len(catalogo_pizzas):
                    pizza_seleccionada = catalogo_pizzas[opcion_pizza - 1]
                else:
                    print("Opción de pizza inválida.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        
        if pizza_seleccionada['stock_disponible'] == 0:
            print(f"Lo sentimos, la pizza '{pizza_seleccionada['nombre']}' está agotada.")
            input("Presione Enter para continuar...")
            continue

        cantidad = 0
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad de '{pizza_seleccionada['nombre']}' a pedir: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                elif cantidad > pizza_seleccionada['stock_disponible']:
                    print(f"No hay suficiente stock. Stock disponible: {pizza_seleccionada['stock_disponible']}")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")

        total_pagar = pizza_seleccionada['precio_unitario'] * cantidad
        pizza_seleccionada['stock_disponible'] -= cantidad

        nuevo_pedido = {
            'cliente': nombre_cliente,
            'pizza': pizza_seleccionada['nombre'],
            'cantidad': cantidad,
            'total_pagado': total_pagar
        }
        pedidos_realizados.append(nuevo_pedido)
        print(f"\nPedido de '{pizza_seleccionada['nombre']}' para '{nombre_cliente}' registrado. Total a pagar: ${total_pagar:.2f}")
        input("Presione Enter para continuar...")

    elif opcion_menu == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Pedidos Realizados ---")
        if not pedidos_realizados:
            print("No hay pedidos realizados aún.")
        else:
            for i, pedido in enumerate(pedidos_realizados):
                print(f"Pedido #{i+1}")
                print(f"Cliente: {pedido['cliente']}")
                print(f"Pizza: {pedido['pizza']}")
                print(f"Cantidad: {pedido['cantidad']}")
                print(f"Total Pagado: ${pedido['total_pagado']:.2f}")
                print("-" * 20)
        input("Presione Enter para continuar...")
    elif opcion_menu == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("¡Gracias por usar el Sistema de Gestión de Pedidos de Pizzería! 🍕")
        print("¡Hasta pronto!")
        break