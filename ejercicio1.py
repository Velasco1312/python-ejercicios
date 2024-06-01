#Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros.
numeroNegativo=0
numeroPositivo=0
numeroNeutro=0
for i in range(1,20):
    numero=int(input("Ingrese un numero"))
    if numero<0:
        numeroNegativo+=1
    elif numero>0:
        numeroPositivo+=1
    else:
        numeroNeutro+=1
    print("La cantidad de numeros negativos es de ",numeroNegativo," La cantidad de numeros positivos es de ",numeroPositivo," y la cantidad de numeros neutros es de ",numeroNeutro)