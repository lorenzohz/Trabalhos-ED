from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Associacao:
    "Associacao entre chave e valor. A"
    chave: str
    valor: int

class Dicionario:
    '''
    Uma coleção de chaves únicas associadas com valores.

    Exemplos

    >>> d = Dicionario()
    >>> d.num_itens()
    0
    >>> d.associa('Jorge', 25)
    >>> d.associa('Bia', 40)
    >>> d.num_itens()
    2
    >>> d.get('Jorge')
    25
    >>> d.get('Bia')
    40
    >>> d.get('Andre') is None
    True
    >>> d.associa('Bia', 50)
    >>> d.get('Bia')
    50
    >>> d.remove('Jorge')
    >>> d.get('Jorge') is None
    True
    >>> d.remove('Ana')
    >>> d.num_itens()
    1

    Testes

    O teste a seguir cria uma lista com uma permutação dos números de 0 a 99 e
    cria um dicionário adicionando cada número (string) como chave associada
    com o próprio número.

    Em seguida, para cada número da lista o get é executado para verificar se a
    associação está correta. Depois a associação é removida e todas as outras
    associações são verificadas.

    >>> import random
    >>> lst = list(range(100))
    >>> random.shuffle(lst)
    >>> d = Dicionario()
    >>> # Faz associação
    >>> for valor in lst:
    ...     d.associa(str(valor), valor)
    >>> for i in range(len(lst)):
    ...     # Associação original
    ...     assert d.get(str(i)) == i
    ...     # Modifica a associação e verifica
    ...     d.associa(str(i), 2 * i)
    ...     assert d.get(str(i)) == 2 * i
    ...     # Remove a associação e verifica
    ...     d.remove(str(i))
    ...     assert d.get(str(i)) is None
    ...     # As associações que não foram removidas permanecem as mesmas?
    ...     for j in range(i + 1, len(lst)):
    ...         assert d.get(str(j)) == j
    '''
    tabela: list[list[Associacao] | None]
    fator_carga: int

    def __init__(self) -> None:
        '''
        Cria um novo dicionário vazio.
        '''
        self.tabela = [None] * 10
        self.fator_carga = 0

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de chaves no dicionário.
        '''
        total = 0
        for i in range(len(self.tabela)):
            if self.tabela[i] is not None:
                total += len(self.tabela[i]) #type:ignore
        return total

    def associa(self, chave: str, valor: int):
        '''
        Associa a *chave* com o *valor* no dicionário. Se *chave* já está
        associada com um valor, ele é sustituído por *valor*.
        '''
        i = self._mapeia(chave)
        if self.tabela[i] is None: # Cria uma nova lista
            self.fator_carga += 1
            self.tabela[i] = [Associacao(chave, valor)]
            if self.fator_carga >= (7 * len(self.tabela) // 10): # Redimensiona a tabela
                self._redimensiona()
        else: 
            for assoc in self.tabela[i]: #type:ignore  # Procura a chave na lista
                if assoc.chave == chave: # Substitui o valor
                    assoc.valor = valor
                    return
            self.tabela[i].append(Associacao(chave, valor)) #type:ignore  # Adiciona a associação na lista

    def get(self, chave: str) -> int | None:
        '''
        Devolve o valor associado com *chave* no dicionário ou None se a chave
        não está no dicionário.
        '''
        i = self._mapeia(chave)
        if self.tabela[i] is not None:
            for assoc in self.tabela[i]: #type:ignore
                if assoc.chave == chave:
                    return assoc.valor
        return None

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado com ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.
        '''
        i = self._mapeia(chave)
        if self.tabela[i] is not None:
            if len(self.tabela[i]) == 1 and self.tabela[i][0].chave == chave: #type:ignore
                self.tabela[i] = None
                self.fator_carga -= 1
                if self.fator_carga < (len(self.tabela) // 8):
                    self._redimensiona()
            elif len(self.tabela[i]) > 1: #type:ignore
                Removeu = False
                j = 0
                while j < len(self.tabela[i]) and not Removeu: #type:ignore
                    if self.tabela[i][j].chave == chave: #type:ignore
                        self.tabela[i].pop(j) #type:ignore
                        Removeu = True
                    j += 1

    def _mapeia(self, chave: str) -> int:
        '''
        Devolve o índice da *chave* na tabela de dispersão.
        O mapeamento é feito com a função hash da chave e o tamanho da tabela, onde usamos o resto da divisão.
        '''
        return hash(chave) % len(self.tabela)

    def _redimensiona(self):
        '''
        Redimensiona a tabela de dispersão. Caso a tabela atual tenha um fator de carga > len(tabela) // 2, a tabela é redimensionada para o dobro do tamanho atual.
        Caso o fator de carga seja < len(tabela) // 8, a tabela é redimensionada para a metade do tamanho atual.
        '''
        if self.fator_carga >= (7 * len(self.tabela) // 10):
            nova_tabela = [None] * (len(self.tabela) * 2)
        elif self.fator_carga < (len(self.tabela) // 8) and len(self.tabela) > 10: # Evita que a tabela seja redimensionada para um tamanho menor que 10
            nova_tabela = [None] * (len(self.tabela) // 2)
        else:
            return

        for i in range(len(self.tabela)):
            if self.tabela[i] is not None:
                for assoc in self.tabela[i]:
                    j = hash(assoc.chave) % len(nova_tabela) # Mapeia a chave na nova tabela
                    if nova_tabela[j] is None:
                        nova_tabela[j] = [assoc]
                    else:
                        nova_tabela[j].append(assoc)
        
        self.tabela = nova_tabela
    
