
def mergeSort(lista): 
    if len(lista) >1: 
        meio = len(lista)//2 #Encontra o meio da Lista
        esquerda = lista[:meio] # Divide os da esquerda 
        direita = lista[meio:] # Divide os da direita
        ''''print ("esquerda:",end="")
        print(esquerda,end="")
        print ("direita:",end="")
        print(direita)'''
        mergeSort(esquerda) # faz a recursão com as da esquerda
        mergeSort(direita) # faz a recursão com as da direita
  
        i = j = k = 0
        # ver a sub lista antes de ordenar
        print (lista)
        # Começa a unir as listas de maneira ordenada
        while i < len(esquerda) and j < len(direita): 
            if esquerda[i] < direita[j]: 
                lista[k] = esquerda[i] 
                i+=1
            else: 
                lista[k] = direita[j] 
                j+=1
        
            k+=1
          
        # verifica se faltou unir algum elemento a esquerda 
        while i < len(esquerda): 
            lista[k] = esquerda[i] 
            i+=1
            k+=1
        # verifica se faltou unir algum elemento a direita
        while j < len(direita): 
            lista[k] = direita[j] 
            j+=1
            k+=1
        #ver a lista unida em cada passo
        print (lista)
  

lista = [20,8,90,13, 31, 25,47,63]
print ("a lista original:")
print (lista)
mergeSort(lista) 
print ("a lista ordenada:")
print (lista)
