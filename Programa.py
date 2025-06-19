control_inventario= []
registro_ventas=[]
clientes= []
costos_producción= []
cliente=[]
cli=[]
menu= -1
categorias = {"Mano de obra" : {"Cascara" : 500, "Chocolate" : 20}}

print(categorias["Mano de obra"]["Chocolate"])




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
                productos = input("Escriba el nombre del producto que desea agregar al inventario de la empresa: ")
                if productos != "":
                    control_inventario.append(productos)
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
            menu_costosprod = int(input("¿Qué desea hacer?\n(1) Costos de producción\n(2) Costos de venta\n(0) Retroceder\n"))
        except:
            print("Carácter o símbolo inválido, intente nuevamente")
            continue
        
        if menu_costosprod == 1:
            while True:
                print("---Menu costos de producción---")
                try:
                    submenuCP = int(input("¿Qué desea hacer?\n(1) Agregar producto\n(2) Agregar categoria\n(3)Eliminar categoria\n(4) Ver categorias\n(0) Retroceder\n"))
                except:
                    print("Carácter o símbolo inválido, intente nuevamente")
                    continue
                
                if submenuCP == 1:
                    if len(categorias) > 0:
                        numero_temp = 0
                        for title in categorias.keys():
                            numero_temp += 1
                            print (f"{numero_temp}. {title}")
                        
                        seleccion = int(input("Seleccione una categoria: "))
                    else:
                        print("No hay categorias!!")
                
                elif submenuCP == 2:
                    nombre_categoria = input("Digite el nombre de la categoria: ")
                    
                

                    

        elif menu_costosprod == 0:
            menu = 1
            break

    if menu < 0 or menu > 4:
        err()