def palindromo(palabra):
    palabra = palabra.replace(" ","").lower()
    palabra_invertidad = palabra[::-1]
    if palabra == palabra_invertidad:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es Palíndromo")
    else:
        print("No es Palíndromo")

if __name__ == "__main__":
    run()