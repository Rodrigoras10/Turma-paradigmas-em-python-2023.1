print("\tTriângulo\n")

#Entrada de dados
lado1 = float(input("1º Lado: "))
lado2 = float(input("2º Lado: "))
lado3 = float(input("3º Lado: "))

#Calculos
if (str(lado1)[0:1] == '-') or (str(lado2)[0:1] == '-') or (str(lado3)[0:1] == '-') :
    print("")
    print("De acordo com as medidas dadas os valores não podem ser um triângulo. ")

else :
    if lado1 == lado2 == lado3 :
        print("")
        print("Triângulo Equilátero!")
    else :    
        if (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3) :
            print("")
            print("Triângulo Isósceles!")

        else :
            print("")
            print("Triângulo Escaleno!")