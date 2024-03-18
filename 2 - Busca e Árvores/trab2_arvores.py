from __future__ import annotations
from dataclasses import dataclass

#Algumas das funções foram utilizadas para a realização de exemplos. (como remove e insere)

@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore

Arvore = No | None


def remove(t: Arvore, val: int) -> Arvore:
    '''
    Remove um elemento da Arvore, caso esse elemento não pertença, nada acontece.

    Exemplos:
    >>> t = None
    >>> t = remove(t, 3)
    >>> t
    >>> t = insere(t, 3)
    >>> t = insere(t, 1)
    >>> t = insere(t, 5)
    >>> t = insere(t, 2)
    >>> t = insere(t, 4)
    >>> t = insere(t, 6)
    >>> t = remove(t, 3)
    >>> t
    No(esq=No(esq=None, val=1, dir=None), val=2, dir=No(esq=No(esq=None, val=4, dir=None), val=5, dir=No(esq=None, val=6, dir=None)))
    >>> t = remove(t, 5)
    >>> t
    No(esq=No(esq=None, val=1, dir=None), val=2, dir=No(esq=None, val=4, dir=No(esq=None, val=6, dir=None)))
    >>> t = remove(t, 1)
    >>> t
    No(esq=None, val=2, dir=No(esq=None, val=4, dir=No(esq=None, val=6, dir=None)))
    '''

    if t is None:
        return None
    elif val > t.val:
        t.dir = remove(t.dir, val)
        return t
    elif val < t.val:
        t.esq = remove(t.esq, val)
        return t
    else: # val == t.val
        if t.esq is None:
            return t.dir
        elif t.dir is None:
            return t.esq
        else: # possui dois filhos
            m = maximo(t.esq)
            t.val = m #type: ignore  #O mypy não consegue inferir que t.val é um int (caso seja None ele para anteriormente)
            t.esq = remove(t.esq, m) #type: ignore
            return t


def insere(t: Arvore, val: int) -> No:
    '''
    Insere um elemento na Arvore, caso o elemento já pertença, não faz nada.

    Exemplos:
    >>> t = None
    >>> t = insere(t, 3)
    >>> t = insere(t, 1)
    >>> t
    No(esq=No(esq=None, val=1, dir=None), val=3, dir=None)
    >>> t = insere(t, 5)
    >>> t = insere(t, 2)
    >>> t
    No(esq=No(esq=None, val=1, dir=No(esq=None, val=2, dir=None)), val=3, dir=No(esq=None, val=5, dir=None))
    >>> t = insere(t, 4)
    >>> t = insere(t, 6)
    >>> t
    No(esq=No(esq=None, val=1, dir=No(esq=None, val=2, dir=None)), val=3, dir=No(esq=No(esq=None, val=4, dir=None), val=5, dir=No(esq=None, val=6, dir=None)))
    '''

    if t is None:
        return No(None, val, None)
    else:
        if val > t.val:
            t.dir = insere(t.dir, val)
        elif val < t.val:
            t.esq = insere(t.esq, val)
        else: # t.val == val (o valor ja pertence à Arvore)
            pass
        return t
    

def maximo(t:Arvore) -> int | None:
    '''
    Retorna o valor do maior item pertencente à Arvore. Retorna None caso a Arvore seja vazia.

    Exemplos:
    >>> t = No(No(None, 1, No(None, 2, None)), 3, No(None, 5, No(None, 9, None)))
    >>> maximo(t)
    9
    >>> t = None
    >>> maximo(t)
    >>> t = No(No(None, 1, No(None, 2, None)), 3, None)
    >>> maximo(t)
    3
    '''

    if t is None:
        return None
    elif t.dir is None:
        return t.val
    else:
        return maximo(t.dir)
    

def busca(t: Arvore, val: int) -> bool:
    '''
    Busca na Arvore o elemento *val*, retorna true caso o elemento pertença à ela e False caso contrário.

    Exemplos:
    >>> t = No(No(None, 1, No(None, 2, None)), 3, No(None, 5, No(None, 9, None)))
    >>> busca(t, 9)
    True
    >>> busca(t, 2)
    True
    >>> busca(t, 3)
    True
    >>> busca(t, 10)
    False
    '''

    if t is None:
        return False
    elif val > t.val:
        return busca(t.dir, val)
    elif val < t.val:
        return busca(t.esq, val)
    else: #val == t.val
        return True
    

def num_elem(t: Arvore) -> int:
    '''
    Retorna a quantidade de elementos pertencentes à Arvore.

    Exemplos:
    >>> t = None
    >>> num_elem(t)
    0
    >>> for i in range(1, 10):
    ...     t = insere(t, i)
    >>> num_elem(t)
    9
    '''

    if t is None:
        return 0
    else:
        return 1 + num_elem(t.esq) + num_elem(t.dir)
    

def balanceada(t: Arvore) -> True:
    '''
    Retorna True caso a Arvore seja balanceada (A diferença absoluta da altura das subárvores a direita e a esquerda de t é no máximo 1)

    Exemplos:
    >>> t: Arvore = None
    >>> balanceada(t)
    True
    >>> t: Arvore = No(No(No(None, 3, No(None, 4, None)),8, None), 2, No(No(None, 7, None), 3, No(No(None, 2, None), 5, No(None, 6, None))))
    >>> balanceada(t)
    False
    >>> t: Arvore = No(No(No(None, 3, No(None, 4, None)), 8, None), 2, No(No(None, 7, None), 3, No(No(None, 2, None), 5, None)))
    >>> balanceada(t)
    False
    >>> t: Arvore = No(No(No(None,1,None), 3, No(None, 4, None)), 5, No(None, 6, None))
    >>> balanceada(t)
    True
    >>> t: Arvore = No(No(No(None,1,None), 3, No(None, 4, None)), 5, No(None, 6, No(None, 7, None)))
    >>> balanceada(t)
    True
    >>> t: Arvore = No(No(No(None,1,None), 3, No(None, 4, None)), 5, No(None, 6, No(None, 7, No(None, 8, None))))
    >>> balanceada(t)
    False
    '''

    return t is None or abs(altura(t.esq) - altura(t.dir)) <= 1 and balanceada(t.esq) and balanceada(t.dir)
    

def altura(t: Arvore) -> int:
    '''
    Retorna a altura da Arvore.

    Exemplos:
    >>> t: Arvore = No(No(No(None, 3, No(None, 4, None)),8, None), 2, No(No(None, 7, None), 3, No(No(None, 2, None), 5, None)))
    >>> altura(t)
    3
    '''

    if t is None:
        return -1
    else:
        return 1 + max(altura(t.esq), altura(t.dir))
    

def caminhos(t: Arvore) -> list[list[int]]:
    '''
    Retorna uma lista com todos os caminhos da Arvore (raíz até folha). Cada caminho é uma lista de valores dos nós.

    Exemplos:
    >>> t: Arvore = None
    >>> caminhos(t)
    []
    >>> t: Arvore = No(No(No(None, 3, No(None, 4, None)),8, None), 2, No(No(None, 7, None), 3, No(No(None, 2, None), 5, None)))
    >>> caminhos(t)
    [[2, 8, 3, 4], [2, 3, 7], [2, 3, 5, 2]]
    '''

    if t is None:
        return []
    elif t.esq is None and t.dir is None:
        return [[t.val]]
    else:
        return [[t.val] + cam for cam in caminhos(t.esq)] + [[t.val] + cam for cam in caminhos(t.dir)]
    

def busca_arvore(t1: Arvore, t2: Arvore) -> bool:
    '''
    Retorna True se todos os elementos de t1 estão contidos em t2, False caso contrário.

    Exemplos:
    >>> t1: Arvore = None
    >>> t2: Arvore = None
    >>> busca_arvore(t1, t2)
    True
    >>> for i in range(1, 10):
    ...     t1 = insere(t1, i)
    ...     t2 = insere(t2, i)
    >>> busca_arvore(t1, t2)
    True
    >>> t2 = remove(t2, 5)
    >>> busca_arvore(t1, t2)
    False
    '''

    if t1 is None:
        return True
    else:
        return busca(t2, t1.val) and busca_arvore(t1.esq, t2) and busca_arvore(t1.dir, t2)



def array_arvore(arr: list[int]) -> Arvore:
    '''
    Recebe uma lista de inteiros e retorna uma Arvore balanceada 
    (a diferença entre a altura de subarvores no meso nível deve ser de no max 1) contendo esses inteiros.
    
    Exemplos:
    >>> t = array_arvore([])
    >>> t

    >>> balanceada(t)
    True
    >>> t = array_arvore([1, 2, 3, 4, 5])
    >>> t
    No(esq=No(esq=No(esq=None, val=1, dir=None), val=2, dir=None), val=3, dir=No(esq=No(esq=None, val=4, dir=None), val=5, dir=None))
    >>> balanceada(t)
    True

    >>> t = array_arvore([1, 2, 3, 4, 5, 6])
    >>> t
    No(esq=No(esq=No(esq=None, val=1, dir=None), val=2, dir=No(esq=None, val=3, dir=None)), val=4, dir=No(esq=No(esq=None, val=5, dir=None), val=6, dir=None))
    >>> balanceada(t)
    True

    >>> t = array_arvore([1, 2, 4, 5, 6, 30, 70])
    >>> t
    No(esq=No(esq=No(esq=None, val=1, dir=None), val=2, dir=No(esq=None, val=4, dir=None)), val=5, dir=No(esq=No(esq=None, val=6, dir=None), val=30, dir=No(esq=None, val=70, dir=None)))
    >>> balanceada(t)
    True

    Teste:
    Esse teste busca verificar se a função está criando uma árvore balanceada independentemente dos valores passados, 
    para isso, é utilizada a função *balanceada* para verificar em um alto número de listas de tamanho aleatório.
    >>> import random
    >>> for i in range(100):
    ...     t = array_arvore([random.randint(0, 100) for i in range(random.randint(0, 100))])
    ...     if not balanceada(t):
    ...         raise ValueError("A árvore não está balanceada")
    '''

    if arr == []:
        return None
    else:
        return No(array_arvore(arr[:len(arr)//2]), arr[len(arr)//2], array_arvore(arr[len(arr)//2+1:]))
    

def elem_iguais(t1: Arvore, t2: Arvore) -> bool:
    '''
    Retorna True se as duas ABB's possuem os mesmos elementos, False caso contrário..

    Exemplos:
    >>> t1: Arvore = None
    >>> t2: Arvore = None
    >>> elem_iguais(t1, t2)
    True
    >>> for i in range(1, 10):
    ...     t1 = insere(t1, i)
    ...     t2 = insere(t2, i)
    >>> elem_iguais(t1, t2)
    True
    >>> t2 = remove(t2, 5)
    >>> elem_iguais(t1, t2)
    False

    #t2 é None e t1 não
    >>> t2 = None
    >>> elem_iguais(t1, t2)
    False
    
    #t1 é None e t2 não
    >>> t1 = None
    >>> for i in range(1, 5):
    ...     t2 = insere(t2, i)
    >>> elem_iguais(t1, t2)
    False

    #Arvores com elementos iguais e estruturas diferentes
    >>> t1: Arvore = None
    >>> t2: Arvore = None
    >>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> t1 = array_arvore(lista) #Arvore balanceada
    >>> for i in lista:
    ...     t2 = insere(t2, i)  #Arvore com os mesmos elementos, mas não balanceada
    >>> elem_iguais(t1, t2)
    True

    #t2 > t1
    >>> t1: Arvore = None
    >>> t2: Arvore = None
    >>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> for i in lista:
    ...     t1 = insere(t1, i)
    ...     t2 = insere(t2, i)
    >>> t1 = remove(t1, 5)
    >>> num_elem(t1) == num_elem(t2)
    False
    >>> elem_iguais(t1, t2)
    False

    #t1 > t2
    >>> t1: Arvore = None
    >>> t2: Arvore = None
    >>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> for i in lista:
    ...     t1 = insere(t1, i)
    ...     t2 = insere(t2, i)
    >>> t2 = remove(t2, 5)
    >>> num_elem(t1) == num_elem(t2)
    False
    >>> elem_iguais(t1, t2)
    False
    '''

    return num_elem(t1) == num_elem(t2) and busca_arvore(t1, t2)


def caminhos_maximos(t: Arvore) -> list[list[int]]:
    '''
    Projete uma função que encontre todos os caminhos de tamanho máximo, partindo da raiz, em uma árvore binária.
    Dica: faça duas funções, uma para encontrar a altura da árvore e outra para encontrar os caminhos. Cada caminho
    deve ser dado como uma lista de valores dos nós

    Exemplos:
    >>> t: Arvore = No(No(No(None, 3, No(None, 4, None)),8, None), 2, No(No(None, 7, None), 3, No(No(None, 2, None), 5, None)))
    >>> caminhos_maximos(t)
    [[2, 8, 3, 4], [2, 3, 5, 2]]
    >>> t = No(None, 5, None)
    >>> caminhos_maximos(t)
    [[5]]
    >>> t = No(No(None, 5, None), 3, None)
    >>> caminhos_maximos(t)
    [[3, 5]]
    >>> t = No(No(None, 5, None), 3, No(None, 7, None))
    >>> caminhos_maximos(t)
    [[3, 5], [3, 7]]
    >>> t = No(No(No(None, 5, None), 3, None), 2, No(None, 7, None))
    >>> caminhos_maximos(t)
    [[2, 3, 5]]
    >>> t = No(No(No(None, 5, None), 3, None), 2, No(None, 7, No(None, 8, None)))
    >>> caminhos_maximos(t)
    [[2, 3, 5], [2, 7, 8]]
    '''

    cam_final = []
    if altura(t) >= 0:
        for i in caminhos(t):
            if len(i) == altura(t) + 1:
                cam_final.append(i)
    return cam_final
