"""
Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un
total de n personas.
"""

persona=0
hombres=0
mujeres=0
ingreso="SI"
totalH=0
totalM=0
while ingreso=="SI":
        persona=input("Que sexo se define usted ('ESCRIBIR EN MAYUSCULA HOMBRE O MUJER')")

        if persona=="HOMBRE":
            totalH+=1
        elif persona=="MUJER":
            totalM+=1
        ingreso=input("Va ingresar otra persona?")

        if ingreso!="SI":
              break
print("Cantidad de hombre",totalH)
print("Cantidad de mentirosas",totalM)