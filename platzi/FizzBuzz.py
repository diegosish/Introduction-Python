# Objetivo
# Crear un algoritmo que reciba un número entero que al ser divisible 5 diga Fizz
# Divisible entre 3 Buzz y Divisible entre 5 y 3 diga FizzBuzz.

# Variables
# número - if - elif - else

from asyncio.windows_events import NULL


numero = int(input("Ingrese un número: "))

if numero % 5 == 0 and numero % 3 != 0:
    print("Fizz") 
elif numero % 5 != 0 and numero % 3 == 0:
    print("Buzz")
elif numero % 5 == 0 and numero % 3 == 0:
    print("FizzBuzz")
else:
    NULL        