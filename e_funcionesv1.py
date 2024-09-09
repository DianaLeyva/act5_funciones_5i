print("manejo de funciones v1")
#creacion de funcion
def hola_mundo():
    #asignando accion a la funcion
    print("Hola aqui estoy")
#creacion de funcion con argumentos
def mensa(msg):
    #seleccionando uso de argumentos
    print(msg+" ")
#otra funcion con argumentos, para mostrar un nombre
def escribenc(nombre,apellido):
    print(nombre+" "+apellido)
    print(f"tu nombre es {nombre} {apellido}")
def suma(n1,n2):
    s=n1+n2
    return (f"la suma de {n1} + {n2}y es:{s}")
#creando variable con ingreso de datos del usuario
respuesta = input("Quieres recibir un anuncio?:")
#condicion if, se compara respuesta (con datos ingresados por el usuario) con la palabra "si", (afirmacion)
if respuesta=="si":
    #llamando funcion hola mundo si el dato ingresado es "si"
    hola_mundo()
else:
    #llamando funcion con argumentos en caso de que el dato ingresado sea diferente a "si"
    mensa("Anuncio cancelado")
    mensa("Anuncio no recibido")
#llamado de la funcion enviando el nombre
escribenc("Diana","Leyva")
print("funciones que regresan numeros ")
print(suma(2,8))
#se le pide al usuario ingresar los valores a sumar
n1 = int(input("que numero quieres sumar?:"))
#"int" funciona como un indicador de que tipo de datos debe ser ingresado y como este debe ser tratado
n2 = int(input("que otro numero quieres sumar?:"))
#nuevamente se llama la funcion enviando los datos ingresados por el usuario
suma(n1,n2)
