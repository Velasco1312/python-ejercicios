"""
La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad
de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo
dígito de la placa de cada carro, se puede determinar el color de la calcomanía
utilizando la siguiente relación:
""" 
placa=0
amarillo=0
rosa=0
roja=0
verde=0
azul=0
auto="SI"
while auto=="SI":
    placa = input("Ingrese la placa: ")
    placaU = placa[-1]
    if placaU == '1' or placaU == '2':
        amarillo += 1
    elif placaU == '3' or placaU == '4':
        rosa += 1
    elif placaU == '5' or placaU == '6':
        roja += 1
    elif placaU == '7' or placaU == '8':
        verde += 1
    elif placaU == '9' or placaU == '0':
        azul += 1
    auto=input("Va ingresar otro auto?[SI/NO]")
    if auto!="SI":
        break

print("La cantidad de carros con el último dígito de la placa 1 y 2 que ingresaron a Ibagué es de:", amarillo)
print("La cantidad de carros con el último dígito de la placa 3 y 4 que ingresaron a Ibagué es de:", rosa)
print("La cantidad de carros con el último dígito de la placa 5 y 6 que ingresaron a Ibagué es de:", roja)
print("La cantidad de carros con el último dígito de la placa 7 y 8 que ingresaron a Ibagué es de:", verde)
print("La cantidad de carros con el último dígito de la placa 9 y 0 que ingresaron a Ibagué es de:", azul)
