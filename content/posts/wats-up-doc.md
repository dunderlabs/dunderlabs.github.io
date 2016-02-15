title: Wat's up, doc?
date: 2016-02-15 10:48
author: Patrick Mazulo
slug: wats-up-doc
category: python
tags: python, python wat, translations
summary: Voltando com as traduções, veremos aqui um post que explica sobre alguns "Wat?!" do Python, baseado na [palestra do Gary Bernhardt sobre JavaScript](https://www.destroyallsoftware.com/talks/wat)
email: pmazulo@gmail.com
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/wat.jpg

![Créditos para a imagem]({filename}/images/posts/wat.jpg)

Créditos para a imagem: <http://www.b-list.org/weblog/2015/nov/15/real-python-wat/>

### Wat's up, doc?
No mesmo rumo da [maravilhosa palestra do Gary Bernhardt sobre JavaScript](https://www.destroyallsoftware.com/talks/wat), há também uma [coleção de momentos de Python "wat"](https://github.com/cosmologicon/pywat) que muitas vezes aparecem por aí. Há também um questionário relacionado na página deste último link (que não vou dar spoiler; você pode ler ele e checar suas respostas). Toda linguagem tem algumas partes não intuitivas — ou, no mínimo, aparentemente não. Mas se você está trabalhando com Python, entender _porque_ esses pedaços de código se comportam dessa maneira é interessante, e potencialmente útil (OK, provavelmente não útil, mas no mínimo interessante). Então vamos dar uma olhada neles e ver o que realmente está acontecendo.

**"Convertendo para uma string e vice-versa"**

O exemplo é este:

````python
>>> bool(str(False))
True
````

Esta é uma muito simples: `str(False)` é `"False"`, e `bool("False")` é `True`, porque qualquer string não vazia é `True` ("truthy", se quiser ser preciso, uma vez que a checagem boolean do Python raramente usa instancias reais de `bool`).

**"Misturar strings com inteiros"**

O exemplo:

````python
>>> int(2 * 3)
6
>>> int(2 * '3')
33
>>> int('2' * 3)
222
````

Esse é um caso um pouco mais interessante, e leva as pessoas a discutirem sobre o sistema de tipos do Python. O comportamento neste caso vem do fato que Python suporta sobrecarga de operador, e não restringe quais tipos você está permitido definir que seus operadores atuem. Neste caso, o operador * está implementado nos tipos numéricos, onde é o operador de multiplicação (e, obviamente, exige que o outro operando seja um número). Mas é também implementado nos tipos sequenciais (lembre, `str` é um tipo sequencial em Python), onde é um operador de repetição e exige que o outro operando seja numérico.

Então, quando usar este operador com um operando numérico e outro operando que é sequencial, Python aplica o comportamento de repetição.

**"O operador de conversão implícita não documentado"**

Hora de brincar:

````python
>>> False ** False == True
True
>>> False ** True == False
True
>>> True ** False == True
True
>>> True ** True == True
True
````

Entender esse requer saber um pouco da história do Python. Inicialmente não havia o tipo boolean built-in (como em muitas das outras linguagens que carecem do tipo boolean), então a convenção era usar o inteiro 1 como o valor "true" e o inteiro 0 como "false". Python 2.2.1 trouxe `bool()` como uma função built-in, mas não o tipo boolean — em vez disso, ele definiu `True` e `False` como alias (apelidos) built-in para 1 e 0. A função `bool()` retornaria 1 para valores "True" e 0 para "False". Python 2.3 implementou o tipo `bool`, como uma sub-classe de `int` com apenas duas instâncias: `True` e `False`, que teriam valores inteiros 1 e 0. Esse comportamento acabou ficando preso para o Python 3, como você pode verificar abaixo:

````python
$ python
Python 3.5.0 (default, Sep 26 2015, 18:41:42)
[GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.53)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> issubclass(bool, int)
True
>>> isinstance(True, int)
True
>>> isinstance(False, int)
True
>>> True + True
2
>>> True - False
1
````

Para mais detalhes sobre essa esquisitice em torno da introdução do tipo `bool`, veja esse [post do Guido](http://python-history.blogspot.com/2013/11/the-history-of-bool-true-and-false.html).

**"Combinação dos tipos numéricos"**

````python
>>> x = (1 << 53) + 1
>>> x + 1.0 < x
True
````

O autor diz "Note: isso não é simplesmente devido a imprecisão de ponto flutuante."
O que é tecnicamente verdade, eu acho, mas um pouco enganador: o truque aqui é empurrar a faixa no qual um float de dupla precisão pode representar cada inteiro (o deslocamento do 53º bit, como floats de dupla precisão têm apenas 53 bits de precisão). Se você brincar com ele, vai descobrir que só tem números anteriores esse ponto, como esperado para esta faixa: no IEEE 754, de `2**51` a `2**52`, floats de dupla precisão são espaçados por 0.5, passando a serem espaçados por 1 — isto é, todos inteiros e apenas inteiros pode ser representados — acima de `2**53`, e além `2**53` eles são espaçados por 2, de modo que apenas inteiros pares possam ser reprensentados.

**"Precedência de operador?"**

````python
>>> False == False in [False]
True
````

Isso não é exatamente sobre precedência; em vez disso, é sobre suporte do Python a operadores de comparação encadeados. Estamos acostumados a poder fazer coisas como `if x< y <= z` em Python, e estamos com isso fazendo contruções como esta. Esse encadeamento de operadores é equivalente a `if (x < y) and (y <= z)`, mas com `y` sendo avaliado só na primeira.

E uma vez que `==` e `in` são operadores de comparação, o mesmo acontece aqui: `False == False in [False]` é equivalente a `(False == False) and (False in [False])`. Ambas comparações são verdadeiras, então o resultado polêmico está correto.

**"Tipo iteráveis em comparação"**

````python
>>> a = [0, 0]
>>> (x, y) = a
>>> (x, y) == a
False

>>> [1,2,3] == sorted([1,2,3])
True
>>> (1,2,3) == sorted((1,2,3))
False
````

Esse tem um alcance maior. O que realmente está acontecendo no primeiro exemplo é que `a` é uma lista, e `(x, y)` é uma tupla. Uma lista e uma tupla não serão idênticas quando comparadas, mesmo se seus conteúdos forem iguais. De igual modo, `sorted()` retorna uma lista, então você só vai ter uma comparação de igualdade bem sucedida quando comparar o resultado com uma lista.

**"Tipos de operações aritméticas"**

````python
>>> type(1) == type(-1)
True
>>> 1 ** 1 == 1 ** -1
True
>>> type(1 ** 1) == type(1 ** -1)
False
````

Python permite que comparações aritméticas de floats e ints funcionem, então `1 == 1.0` (e `1 ** -1` é igual a `1.0` — expoentes negativos sempre retornam um valor float). Mas `int` e `float` não são do mesmo tipo, então a igualdade de tipo dará falso.

**"Brincando com iteradores"**

````python
>>> a = 2, 1, 3
>>> sorted(a) == sorted(a)
True
>>> reversed(a) == reversed(a)
False

>>> b = reversed(a)
>>> sorted(b) == sorted(b)
False
````

Novamente, esta é uma brincadeira com tipos. A função built-in `sorted()` do Python recebe uma sequência, e retorna uma lista contendo os mesmos valores ordenados. Mas `reversed()` retorna um objeto iterador que vai percorrer a sequência na ordem reversa.

O iterador retornado pela função `reversed()` não implementa o método `__eq__()`, então para comparações Python volta para chamar `__hash__()` em cada operando e compara os resultados. O iterador também não implementa `__hash__()`, então ele pega a implementação padrão de `object`, que por sua vez é derivada do endereço de memória do objeto. Uma vez que duas diferentes instâncias de iteradores tem endereços de memória diferentes, o resultado de duas chamadas a `reversed()` na mesma sequência irá comparar como desigual.

A comparação dos resultados de `sorted()` no segundo exemplo é mais complicado: a primeira chamada para `sorted()` consome o iterador retornado pelo `reversed()` e produz a lista ordenada `[1, 2, 3]`. Mas a segunda chamada para `sorted()` não tem mais nada para consumir, e retorna uma lista vazia `[]`, e é o caso em que `[1, 2, 3] != []`;

**"Tipos circulares"**

````python
>>> isinstance(object, type)
True
>>> isinstance(type, object)
True
````

Isso é uma daquelas coisas :)

**"extend vs +="**

````python
>>> a = ([],)
>>> a[0].extend([1])
>>> a[0]
[1]
>>> a[0] += [2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> a[0]
[1, 2]
````

Python não vai permitir você atribuir diretamente aos índices de uma tupla, seja através da sintaxe normal ou aumentada (+= e similares). Mas ele vai deixar você chamar métodos dos objetos na tupla, e se acontecer desses objetos serem mutáveis e deles definirem métodos que permitem você mudá-los sem usar sintaxe de atribuição, vai funcionar.

**“Indexando com floats”**

````python
>>> [4][0]
4
>>> [4][0.0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers, not float
>>> {0:4}[0]
4
>>> {0:4}[0.0]
4
````

Esse é um pouco sorrateiro: os dois primeiros exemplos usam uma lista, e índices de listas devem ser inteiros. Os outros dois exemplos usam um dicionário, e qualquer tipo "hasheável" pode servir como uma chave de dicionário.

Quanto ao motivo de `0` e `0.0` devolverem o mesmo valor, não estou 100% certo disso (como não tenho analisado a implementação de dicionário do CPython ultimamente), mas eu acredito que a prevenção de colisões permitem que duas chaves peguem o mesmo valor do dicionário se eles tem o mesmo hash e são comparados iguais (e uma vez que `hash(0) == hash(0.0)` e `0 == 0.0` você tem o resultado no exemplo).

**"tudo e vazio"**

````python
>>> all([])
True
>>> all([[]])
False
>>> all([[[]]])
True
````

Complicado, né? O argumento para `all()` é uma sequência. Então no primeiro exemplo, nós estamos pedindo para ele avaliar uma sequência vazia; `all()` está definido para retornar `True` para uma sequência vazia. O segundo exemplo tem uma sequência contendo um item — uma lista vazia — que é avaliado como `False`, então retorna `False`. O terceiro pega uma sequência contendo um item — uma lista contendo uma lista vazia — que é avaliada como `True` (porque a lista contendo a lista vazia é por si só não vazia), e então retorna `True`.

**“sum and strings”**

````python
>>> sum("")
0
>>> sum("", ())
()
>>> sum("", [])
[]
>>> sum("", {})
{}
>>> sum("", "")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() can't sum strings [use ''.join(seq) instead]
````

Esse é outra onde uma rápida olhada na documentação da função revela o que está acontecendo.

Quando dá-se uma sequência vazia, `sum()` retornará 0, e a string vazia é uma sequência vazia. Quando dado dois argumentos, `sum()` trata o segundo argumento como um valor acumulador inicial para retornar quando a sequência fornecida é vazia (de fato, a definição dessa função é `sum(sequence, start=0)` então realmente, no caso de uma sequência vazia com um argumento, ela está apenas retornando o valor padrão de `start`); isso que está acontecendo no segundo, terceiro e quarto exemplos. No quinto exemplo, `sum()` reclama que não funciona com um valor string para o segundo parâmetro, uma vez que `sum()` está definido para ser capaz de rejeitar tipos não numéricos.

Há outro "wat": `sum()` apenas checa o tipo do seu segundo argumento (se você quiser verificar, é a função `builtin_sum()` no Python 2, e `builtin_sum_impl()` no Python 3, e em ambas as versões está localizado em `Python/bltinmodule.c` na árvore de código fonte). No Python 2, ele curto-circuita com um `TypeError` se o segundo argumento é uma instância de `basestring`; no Python 3 ele curto-circuita com `TypeError` quando o segundo argumento é uma instância de `str`, `bytes` ou `bytearray`.

Mas ele nunca checa o tipo do primeiro argumento, ou dos itens na sequência (se for uma sequência); ela simplesmente confia no fato que iteração em um tipo não sequencial lança uma exceção `TypeError`, e adição de uma string para um inteiro vai levantar um `TypeError` (o último porque você não pode passar um valor do tipo string para o segundo argumento, e esse argumento é padrão 0 quando não especificado).

**“Comparing NaNs”**

````python
>>> x = 0*1e400  # nan
>>> len({x, x, float(x), float(x), 0*1e400, 0*1e400})
3
>>> len({x, float(x), 0*1e400})
2
````

`NaN` é estranho. IEEE 754 nos fala que comparações com `NaN` são desordenadas; `NaN` não é nem maior, menor ou igual a qualquer valor de ponto flutuante, incluindo ele mesmo.

Então, na primeira chamada de `len()`, em teoria nós devemos esperar 6 como resposta; todos os valores são `NaN` e nenhum deles são iguais aos outros, de modo que o conjunto literal não deve suprimir qualquer valor duplicado. De igual modo, a segunda chamada de `len()` deveria retornar 3.

O que realmente parece estar acontecendo é que Python está considerando `x` e `x` serem valores duplicados, `float(x)` e `float(x)` também serem valores duplicados, e `0*1e400` and `0*1e400` serem valores "distintos". ~~O porque eu não tenho certeza. Eu acredito que é possível que esteja acontecendo algum tipo complicado de avaliação única, mas isso exigiria Python saber `float(x)` sempre retorna o mesmo valor para o mesmo `x` (e neste caso não é verdade no caso que ambas as chamadas retornam valores `NaN` que são desiguais).~~

*Edit*: [um comentário no reddit acertou na solução](https://www.reddit.com/r/Python/comments/3ojwf9/explaining_the_python_wats/cvxxto3). Python parece estar usando o identificador como um curto-circuito otimizado para evitar fazer uma checagem de igualdade potencialmente custosa. E realmente, ambos `x is x` e `float(x) is float(x)` retornam `True` com `x = 0*1e400`, mas `0*1e400 is 0*1e400` retorna `False`. Se alguém mais quiser se divertir um pouco mais, dê uma olhada em _porquê_ `*1e400 is not 0*1e400` retorna `True`.



**_Viu algum trecho que poderia ficar com uma tradução melhor? Manda lá nos comentários mais abaixo. Valeu pessoal, e até a próxima!_**


Referências:

- [Post original](http://www.b-list.org/weblog/2015/oct/13/wats-doc/)


