"""
8.un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un
algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e
imprima:
• La cantidad de estudiantes que obtuvieron una calificación menor a 50.
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero
menor que 70.
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero
menor que 80.
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100.
"""
calificacionS=0
calificacionB=0
calificacionR=0
calificacionM=0
for i in range(1,5):
    calificacion=float(input("Ingrese la calificacion del estudiante"))
    if calificacion>=80:
        calificacionS+=1
    elif calificacion>=70 and calificacion<80:
        calificacionB+=1
    elif calificacion>=50 and calificacion<70:
        calificacionR+=1
    elif calificacion<50:
        calificacionM+=1 
print("La cantidad de estudiantes que pasaron la materia en superior fueron ",calificacionS)
print("La cantidad de estudiantes que pasaron la materia en bueno fueron ",calificacionB)    
print("La cantidad de estudiantes que pasaron la materia en regular fueron ",calificacionR)    
print("La cantidad de estudiantes que no pasaron fueron ",calificacionM)    

    