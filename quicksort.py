def dividir(arr,menor,maior): 
    i = ( menor-1 )         # indice do menor elemento 
    pivot = arr[maior]     # pivo
  
    for j in range(menor , maior): 
  
        # se o elemento atual é menor que o pivo
        if   arr[j] < pivot: 
          
            # aumenta o indice do menor elemento
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    #faz a troca
    arr[i+1],arr[maior] = arr[maior],arr[i+1] 
    return ( i+1 ) 
 
  
# função principal
def quickSort(arr,menor,maior): 
    if menor < maior: 
  
        # pi é a posição atual do pivo no fim da divisao
        pAtual = dividir(arr,menor,maior) 
  
        # Separately sort elements before 
        # dividir and after dividir 
        quickSort(arr, menor, pAtual-1) 
        quickSort(arr, pAtual+1, maior) 
  

lista = [13, 55, 51, 87, 12, 64, 3, 94, 21] 
n = len(lista) 
quickSort(lista,0,n-1) 
print ("Lista ordenada:",lista) 
