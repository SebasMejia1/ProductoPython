'''3.Construir un programa para ir de compras en un supermercado
que permita la construcción del siguiente MENU:
1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
2. Digitar 2 para mostrar todos los productos registrados (+0.4)
3. Digitar 3 para permitir buscar por código un producto y editar el precio
de este (+0.4)
4. Digitar 4 para permitir buscar por código un producto y eliminar el
producto (+0.4)
5. Digitar 0 para SALIR'''

from math import prod


print("*********MENU DINDO*****")
print("1. Ingresar datos del producto")
print("2. Mostrar productos registrados")
print("3. Buscar por codigo y editar el precio")
print("4. Buscar por codigo y eliminar producto")
print("5. Salir")
productos= []
opcion = int(100)
while(opcion!=5):
    producto = {}
    opcion=int(input("Digita una opcion: "))
    if(opcion==1):
        
        codigo = int(input("Codigo del producto: "))
        producto['codigo'] = codigo
        print("Codigo creado")
        producto['nombre'] = input("Nombre del producto: ")
        print("Nombre agregado")
        producto['precio'] = int(input("Precio producto: "))
        print("precio agregado")
        productos.append(producto)
                
            
        
    elif(opcion==2):
        for i in productos:
            print (i)
    elif(opcion==3):
        editar = int(input("Digite el codigo del producto que quiere editar: "))
        for i in productos:
            if(i['codigo']==editar):
                valornuevo = int(input("Digita el nuevo valor del producto: "))
                i['precio'] = valornuevo
                print("Valor cambiado")
                break
            else:
                print("Codigo no existente")
    elif(opcion==4):
        for i in productos:
            borrar = int(input("Digite el codigo del producto que quiere eliminar: "))
        
            if(i['codigo']==borrar):
                productos.remove(i)
                print("Eliminado con exito")
            else:
                print("Codigo no creado")
            break
    elif(opcion==5):
        break
    else:
        print("Cerrando")
