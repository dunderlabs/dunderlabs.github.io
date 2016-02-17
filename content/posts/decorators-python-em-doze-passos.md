title: Python decorators em 12 passos fáceis
date: 2016-02-17 12:06
author: Patrick Mazulo
slug: decorators-python-em-doze-passos
category: python
tags: python, python decorators, decorators, translations
summary: Já usou decorators mas ainda não sabe o que é? Neste artigo que traduzimos Simeon Franklin explica sobre o que são e como criá-los em 12 passos bem fáceis.
email: pmazulo@gmail.com
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/decorator2.jpg

![Créditos para a imagem]({filename}/images/posts/decorator2.jpg)

Créditos para a imagem: <http://slideplayer.com.br/slide/4928758/>

## Entendendo Python decorators em 12 passos fáceis!

Ok, talvez eu esteja brincando. Como um instrutor Python, entender decorators é um tópico onde acho estudantes lutando constantemente após a primeira exposição ao assunto. O motivo é que decorators são difíceis de entender! Entendê-los requer compreender vários conceitos de programação funcional bem como se sentir confortável com algumas funcionalidades únicas da definição de função do Python e sintaxe de chamada de função. *Usar* decorators é fácil (veja na Seção 10)! Mas escrevê-los pode ser complicado.

Eu não posso tornar os decorators fáceis - mas talvez ao caminharmos por cada pedaço desse puzzle, um passo de cada vez, eu possa ajudar você a se sentir mais confiante em entender decorators. Pelo motivo de decorators ser um assunto complexo, esse artigo vai ser longo - mas desista dele! Eu prometo fazer cada pedaço tão simples quanto possível - e se você entender cada pedaço, vai entender como decorators funcionam! Estou tentando assumir mínimo conhecimento de Python mas esse artigo provavelmente vai ser mais útils para pessoas que já tenha tido pelo menos um trabalho ocasional com Python.

Eu gostaria também de salientar que eu usei o módulo de doctest do Python para rodar os exemplos de código neste artigo. O código parece com uma sessão no console interativo do Python (`>>>` e `...` indicam comandos Python enquanto a saída tem sua própria linha). Eventualmente podem haver comentários enigmáticos que começam com "doctest" - eles são apenas diretivas para o doctest e podem ser ignorados.

### 1. Funções
Funções em Python são criadas com a palavra chave `def` e recebe um nome e uma lista opcional de parâmetros. Elas podem retornar valores com a palavra chave `return`. Vamos fazer e chamar uma função bem simples.

````shell
>>> def foo():
...     return 1
>>> foo()
1
````

O corpo da função (assim como todas as declarações multi-linhas em Python) é obrigatório e indicado por indentação. Podemos chamar funções acrescentando parênteses ao nome da função.

### 2. Escopo
Em Python, funções criam um novo escopo. Pythonistas também podem dizer que funções têm seu próprio namespace. Isso significa que Python olha primeiro no namespace da função para procurar nomes de variáveis que encontra no corpo da função. Python inclui algumas funções que nos deixam olhar no nosso namespace. Vamos escrever uma função simples para investigar a diferença entre escopo local e global.

````shell
>>> a_string = "This is a global variable"
>>> def foo():
...     print locals()
>>> print globals() # doctest: +ELLIPSIS
{..., 'a_string': 'This is a global variable'}
>>> foo() # 2
{}
````

A função builtin `globals` retorna um dicionário contendo todas os nomes de variáveis que o Python conhece. (Por uma questão de clareza, eu omiti na saída algumas variáveis que o Python cria automaticamente.) No ponto #2 eu chamei minha função `foo` que mostra o conteúdo do namespace local de dentro da função. Como nós podemos ver, a função `foo` tem seu próprio e separado namespace que está atualmente vazio.

### 3. Regras de resolução de variáveis
Claro que isso não significa que não podemos acessar variáveis globais dentro de nossas funções. A regra do escopo do Python é que a criação de variáveis sempre cria uma nova variável local, mas acesso de variável (incluindo modificação) verificano escopo local e então procura por todo o escopo envolvido para procurar uma que bata com a busca. Então se nós modificarmos nossa função `foo` para mostrar nossa variável global, tudo vai funcionar como esperado:

````shell
>>> a_string = "This is a global variable"
>>> def foo():
...     print a_string # 1
>>> foo()
This is a global variable
````

No ponto #1 Python procura por uma variável local na nossa função e não a encontra, então ele vai em busca de uma variável global com o mesmo nome.

Por outro lado, se nós tentarmos fazer uma atribuição na variável global dentro da nossa função, isso não vai fazer o que nós pensamos:

````shell
>>> a_string = "This is a global variable"
>>> def foo():
...     a_string = "test" # 1
...     print locals()
>>> foo()
{'a_string': 'test'}
>>> a_string # 2
'This is a global variable'
````

Como podemos ver, variáveis globais pode ser acessadas (mesmo se elas são  de tipos mutáveis) mas não podem (por padrão) receber atribuição. No ponto #1 dentro da nossa função, na realidade estamos criando uma nova variável local que "cobre" a variável global com o mesmo nome. Podemos ver isso ao dar `print` no namespace `local` dentro da nossa função `foo` e perceber que agora ele tem uma entrada. Podemos também ver novamente o namespace global no ponto #2 que ao checarmos o valor da variável `a_string` que esta não foi de fato alterada.

### 4. Tempo de vida da variável
É importante também notar que não apenas as variáveis "vivem" dentro de um namespace, elas também tem um tempo de vida.
Considere:

````shell
>>> def foo():
...     x = 1
>>> foo()
>>> print x # 1
Traceback (most recent call last):
  ...
NameError: name 'x' is not defined
````

Não é apenas uma questão de regra de escopo no ponto #1 que causa o problema (embora esse é o porque de nós termos um `NameError`) isso também tem a ver com a forma que as chamadas de função são implementadas em Python e muitas outras linguagens. Não existe nenhuma sintaxe que possamos usar para pegar o valor da variável `x` nesse ponto - ela literalmente não existe! O namespace criado para nossa função `foo` é criado do zero toda vez que a função é chamada, e é destruído quando a função termina.

### 5. Argumentos e parâmetros de função
Python nos permite passar argumentos para funções. O nome do parâmetro se torna uma variável local na nossa função.

````shell
>>> def foo(x):
...     print locals()
>>> foo(1)
{'x': 1}
````

Python tem uma variedade de maneiras para definir parâmetros de função e passar argumentos para eles. Você poderá ver uma lista completa e detalhada na [documentação oficial do Python sobre definição de funções](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions). Vou mostrar aqui a versão resumida: parâmetros de função podem ser tanto **posicionais** quanto podem ser **obrigatórios** ou **nomeados**, parâmetros que tem **valor padrão** são **opcionais**.

````shell
>>> def foo(x, y=0): # 1
...     return x - y
>>> foo(3, 1) # 2
2
>>> foo(3) # 3
3
>>> foo() # 4
Traceback (most recent call last):
  ...
TypeError: foo() takes at least 1 argument (0 given)
>>> foo(y=1, x=3) # 5
2
````

No ponto #1 estamos definindo uma função que tem um parâmetro posicional `x` e um parâmetro nomeado `y`. Como vemos no ponto #2 podemos chamar essa função passando argumentos normalmente - os valores são passados para os parâmetros de `foo` pela posição embora um dele está definido na definição da função como um parâmetro nomeado. Também podemos chamar a função sem passar nenhum argumento para o parâmetro nomeado, como você pode ver no ponto #3 - Python usa o valor padrão de `0` que declaramos se ele não receber um valor para o parâmetro nomeado `y`. Claro que não podemos deixar de passar valores para o primeiro (obrigatório, posicional) parâmetro - ponto #4 mostra que o resultado disso é uma exceção.

Tudo simples e claro? Agora vai começar a ficar um pouco confuso - Python suporta argumentos nomeados na chamada da função. Olhe no ponto #5 - aqui estamos chamando a função com dois argumentos nomeados embora ela esteja definida com um parâmetro nomeado e outro sendo posicional. Desde que tenhamos nomes para nossos parâmetros, a ordem em que passamos eles não importa.

O caso contrário é verdadeiro, claro. Um dos parâmetros para nossa função está definido como um parâmetro nomeado, mas passamos um argumento para ele pela posição - a chamada `foo(3,1)` no ponto #2 passa o `3` como o argumento para o nosso parâmetro obrigatório `x` e passa o segundo (o inteiro `1`) para o segundo parâmetro embora ele já estivesse definido como um parâmetro nomeado.

Wooow! Parecem ser muitas palavras para explicar um conceito bem simples: parâmetros de função podem ser nomes ou posições. Isso significa coisas ligeiramente diferentes dependendo se estamos na definição de função ou na hora da chamada de função, e podemos usar argumentos nomeados para funções definidas apenas com paramêtros posicionais e vice-versa! Novamente - se tudo isso foi muito rápido, dê uma olhada nas [documentações](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

### 6. Funções aninhadas
Python permite a criação de funções aninhadas. Isso significa que podemos declarar funções dentro de funções e as regras sobre escopo e tempo de vida continuam valendo normalmente.

````shell
>>> def outer():
...     x = 1
...     def inner():
...         print x # 1
...     inner() # 2
...
>>> outer()
1
````

Parece um pouco complicado, mas ainda continua se comportando de uma maneira bem sensata. Considere o que acontece no ponto #1 - Python procura por uma variável local de nome `x`, não achando ele então procura no escopo em volta que é outra função! A variável `x` é uma variável local para nossa função `outer` mas como antes nossa função `inner` tem acesso ao escopo em que está envolta (pelo menos ler e modificar o acesso). No ponto #2 nós chamamos a função `inner`. É importante lembrar que `inner` também é apenas um nome de variável que segue as regras de busca de variáveis do Python - Python procura no escopo de `outer` primeiro e encontra uma variável local de nome `inner`.

### 7. Funções são objetos de primeira classe em Python
Esta é uma simples observação de que, em Python, funções são objetos como qualquer outro. Ah, função contendo variável, você não é tão especial!

````shell
>>> issubclass(int, object) # all objects in Python inherit from a common baseclass
True
>>> def foo():
...     pass
>>> foo.__class__ # 1
<type 'function'>
>>> issubclass(foo.__class__, object)
True
````

Você pode nunca ter pensando em suas funções tendo atributos - mas funções são objetos em Python, assim como qualquer outro. (E se você achou isso confuso, espere até ver que classes são objetos em Python, assim como qualquer outro objeto!) Talvez isso esteja tornando o ponto em uma maneira acadêmica - funções são apenas valores normais como qualquer outro valor em Python. Isso significa que você pode passar funções para outras funções como argumentos, ou retornar funções em uma função como seu valor de retorno! Se você nunca pensou nesse tipo de coisa, considere o seguinte código Python que funciona perfeitamente:

````shell
>>> def add(x, y):
...     return x + y
>>> def sub(x, y):
...     return x - y
>>> def apply(func, x, y): # 1
...     return func(x, y) # 2
>>> apply(add, 2, 1) # 3
3
>>> apply(sub, 2, 1)
1
````

Esse exemplo pode não parecer tão estranho pra você - `add` e `sub` são funções Python normais que recebem dois valores e retornam um valor calculado. No ponto #1 pode ver que a variável espera receber uma função é uma variável como qualquer outra. No ponto #2 chamamos a função passamos para `apply` - parêntesis em Python são o operador de chamada, e eles chamam o valor que o nome daquela variável contém. E no ponto #3 você pode ver que passar funções como valores não tem nenhuma sintaxe especial em Python - nomes de função são apenas rótulos/nomes de variáveis como qualquer outra variável.

Você pode ver esse tipo de comportamento antes - Python usa funções como argumentos para operações frequentemente usadas como personalização da função built-in `sorted`, ao fornever uma função para o parâmetro `key`. Mas e sobre retornar funções como valores? Veja:

````shell
>>> def outer():
...     def inner():
...         print "Inside inner"
...     return inner # 1
...
>>> foo = outer() #2
>>> foo # doctest:+ELLIPSIS
<function inner at 0x...>
>>> foo()
Inside inner
````

Isso pode parecer um pouco bizarro. No ponto #1 retornamos a variável `inner` que passa a ser um rótulo/nome de função. Não há sintaxe especial aqui - nossa função está retornando a função `inner` que de outra forma não poderia ser chamada. Lembra do tempo de vida da variável? A função `inner` é sempre redefinida toda vez que a função `outer` é chamada, mas se `inner` não fosse retornada pela função, ela iria simplesmente deixar de existir quando o escopo se fosse.

No ponto #2 podemos pegar o valor de retorno que é nossa função `inner` e armazená-la em uma nova variável `foo`. Podemos ver que se nós avaliarmos `foo`, veremos que ela realmente contém nossa função `inner` e que podemos chamá-la ao usar o operador de chamada (parêntesis, lembra?). Isso pode parecer um pouco estranho, mas nada difícil de entender, né? Mas calma, porque as coisas estão prestes a ficar realmente estranhas!

### 8. Closures
Não vamos começar com uma definição, mas sim com outro exemplo de código. Vamos dar uma copiada no nosso último exemplo:

````shell
>>> def outer():
...     x = 1
...     def inner():
...         print x # 1
...     return inner
>>> foo = outer()
>>> foo.func_closure # doctest: +ELLIPSIS
(<cell at 0x...: int object at 0x...>,)
````

A partir do nosso último exemplo, podemos ver que `inner` é uma função retornada por `outer` em uma variável chamada `foo`, e que poderíamos chamar ela com `foo()`. Mas ela vai rodar? Vamos considerar primeiro as regras de escopo.

Tudo funciona de acordo com as regras de escopo do Python - `x` é uma variável local na nossa função `outer`. Quando `inner` imprime `x` no ponto #1 Python procura por uma variável local em `inner`, e ao não encontrar, procura no escopo que está envolta, que é a função `outer`, encontrando a variável lá.

Mas o que acontece do ponto de vista do tempo de vida da variável? Nossa variável `x` é local para a função `outer`, o que significa que ela existe apenas enquanto a função `outer` está sendo executada. Não somos capazes de chamar a função `inner` até depois do retorno de `outer`, então de acordo com o nosso modelo de como Python funciona, `x` não deveria existir mais na hora que chamamos `inner`, e talvez um erro de runtime ou algo do tipo deveria acontecer.

Acontece que, contra nossas expectativas, nossa função retornada `inner` funciona. Python tem suporte para uma funcionalidade chamada **function closures** que significa que funções internas (isso é, uma função que está dentro de outra função) definidas em escopo não global lembram como era o namespace em que estava envolto em tempo de definição. Isso pode ser visto ao acessar o atributo `func_closure` da nossa função `inner` que contém as variáveis no escopo envolto.

Lembre - a função interna está sendo definida novamente cada vezes que a função `outer` é chamada. Agora o valor de `x` não muda, então cada função `inner` faz a mesma coisa como outra função `inner` - mas e se mexermos nela um pouco mais?

````shell
>>> def outer(x):
...     def inner():
...         print x # 1
...     return inner
>>> print1 = outer(1)
>>> print2 = outer(2)
>>> print1()
1
>>> print2()
2
````

A partir desse exemplo, você pode ver que **closures** - o fato que funções lembram seus escopo - podem ser usadas para construir funções customizadas que têm, essencialmente, um argumento explicito. Não estamos passando os números 1 ou 2 para nossa função `inner`, mas estamos construindo versões customizadas da nossa função `inner` que "se lembram" que números elas devem imprimir.

Isso por si só é uma técnica poderosa - você pode até pensar dele como similar a técnicas de orientação de objeto em algumas maneiras: `outer` é um construtor para `inner` com `x` agindo como uma variável privada. E os usos são numerosos - se você está familiarizado com o parâmetro `key` da função `sorted`, provavelmente escreveu uma função lambda para ordenar uma lista de listas pelo segundo item ao invés do primeiro. Você pode agora estar capacitado a escrever uma função `itemgetter` que recebe o índice para recuperar e retornar uma função que poderia adequadamente ser passada ao parâmetro key.

Mas não vamos fazer nada tão mundano com closures! Ao invés disso, vamos em frente mais uma vez e escrever um decorator!

### 9. Decorator!
Um decorator é apenas um objeto chamável que recebe uma função uma função substituta. Vamos começar de forma simples e trabalhar nosso caminho até úteis decorators.

````shell
>>> def outer(some_func):
...     def inner():
...         print "before some_func"
...         ret = some_func() # 1
...         return ret + 1
...     return inner
>>> def foo():
...     return 1
>>> decorated = outer(foo) # 2
>>> decorated()
before some_func
2
````

Veja cuidadosamente nosso exemplo de decorator. Definimos uma função chamada `outer` que tem um único parâmetro `some_func`. Dentro de `outer` definimos uma função aninhada chamada `inner`. A função `inner` vai imprimir uma string e então chamar `some_func`, pegando seu valor de retorno no ponto #1. O valor de `some_func` pode ser diferente em cada vez que `outer` é chamada, mas não importa que função seja, nós vamos chamá-la. Finalmente `inner` retorna o valor de retorno de `some_func()` + 1 - e podemos ver que quando chamamos nossa função retornada armazenada em `decorated` no ponto #2 temos os resultados do print e também retorna o valor 2 ao invés do valor original 1 que nós poderíamos estar esperando receber ao chamar `foo`.

Poderíamos dizer que a variável `decorated` é uma versão decorada de `foo` - é `foo` mais alguma coisa. De fato se nós escrevemos um decorator útil podemos querer substituir completamente `foo` com a versão decorada, então sempre vamos ter nossa versão "mais alguma coisa" de `foo`. Podemos fazer isso sem aprender uma nova sintaxe, simplesmente reatribuindo a variável que contém nossa função:

````shell
>>> def outer(some_func):
>>> foo = outer(foo)
>>> foo # doctest: +ELLIPSIS
<function inner at 0x...>
````

Agora todas as chamadas de `foo()` não vão ter o resultado original de antes, terão a nossa versão decorada! Pegou a ideia? Vamos escrever um decorator mais útil.

Imagine que nós temos uma biblioteca que nos dá objetos de coordenadas. Talvez eles sejam primariamente compostos de pares de coordenadas `x` e `y`. Infelizmente os objetos de coordenadas não suportam operações matemáticas e não podemos modificar o código fonte, então não podemos adicionar esse suporte. No entanto, vamos estar fazendo muita matemática então queremos fazer funções `add` e `sub` para receberem dois objetos de coordenada e fazerem a operação matemática apropriada. Esas funções seriam fácil de escrever (vou fornecer um exemplo da classe Coordenada para ilustrar)

````shell
>>> class Coordinate(object):
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...     def __repr__(self):
...         return "Coord: " + str(self.__dict__)
>>> def add(a, b):
...     return Coordinate(a.x + b.x, a.y + b.y)
>>> def sub(a, b):
...     return Coordinate(a.x - b.x, a.y - b.y)
>>> one = Coordinate(100, 200)
>>> two = Coordinate(300, 200)
>>> add(one, two)
Coord: {'y': 400, 'x': 400}
````

Mas e se nossas funções de adição e subtração tivessem que também ter um comportamento de verificação de limites? Talvez você possa apenas somar ou subtrair baseado em coordenadas positivas e qualquer resultado deveria ser limitado a coordenadas positivas. Então atualmente:

````shell
>>> one = Coordinate(100, 200)
>>> two = Coordinate(300, 200)
>>> three = Coordinate(-100, -100)
>>> sub(one, two)
Coord: {'y': 0, 'x': -200}
>>> add(one, three)
Coord: {'y': 100, 'x': 0}
````

mas preferimos ter a diferença de `one` e `two` sendo `{x: 0, y: 0}` e a soma de `one` e `three` sendo `{x: 100, y: 200}` sem modificar `one`, `two` ou `three`. Invés de adicionar verificação de limites na entrada de argumentos de cada função e o valor de retorno de cada função, vamos escrever um decorator de verificação de limites!

````shell
>>> def wrapper(func):
...     def checker(a, b): # 1
...         if a.x < 0 or a.y < 0:
...             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
...         if b.x < 0 or b.y < 0:
...             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
...         ret = func(a, b)
...         if ret.x < 0 or ret.y < 0:
...             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
...         return ret
...     return checker
>>> add = wrapper(add)
>>> sub = wrapper(sub)
>>> sub(one, two)
Coord: {'y': 0, 'x': 0}
>>> add(one, three)
Coord: {'y': 200, 'x': 100}
````

O decorator funciona do mesmo jeito que antes - retorna uma versão modificada de uma função, mas neste caso ela faz algo útil ao checar e normalizar a entrada de parâmetros e o valor de retorno, substituindo qualquer valor negativo de `x` ou `y` por 0.

É uma questão de opinião quanto ao fazer isso torna nosso código mais limpo: isolar a checagem de limites na sua própria função e aplicá-la para todas as funções que nos interessam envolvendo-as com um decorator. A alternativa seria uma chamada de função em cada argumento de entrada e na saída resultante antes de retornar dentro de cada função matemática, e é inegável que usar o decorator é, pelo menos, menos repetitivo em termos de quantidade de código necessário para aplicar checagem de limites para uma função.

### 10. O símbolo @ aplica um decorator a uma função
A versão 2.4 do Python nos trouxe suporte para envolver uma função em um decorator ao adicionar antes da definição da função o nome do decorator e o símbolo `@`. Nos exemplos de código acima, nós usamos decorators nas nossas funções ao substituir a variável contendo a função com a versão decorada.

````shell
>>> add = wrapper(add)
````

Esse padrão pode ser usado em qualquer momento, para envolver qualquer função. Mas se estamos definindo uma função, podemos "decorá-la" com o símbolo `@` dessa maneira:

````shell
>>> @wrapper
... def add(a, b):
...     return Coordinate(a.x + b.x, a.y + b.y)
````

É importante notar que essa maneira não é diferente do que simplesmente substituir a variável original `add` com o retorno da função `wrapper` - Python apenas adiciona um `syntatic sugar` para fazer aquilo que acontece de maneira explícita.

Novamente - usar decorators é fácil! Ainda que escrever decorators úteis como `staticmethod` ou `classmethod` seja difícil, usá-los é apenas uma questão de adicionar à sua função o `@nomedodecorator`!

### 11. *args e **kwargs
Fizemos um decorator bem útil, mas ele está codificado para funcionar em apenas um tipo particular de função - uma que recebe dois argumentos. Nossa função interna `checker` aceita dois argumentos e passa os argumentos para a função que foi capturada na closure. E se nós quiséssemos um decorator que fizesse alguma coisa para qualquer função possível? Vamos fazer um decorator que incrementa o contador para cada chamada de função de cada função decorada sem mudar nenhuma das funções decoradas. Isso significa que o decorator teria que aceitar a assinatura de chamada de qualquer função que ele decora e também chamar as funções decoradas passando quaisquer argumentos que foram passados pra ele.

Acontece que Python tem um suporte sintático para essa funcionalidade. Certifique-se de ter lido o [Tutorial Python](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists) para mais detalhes, mas o operador `*` usado ao definir uma função significa que qualquer argumento posicional extra passado para a função vão ficar na variável antecedida por `*`. Então:

````shell
>>> def one(*args):
...     print args # 1
>>> one()
()
>>> one(1, 2, 3)
(1, 2, 3)
>>> def two(x, y, *args): # 2
...     print x, y, args
>>> two('a', 'b', 'c')
a b ('c',)
````

A primeira função `one` simplesmente mostra quaisquer (se houver) argumentos posicionais que foram passados pra ela. Como você pode ver no ponto #1, nos referimos a variável `args` dentro da função - `*args` é usado apenas na definição da função para indicar que argumentos posicionais devem ser armazenados na variável `args`. Python também nos permite especificar algumas variáveis e pegar os parâmetros adicionais em `args`, como podemos ver no ponto #2.

O operador `*` também pode ser usado ao chamar funções, e aqui ele tem um significado semelhante ao anterior. Uma variável antecedida por `*` ao **chamar** uma função significa que o conteúdo da variável deve ser extraído e usado como argumentos posicionais. Um exemplo para entender melhor:

````shell
>>> def add(x, y):
...     return x + y
>>> lst = [1,2]
>>> add(lst[0], lst[1]) # 1
3
>>> add(*lst) # 2
3
````

O código no ponto #1 faz exatamente a mesma coisa que o código no ponto #2 - Python está fazendo isso automaticamente pra nós no ponto #2 o que poderíamos fazer manualmente. Isso não é nada mal - `*args` tanto extrair variáveis posicionais a partir de um iterável na *chamada de uma função* quanto na *definição de uma função* aceitar qualquer quantidade de variáveis posicionais.

As coisas ficam um pouco mais complicadas ao introduzirmos o `**` que faz em dicionários e pares chave/valor exatamente a mesma coisa que `*` em iteráveis e parâmetros posicionais. Simples, né?

````shell
>>> def foo(**kwargs):
...     print kwargs
>>> foo()
{}
>>> foo(x=1, y=2)
{'y': 2, 'x': 1}
````

Quando definimos uma função, podemos usar `**kwargs` para indicar que todos os argumentos nomeados não capturados devem ser armazenados em um dicionário chamado `kwargs`. Da mesma forma que antes, nem a variável `args` ou `kwargs` fazem parte da sintaxe do Python, mas é uma convenção usar esse nome para essas variáveis ao declarar funções. Assim como `*`, podemos usar `**` ao chamar uma função bem como quando definí-la.

````shell
>>> dct = {'x': 1, 'y': 2}
>>> def bar(x, y):
...     return x + y
>>> bar(**dct)
3
````

### 12. Decorators mais genéricos
Dado nosso novo poder, podemos criar um decorator que "registra" os argumentos para funções. Vamos apenas imprimir, por questões de simplicidade:

````shell
>>> def logger(func):
...     def inner(*args, **kwargs): #1
...         print "Arguments were: %s, %s" % (args, kwargs)
...         return func(*args, **kwargs) #2
...     return inner
````

Perceba que nossa função `inner` recebe qualquer quantidade de parâmetros, independente de tipo no ponto #1 e os passa como argumentos para a função que foi decorada, no ponto #2. Isso nos permite envolver/decorar qualquer função, não importando sua assinatura.

````shell
>>> @logger
... def foo1(x, y=1):
...     return x * y
>>> @logger
... def foo2():
...     return 2
>>> foo1(5, 4)
Arguments were: (5, 4), {}
20
>>> foo1(1)
Arguments were: (1,), {}
1
>>> foo2()
Arguments were: (), {}
2
````

Chamar nossas funções resulta eu um "log" de saída, bem como o retorno do valor esperado de cada função.

### Mais sobre decorators
Se você conseguiu acompanhar o último exemplo, você entendeu decorators! Parabéns - Siga em frente e use seus novos poderes para o bem!

Se você estiver interessado em um estudo mais aprofundado: [Bruce Eckel tem um excelente artigo sobre decorators](http://www.artima.com/weblogs/viewpost.jsp?thread=240808) e implementa eles em Python com objetos ao invés de funções. Pode ser que você ache que o código na sua versão orientada a objetos mais fácil de ler do que nossa versão puramente funcional. Bruce também tem um artigo após esse primeiro sobre [fornecer argumentos para decorators](http://www.artima.com/weblogs/viewpost.jsp?thread=240845) que pode também ser mais fácil de implementar com objetos do que com funções. E por fim - você também pode estudar a função built-ing `wraps` do módulo [functools](https://docs.python.org/3/library/functools.html), que (talvez de uma maneira confusa inicialmente) é um decorator que pode ser usado em nossos decorators para modificar a assinatura das nossas funções substitutas, para que elas se pareçam mais com a função decorada.

[1] Eu também li recentemente um artigo sobre [decorators]() que me fez refletir...
[2] "global" é uma grande mentira no Python que dizem ser uma coisa maravilhosa, mas é uma discussão para outro dia...

**Update:** Graças ao Nick eu atualizei minha terminologia no artigo para deixar mais claro que "parâmetros" são as variáveis nomeadas na assinatura da função, enquanto "argumentos" são os valores que são passados para a função.



**_Viu algum trecho que poderia ficar com uma tradução melhor? Manda lá nos comentários mais abaixo. Valeu pessoal, e até a próxima!_**


Referências:

- [Post original](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)

