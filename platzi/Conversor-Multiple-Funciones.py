def conversor(tipo_pesos, v_Dolar):
    Pesos = float(input("¿Cuántos Pesos" + tipo_pesos + "tiene?: "))
    Dolares = Pesos / v_Dolar
    Dolares = str(round(Dolares,2))
    print("Tienes $" + Dolares + " Dolares")

Menu = """"
Bienvenido al conversor de monedas 🤑

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(Menu))

if opcion == 1:
    conversor(" colombianos ", 4033)
elif opcion == 2:
    conversor(" argentinos ", 104)
elif opcion == 3:
    conversor(" mexicanos ", 20.5)
else:
    print("Escribe una opción correcta")




