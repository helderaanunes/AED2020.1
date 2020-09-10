class No:
    conteudo=""
    prox=None

class LSE:
    cabeca=None
    cauda= None
    tam=0 #tamanho da lista
    def tamanho(self):
        return self.tam

    def inserirInicio(self,novo):
        if (self.cabeca==None):
            self.cabeca=novo
            self.cauda=novo
        else:
            novo.prox=self.cabeca
            self.cabeca=novo
        self.tam+=1

    def imprimir(self):
        noAux=self.cabeca
        while (noAux.prox!=None):
            print (noAux.conteudo)
            noAux=noAux.prox
        print (noAux.conteudo)
        
    
    def removerInicio (self):
        if (self.cabeca==None):
            print ("lista vazia!")
        elif (self.cabeca==self.cauda):
            self.cabeca=None
            self.cauda=None
            self.tam-=1
        else:
            aux=self.cabeca
            self.cabeca=aux.prox
            aux=None
            self.tam-=1
        

    def inserirFinal(self,novo):
        if(self.cabeca==None):
            self.cabeca=novo
            self.cauda=novo
        else:
            self.cauda.prox=novo
            self.cauda=novo
        self.tam+=1

    def inserir(self, novo, i):
        if (i>self.tam or i<0):
            print ("indice inválido")
        elif (i== self.tam):
            self.inserirFinal(novo)
        elif(i==0):
            self.inserirInicio(novo)
        else :
            aux = self.cabeca
            j=0
            while (j<i-1):
                aux=aux.prox
                j+=1
            novo.prox= aux.prox
            aux.prox=novo

n1 = No()
n2 = No()
n3 = No()
n4 = No()
n5 = No()
n1.conteudo ="1"
n2.conteudo ="2"
n3.conteudo ="3"
n4.conteudo="4"
n5.conteudo="5"
lista = LSE()
lista.inserirInicio (n1)
lista.inserirInicio (n3)
lista.inserirFinal(n4)
lista.inserirInicio (n2)

lista.imprimir()

lista.inserir(n5,0)
print ("---------------------------")
lista.imprimir()
print ("O tamanho da lista é:",lista.tamanho())