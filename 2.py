def crear():
    archivo=open('2.txt','w')
    archivo.close()


def  grabar():
    archivo=open('2.txt','a')

    cadena = "mi mama me mima"
    print("")
    archivo.write(cadena)

    cadena.istitle()
    print("\n")
    archivo.write(cadena)

    archivo.close()

crear()
grabar()

