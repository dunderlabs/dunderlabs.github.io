title: Introdução ao Python Generators
date: 2015-02-04 12:16
author: Patrick Mazulo
slug: introducao-ao-python-generators
category: python
tags: python, python iterators, generators, translations
summary: 2º post da série Pythonista Intermediário. Seguindo ainda no fluxo do primeiro post, vamos falar sobre iteradores e generators em Python.
email: pmazulo@gmail.com
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/relationships-generator-iterator.png

![Créditos da imagem]({filename}/images/posts/relationships-generator-iterator.png)
Créditos da imagem: <http://nvie.com/posts/iterators-vs-generators/>

*Geradores* (*generators*) é um conceito muito fascinante em Python;
*geradores* tem uma ampla gama de aplicações, que vai desde simples
avaliação preguiçosa (*lazy evaluation*) até avançadas execuções
simultâneas de tarefas (*veja* [David
Beazley](http://www.dabeaz.com/finalgenerator/)). Antes de mergulharmos
no fascinante mundo dos geradores Python, nós pegaremos um pequeno
desvio para explicar iteradores Python (*python iterators*), um conceito
que eu acho que seja parte integrante para entender geradores.

### Iteradores Python

Simplificando, um iterador em Python é qualquer tipo Python que pode ser
usado com um loop *for.* Listas, tuplas, dicionários e *sets* Python são
todos exemplos de iteradores embutidos. Alguém pode perguntar: "O que
faz desses tipos um iterador, e essa é uma propriedade apenas dos tipos
embutidos do Python?"

Esses tipos são iteradores porque eles implementam o **protocolo
iterador**. Então, **O que é um protocolo iterador**? Para responder
esta pergunta, vamos precisar fazer outro pequeno desvio. Em Python,
existem alguns métodos especiais, comumente chamados como ***métodos
mágicos***. Pode parecer estranho, mas apenas fique comigo e acredite
pela fé no que digo, pelo menos, até chegarmos à orientação a objetos em
Python.

Esses métodos normalmente não são chamados explicitamente no código, mas
são chamados implicitamente durante sua execução. Um exemplo muito
familiar desses métodos mágicos, é o método *\_\_<span
style="color: #000000;">init</span>\_\_*, que é mais ou menos como se
fosse um construtor que é chamado durante a inicialização de um objeto
Python. Semelhante a maneira como o método *\_\_<span
style="color: #000000;">init</span>\_\_* tem de ser implementado na
inicialização de um objeto personalizado, o protocolo iterador tem uma
série de métodos mágicos que precisam ser implementados em qualquer
objeto que queira ser usado como um **iterador**.

Esses são os seguintes métodos:

-   O método \_\_<span style="color: #000000;">iter</span>\_\_ que é
    chamado na inicialização de um iterador. Ele deve retornar um objeto
    que tem o método *<span style="color: #000088;">next</span>()* (no
    Python 3 este método foi mudado para \_\_<span
    style="color: #000000;">next</span>\_\_).
-   O método <span style="color: #000088;">*next*</span> que é chamado
    sempre que a função global *<span
    style="color: #000088;">next</span>()* é invocada com o iterador
    como argumento. O método iterador <span
    style="color: #000088;">*next*</span>deve retornar o próximo valor
    do iterável. Quando um iterador é usado com um loop *for*, o *for*
    chama implicitamente o método *<span
    style="color: #000088;">next</span>()*. Este método levanta uma
    exceção <span style="color: #660066;">*StopIteration*</span> quando
    não existe mais nenhum novo valor, para sinalizar o fim da iteração.

Qualquer classe Python pode ser definida para agir como um iterador,
desde que o protocolo iterador seja implementado. Isto é ilustrado
através da implementação de um simples iterador que retorna os números
da sequência Fibonacci até um determinado valor máximo.

````python
class Fib:                                        
    def __init__(self, max):                      
        self.max = max

    def __iter__(self):                          
        self.a = 0
        self.b = 1
        return self

    def next(self):                          
        fib = self.a
        if fib > self.max:
            raise StopIteration                  
        self.a, self.b = self.b, self.a + self.b
        return fib           
````

````shell
>>>for i in Fib(10):
        print i      

0
1
1
2
3
5
8
````

Nós também podemos ir mais em frente e implementar nossa própria função
<span style="color: #000000;">*range*</span> personalizada para loop em
números. Esta simples implementação apenas entra no loop partindo do 0
para cima.

````python
class CustomRange:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.curr = 0
        return self

    def next(self):
        numb = self.curr
        if self.curr >= self.max:
            raise StopIteration
        self.curr += 1
        return numb
````

````shell
>>> for i in CustomRange(10):
        print i 
0
1
2
3
4
5
6
7
8
9
````

### Voltando aos Geradores

Agora, nós temos um entendimento básico sobre iteradores, mas não como
eles se relacionam com geradores. Em resumo, geradores são iteradores. A
***PEP 255***, que descreve simples geradores, refere-se a geradores
pelo seu nome completo: ***generator-iterator*** (gerador de
iteradores). Geradores são utilizados quer chamando o método *next* no
objeto gerador, ou usando o objeto gerador em um loop *for*.

Em Python, funções geradoras ou apenas geradores retornam objetos
geradores. Esses geradores são funções que contêm a palavra reservada
<span style="color: #000088;">*yield*</span>. Ao invés de ter que
escrever cada gerador com o método *\_\_<span
style="color: #000000;">iter</span>\_\_* e <span
style="color: #000088;">*next*</span>, que é bastante complicado, Python
fornece a palavra reservada <span style="color: #000088;">*yield*</span>
que provê uma maneira fácil para definir geradores. Por exemplo, o
iterador de Fibonacci pode ser remodelado como um gerador usando a
palavra reservada <span style="color: #000088;">*yield*</span>, como
mostrado abaixo:

````python
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
````

O uso da palavra reservada <span
style="color: #000088;">*yield*</span>simplifica muito a criação do
gerador.

### A palavra reservada *yield*

A palavra reservada <span style="color: #000088;">*yield*</span>é usada
da seguinte maneira.

````python
yield lista_expressao
````

O <span style="color: #000088;">*yield*</span>é fundamental para as
funções geradoras em Python, mas o que essa palavra reservada <span
style="color: #000088;">*yield*</span> faz? Para entender o <span
style="color: #000088;">*yield*</span>, nós contrastamos ela com a
palavra reservada <span style="color: #000088;">*return*</span>;  uma
outra palavra chave que devolve o controle para o chamador de uma
função. Quando uma função que está executando encontra o <span
style="color: #000088;">*yield*</span>, ela suspende a execução naquele
ponto, salva seu contexto e retorna para o chamador, juntamente com
qualquer valor na lista\_expressao; quando o chamador invoca o método
*next* no objeto, a execução da função continua até outro <span
style="color: #000000;">*yield*</span> ou <span
style="color: #000000;">*return*</span> ser encontrado, ou quando o fim
da função é atingido. Citando a ***PEP 255***:

> Se a declaração de um yield é encontrado, o estado da função é
> congelado, e o valor da lista\_expressao é retornado para o chamador
> do método next(). Por "congelado" nós queremos dizer que todo o estado
> local é retido, incluindo a ligação das variáveis locais, o ponteiro
> de instrução e a pilha de avaliação interna: informação suficiente é
> salva para que na próxima vez que o .next() é invocado, a função pode
> proceder exatamente como se a declaração yield fosse apenas outra
> chamada externa. Por outro lado, quando uma função encontra a
> declaração de um <span style="color: #000088;">return</span>, ele
> retorna para o chamador junto com qualquer valor que prosseguir a
> declaração do <span style="color: #000088;">return</span>, e a
> execução de tal função é completa para todos os efeitos. Pode-se
> pensar do <span style="color: #000088;">yield</span> como o causador
> de uma interrupção temporária.

###  Geradores Python em ação

Retornando para a função de números Fibonacci, se nós queremos gerar
todos os número Fibonacci até um determinado valor, o seguinte trecho de
código não-gerador pode ser usado para criar a sequência

````python
def fib(max):
    numbers = []
    a, b = 0, 1
    while a < max:
        numbers.append(a)
        a, b = b, a + b
     return numbers
````

O trecho acima calcula avidamente todos os números abaixo do valor *max*
e retorna a coleção de tais números usando uma simples chamada de
função. Por outro lado, usando o gerador Fibonacci para resolver o mesmo
problema é um jogada diferente. Nós podemos usá-lo em um loop *for* e
permitir o construtor do *for* implicitamente inicializar o gerador e
chamar o método <span style="color: #000088;">next</span> no objeto
gerador, ou ao explicitamente inicializá-lo e chamar o método <span
style="color: #000088;">next</span> no objeto. Os valores são
retornados, um depois do outro, ao chamar o método <span
style="color: #000088;">next</span> no gerador. O gerador de números
Fibonacci é implementado usando <span
style="color: #000088;">*yield*</span> logo abaixo:

````python
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
````

Nas seções seguintes, nós explicitamente inicializaremos o gerador, e
faremos uso da função <span style="color: #000088;">next</span> para
pegar os valores do gerador. Primeiro, nós vamos inicializar o objeto
gerador como mostrado abaixo:

````shell
>>> gen = fib(10)
>>> gen
<generator object fib at 0x1069a6d20>
>>>
````

O que aconteceu acima é que quando o gerador é chamado, os argumentos
(max tem um valor máximo de 10) são ligados aos nomes, mas o corpo da
função não é executado. Ao invés disso, um objeto **generator-iterator**
é retornado como mostrado pelo valor de gen. Este objeto pode então ser
usado como um iterador. Note que é a presença da palavra reservada <span
style="color: #000088;">*yield*</span> é responsável por isso.

````shell
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
>>> next(gen)
5
>>> next(gen)
8
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
````

Agora quando chamamos a função <span style="color: #000088;">next</span>
com o objeto gerador como argumento, o corpo da função geradora é
executado até ela encontrar a declaração de um *<span
style="color: #000088;">yield</span>,* <span
style="color: #000088;">*return*</span> ou o fim da função ser atingido.
No caso de encontrar a declaração de um *yield*, a expressão seguinte ao
*yield* é retornado para o chamador, e o estado da função é salvo.
Quando a função <span style="color: #000088;">next</span> é chamada no
objeto gerador de Fibonacci, a variável <span
style="color: #000000;">a</span> <span style="color: #000000;">está
ligado a 0</span> e <span style="color: #000000;">b está ligado a
1</span>. A condição do <span style="color: #000088;">*while*</span> é
verdadeira, de modo que a primeira declaração do loop *while* é
executada, que passa a ser uma expressão <span
style="color: #000088;">*yield*</span>.

Esta expressão retorna para o chamador o valor de a que passa a ser 0, e
suspende naquele ponto com todo o contexto local salvo. Pense nisso como
comer seu almoço em partes, e que em seguida você guarda ele pra
continuar a comer mais tarde. Você pode continuar comendo até seu almoço
se esgotar, e no caso de um gerador isto é a função obtendo a declaração
de um *return* ou o fim do corpo da função. Quando a função <span
style="color: #000088;">next</span> é chamada no objeto Fibonacci
novamente, a execução é retomada na linha a, b = b, a+b e continua
executando normalmente até um <span
style="color: #000088;">*yield*</span> ser encontrado novamente. E assim
continua até a condição do loop for false e uma exceção <span
style="color: #660066;">StopIteration</span> seja levantada, que é o
sinal que não há mais dados para gerar.

### Expressões Geradoras

Em [Python
Comprehensions](http://indacode.com/python-comprehensions/ "Python Comprehensions")nós
discutimos sobre list comprehensions e como elas são formadas. Uma
desvantagem com list comprehensions é que os valores são todos
calculados de uma vez, independente se esses valores são necessários
naquele momento ou não. Isto pode algumas vezes consumir uma quantidade
excessiva de memória. A [**PEP
289**](https://www.python.org/dev/peps/pep-0289/)propôs a expressão
geradora para resolver isto, e esta proposta foi aceita e adicionada a
linguagem. Expressões geradoras são como list comprehensions; a única
diferença é que os colchetes na list comprehensions são substituídos por
parênteses. Nós contrastamos uma list comprehension com uma expressão
geradora logo abaixo.

Para gerar uma lista com o quadrado dos número de 0 e 10 usando list
comprehensions é feita da seguinte forma:

````shell
>>> squares = [i**2 for i in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
````

Nós poderíamos usar uma expressão geradora, tal como mostrada abaixo, no
lugar de uma list comprehension:

````shell
>>> squares = (i**2 for i in range(10))
>>> squares
<generator object <genexpr> at 0x7f8c48ec8cd0>
````

Nós podemos então acessar os valores do gerador usando um loop *for* ou
o método <span style="color: #000088;">next</span>, como mostrado
abaixo. Cada valor é computado sob demanda, ou seja, só quando
requisitado.

````shell
>>> for square in squares:
            print square
0
1
4
9
16
25
36
49
64
81
````

### De que servem esses geradores?

Geradores Python fornecem a base para **avaliação preguiçosa** e
**cálculo sob demanda** em Python. Avaliação preguiçosa é uma parte
integral do processamento de fluxo (processamento de grande quantidades
de dados). Por exemplo, imagine que nós queremos criar uma quantidade
indeterminada de números Fibonacci, isto não seria possível com uma
abordagem sem geradores, porque nós temos que definir a quantidade de
números que precisamos ou entrar num loop infinito. Por outro lado,
adotando a abordagem dos geradores, fazer isso se torna trivial; nós
apenas temos que chamar o <span style="color: #000088;">next</span> para
pegar o próximo número Fibonacci, sem se preocupar sobre onde ou quando
o fluxo de números terminam.

Um tipo mais prático de processamento de fluxo é manipulando grandes
arquivos de dados tais como arquivos de log. Geradores fornecem métodos
eficientes para processamento desses dados, onde só algumas partes do
arquivo são tratadas em um ponto no tempo. ([David
Beazley](http://www.dabeaz.com/generators-uk/GeneratorsUK.pdf))

Geradores também podem ser usados para substituir callbacks (*retorno de
chamada de funções*). Ao invés de passar um callback para uma função, a
função pode ceder o controle (*yield control*) para o chamador quando
ele precisar informar algo ao chamador. O chamador pode então invocar
uma função que teria sido usada como callback. Isto libera a função
principal da obrigação de saber sobre o callback.

Em um nível mais avançado, geradores podem ser usados para implementar
concorrência ([David Beazley](http://www.dabeaz.com/finalgenerator/)).
Quando um gerador <span style="color: #000000;">*yields*</span> cede o
controle para o chamador, o chamador pode então ir em frente e chamar
outro gerador, simulando concorrência.

O que listamos acima são apenas algumas das aplicabilidades dos
geradores Python. Em um post futuro, nós discutiremos novas adições ao
gerador Python que permitem um chamador enviar valores para o gerador,
bem como alguns usos avançados de geradores.

 

### Leitura complementar

-   [PEP 255 – Simple Generators](https://www.python.org/dev/peps/pep-0255/)
-   [PEP 289 – Generator Expressions](https://www.python.org/dev/peps/pep-0289/)
-   [Generators: The Final Frontier by David Beazley](http://www.dabeaz.com/finalgenerator/FinalGenerator.pdf)
-   [Python Tutorials - Generators](https://docs.python.org/2/tutorial/classes.html#generators)
-   [Python Tutorials - Generator Expressions](https://docs.python.org/2/tutorial/classes.html#generator-expressions)
-   [Python Tutorials - Iterators](https://docs.python.org/2/tutorial/classes.html#iterators)

[Clique aqui para voltar para a tabela de conteúdo.]({filename}/pages/pythonista-intermediario.md)

 
