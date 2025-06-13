control_inventario= []
registro_ventas=[]
clientes= []
costos_producción= []
menu = -1
fecha = 0
print("¡Bienvenido a nuestro programa! Antes de iniciar")



try:
    with open("inventario.txt", "r") as file:
        for text in file:
            control_inventario.append(text.strip())
except:
    pass


def poner_fecha():
    fecha = input("Escriba la fecha exacta en formato (día.mes.año): ")
    print(fecha)
    try:
        a_option = int(input("Desea dejar esa fecha? \n1. Si \n2. No: "))
        if a_option == 1:
            return fecha
        elif a_option == 2:
            poner_fecha()
        else:
            print("Digito invalido")
            poner_fecha()
        
        
    except:
        print("Ocurrio un error. Reintentando...")
        poner_fecha()


fecha = poner_fecha()

print(fecha)

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
            if len(control_inventario) > 0:
                print(control_inventario)
                print("Hay", len(control_inventario), "producto(s) en el inventario de la empresa")
            else:
                print ("No se han registrado productos en el inventario de la empresa")
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
                    producto_elim = int(input("Digite el número del producto que desea eliminar (si desea cancelar digite 0): "))
                    if producto_elim == 0:
                        break
                    else:
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
                if len(control_inventario) > 0:
                    print("Productos registrados:")
                for i in range(len(control_inventario)):
                    print(f"{i + 1}. {control_inventario[i]}")
                prod = input("Escriba el nombre del producto que vendió: ")
                uni = int(input("¿Cuántas unidades de este producto vendió?: "))
                prec = int(input("Digite el valor del producto vendido: "))
                venta_total = uni * prec
                venta = ("Fecha:", fecha, "Producto", prod, "Unidades vendidas", uni, "Monto total", venta_total)
                registro_ventas.append(venta)
                print("La venta se registró!.")
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

    while menu == 3 or menu == 4:
        trabajando()
        menu = -1
        break

    if menu < 0 or menu > 4:
        err()

