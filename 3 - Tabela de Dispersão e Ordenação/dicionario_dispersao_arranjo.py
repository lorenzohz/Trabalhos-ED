from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Associacao:
    " Associacao entre chave e valor."
    chave: str
    valor: int

class Dicionario:
    '''
    Uma coleção de chaves únicas associadas com valores.

    Exemplos:

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
    tabela: list[list[Associacao]]
    numero_elem: int

    def __init__(self) -> None:
        '''
        Cria um novo dicionário vazio.
        '''
        self.tabela = [[] for _ in range(10)]
        self.numero_elem = 0

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de chaves no dicionário.
        '''
        return self.numero_elem

    def associa(self, chave: str, valor: int):
        '''
        Associa a *chave* com o *valor* no dicionário. Se *chave* já está
        associada com um valor, ele é sustituído por *valor*.
        '''
        i = self._mapeia(chave)
        for j in self.tabela[i]:
            if j.chave == chave:
                j.valor = valor
                return
        self.numero_elem += 1
        self.tabela[i].append(Associacao(chave, valor))
        self._redimensiona()

    def get(self, chave: str) -> int | None:
        '''
        Devolve o valor associado com *chave* no dicionário ou None se a chave
        não está no dicionário.
        '''
        i = self._mapeia(chave)
        if self.tabela[i] != []:
            for assoc in self.tabela[i]:
                if assoc.chave == chave:
                    return assoc.valor
        return None

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado com ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.
        '''
        i = self._mapeia(chave)
        if self.tabela[i] != []:
            for assoc in self.tabela[i]:
                if assoc.chave == chave:
                    self.tabela[i] = [assoc for assoc in self.tabela[i] if assoc.chave != chave]
                    self.numero_elem -= 1
                    self._redimensiona()
                    return

    def _mapeia(self, chave: str) -> int:
        '''
        Devolve o índice da *chave* na tabela de dispersão.
        O mapeamento é feito com a função hash da chave e o tamanho da tabela, onde usamos o resto da divisão.
        '''
        return hash(chave) % len(self.tabela)

    def _redimensiona(self):
        '''
        Redimensiona a tabela de dispersão. Caso a tabela atual tenha um fator de carga > 0.7, a tabela é redimensionada para o dobro do tamanho atual.
        Caso o fator de carga seja < 0.125 e o len(self.tabela > 10), a tabela é redimensionada para a metade do tamanho atual.
        '''
        if self._fator_carga() > 0.7:
            nova_tabela = [[] for _ in range(len(self.tabela) * 2)]
        elif self._fator_carga() < 0.125 and len(self.tabela) > 10:
            nova_tabela = [[] for _ in range(len(self.tabela) // 2)]
        else:
            return
        for lista in self.tabela:
            for assoc in lista:
                i = hash(assoc.chave) % len(nova_tabela)
                nova_tabela[i].append(assoc)
        self.tabela = nova_tabela

    def _fator_carga(self) -> float:
        '''
        Devolve o fator de carga da tabela de dispersão.
        '''
        return self.numero_elem / len(self.tabela)
        
    def __repr__(self) -> str:
        '''
        Devolve uma representação da tabela de dispersão.
        '''
        return self.tabela.__repr__()
