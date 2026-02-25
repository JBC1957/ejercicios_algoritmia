# ## Algoritmia
# ### Práctica 1
# El objetivo de esta práctica es trabajar con iteradores y generadores.


# Se pide la implementación de las funciones que aparecen a continuación. 
# 
# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada. 
# 
# Para cada función que se pide se proporciona una función con algunos tests. 
# 
# Al llamar a las funciones de test no debería saltar ninguna aserción.


# Importaciones
from itertools import chain, count, cycle, repeat, zip_longest
import collections

# ### Iterador con sustitución

def iterador_con_sustitucion(iterable, cambios):
    """
    Dado un iterable genera sus valores una vez aplicadas las sustituciones 
    indicadas por el diccionario de cambios.
    Los valores no hay que devolverlos todos a la vez, se deben generar de uno 
    en uno.
    """
    for elemento in iterable:
        if elemento in cambios:
            yield cambios[elemento]
        else:
            yield elemento


# ### Iterador anidado

def iterador_anidado(elemento):
    """
    Iterador que genera los valores en elemento recursivamente: si elemento no 
    es iterable genera solo elemento, pero si elemento es iterable genera sus
    elementos de manera recursiva.
    Los valores se deben generar de uno en uno.
    """

    if not isinstance(elemento, collections.abc.Iterable):
        yield elemento
    else:
        for e in elemento:
            for i in iterador_anidado(e):
                yield i
            # yield from iterador_anidado(e)

# ### Generador de media móvil


def generador_media_movil(iterable, longitud):
    """
    Dado un iterable de valores numéricos, genera los valores de la media móvil 
    de la longitud indicada.
    Por ejemplo, si la longitud es 3, generaría la media de los 3 primeros
    valores, de los valores del 2º al 4º, de los valores del 3º al 5º...
    Los valores se deben generar de uno en uno.
    """ 

    suma = 0
    ventana = []
    for e in iterable:
        ventana.append(e)
        suma += e
        if len(ventana) > longitud:
            suma -= ventana.pop(0)
        if len(ventana) == longitud:
            yield suma / longitud



# ### Iterador Incluido

def iterador_incluido(itera_1, itera_2):
    """
    Dado un primer iterador o iterable, comprueba que sus elementos están
    incluidos en el mismo orden en los elementos de un segundo iterador o 
    iterable.
    """
    
    it_1 = iter(itera_1)
    it_2 = iter(itera_2)
    for e in it_1:
        try:
            while next(it_2) != e:
                pass
        except StopIteration:
            return False
    return True



# ### Secuencia generalizada de Fibonacci
# En la secuencia de Fibonacci, cada valor se obtiene sumando los dos anteriores. Se considera una generalización en la que cada valor se obtiene sumando los *k* anteriores:
# - F(0) = ... = F(k-1) = 1
# - F(n) = F(n-1) + ... + F(n-k+1)

def fibonacci_generalizado(k, iniciales = None):
    """
    Genera indefinidamente valores de la secuencia generalizada de Fibonacci.
    Cada valor, salvo los iniciales, es la suma de los k anteriores.
    Los valores iniciales, que deben ser k, son los valores de F(0) ... F(k-1).
    El valor por defecto de los valores iniciales es 1.
    El espacio de memoria utilizado debería ser O(k)
    """

    if iniciales is None:
        iniciales = [1] * k

    iniciales = list(iniciales)

    yield from iniciales
    while True:
        last = sum(iniciales)
        iniciales.append(last)
        iniciales.pop(0)
        yield last



# ### Iterador repetido

def iter_repetido(itera, repeticiones):
    """
    Genera los elementos del primer argumento tantas veces como el elemento 
    correspondiente del segundo argumento.
    Se espera que los elementos del segundo argumento sean números naturales.
    El primer elemento del primer argumento se genera tantas veces como el 
    primer elemento del segundo argumento, ... el elemento i-ésimo del primer 
    argumento se genera tantas veces como el elemento i-ésimo del segundo
    argumento...
    Si el número de elementos de los dos argumentos fuera diferente, se
    generarán elementos hasta que uno se quede sin elementos.
    """

    from itertools import repeat

    for e, r in zip(itera, repeticiones):
        yield from repeat(e, r)


# ### Mezcla de iteradores ordenados

def iter_mezcla(iter_1, iter_2):
    """
    Dados dos iteradores o iterables, suponiendo que ambos generan valores en
    orden, se generan los elementos de ambos de manera ordenada.
    La cantidad de memoria usada debe ser O(1).
    """

    iter_1 = iter(iter_1)
    iter_2 = iter(iter_2)

    e1 = next(iter_1, None)
    e2 = next(iter_2, None)

    while e1 is not None and e2 is not None:
        if e1 < e2:
            yield e1
            ei = next(iter_1, None)
        else:
            yield e2
            e2 = next(iter_2, None)
    else:
        if e1 is not None:
            yield e1
            yield from iter_1
        elif e2 is not None:
            yield e2
            yield from iter_2





