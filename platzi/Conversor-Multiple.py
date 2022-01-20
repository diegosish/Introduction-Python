Menu = """"
Bienvenido al conversor de monedas 🤑

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(Menu))

if opcion == 1:
    Pesos = float(input("¿Cuántos Pesos Colombianos tiene?: "))
    v_Dolar = 3990
    Dolares = Pesos / v_Dolar
    Dolares = str(round(Dolares,2))
    print("Tienes $" + Dolares + " Dolares")
elif opcion == 2:
    PesosA = float(input("¿Cuántos Pesos Argentinos tiene?: "))
    v_Dolar = 104
    Dolares = PesosA / v_Dolar
    Dolares = str(round(Dolares,2))
    print("Tienes $" + Dolares + " Dolares")
elif opcion == 3:
    PesosM = float(input("¿Cuántos Pesos Mexicanos tiene?: "))
    v_Dolar = 20.5
    Dolares = PesosM / v_Dolar
    Dolares = str(round(Dolares,2))
    print("Tienes $" + Dolares + " Dolares")
else:
    print("Escribe una opción correcta")




