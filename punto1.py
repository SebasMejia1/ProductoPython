'''1.Construir un programa que permita ingresar N (cantidad digitada por
el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3
fueron ingresados (+1)'''
cantnumero = int(input("Digite la cantidad de numeros a ingresar: "))
mult2 = 0
mult3 = 0
for i in range(cantnumero):
    numero = int(input("Digite un numero entero: "))
    if(numero%2 == 0 and numero%3 == 0):
        mult2 += 1
        mult3 += 1
    elif (numero%2==0):
        mult2 +=1 
    elif (numero%3 ==0):
        mult3 +=1
    else:
        print("Digite numero valido")
print(f'Los multiplos de 2 son: {mult2}')
print(f'Los multiplos de 3 son: {mult3}')
