'''2.Leer el nombre de 10 frutas {nombre, color, precio} para preparar un
salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al
mismo tiempo en sentido inverso al ingresado+(1)
'''
frutas = []
for i in range (10):
    frutas.append(input("Digita una fruta: "))

frutas.reverse()
print(f'Las frutas al reves {frutas}')