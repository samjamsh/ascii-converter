get_inn=input("getin: ").upper()

get_in=tuple(get_inn)

lista = {"A":"01000001", "B":"01000010", "C":"01000011", "D":"01000100", "E":"01000101", "F":"01000110", "G":"01000111", "H":"01001000", "I":"01001001", "J":"01001010", "K":"01001011", "L":"01001100", "M":"01001101", "N":"01001110", "O":"01001111", "P":"01010000", "Q":"01010001", "R":"01010010", "S":"01010011", "T":"01010100", "U":"01010101", "V":"01010110", "W":"01010111", "X":"01011000", "Y":"01011001", "Z":"01011010"}
# BLOCO DE CODIGO RESERVADO PARA OS TESTES

liste=[]

alist=list(get_inn)

import sys
if len(alist) == 1:
   
    for letra in get_in:

        if letra in lista:
            for caracter in letra:

                encode=lista[caracter]
                deco=liste.append(encode)            
                db=liste
                db=db
                print(str(db)[2:-2])
        else:
      
            print("Caracter invalido!")
            sys.exit(1)

elif len(alist) < 1:
    print("digite um texto ou caracter")
    sys.exit(0)

else:

    for letra in get_in:

        if letra in lista:

            for caracter in letra:
                encode=lista[caracter]
                deco=liste.append(encode)            
                db=liste
                db=liste[0:]
                last=len(liste)
                print(liste[-1] + " ", end=" ")

        else:
            print("Texto invalido!")
            sys.exit(1)

    print()
