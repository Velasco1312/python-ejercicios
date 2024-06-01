"""
. Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.
"""
sexo=0
edad=0
contH=0
edadH=0
contM=0
edadM=0
estudiantes=int(input("Ingrese cuanto estudiantes tiene el curso"))
for i in range(estudiantes):
    sexo=input("Ingrese a que tipo de sexo se identifica[HOMBRE/MUJER]")
    edad=int(input("Ingrese la edad "))
    if sexo=="HOMBRE":
        contH+=1
        edadH+=edad
    elif sexo=="MUJER":
        contM+=1
        edadM+=edad
promedioH=edadH/contH
promedioM=edadM/contM
promedioT=(edadH+edadM)/estudiantes
print("El promedio de edad en los hombres es de ",promedioH)
print("El promedio de edades de las mujeres es de ",promedioM)
print("El promedio de edades de todo el salon es de ",promedioT)

