# PROYECTO FUNDAMENTOS DE PYTHON / RANGEL ANAYA EMILIANO ISRAEL
print("#########################################################################################################################")
print("Bienvenid@ a la calculadora de IMC, porfavor llena los siguientes datos. ")
nombre = input("Primero ingrese su nombre: ")
if len(nombre) > 0:
    pass
else:
    print("No se puede dejar ningun dato vacio, vuelve a ejecutar porfavor.")

apellidoPaterno = input("¡Hola " + nombre.title() + "!, ingresa tu apellido paterno: ")
if len(apellidoPaterno) > 0:
    pass
else:
    print("No se puede dejar ningun dato vacio, vuelve a ejecutar porfavor.")

apellidoMaterno = input("Ahora porfavor ingresa tu apellido materno: ")
if len(apellidoMaterno) > 0:
    pass
else:
    print("No se puede dejar ningun dato vacio, vuelve a ejecutar porfavor.")

edad = input("¿Cuantos años tienes " + nombre.title() + "? ")
if len(edad) > 0:
    try:
        edad = int(edad)
    except ValueError:
        print("{} no es o son caracteres validos, vuelve a ejecutar porfavor".format(edad))
else:
    print("No se puede dejar ningun dato vacio, vuelve a ejecutar porfavor.")

peso = input("Introduce tu peso en Kg: ")
if len(peso) > 0:
    try:
        peso = float(peso)
    except ValueError:
        print("{} no es o son caracteres validos, vuelve a ejecutar".format(peso))
else:
    print("No se puede dejar ningun dato vacio, vuelve a ejecutar porfavor.")

estatura = input("Por ultimo, ingresa tu estatura en metros: ")
if len(estatura) > 0:
    try:
        estatura = float(estatura)
    except ValueError:
        print("{} no es o son caracteres validos, vuelve a ejecutar porfavor".format(estatura))
else:
    print("No se puede dejar ningun dato vacio, vuelve a ejecutar porfavor.")
# FORMULA CALCULO IMC
imc = peso / estatura ** 2
# Impresion de los datos
print("#########################################################################################################################")
print("Nombre: " + nombre.title() + ".")
print("Apellidos: " + apellidoPaterno.title() + " " + apellidoMaterno.title() + ".")
print("Edad: " + str(edad) + " años.")
print("Peso: " + str(peso) + " Kg.")
print("Estatura: " + str(estatura) + " m.")
print("IMC: {: .2f}.".format(imc))
print("#########################################################################################################################")
if imc <= 18.49:
    print("Tu IMC ({: .2f}) esta en la clasificacion de Peso bajo".format(imc))
elif imc >= 18.50 and imc <= 24.99:
    print("Tu IMC ({: .2f}) esta en la clasificacion de Peso normal".format(imc))
elif imc >= 25.00 and imc <= 29.99:
    print("Tu IMC ({: .2f}) esta en la clasificacion de Sobrepeso".format(imc))
elif imc >= 30.00 and imc <= 34.99:
    print("Tu IMC ({: .2f}) esta en la clasificacion de Obesidad leve".format(imc))
elif imc >= 35.00 and imc <= 39.99:
    print("Tu IMC ({: .2f}) esta en la clasificacion de Obesidad media".format(imc))
else:
    print("Tu IMC ({: .2f}) esta en la clasificacion de Obesidad morbida".format(imc))
print("#########################################################################################################################")
print("Gracias por ejecutar.")