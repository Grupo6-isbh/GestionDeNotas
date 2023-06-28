from Inicio_usuarios import ingresar_usuario_alu
from Inicio_usuarios import ingresar_usuario_prof 
from Inicio_usuarios import ingresar_usuario_prec

menuprincipal= int(input("Ingrese el rol que cumple: \n 1-Alumno \n 2-Profesor \n 3-Preceptor\n"))
while menuprincipal !=0:
    if menuprincipal == 1:
        ingresar_usuario_alu()
        break
    elif menuprincipal == 2:
        ingresar_usuario_prof()
        break
    elif menuprincipal == 3:
        ingresar_usuario_prec()
        break
    else:
        print("\n ingrese una opcion valida")