"""
Una persona debe realizar un muestreo con 50 personas para determinar el
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona.
Las categorías se determinar de acuerdo a la siguiente tabla:
"""
cantidadNiños=0
cantidadJovenes=0
cantidadAdultos=0
cantidadViejos=0
pesoViejos=0
pesoAdultos=0
pesoJovenes=0
pesoNiños=0
for i in range(1,51):
    edad=int(input("Ingrese la edad de la persona"))
    peso=int(input("Ingrese el peso de la persona"))
    if edad>=60:
        cantidadViejos+=1
        pesoViejos+=peso
        promedioViejos=pesoViejos/cantidadViejos
    elif edad<=59 and edad>=30:
        cantidadAdultos+=1
        pesoAdultos+=peso
        promedioAdultos=pesoAdultos/cantidadAdultos
    elif edad<=29 and edad>=13:
        cantidadJovenes+=1
        pesoJovenes+=peso
        promedioJovenes=pesoJovenes/cantidadJovenes
    elif edad<=12:
        cantidadNiños+=1
        pesoNiños+=peso
        promedioNiños=pesoNiños/cantidadNiños
print("El promedio de los niños en el peso es de ",promedioNiños," con la cantidad de ",cantidadNiños," niños")
print("El promedio de los jovenes en el peso es de ",promedioJovenes," con la cantidad de ",cantidadJovenes," jovenes")
print("El promedio de los adultos en el peso es de ",promedioAdultos," con la cantidad de ",cantidadAdultos," adultos")
print("El promedio de los viejos en el peso es de ",promedioViejos," con la cantidad de ",cantidadViejos," viejos")