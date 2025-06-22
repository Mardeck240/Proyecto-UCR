import pickle

control_inventario= []
registro_ventas=[]
clientes= []
costos_producción= []
cliente=[]
cli=[]
menu= -1
columnas = ["", "", "", "", "", "", ""]
productos = {}
ventas = {}

try:
    with open("ventas.pkl", "rb") as file2:
        ventas = pickle.load(file2)
        print(ventas)
except:
    pass


try:
    with open("productos.pkl", "rb") as file:
        productos = pickle.load(file)
        print(productos)
except:
    pass


try:
    with open("inventario.txt", "r") as file:
        for text in file:
            control_inventario.append(text.strip())
        print(control_inventario)
except:
    pass

try: 
    with open ("ventas.txt", "r") as file: 
        for texr in file: 
            registro_ventas.append(texr.strip()) 
        print (registro_ventas)
except:
    pass 


def err():
    print("Lo que digitó no se encuentra dentro de las opciones, intente otra vez")

def trabajando():
    print("Esta función aun no está finalizada. Por favor, escoja otra.")

def des():
    try:
        return int(input("¿Qué desea hacer? (1) Agregar otro producto (0) Regresar: "))
    except:
        print("Carácter o símbolo inválido, intente nuevamente")
        return des()

def menuu():
    return int(input("¿Qué desea hacer? \n(1) Control del inventario\n(2) Registro de ventas\n(3) Clientes y proveedores\n(4) Costos de producción y venta\n(0) Salir: "))

def regresar():
    try:
        return int(input("(0) Regresar: "))
    except:
        print("Carácter o símbolo inválido, intente nuevamente")
        return regresar()

def calculo_costo_prod(mode = 0):
    global columnas
    columnas = ["", "", "", "", "", "", ""]
    producto_cambio = ""
    if mode != 0 and len(productos) > 0:
        for i in productos.keys():
            mode -= 1
            if mode == 0:
                mode -= 1
                producto_cambio = i


    try:
        print(columnas)
        nombre_prod = input("Digite el nombre del producto: ")
        columnas[0] = nombre_prod
        print(columnas)
        cant_prod = float(input("Digite la cantidad del producto: "))
        columnas[1] = cant_prod
        print(columnas)
        precio_prod = float(input("Digite el precio del producto: "))
        columnas[2] = precio_prod
        print(columnas)
        medida1 = int(input("Digite la medida que desea utilizar\n1. Kg/L\n2. g/ml\n"))
        if medida1 >= 2:
            columnas[3] = "g/ml"
        else:
            columnas[3] = "Kg/L"
        print(columnas)
        cant_utilizar = float(input("Digite la cantidad que va a utilizar: "))
        columnas[4] = cant_utilizar
        print(columnas)
        medida2 = int(input("Digite la medida que desea utilizar para trabajar\n1. Kg/L\n2. g/ml\n"))
        if medida2 >= 2:
            columnas[5] = "g/ml"
        else:
            columnas[5] = "Kg/L"
        
        variable_temp_division = precio_prod / cant_prod
        if medida1 != medida2:
            if medida1 < medida2:
                costo_final = variable_temp_division * (cant_utilizar * 0.001)
                columnas[6] = costo_final
               
                if medida1 > medida2:
                   costo_final = variable_temp_division * (cant_utilizar * 1000)
                   columnas[6] = costo_final
        elif medida1 == medida2:
            costo_final = variable_temp_division * cant_utilizar
            columnas[6] = costo_final
        print(columnas)
        print(f"El costo final de este producto es: {costo_final}")
        if mode != 0:
            del productos[producto_cambio]
        
        productos[columnas[0]] = columnas[6]
            
        print(f"Producto guardado correctamente\n{productos}")
        columnas = ["", "", "", "", "", "", ""]
    except:
        print("Ops... Algo salio mal, intentelo nuevamente")



print("¡Bienvenido a nuestro programa!")

while menu != 0:
    try:
        menu = menuu()
    except:
        print("Carácter o símbolo inválido, intente nuevamente")
        continue

    while menu == 1:
        try:
            menu_interno = int(input("¿Qué desea hacer?\n(1) Agregar producto\n(2) Ver productos\n(3) Eliminar productos\n(0) Retroceder\n"))
        except:
            print("Carácter o símbolo inválido, intente nuevamente")
            continue

        if menu_interno == 1:
            repetir = True
            while repetir:
                producto = input("Escriba el nombre del producto que desea agregar al inventario de la empresa: ")
                if producto != "":
                    control_inventario.append(producto)
                decision = des()
                if decision != 1:
                    repetir = False

        elif menu_interno == 2:
            print(control_inventario)
            print("Hay", len(control_inventario), "producto(s) en el inventario de la empresa")
            regresar()

        elif menu_interno == 3:
            if len(control_inventario) > 0:
                for i in range(len(control_inventario)):
                    print(f"{i+1}. {control_inventario[i]}")
            else:
                print("No hay ningún elemento en la lista!")
                continue

            while True:
                try:
                    producto_elim = int(input("Digite el número del producto que desea eliminar: "))
                    control_inventario.pop(producto_elim - 1)
                    print(control_inventario)
                    break
                except:
                    print("Carácter o símbolo inválido, intente nuevamente")

        elif menu_interno == 0:
            with open("inventario.txt", "w") as file:
                for text in control_inventario:
                    file.write(text + "\n")
            menu = -1
            break
        else:
            err()

    while menu == 2:
        try:
            print("Menú de Registro de Ventas")
            print("(1) Agregar una venta realizada\n(2) Ver registro de ventas\n(3) Eliminar una venta\n(0) Retroceder ")
        
            menu_registro_ventas = int(input("Seleccione una opción: "))
        except:
            print("Carácter o símbolo inválido, intente nuevamente")
            continue

        if menu_registro_ventas == 1:
            try:
                if len(cliente)>0:
                    fecha = input("Escriba la fecha exacta en formato (día.mes.año) en que se realizó la venta: ")
                    print("Productos registrados:")
                    for i in range(len(control_inventario)):
                        print(f"{i + 1}. {control_inventario[i]}")
                        
                        prod = input("Escriba el nombre del producto que vendió: ")
                        uni = int(input("¿Cuántas unidades de este producto vendió?: "))
                        prec = int(input("Digite el valor del producto vendido: "))
                        
                        print("Clientes registrados:")
                        for i, c in enumerate(cliente, 1):
                            print(f"\n{i}. {c[0]}")
                        cli_ente= int(input("Digite el número del cliente al que se le realizó la venta"))
                        
                        if 1<= cli_ente <= len(cliente):
                            nombre_cliente = cliente[cli_ente - 1][0]  # aqui extraemos solo el nombre
                            venta_total = uni * prec
                            venta = ("Fecha:", fecha, "Cliente:", nombre_cliente, "Producto", prod, "Unidades vendidas", uni, "Monto total", venta_total)
                            registro_ventas.append(venta)
                            print("La venta se registró correctamente!")
                        else: 
                            print("Número de cliente inválido")
                    
                else:
                    print("No hay clientes registrados. Por favor registre el cliente antes de registrar la venta")
                regresar()
            except:
                print("La venta no se registró, intente de nuevo.")

        elif menu_registro_ventas == 2:
            if registro_ventas:
                for i, v in enumerate(registro_ventas, 1):
                    print(f"{i}. {v}")
            else:
                print("No hay ventas registradas.")
            while True:
                try:
                    opcion = int(input("Digite (0) para regresar: "))
                    if opcion == 0:
                        break
                    else:
                        print("Error, digite 0 para regresar.")
                except:
                    print("Carácter inválido o símbolo inválido, intente nuevamente.")

        elif menu_registro_ventas == 3:
            if registro_ventas:
                for i, v in enumerate(registro_ventas, 1):
                    print(f"{i}. {v}")
                try:
                    num = int(input("Digite el número de la venta que desea eliminar: "))
                    if 1 <= num <= len(registro_ventas):
                        registro_ventas.pop(num - 1)
                        print("Venta eliminada correctamente.")
                    else:
                        print("El número que escogió no es válido.")
                except:
                    print ("Ocurrió un error")
            else:
                print("No hay ventas registradas.")
            while True:
                try:
                    opcion = int(input("Digite (0) para regresar: "))
                    if opcion == 0:
                        break
                    else:
                        print("Opción no válida, digite 0 para regresar.")
                except:
                    print("Carácter inválido o símbolo inválido, intente nuevamente.")

        elif menu_registro_ventas == 0:
            menu = 1
            break
    
    while menu == 3:
        try:
            menu_clientesprovedores = int(input("¿Qué desea hacer?\n(1) Apartado de clientes\n(2) Apartado de provedores\n(0) Retroceder\n"))
        except:
            print("Carácter o símbolo inválido, intente nuevamente")
            continue

        if menu_clientesprovedores == 1:
            while True:
                try:
                    menu_clientes = int(input("----Menú clientes----\n¿Qué desea hacer?\n(1) Agregar un cliente nuevo\n(2) Ver clientes registrados\n(3) Eliminar un cliente registrado en el sistema\n(0) Retroceder "))
                except:
                    print("Carácter o símbolo inválido, intente nuevamente")
                    continue
                    
                if menu_clientes ==1:
                    try:
                        print("----Agregar nuevo cliente----")
                        nombre_cliente= input("¿Cómo se llama el cliente (incluya nombre y apellidos)?")
                        id_cliente= input("¿Digite el número de identidad del cliente")
                        fecha_cliente= input("¿Digite la fecha de nacimiento del cliente en formato (día.mes.año)")
                        telefono= int(input("Digite el número telefónico del cliente"))
                        correo= input("Escriba el correo electónico del cliente")
                        direccion= input("Escriba la dirección de residencia del cliente")
                        cliente.append([nombre_cliente, id_cliente, fecha_cliente, telefono, correo, direccion])
                        cli.append(nombre_cliente)
                        print("El cliente se registró!.")
                        regresar()
                    except:
                        print("El cliente no se registró, intente de nuevo.") 
                        
                elif menu_clientes ==2:
                    if len(cliente)>0:
                        for i, c in enumerate(cliente, 1):
                            print(f"\n{i}. {c}")
                    else:
                        print("No hay clientes registrados.")
                    regresar()
                    
                elif menu_clientes == 3:
                    if len(cliente) > 0:
                        for i, c in enumerate(cliente, 1):
                            print(f"\n{i}. {c}")
                        try:
                            borrar = int(input("Digite el número del cliente que desea borrar: "))
                            if 1 <= borrar <= len(cliente):
                                del cliente[borrar - 1]
                                print("Cliente borrado correctamente.")
                            else:
                                print("Número inválido.")
                        except ValueError:
                            print("Debe ingresar un número válido.")
                    else:
                        print("No hay clientes registrados.")
                    regresar()
                    
                    
        elif menu_clientesprovedores ==0:
            menu= 1
            break
            
        else: 
            err()
                    

    while menu == 4:
        try:
            print("---Menu costos de produccion y de ventas---")
            menu_costosprodvent = int(input("¿Qué desea hacer?\n(1) Costos de producción\n(2) Costos de venta\n(0) Retroceder\n"))
        except:
            print("Carácter o símbolo inválido, intente nuevamente")
            continue
        
        if menu_costosprodvent == 1:
            while True:
                print("---Menu costos de producción---")
                try:
                    submenuCP = int(input("Seleccione una opción\n(1) Nuevo producto\n(2) Configurar producto\n(3) Eliminar producto\n(4) Ver productos\n(0) Retroceder\n"))
                except:
                    print("Carácter o símbolo inválido, intente nuevamente")
                    continue
                
                if submenuCP == 1:
                    calculo_costo_prod(0)
                        
                
                elif submenuCP == 2:
                    if len(productos) > 0:
                        numero_temp = 0
                        for prod in productos.keys():
                            numero_temp += 1
                            print(f"{numero_temp}. {prod}")
                        
                        product = int(input("Seleccione el producto que desea cambiar (si desea volver, pulse 0): "))
                        if product != 0:
                            calculo_costo_prod(product)
                    else:
                        print("No hay productos!!")
                
                elif submenuCP == 3:
                    if len(productos) > 0:
                        numero_temp = 0
                        for prod in productos.keys():
                            numero_temp += 1
                            print(f"{numero_temp}. {prod}")
                        
                        product_elim = int(input("Seleccione el producto que desea eliminar (para cancelar, oprima 0): "))
                        if product_elim != 0:
                            for elim in productos.keys():
                                product_elim -= 1
                                if product_elim == 0:
                                    variable_temp = elim
                            
                            del productos[variable_temp] # No se puede meter dentro del for, dara error
                            print(f"Producto eliminado correctamente\n{productos}")
                            
                            
                    else:
                        print("No hay productos!!")
                
                elif submenuCP == 4:
                    if len(productos) > 0:
                        
                        print ("Los producto se dividen por Nombre | Costo final")
                        
                        print(productos)
                            

                        
                        regresar()
                    else:
                        print("No hay productos!!")
                    

                elif submenuCP == 0:
                    if len(productos) > 0:
                        with open("productos.pkl", "wb") as file:
                            pickle.dump(productos, file)
                    menu = 4
                    break
                    
        if menu_costosprodvent == 2:
            while True:
                print("---Menu costos de venta---")
                try:
                    submenuCV = int(input("Seleccione una opción\n(1) Nuevo producto\n(2) Eliminar producto\n(3) Ver productos\n(0) Retroceder\n"))
                except:
                    print("Carácter o símbolo inválido, intente nuevamente")
                    continue
                
                if submenuCV == 1:
                    prod_selec = -1
                    another_columns = ["", "", ""]
                    if len(productos) > 0:
                        nombre_product = input("Digite el nombre de producto a registrar: ")
                        another_columns[0] = nombre_product
                        products_selected = []
                        numero_temp = 0
                        for venta in productos.keys():
                            numero_temp += 1
                            print(f"{numero_temp}. {venta}")

                        while True:
                            while prod_selec != 0:
                                prod_selec = int(input("Seleccione los ingredientes que se uso para este producto (si desea terminar, seleccione 0): "))
                            
                                
                                if 0 > prod_selec or prod_selec > len(productos):
                                    print("Fuera de rango, intente nuevamente")
                            
                                elif prod_selec != 0:
                                    for i in productos.keys():
                                        prod_selec -= 1
                                        if prod_selec == 0:
                                            products_selected.append(i)
                                            prod_selec -= 1

                            ("Finalizado!")
                            print(another_columns)
                            break
                        
                    else:
                        print("No hay productos!!")
                        break
                    
                    if len(products_selected) > 0:
                        suma_total = 0
                        for sum in products_selected:
                            suma_total += productos[sum]
                        
                        another_columns[1] = suma_total
                        print(another_columns)

                        porcentaje = int(input("Digite el porcentaje de ganancia (digitelo como numero entero, ej: 12 = 12%): "))
                        if porcentaje > 100:
                            porcentaje = 100
                        elif porcentaje < 0:
                            porcentaje = 0
                        another_columns[2] = suma_total * (1 + (porcentaje / 100))
                        print(another_columns)

                        ventas[another_columns[0]] = another_columns[2]
                    
                    else:
                        print("No se encontraron los ingredientes")
                        break
                
                if submenuCV == 2:
                    numero_temp = 0
                    for venta in ventas.keys():
                        numero_temp += 1
                        print(f"{numero_temp}. {venta}")
                    
                    elim = int(input("Digite el producto que desea eliminar (presione 0 para cancelar): "))
                    if elim != 0 and elim <= len(ventas):
                        for eliminate in ventas.keys():
                            elim -= 1
                            if elim == 0:
                                variable_temp = eliminate
                        del ventas[variable_temp] # No se puede meter dentro del for, dara error
                        print(f"Producto eliminado correctamente\n{ventas}")
                    
                    else:
                        print("Producto no encontrado")
                    
                if submenuCV == 3:
                    if len(ventas) > 0:
                        
                        print ("Los producto se dividen por Nombre | Costo de venta")
                        
                        print(ventas)
                            

                        
                        regresar()
                    else:
                        print("No hay productos!!")

                if submenuCV == 0:
                    if len(ventas) > 0:
                        with open("ventas.pkl", "wb") as file2:
                            pickle.dump(ventas, file2)
                    menu = 4
                    break
        


        elif menu_costosprodvent == 0:
            menu = 1
            break

    if menu < 0 or menu > 4:
        err()