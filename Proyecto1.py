## EPN-ESFOT-ASI PROGRAMACIÓN AVANZADA 2016-B

## Autores: Campoverde Jorge - Montoya Katherine - Sanchez Jordan
## Fecha: 23-Nov-2016

def menu ():
    print("\t\t\t**CALCULO DE PERIMETROS Y AREAS")
    print("\n-OPCIONES:")
    print("1.- Circulo")
    print("2.- Triangulo")
    print("3.- Cuadrado")
    


def circulo():
    pi=3.1415
    radio=int(input("\nINGRESE EL VALOR DEL RADIO"))
    a= 2*pi*radio
    p= pi*radio**2
    print ("\nEl valor del perimetro es: ",p)
    print ("El valor del area es: ",a)
    

def triangulo():
    x=int (input("Ingrese el valor de los lados:"))
    h=int (input("Ingrese el valor de la altura:"))
    a=(x*h)/2
    p=x+x+x
    print ("\nEl valor del perimetro es: ",p)
    print ("El valor del area es: ",a)

def cuadrado():
    l=int(input("Igrese el valor del lado: "))
    a=l*l 
    p=l+l+l+l
    print ("\nEl valor del perimetro es: ",p)
    print ("El valor del area es: ",a)
    

def main():
    menu()
    opc=int(input("\nESCOJA UNA OPCION"))
    if opc==1:
        circulo()
    if opc==2:
        triangulo()
    if opc==3:
        cuadrado()

    
main()
