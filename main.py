#Condicional if: Condicion donde se detiene el flujo de ejecucion y mira si se cumple lo que
#contiene el interior. Si se cumple sigue sino sigue con lo que tenga fuera ya del if.

""""sintaxis if"""
def resultado(nota1,nota2,nota3):
    notafinal=nota1+nota2+nota3
    return notafinal
def evaluacion(resultado):
    if resultado< 5:
        return f"Suspenso{resultado}"
    if resultado < 6:
        return f"Aprobado {resultado}"
    if resultado < 7:
        return f"Bien {resultado}"
    if resultado < 9:
        return f"Notable {resultado}"
    if resultado <=10:
        return f"Sobresaliente {resultado}"
    if resultado<0:
        return f"Nota incorrecta {resultado}"
    if resultado<0:
        return f"Nota incorrecta {resultado}"
    else:
        return "Valor no valido"


alumnosprimero=("Nagore","Daniel","Pablo","Marcos")
print("Evaluacion alumnos primero")
for alumno in alumnosprimero:
    print("\n Introduzca la nota de", alumno)

    print("introduzca puntos lectura ")
    lectura = float(input())
    print(f"total lectura {lectura * 10/3}")

    print("introduzca puntos teoria ")
    teoria = float(input())
    print(f"total teoria {teoria * 10/3}")

    print("introduzca puntos dictado ")
    dictado = float(input())
    print(f"total dictado {dictado * 10/4}")

    notaalumno=resultado(lectura,teoria,dictado)
    print("nota final",evaluacion(int(notaalumno)))


