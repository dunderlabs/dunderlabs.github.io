title: Python Comprehensions
date: 2015-01-30 02:25
author: Patrick Mazulo
slug: python-comprehensions
category: python
tags: python, iterators, list comprehensions, translations
summary: Neste 1º post da série Pythonista Intermediário vamos mostrar o que são e como funcionam as lists comprehensions em Python.
email: pmazulo@gmail.com
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/list1.jpg

![Créditos da imagem]({filename}/images/posts/list1.jpg)

Créditos da imagem: <https://datasciencelab.wordpress.com/2014/01/08/list-comprehension-in-python/>

Python comprehensions são construções sintáticas que permitem que
sequências sejam construídas a partir de outras sequências de forma
clara e concisa. Existem três tipo de Python comprehensions:

1.  list comprehensions,
2.  set comprehenscions, e
3.  dict comprehensions.

Construções de list comprehensions tem sido parte do Python desde a
versão 2.0, enquanto set e dict comprehensions só a partir do Python
2.7.

### List Comprehensions

List comprehensions são de longe a construção de comprehensions mais
popular. List comprehensions fornecem uma maneira concisa de criar uma
nova lista de elementos que satisfazem uma dada condição a partir de um
**iterável**. Um **iterável** é qualquer construção python que possa ser
posto/iterado em um loop. Exemplos de iteráveis embutidos incluem lists,
sets e tuples. O exemplo abaixo da [Documentação
Python](https://docs.python.org/2/tutorial/datastructures.html) ilustra
o uso de list comprehensions. Neste exemplo, nós queremos criar uma
lista com os números elevado ao quadrado de 0 a 10. Uma maneira
convencional de criar esta lista sem comprehensions é mostrada abaixo:

 

````shell
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
````

A mesma lista pode ser criada de uma maneira mais concisa usando list
comprehensions, como abaixo:

````shell
>>> squares = [x**2 for x in range(10)]
````

A versão com comprehension parece ser obviamente mais clara e concisa do
que o método convencional.

De acordo com a documentação python, **uma list comprehension consiste
de colchetes contendo uma expressão seguida por uma ou mais cláusulas 
*for* ou cláusulas *if,* como mostrado abaixo**.

````
[expression for item1 in iterable1 if condition1 
            for item2 in iterable2 if condition2
            ...
            for itemN in iterableN if conditionN ]
````

O resultado é uma nova lista resultante da avaliação da expressão no
contexto das cláusulas *for* e *if* em seguida. Por exemplo, para criar
uma lista com o quadrado dos números pares entre 0 e 10, a seguinte
comprehension é usada:

````shell
>>> even_squares = [i**2 for i in range(10) if i % 2 == 0]
>>> even_squares
[0, 4, 16, 36, 64]
````

A expressão i\*\*2 é computada no contexto da cláusula *for* que itera
sobre os número de 0 a 10, e a cláusula *if*  filtra os números não
pares.

### Loops *for* aninhandos numa list comprehensions

List comprehensions também podem ser usadas com múltiplos ou loops *for*
aninhados. Considerando, por exemplo, o simples fragmento de código
mostrado logo abaixo que cria uma tupla de pares de números extraídos
das duas sequências apresentadas.

````shell
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
````

O código acima pode ser reescrito de uma maneira mais simples e concisa,
como demonstrado abaixo usando list comprehensions.

````shell
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
````

É importante levar em consideração em como a ordem dos loops *for* foi
usada nesta list comprehension. A observação cuidadosa dos trechos de
código usando comprehension e aquele sem comprehension mostra que a
ordem dos loops *for* na comprehension seguiu a mesma ordem, como se
tivesse sido escrita sem comprehensions. O mesmo se aplica para loops
*for* aninhados com profundidade maior que 2 loops.

### List Comprehensions Aninhadas

List comprehensions também podem ser aninhadas. Considere o seguinte
exemplo extraído da documentação python, de uma matriz 3x4 implementada
como uma lista de 3 listas de tamanho 4:

````shell
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
````

Transposição é uma operação das matrizes que cria uma nova matriz a
partir de uma velha, usando as linhas da matriz velha como as colunas da
matriz nova, e as colunas da matriz velha como as linhas da matriz nova.
As linhas e colunas da matriz precisam ser transpostas usando a seguinte
list comprehension:

````shell
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
````

O código acima é equivalente ao trecho dado abaixo:

````shell
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
````

 

### Set comprehensions

Set comprehensions foram adicionado ao python na versão 2.7. Em set
comprehensions, nós usamos chaves ao invés de colchetes. Por exemplo,
para criar o set do quadrado de todos os números entre 0 e 10, o
seguinte set comprehension pode ser usado em vez do loop normal:

````shell
>>> x = {i**2 for i in range(10)}
>>> x
set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])
>>>
````

 

### Dict Comprehension

Assim como set comprehensions, dict comprehensions foram adicionados ao
python na versão 2.7. Abaixo nós criamos um mapping, sendo as chaves os
números entre 0 e 10, e os valores seus quadrados, usando dict
comprehensions.

````shell
>>> x = {i:i**2 for i in range(10)}
>>> x
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
````

 

###  Leitura complementar

1.  [Documentação Python](https://docs.python.org/2/tutorial/datastructures.html)
2.  Python Essential Reference, Fourth Edition
3.  [Python 3 Patterns, Recipes and Idioms](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Comprehensions.html)

[Clique aqui para voltar para a tabela de conteúdo.]({filename}/pages/pythonista-intermediario.md)

 
