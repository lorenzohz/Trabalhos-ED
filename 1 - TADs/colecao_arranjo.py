from __future__ import annotations
from ed import array


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

    figurinhas: array[int]

    def __init__(self, tam_album: int) -> None:
        '''
        Construtor da classe 'Colecao', que inicializa a coleção vazia.

        Exemplos:
        >>> c = Colecao(100)
        >>> c.visualizar()
        '[]'
        >>> c.repetidas()
        '[]'
        '''

        self.figurinhas = array(tam_album, 0)



    def insere(self, fig: int) -> None:
        '''
        Insere uma figurinha na coleção, sua posição é ajustada com base na sua enumeração.
        Requer que a figurinha exista no álbum.

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

        if fig > len(self.figurinhas) or fig < 1:
            raise ValueError('Figurinha não existe')

        self.figurinhas[fig - 1] += 1



    def remove(self, fig: int) -> None:
        '''
        Remove uma figurinha da coleção. Requer que a figurinha exista e que haja ao menos 1 figurinha da removida na coleção.

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

        if fig > len(self.figurinhas) or fig < 1:
            raise ValueError('figurinha não faz parte do álbum (não existe)')
        elif self.figurinhas[fig - 1] < 1:
            raise ValueError('figurinha não está na coleção (quantidade < 1)')

        self.figurinhas[fig - 1] -= 1



    def visualizar(self) -> str:
        '''
        Retorna uma string que representa a coleção, sem repetições.

        Exemplos:
        >>> c = Colecao(100)
        >>> c.visualizar()
        '[]'
        >>> c.insere(1)
        >>> c.insere(4)
        >>> c.insere(2)
        >>> c.insere(4)
        >>> c.visualizar()
        '[1, 2, 4]'
        >>> c.remove(1)
        >>> c.visualizar()
        '[2, 4]'
        '''

        x = '['
        for i in range(len(self.figurinhas)):
            if self.figurinhas[i] > 0:
                x += str(i + 1) + ', '

        if x[-1] != '[' and x[-2] == ',': # Se a string não está vazia
            x = x[:-2]

        x += ']'

        return x
    


    def repetidas(self) -> str:
        '''
        Retorna uma string que representa as figurinhas repetidas da coleção seguidas 
        de sua quantidade em excesso entre parênteses.

        Exemplos:
        >>> c = Colecao(100)
        >>> c.repetidas()
        '[]'
        >>> c.insere(1)
        >>> c.insere(1)
        >>> c.insere(2)
        >>> c.insere(3)
        >>> c.insere(3)
        >>> c.visualizar()
        '[1, 2, 3]'
        >>> c.repetidas()
        '[1 (1), 3 (1)]'
        '''
        
        x = '['
        for i in range(len(self.figurinhas)):
            if self.figurinhas[i] > 1:
                x += str(i + 1) + ' (' + str(self.figurinhas[i] - 1) + ')' + ', '

        if x[-1] != '[' and x[-2] == ',':
            x = x[:-2]

        x += ']'

        return x
    


    def troca(self, col: Colecao) -> None:
        '''
        Realiza a troca de figurinhas entre dois colecionadores, na quantidade máxima possível (troca o máximo de figurinhas
        não obtidas pelos recipientes, limitado ao número menor de figurinhas trocáveis de uma das coleções).

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

        if len(self.figurinhas) != len(col.figurinhas):
            raise ValueError('os álbuns não possuem o mesmo tamanho (diferentes)')

        trocaveis1 = array(len(self.figurinhas), 0)  #figurinhas que o album1 (self) pode receber
        trocaveis2 = array(len(self.figurinhas), 0)  #figurinhas que o album2 (col) pode receber
        x,y = 0,0

        for i in range(len(self.figurinhas)):
            if self.figurinhas[i] == 0 and col.figurinhas[i] > 1: #album1 sem figurinha e album2 com figurinha repetida
                trocaveis1[x] = i + 1
                x += 1

            elif self.figurinhas[i] > 1 and col.figurinhas[i] == 0: #album1 com figurinha repetida e album2 sem figurinha
                trocaveis2[y] = i + 1
                y += 1

        index = 0
        while trocaveis1[index] > 0 and trocaveis2[index] > 0 and index < len(trocaveis2):
            self.remove(trocaveis2[index])
            self.insere(trocaveis1[index])
            col.remove(trocaveis1[index])
            col.insere(trocaveis2[index])
            index += 1
