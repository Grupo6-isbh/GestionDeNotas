print("\n")
def calcular_promedio():
    print("Ingrese el nombre del alumno")
    nom=input()
    n = int (input("ingrese la cantida de notas a promediar: "))
    suma = 0
    i = 1
    while(i <= n):
        print("ingrese el valor de la nota " ,i,":")
        nota = float(input())
        suma = suma+nota
        i+=1
    prom= suma / n
    print("el promedio de notas del alumno",nom,"es :", prom)

    if (prom >7 ):
        print("El estado del alumno es: Promocion")
    elif (prom <= 4):
        print("El estado del alumno es: Libre")
    else:
        print("El estado del alumno es: Regular")

