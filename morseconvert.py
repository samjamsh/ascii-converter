import sys
if len(sys.argv) >1:
    print("Use sem parametros")
    sys.exit(1)
else:
    pass # continue 



get_inn=input("getin: ").upper()


#checagem de int not alpha (str)
str=get_inn.isalpha()
if str is False:
    print("Apenas string")
    sys.exit(0)
#fim checagem int or values != alpha

get_in=tuple(get_inn)

lista={'A':'.-','B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'—.','H':'....', 'I':'..', 'J':'.—-', 'K':'-._-', 'L':'.-..','M':'—', 'N':'-.', 'O':'—-', 'P':'.—.', 'Q':'—.-', 'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.—', 'X':'-..-', 'Y':'-.--', 'Z':'—..',' ':' '}


#iniciando a parte funcional
liste=[]

alist=list(get_inn)

if len(alist) <= 1: 

    for letra in get_in:

        if letra in lista:
            
            for caracter in letra:
                    
                encode=lista[caracter]
      
                deco=liste.append(encode)
                  
                db=liste         
                db=db
                print(db[0])
              
        else:
    
            pass
else:
# se nao for pasado apenas um carcter 
#repete o procedimento se caracteres for >1
    for letra in get_in:

        if letra in lista:

            for caracter in letra:
         
                encode=lista[caracter]
          
                deco=liste.append(encode)
      
            
                db=liste
         
                db=liste[0:]
              
                last=len(liste)
                print(liste[-1] + " ", end="")
        else:
       
            pass

