''' Definir classe no '''
class No:
    chave=""
    conteudo=""
    dir=None
    esq=None

class ABB:
# atributos da nossa classe arvore binaria de busca '''
    raiz=None

    def inserir(self, novo, aux):
        # inserir em uma ABB vazia '''
        if (self.raiz==None):
            self.raiz=novo
        # inserir em ABB que já possui elementos'''
        else:
            if (novo.chave > aux.chave):
        # se a direita não tiver ninguem'''
                if (aux.dir ==None):
                    aux.dir=novo
        # se a direita já possuir alguem'''
                else:
                    self.inserir(novo,aux.dir)
            else:
                if(aux.esq == None):
                    aux.esq=novo
                else:
                    self.inserir(novo,aux.esq)
#
#Pre ordem = p e d
#Em ordem =  e p d
#Pos ordem=  e d p

    def imprimirPreOrdem(self, aux):
        print(aux.chave)
        if (aux.esq!=None):
            self.imprimirPreOrdem(aux.esq)
        if (aux.dir!=None):
            self.imprimirPreOrdem(aux.dir)
        

    def imprimirEmOrdem(self, aux):
        if (aux.esq!=None):
            self.imprimirEmOrdem(aux.esq)
        print(aux.chave)
        if (aux.dir!=None):
            self.imprimirEmOrdem(aux.dir)


    def imprimirPosOrdem(self, aux):
        if (aux.esq!=None):
            self.imprimirPosOrdem(aux.esq)
        if (aux.dir!=None):
            self.imprimirPosOrdem(aux.dir)
        print(aux.chave)

n1 = No()
n2 = No()
n3 = No()
n4 = No()
n5 = No()
n6 = No()
n7 = No()
abb = ABB()

n1.chave =100
n1.conteudo="Batata Doce"
n2.chave =20
n3.chave =30
n4.chave =14
n5.chave =51
n6.chave =16
n7.chave =27

abb.inserir(n5,abb.raiz)
abb.inserir(n2,abb.raiz)
abb.inserir(n6,abb.raiz)
abb.inserir(n4,abb.raiz)
abb.inserir(n1,abb.raiz)
abb.inserir(n3,abb.raiz)
abb.inserir(n7,abb.raiz)

print ("---------- Pre Ordem --------------")
abb.imprimirPreOrdem(abb.raiz)
print ("---------- Em Ordem --------------")
abb.imprimirEmOrdem(abb.raiz)
print ("---------- Pos Ordem --------------")
abb.imprimirPosOrdem(abb.raiz)