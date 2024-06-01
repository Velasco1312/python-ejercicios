#Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números.
suma=0
resultado=0
for i in range(1,11):
    numeros=int(input("Ingrese el numero negativo"))
    if numeros<0:
       # resultado=numeros-(numeros)-(numeros)
        resultado=abs(numeros)
        suma+=resultado
    print(resultado)
print("Suma total de datos es de ",suma)
    