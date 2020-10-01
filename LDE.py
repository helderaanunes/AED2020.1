inserir cab    O (1)
remover cau    O (n)
Primeira

____________________

Segunda na lista SIMPLESMENTE ENCADEADA??
remover cab     O(1)
inserir cau     O(1)


class No:
    conteudo=""
    ant=None
    prox=None

class LDE:
    cab=None
    cau=None
    tam=0

    def inserirInicio(self, novo):
        if (self.cab == None and self.cau==None):
            self.cab = novo
            self.cau = novo
        else:
            novo.prox=self.cab
            self.cab=novo
            novo.prox.ant=novo
        self.tam+=1

    def inserirFim (self,novo):
        if (self.tam==0):
            self.cab = novo
            self.cau = novo
        else:
            novo.ant= self.cau
            self.cau.prox=novo
            self.cau=novo
        self.tam+=1

    def removerFinal(self):
        if (self.cau == None and  self.cab == None):
            print ("lista vazia")
        elif (self.cab == self.cau):
            self.cab = None
            self.cau=None
            self.tam-=1
        else:
            p = self.cau.ant
            self.caud=p
            p.prox.ant=None
            p.prox=None
            self.tam-=1

    def removerInicio(self):
        pass

    def remover (self, i):
        if (i==0):
            self.removerInicio()
        elif (i== self.tam-1):
            self.removerFinal()
        elif (i>0 and i<self.tam-1):
            j = 0
            elemento = self.cab
            while (j<i):
                elemento=elemento.prox
                j+=1
            elemento.ant.prox=elemento.prox
            elemento.prox.ant=elemento.ant
            elemento.prox=None
            elemento.ant=None
            elemento=None
            self.tam-=1
    