from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None



class Colecao:
    '''
    Uma classe que representa uma coleção de figurinhas, com métodos para adicionar e remover figurinhas,
    vizualizar a coleção e realizar a troca entre a quantidade máxima possível entre dois colecionadores.
    Exemplos:
    >>> c = Colecao(100)
    >>> c.visualizar()
    '[]'
    >>> c.repetidas()
    '[]'
    >>> c.insere(2)
    >>> c.insere(1)
    >>> c.insere(3)
    >>> c.visualizar()
    '[1, 2, 3]'
    >>> c.repetidas()
    '[]'
    >>> c.insere(1)
    >>> c.insere(2)
    >>> c.insere(3)
    >>> c.visualizar()
    '[1, 2, 3]'
    >>> c.repetidas()
    '[1 (1), 2 (1), 3 (1)]'
    >>> c.remove(1)
    >>> c.visualizar()
    '[1, 2, 3]'
    >>> c.repetidas()
    '[2 (1), 3 (1)]'

    #troca
    >>> c1 = Colecao(100)
    >>> c2 = Colecao(100)
    >>> c1.insere(1)
    >>> c1.insere(3)
    >>> c1.insere(4)
    >>> c1.insere(4)
    >>> c2.insere(1)
    >>> c2.insere(2)
    >>> c2.insere(2)
    >>> c2.insere(3)
    >>> c1.visualizar()
    '[1, 3, 4]'
    >>> c2.visualizar()
    '[1, 2, 3]'
    >>> c1.repetidas()
    '[4 (1)]'
    >>> c2.repetidas()
    '[2 (1)]'
    >>> c1.troca(c2)
    >>> c1.visualizar()
    '[1, 2, 3, 4]'
    >>> c2.visualizar()
    '[1, 2, 3, 4]'
    >>> c1.repetidas()
    '[]'
    >>> c2.repetidas()
    '[]'
    '''

    figurinhas: No | None
    tam_album: int

    def __init__(self, tam_album: int) -> None:
        '''
        Construtor da classe 'Colecao', que inicializa a coleção vazia. Recebe como parâmetro o tamanho do álbum.

        Exemplos:
        >>> colecao = Colecao(100)
        >>> colecao.visualizar()
        '[]'
        >>> colecao.repetidas()
        '[]'
        '''
        self.figurinhas = None
        self.tam_album = tam_album



    def insere(self, fig: int) -> None:
        '''
        Insere uma figurinha na coleção, sua posição é ajustada com base na sua enumeração.
        Requer que a figurinha exista no álbum.

        Exemplos:
        Exemplos:
        #erro: a figurinha não existe.
        >>> c = Colecao(100)
        >>> c.insere(-1)
        Traceback (most recent call last):
        ...
        ValueError: Figurinha não existe
        >>> c.insere(101)
        Traceback (most recent call last):
        ...
        ValueError: Figurinha não existe

        #sucesso: a figurinha existe.
        >>> c = Colecao(100)
        >>> c.insere(1)
        >>> c.visualizar()
        '[1]'
        >>> c.insere(3)
        >>> c.visualizar()
        '[1, 3]'
        >>> c.insere(2)
        >>> c.visualizar()
        '[1, 2, 3]'
        '''
        if fig < 1 or fig > self.tam_album:
            raise ValueError('Figurinha não existe')
        elif self.figurinhas is None:
            self.figurinhas = No(fig, None)
        elif fig < self.figurinhas.item:
            self.figurinhas = No(fig, self.figurinhas)
        else:
            no = self.figurinhas
            while no.prox is not None and fig > no.prox.item:
                no = no.prox
            no.prox = No(fig, no.prox)



    def remove(self, fig: int) -> None:
        '''
        Remove uma figurinha da coleção. Requer que exista ao menos 1 figurinha da removida na coleção.

        Exemplos:
        #erro: a figurinha não existe.
        >>> c = Colecao(100) #erro: a figurinha não existe.
        >>> c.insere(1)
        >>> c.insere(2)
        >>> c.insere(3)
        >>> c.visualizar()
        '[1, 2, 3]'
        >>> c.remove(-1)
        Traceback (most recent call last):
        ...
        ValueError: figurinha não faz parte do álbum (não existe)

        #erro: a figurinha existe mas não está na coleção (não foi inserida).
        >>> c = Colecao(100)
        >>> c.insere(1)
        >>> c.insere(2)
        >>> c.insere(3)
        >>> c.visualizar()
        '[1, 2, 3]'
        >>> c.remove(4)
        Traceback (most recent call last):
        ...
        ValueError: figurinha não está na coleção (quantidade < 1)
        
        #sucesso: a figurinha existe e está na coleção.
        >>> c = Colecao(100)
        >>> c.insere(1)
        >>> c.insere(2)
        >>> c.insere(3)
        >>> c.visualizar()
        '[1, 2, 3]'
        >>> c.remove(2)
        >>> c.visualizar()
        '[1, 3]'
        '''
        if fig < 1 or fig > self.tam_album:
            raise ValueError('figurinha não faz parte do álbum (não existe)')
        elif self.figurinhas is None:
            raise ValueError('figurinha não está na coleção (quantidade < 1)')

        no = self.figurinhas
        if no is not None and no.prox is None and no.item == fig:
            self.figurinhas = None
            return
        elif no.item == fig:
            self.figurinhas = no.prox
            return

        while no.prox is not None and fig != no.prox.item:
            no = no.prox

        if no.prox is None:
            raise ValueError('figurinha não está na coleção (quantidade < 1)')
        else:
            if no.prox.prox is not None:
                no.prox = no.prox.prox
            else:
                no.prox = None    



    def visualizar(self) -> str:
        '''
        Retorna uma string que representa a coleção, sem repetições.

        Exemplos:
        >>> colecao = Colecao(100)
        >>> colecao.visualizar()
        '[]'
        >>> colecao.insere(1)
        >>> colecao.insere(2)
        >>> colecao.insere(4)
        >>> colecao.insere(4)
        >>> colecao.visualizar()
        '[1, 2, 4]'
        >>> colecao.remove(1)
        >>> colecao.visualizar()
        '[2, 4]'
        '''
        if self.figurinhas is None:
            return '[]'
        else:
            s = '['
            anterior: None | int = None
            no = self.figurinhas
            final = False
            while not final:
                if no.item != anterior:
                    s += str(no.item) + ', '
                anterior = no.item
                if no.prox is None:
                    final = True
                else:
                    no = no.prox

            return s[:-2] + ']'
    


    def repetidas(self) -> str:
        '''
        Retorna uma string que representa as figurinhas repetidas da coleção seguidas de sua quantidade de excesso entre parênteses.

        Exemplos:
        >>> colecao = Colecao(100)
        >>> colecao.repetidas()
        '[]'
        >>> colecao.insere(1)
        >>> colecao.insere(1)
        >>> colecao.insere(2)
        >>> colecao.insere(3)
        >>> colecao.insere(3)
        >>> colecao.visualizar()
        '[1, 2, 3]'
        >>> colecao.repetidas()
        '[1 (1), 3 (1)]'
        '''
        if self.figurinhas is None:
            return '[]'
        else:
            s = '['
            anterior: None | int = None
            no = self.figurinhas
            final = False
            while not final:
                if no.item != anterior:
                    qtd = 1
                    no_aux = no.prox
                    while no_aux is not None and no_aux.item == no.item:
                        qtd += 1
                        no_aux = no_aux.prox
                    if qtd > 1:
                        s += f'{no.item} ({qtd - 1}), '
                anterior = no.item
                if no.prox is None:
                    final = True
                else:
                    no = no.prox

    
            if s == '[':
                return '[]'
            return s[:-2] + ']'
    


    def troca(self, colecionador: Colecao) -> None:
        '''
        Realiza a troca de figurinhas entre dois colecionadores, na quantidade máxima possível (troca o máximo de figurinhas
        não obtidas pelos recipientes, limitado ao número menor de figurinhas trocáveis de uma coleção).

        Exemplos:
        #erro: álbuns de tamanhos diferentes.
        >>> c1 = Colecao(100)
        >>> c2 = Colecao(50)
        >>> c1.insere(1)
        >>> c1.insere(1)
        >>> c2.insere(2)
        >>> c2.insere(2)
        >>> c1.visualizar()
        '[1]'
        >>> c2.visualizar()
        '[2]'
        >>> c1.troca(c2)
        Traceback (most recent call last):
        ...
        ValueError: os álbuns não possuem o mesmo tamanho (diferentes)

        #troca com um album contendo repetidas e outro sem repetidas (troca é possível mas não ocorre devido a falta de repetidas trocáveis em c2).
        >>> c1 = Colecao(100)
        >>> c2 = Colecao(100)
        >>> c1.insere(1)
        >>> c1.insere(2)
        >>> c1.insere(3)
        >>> c1.insere(4)
        >>> c1.insere(4)
        >>> c1.insere(4)
        >>> c2.insere(1)
        >>> c2.insere(2)
        >>> c2.insere(3)
        >>> c2.insere(5)
        >>> c1.visualizar()
        '[1, 2, 3, 4]'
        >>> c2.visualizar()
        '[1, 2, 3, 5]'
        >>> c1.repetidas()
        '[4 (2)]'
        >>> c2.repetidas()
        '[]'
        >>> c1.troca(c2)
        >>> c1.visualizar()
        '[1, 2, 3, 4]'
        >>> c2.visualizar()
        '[1, 2, 3, 5]'

        #troca com ambos os álbuns com repetidas mas sem nenhuma troca possível (sem mudança).
        >>> c1 = Colecao(100)
        >>> c2 = Colecao(100)
        >>> c1.insere(1)
        >>> c1.insere(2)
        >>> c1.insere(3)
        >>> c1.insere(4)
        >>> c1.insere(4)
        >>> c1.insere(4)
        >>> c2.insere(1)
        >>> c2.insere(2)
        >>> c2.insere(3)
        >>> c2.insere(5)
        >>> c2.insere(1)
        >>> c1.visualizar()
        '[1, 2, 3, 4]'
        >>> c2.visualizar()
        '[1, 2, 3, 5]'
        >>> c1.repetidas()
        '[4 (2)]'
        >>> c2.repetidas()
        '[1 (1)]'
        >>> c1.troca(c2)
        >>> c1.visualizar()
        '[1, 2, 3, 4]'
        >>> c2.visualizar()
        '[1, 2, 3, 5]'

        #troca com nenhuma repetida (sem mudança).
        >>> c1 = Colecao(100)
        >>> c2 = Colecao(100)
        >>> c1.insere(1)
        >>> c1.insere(2)
        >>> c1.insere(3)
        >>> c2.insere(4)
        >>> c2.insere(5)
        >>> c2.insere(6)
        >>> c1.visualizar()
        '[1, 2, 3]'
        >>> c2.visualizar()
        '[4, 5, 6]'
        >>> c1.troca(c2)
        >>> c1.visualizar()
        '[1, 2, 3]'
        >>> c2.visualizar()
        '[4, 5, 6]'

        #Troca com repetidas trocáveis (sucesso).
        >>> c1 = Colecao(100)
        >>> c2 = Colecao(100)
        >>> c1.insere(1)
        >>> c1.insere(2)
        >>> c1.insere(3)
        >>> c1.insere(4)
        >>> c1.insere(4)
        >>> c1.insere(4)
        >>> c2.insere(1)
        >>> c2.insere(2)
        >>> c2.insere(3)
        >>> c2.insere(5)
        >>> c2.insere(5)
        >>> c1.visualizar()
        '[1, 2, 3, 4]'
        >>> c2.visualizar()
        '[1, 2, 3, 5]'
        >>> c1.troca(c2)
        >>> c1.visualizar()
        '[1, 2, 3, 4, 5]'
        >>> c2.visualizar()
        '[1, 2, 3, 4, 5]'
        >>> c1.repetidas()
        '[4 (1)]'
        >>> c2.repetidas()
        '[]'

        #Troca com a última figurinha repetida trocada.
        >>> c1 = Colecao(100)
        >>> c2 = Colecao(100)
        >>> c1.insere(1)
        >>> c1.insere(2)
        >>> c1.insere(3)
        >>> c1.insere(4)
        >>> c1.insere(4)
        >>> c1.insere(4)
        >>> c2.insere(1)
        >>> c2.insere(2)
        >>> c2.insere(3)
        >>> c2.insere(5)
        >>> c2.insere(5)
        >>> c1.visualizar()
        '[1, 2, 3, 4]'
        >>> c2.visualizar()
        '[1, 2, 3, 5]'
        >>> c1.repetidas()
        '[4 (2)]'
        >>> c2.repetidas()
        '[5 (1)]'
        >>> c1.troca(c2)
        >>> c1.visualizar()
        '[1, 2, 3, 4, 5]'
        >>> c2.visualizar()
        '[1, 2, 3, 4, 5]'

        #Verificação de ordem (as figurinhas trocadas devem ser escolhidas em ordem crescente).
        >>> c1 = Colecao(100)
        >>> c2 = Colecao(100)
        >>> c1.insere(1)
        >>> c1.insere(2)
        >>> c1.insere(4)
        >>> c1.insere(4)
        >>> c2.insere(5)
        >>> c2.insere(5)
        >>> c2.insere(10)
        >>> c2.insere(10)
        >>> c1.visualizar()
        '[1, 2, 4]'
        >>> c1.repetidas()
        '[4 (1)]'
        >>> c2.visualizar()
        '[5, 10]'
        >>> c2.repetidas()
        '[5 (1), 10 (1)]'
        >>> c1.troca(c2)
        >>> c1.visualizar()
        '[1, 2, 4, 5]'
        >>> c2.visualizar()
        '[4, 5, 10]'
        '''
        if self.tam_album != colecionador.tam_album:
            raise ValueError('os álbuns não possuem o mesmo tamanho (diferentes)')
        
        no1 = self.__no_sem_repeticao()
        no2 = colecionador.__no_sem_repeticao()

        repetidas1 = self.__no_repetidas()
        repetidas2 = colecionador.__no_repetidas()

        recebiveis1: No | None = None
        recebiveis2: No | None = None

        # O propósito dos loops a seguir é criar dois encadeamentos com as figurinhas que podem ser trocadas.
        while repetidas2 is not None and no1 is not None:
            if no1.prox is None and no1.item > repetidas2.item: #garante que a última figurinha de no1 seja verificada.
                recebiveis1 = No(repetidas2.item, recebiveis1)
                repetidas2 = repetidas2.prox
            elif no1 is not None and no1.item > repetidas2.item: #se a figurinha de no1 é maior que a de repetidas2, avança o no1.
                no1 = no1.prox
            elif no1 is not None and no1.item < repetidas2.item: #se a figurinha de no1 é menor que a de repetidas2, adiciona a figurinha de repetidas2 ao encadeamento recebiveis1.
                recebiveis1 = No(repetidas2.item, recebiveis1)
                repetidas2 = repetidas2.prox
            elif no1 is not None and no1.item == repetidas2.item: #se as figurinhas são iguais, avança ambos os encadeamentos. (a figurinha repetida não se caracteriza como trocável, pois já está no álbum)
                no1 = no1.prox
                repetidas2 = repetidas2.prox
            else:
                repetidas2 = repetidas2.prox
        
        while repetidas1 is not None and no2 is not None:
            if no2.prox is None and no2.item > repetidas1.item:
                recebiveis2 = No(repetidas1.item, recebiveis2)
                repetidas1 = repetidas1.prox
            elif no2 is not None and no2.item > repetidas1.item:
                no2 = no2.prox
            elif no2 is not None and no2.item < repetidas1.item:
                recebiveis2 = No(repetidas1.item, recebiveis2)
                repetidas1 = repetidas1.prox
            elif no2 is not None and no2.item == repetidas1.item:
                no2 = no2.prox
                repetidas1 = repetidas1.prox
            else:
                repetidas1 = repetidas1.prox
        
        while recebiveis1 is not None and recebiveis2 is not None: #insere e remove as figurinhas trocadas enquanto nenhum dos encadeamentos chega ao fim.
            self.insere(recebiveis1.item)
            colecionador.insere(recebiveis2.item)
            self.remove(recebiveis2.item)
            colecionador.remove(recebiveis1.item)
            recebiveis1 = recebiveis1.prox
            recebiveis2 = recebiveis2.prox



    def __no_repetidas(self) -> No | None:
        '''
        Retorna um encadeamento com as figurinhas repetidas de uma coleção. (ordem decrescente, sem repetições)
        Exemplos:
        >>> c = Colecao(100)
        >>> c.insere(1)
        >>> c.insere(2)
        >>> c.insere(3)
        >>> c._Colecao__no_repetidas()

        >>> c.insere(1)
        >>> c.insere(2)
        >>> c._Colecao__no_repetidas()
        No(item=2, prox=No(item=1, prox=None))
        '''
        no_repetidas: No | None = None
        anterior: None | int = None
        no = self.figurinhas
        while no is not None:
            if no.item != anterior:
                qtd = 1
                no_aux = no.prox
                while no_aux is not None and no_aux.item == no.item:
                    qtd += 1
                    no_aux = no_aux.prox
                if qtd > 1:
                    no_repetidas = No(no.item, no_repetidas)
            anterior = no.item
            no = no.prox
        return no_repetidas
    

    def __no_sem_repeticao(self) -> No | None:
        '''
        Retorna um encadeamento com as figurinhas sem repetição de uma coleção. (ordem decrescente, sem repetições)
        Exemplos:
        >>> c = Colecao(100)
        >>> c.insere(1)
        >>> c.insere(2)
        >>> c.insere(3)
        >>> c._Colecao__no_sem_repeticao()
        No(item=3, prox=No(item=2, prox=No(item=1, prox=None)))
        >>> c.insere(1)
        >>> c.insere(2)
        >>> c._Colecao__no_sem_repeticao()
        No(item=3, prox=No(item=2, prox=No(item=1, prox=None)))
        '''
        no_sem_repeticao: No | None = None
        anterior: None | int = None
        no = self.figurinhas
        while no is not None:
            if no.item != anterior:
                no_sem_repeticao = No(no.item, no_sem_repeticao)
            anterior = no.item
            no = no.prox
        return no_sem_repeticao

#oie