
def run(): # funcion principal
    lista=[]
    suma=0
    menor=9999
    mayor=0

#-------------------------generandos los numeros------------------------------
    for i in range(15):
        a=2+i*2
        lista.append(a)

    print(lista)
#----------------------suma de los elementos-----------------------------------
    for i in range(len(lista)):
        suma=suma+lista[i]

    print('la suma de los elementos es: ',suma )

#---------------------numero menor -------------------------------------------
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]

    print('El numero menor es: ',menor)

#-----------------------numero mayor---------------------------------------------

    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]

    print('El numero mayor es: ',mayor)

#--------------------cantidad de pares ------------------------------------------
    pares=0
    for i in range(len(lista)):
        if lista[i]%2==0:
            pares+=1

    print('la cantidad de pares es: ',pares)

    # --------------------cantidad de inpares ------------------------------------------
    inpares=0
    for i in range(len(lista)):
        if lista[i]%2!=0:
            inpares+=1

    print('la cantidad de inpares es',inpares)


if __name__ == '__main__':# punto de entrada
	run()