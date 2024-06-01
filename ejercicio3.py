"""
Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja
de todo el grupo.
"""
sumaCalificaciones=0
cantidadCalificaciones=0
calificacionMenor=5
calificacionMayor=0

for i in range(1,21):
    calificaciones=float(input("Ingrese la calificacion final del estudiate"))
    if calificaciones<calificacionMenor:
        calificacionMenor=calificaciones
    elif calificaciones>calificacionMayor:
        calificacionMayor=calificaciones
    cantidadCalificaciones+=1
    sumaCalificaciones+=calificaciones
    promedio=sumaCalificaciones/cantidadCalificaciones

print("El promedio del curso es de ",promedio)
print("La calificacion mas alta fue de ",calificacionMayor)
print("La calificacion mas baja fue de ", calificacionMenor)