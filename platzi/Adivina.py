import random

def run():
    num_aleatorio = random.randint(1, 100)
    num_elegido = int(input("Elige un número del 1 al 100: "))
    while num_elegido > 100 or num_elegido <= 0:
        print("Elige un número no valido")
        num_elegido = int(input("Elige un número, recuerda que debe ser entre 1 y 100: "))


    while num_elegido != num_aleatorio:
        if num_elegido < num_aleatorio:
            print("Piensa un número mayor")
        else:
            print("Piensa un número menor")
        num_elegido = int(input("Elige otro número: "))
    print("!Has Acertado¡")


if __name__ == "__main__":
    run()