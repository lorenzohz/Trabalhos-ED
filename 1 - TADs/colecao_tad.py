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
        pass


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
        pass


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
        pass


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
        return ''
    

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
        return ''
    

    def troca(self, colecionador: 'Colecao') -> None:
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
        '''
        pass

    