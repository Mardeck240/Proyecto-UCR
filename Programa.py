
control_inventario= []
registro_ventas=[]
clientes= []
costos_producción= []
menu= -1 # Movi menuu() adentro del while para que se repitiece el programa las veces necesarias

try:
    with open("inventario.txt", "r") as file:
        for text in file:
            control_inventario.append(text)
        print(control_inventario)
except:
    pass


def err():
     print("Lo que digitó no se encuentra dentro de las opciones, digite nuevamente")
    
def trabajando():
     print ("Esta función aun no está finalizada. Por favor, escoja otra.")

def des():
    try:
        return int(input("¿Que desea hacer? (1) Agregar otro producto (0) Regresar"))
    except:
        print("Caracter o simbolo invalido, intente nuevamente")
        return des()

def menuu():
    return int(input("¿Que desea hacer? \n(1) Control del inventario\n(2) Registro de ventas \n(3) Clientes y provedores \n(4) Costos de producción y venta \n(0) Salir "))

def regresar():
    try:
        return int(input("(0) Regresar"))
    except:
        print("Caracter o simbolo invalido, intente nuevamente")
        regresar()

print("¡Bienvenido a nuestro programa!")


while menu!=0:
    try:
        menu = menuu()
    except:
        print("Caracter o simbolo invalido, intente nuevamente")
        continue
    while menu==1:
        try:
            menu_interno= int(input("¿Que desea hacer? \n(1) Agregar producto \n(2) Ver productos \n(3) Eliminar productos \n(0) Retroceder \n"))
        except:
            print("Caracter o simbolo invalido, intente nuevamente")
            menu = 1
            continue
        
        if menu_interno==1:
            repetir=True
            while repetir:
                productos= input("Escriba el nombre del producto que desea agregar al inventario de la empresa")
                if productos != "":
                    control_inventario.append(productos)
                
                decision=des()
                if decision!=1:
                    repetir= False
                
                
        elif menu_interno==2:
            re=True
            print (control_inventario)
            print ("Hay", len(control_inventario), "producto(s) en el inventario de la empresa")
            regre= regresar()
            if regre!=0:
                re= False
        
        elif menu_interno == 3:
            if len(control_inventario) > 0:
                for i in range(len(control_inventario)):
                    print(f"{i+1}. {control_inventario[i]}")
            
            else:
                print("No hay ningun elemento en la lista!")
                menu = 1
                continue
            
            while True:
                try:
                    producto_elim = int(input("Digite el numero del producto que desea eliminar"))
                    control_inventario.pop(producto_elim - 1)
                    print (control_inventario)
                    break
                except:
                    print("Caracter o simbolo invalido, intente nuevamente")
                
        
        elif menu_interno == 0:
            menu = 1
            file = open("inventario.txt", "w")
            for text in control_inventario:
                file.write(text + "\n")
            file.close()
            break
        
        else:
            error= err()
            error
        
        
        
    while menu == 2 or menu == 3 or menu ==4:
        trabajando() #Quite el Break, puesto que necesitamos que el cliente pueda volver a escoger otra opcion sin que se cierre el programa
        break
    if menu < 0 or menu > 4: #Cambie el else por un if porque estaba dando problemas
        err()
