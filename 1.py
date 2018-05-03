def crear():
    archivo=open('1.txt','w')
    archivo = open('1,1.txt', 'w')
    archivo.close()


def  grabar():
    num2=0
    archivo=open('1.txt','a')
    archivo1 = open('1,1.txt', 'a')
    archivo.write('calculadora de numeros binarios')

    archivo1.write("110101")
    num=7
    for i in range (num) :

        num1=(2**i)
        print(i)

        num2=num2+num1

    print(num2)
    archivo.write(str(num2) )
    archivo1.close()
    archivo.close()


crear()
grabar()
