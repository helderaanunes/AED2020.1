def heapify(lista, n, i): 
    maior = i # Inicializa o maior como raiz do heap
    esq = 2 * i + 1     # filho a esquerda = 2*i + 1 
    dir = 2 * i + 2     # filho a direita = 2*i + 2 
  
    # se o filho a esquerda existir e for maior que a raiz
    if esq < n and lista[i] < lista[esq]: 
        maior = esq 
  
    # agora a vez de verificar com o filho a direita
    if dir < n and lista[maior] < lista[dir]: 
        maior = dir
  
    # troca o filho pelo pai caso necessário
    if maior != i: 
        lista[i],lista[maior] = lista[maior],lista[i] 
  
        # novamente a recursão indo para o maior elemento
        heapify(lista, n, maior) 
  
# a função principal do programa 
def heapSort(lista): 
    #pega o tamanho da lista
    n = len(lista) 
  
    # constroi a árvore/heap
    for i in range(n, -1, -1): 
        heapify(lista, n, i) 
  
    # agora vai extraindo os elementos da lista um por um,
    # porem de maneira inversa
    for i in range(n-1, 0, -1): 
        lista[i], lista[0] = lista[0], lista[i] # swap 
        heapify(lista, i, 0) 
  
# Driver code to test above 
lista = [ 12, 11, 13, 5, 6, 7, 55, 90, 87, 51] 
heapSort(lista) 
print (lista)