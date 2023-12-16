def salibario(Word):
    S = [['ba','be','bi','bo','bu'],['ca','ce','ci','co','cu'],['da','de','di','do','du'],['fa','fe','fi','fo','fu'],['ga','ge','gi','go','gu'],['ha','he','hi','ho','hu'],['ja','je','ji','jo','ju'],['ka','ke','ki','ko','ku'],['la','le','li','lo','lu'],['ma','me','mi','mo','mu'],['na','ne','ni','no','nu'],['pa','pe','pi','po','pu'],['ra','re','ri','ro','ru'],['sa','se','si','so','su'],['ta','te','ti','to','tu'],['va','ve','vi','vo','vu'],['xa','xe','xi','xo','xu'],['za','ze','zi','zo','zu'],['us','es','as','os']]
    for i in S:
        if Word in i:
           return Word

def Encontados(S_encontadas,ListSilabas):
    for I in range(S_encontadas):
        if S_encontadas[I] == ListSilabas[I]:
            pass

def silaba(palavra,lista):
        lista.append(palavra)
        
        for Indice in range(len(lista)):
            if lista[Indice] == None:
                del lista[Indice]
        return lista


words = [str(x) for x in input().split()]

silabas = []
silabas_copy = []
encotrados = []
Resposta = "' '"

erros = 0

for i in range(1,len(words)):

    for p in range(0,len(words[i-1])-1):
        silabas = silaba(salibario(words[i-1][p:p+2]),silabas)

    
    for p2 in range(0,len(words[i])-1):
       silabas_copy = silaba(salibario(words[i][p2:p2+2]),silabas_copy)
    

    for silaba_1 in silabas_copy:
       for silba_2 in silabas:
            if silaba_1 == silba_2:
                encotrados.append(silaba_1)
                Resposta = encotrados[-1]
            else:
                erros += 1
        
    if len(silabas)*len(silabas_copy) == erros:
        encotrados = []
        Resposta = "' '"
        break
    erros = 0
    silabas.clear()
    silabas_copy.clear()

    
print(Resposta)



    
