tabla = int(input("Escriba el número de la tabla que desee saber: "))
for i in range (1,11):
    producto = (tabla * i)
    print(str(tabla) + " x " + str(i) + " = " + str(producto))

