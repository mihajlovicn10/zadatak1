import numpy as np 

lista_imena = []
lista_vrednosti = []
printovalo = False 
pogodak = [] 

def rekurzija(l, sum, k, local, niz):
    if sum == k:
        global printovalo
        if len(local) != 0: 
           # print(local)
            if len(pogodak) == 0: 
                for i in local: 
                    pogodak.append(i)
            
            printovalo = True  
    
    for i in range(l, len(niz)): 
        if sum + niz[i] > k: 
            continue 
        if i > l and niz[i] == niz[i - 1]: 
            continue 
        local.append(niz[i])
        rekurzija(i + 1, sum + niz[i], k , local , niz)
        local.pop()

def nadji_najblizi(resenja): 
    resenja = np.asarray(resenja)
    pozicija_u_listi = (abs(resenja - 0)).argmin()
    return resenja[pozicija_u_listi]  

for i in range(1,50):

    privremena = str(input("Unesite vrednost " + str(i)))
    if privremena == "": 
        break
    razbijena = privremena.split(" ")
    lista_imena.append(razbijena[0])
    lista_vrednosti.append(int(razbijena[1]))

lista_vrednosti.sort(reverse=False)

lokal = []
rekurzija(0,0,0,lokal, lista_vrednosti)
if printovalo == False: 
    resenja = []
    sum = 0 
    for i in lista_vrednosti: 
        sum = sum + i 
    if sum < 0: 
        sum = sum * -1 
    while len(resenja) == 0: 
        for i in range (sum * -1, sum): 
            printovalo = False 
            rekurzija(0,0,i,lokal, lista_vrednosti)
            if printovalo == True: 
                resenja.append(i)
        sum = sum * 2
    print("Balans nije moguc. Najmanja vrednost je ",nadji_najblizi(resenja))
else: 
    print("Balans je moguc.") 
    print(pogodak)

