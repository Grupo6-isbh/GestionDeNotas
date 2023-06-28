from Func_prof import calcular_promedio
def ingresar_usuario_alu ():
    Usuario_alumno = "ignacio forno"
    pwd_ = "1234"

    print("por favor ingrese su nombre: ")
    User = input()
    print("por favor ingrese su contraseña: ")
    pwd = input()

    if pwd==pwd_ and User==Usuario_alumno:
        print("Bienvenido:" , User, "\n")

    else:
        print("Usuario o contraseña incorrectos")

def ingresar_usuario_prof():
    Usuario_prof = "Narciso"
    pwd_ = "1234"

    print("por favor ingrese su nombre: ")
    User = input()
    print("por favor ingrese su contraseña: ")
    pwd = input()

    if pwd==pwd_ and User==Usuario_prof:
        print("Bienvenido:" , User,"\n")
        calcular_promedio()
    else:
        print("Usuario o contraseña incorrectos")

def ingresar_usuario_prec():
    Usuario_preceptor = "Sabino"
    pwd_ = "1234"

    print("por favor ingrese su nombre: ")
    User = input()
    print("por favor ingrese su contraseña: ")
    pwd = input()

    if pwd==pwd_ and User==Usuario_preceptor:
        print("Bienvenido:" , User, "\n")
    else:
        print("Usuario o contraseña incorrectos")
