title: Funções Python
date: 2015-02-11 13:15
author: Patrick Mazulo
slug: funcoes-python
category: python
tags: python, python function, translations
summary: 3º post da série Pythonista Intermediário. Vamos conhecer como Python trata funções.
email: pmazulo@gmail.com
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/python_function_syntax.png

![Créditos da imagem]({filename}/images/posts/python_function_syntax.png)
Créditos da imagem: <http://www.voidspace.org.uk/python/weblog/arch_Tools.shtml>

Funções Python nomeadas ou *anônimas* são um conjunto de declarações ou
expressões. Em Python, ***funções são objetos de primeira classe***.
Isso significa que não há restrição no uso de funções. Funções python
podem ser usadas assim como qualquer outro valor python, tal como
strings e números. Funções Python tem atributos que podem ser
introspectados ao usar a função <span style="color: #000088;">[dir](https://docs.python.org/2/library/functions.html#dir)</span>
do Python, como mostrado abaixo:

````python
def square(x):
    return x**2
````

````shell
>>> square
<function square at 0x031AA230>
>>> dir(square)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>>
````

Alguns atributos importantes das funções incluem:

-   \_\_<span style="color: #000000;">doc</span>\_\_ retorna a string da
    documentação da função.

````shell
def square(x):
    """return square of given number"""
    return x**2

>>> square.__doc__
'return square of given number'
````

-   \_\_<span style="color: #000000;">name</span>\_\_ retorna o nome da
    função

```` {.theme:shell-default .toolbar:1 .toolbar-overlay:false .striped:false .nums:false .lang:sh .decode:true}
def square(x):
    """return square of given number"""
    return x**2

>>> square.func_name
'square'
````

-   \_\_<span style="color: #000000;">module</span>\_\_ retorna o nome
    do módulo que a função está definida.

````python
def square(x):
    """return square of given number"""
    return x**2
````

````shell
>>> square.__module__
'__main__'
````

-   <span style="color: #000000;">func\_defaults</span> retorna uma
    tupla com os valores padrões dos argumentos.
-   <span style="color: #000000;">func\_globals</span> retorna uma
    referência para um dicionário que contém as variáveis globais
    da função.

````python
def square(x):
    """return square of given number"""
    return x**2
````

````shell
>>> square.func_globals
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', 'square': <function square at 0x10f099c08>, '__doc__': None, '__package__': None}
````

-   <span style="color: #000000;">func\_dict</span> retorna o dicionário
    que define o namespace local para os atributos desta função

````python
def square(x):
    """return square of given number"""
    return x**2
````python

````shell
>>> square.func_dict
{}
````

-   <span style="color: #000000;">func\_closure</span> retorna tupla de
    células que contém ligações para variáveis livres das funções.
    Closure serão discutidos mais tarde.

Funções podem ser repassadas como argumentos para outras funções. Essas
funções que recebem outras funções como argumento são comumente chamadas
como funções ***de alta ordem*** (ou ***ordem superior***) e elas formam
uma parte muito importante na ***programação funcional***. Um exemplo
muito bom dessas funções de alta ordem é a função [<span
style="color: #000000;">map</span>](https://docs.python.org/2/library/functions.html#map)
que recebe uma função e um <span
style="color: #000000;">iterável</span>, e aplica a função para cada
item no <span style="color: #000000;">iterável</span>, retornando uma
nova lista. No exemplo abaixo, nós ilustramos isso ao passar a função
<span style="color: #000000;">square</span> definida anteriormente e um
<span style="color: #000000;">iterável</span> de números para a função
<span style="color: #000000;">map</span>.

````shell
>>> map(square, range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
````

Funções podem ser definidas dentro do bloco de código de outras funções,
e podem ser retornadas a partir da chamada de outras funções.

````python
def outer():
    outer_var = "outer variable"
    def inner():
        return outer_var
    return inner
````

No exemplo acima, nós declaramos uma função, <span
style="color: #000000;">inner</span>, dentro de uma outra função, <span
style="color: #000000;">outer</span>, e retornamos a função <span
style="color: #000000;">inner</span> quando a função <span
style="color: #000000;">outer</span> é executada.

````python
def outer():
    outer_var = "outer variable"
    def inner():
        return outer_var
    return inner
````

````shell
>>> func = outer()
>>> func
<function inner at 0x031AA270>
>>>
````

No exemplo acima, a função outer retorna uma função quando é chamada, e
esta é atribuída para a variável func. Essa variável pode ser chamada
assim como a função retornada:

````shell
>>> func()
'outer variable'
````

Definições de Função
--------------------

A palavra reservada <span style="color: #000088;">def</span> é usada
para criar funções definidas pelo usuário. Definições de funções são
instruções executadas.

````python
def square(x):
    return x**2
````

Na função <span style="color: #000000;">square</span> acima, quando o
módulo contendo a função é carregado no interpretador python, ou se está
definida dentro do **REPL** python, então a instrução da definição da
função que está em <span style="color: #000088;">def</span> <span
style="color: #000000;">square</span>(x) é executada. Isso tem algumas
implicações para argumentos padrões que tem estruturas de dados mutáveis
como valores; isso será coberto mais a frente neste tutorial. A execução
de uma definição de função liga o nome da função no atual namespace
local (*pense em namespaces como nomes para mapeamento de valores que
podem também ser aninhados. namespaces e escopo serão cobertos em mais
detalhes em um outro tutorial*) para um objeto de função que é um
wrapper em torno do código executável para a função. Esse objeto função
contém uma referência para o atual namespace global que é o namespace
global que é usado quando a função é chamada. A definição da função não
executa o corpo da função; este é executado apenas quando a função é
chamada.

Argumentos da Chamada de Função
-------------------------------

Além dos argumentos normais, funções python suportam número variável de
argumentos. Esses números variáveis de argumentos vêm em três tipos que
estão descritos abaixo:

-   **Valor padrão do argumento**: Isso permite um usuário definir
    alguns valores padrões para os argumentos da função. Nesse caso, tal
    função pode ser chamada com menos argumentos. Python usa o valor
    padrão fornecido para argumentos que não são fornecidos durante a
    chamada da função. Este exemplo abaixo é ilustrativo:

        def show_args(arg, def_arg=1, def_arg2=2):
            return "arg={}, def_arg={}, def_arg2={}".format(arg, def_arg, def_arg2)

    A função acima foi definida com um único argumento posicional
    normal, <span style="color: #000000;">arg</span> e dois argumentos
    padrões, <span style="color: #000000;">def\_arg</span> e <span
    style="color: #000000;">def\_arg2</span>. A função acima pode ser
    chamada em qualquer das seguintes maneiras abaixo:

    -   Fornecendo apenas o valor do argumento posicional não
        predefinido; nesse caso os outros argumentos recebem os valores
        padrões fornecidos:

            def show_args(arg, def_arg=1, def_arg2=2):
                return "arg={}, def_arg={}, def_arg2={}".format(arg, def_arg, def_arg2)

        -   shell

                >>> show_args("tranquility")
                    'arg=tranquility, def_arg=1, def_arg2=2'

    -   Fornecendo valores para sobrescrever algum argumento padrão além
        do argumento posicional que não foi predefinido.


            def show_args(arg, def_arg=1, def_arg2=2):
                return "arg={}, def_arg={}, def_arg2={}".format(arg, def_arg, def_arg2)

        -   shell

                >>> show_args("tranquility", "to Houston")
                    'arg=tranquility, def_arg=to Houston, def_arg2=2'

    -   Fornecendo valores para todos os argumentos, sobrescrevendo
        todos os argumentos com valores padrões.

            def show_args(arg, def_arg=1, def_arg2=2):
                return "arg={}, def_arg={}, def_arg2={}".format(arg, def_arg, def_arg2)

        -   shell

                >>> show_args("tranquility", "to Houston", "the eagle has landed")
                    'arg=tranquility, def_arg=to Houston, def_arg2=the eagle has landed'

    -   É também muito importante ser cuidadoso quando usar estruturas
        de dados mutáveis como argumentos padrões. Definições de função
        são executadas uma vez que essas estruturas de dados mutáveis,
        que são valores de referência, são criados na hora da definição.
        Isto significa que a mesma estrutura mutável de dado é usada
        para todas as funções chamadas, como mostrado abaixo:

            def show_args_using_mutable_defaults(arg, def_arg=[]):
                def_arg.append("Hello World")
                return "arg={}, def_arg={}".format(arg, def_arg)

        -   shell

                >>> show_args_using_mutable_defaults("test")
                    "arg=test, def_arg=['Hello World']" 
                >>> show_args_using_mutable_defaults("test 2")
                    "arg=test 2, def_arg=['Hello World', 'Hello World']"

        <p>
        Em cada chamada de função, <span style="color: #660066;">Hello
        World</span> é adicionado a lista <span
        style="color: #000000;">def\_arg</span>, e depois de duas
        chamadas de função, o argumento padrão tem 2 strings
        hello world. É importante tomar nota disso quando usar
        argumentos mutáveis padrão como valores padrão. A razão para
        isso ficará claro quando nós discutirmos o Python Data Model.

-   **Argumento Chave**: funções podem ser chamadas usando argumentos
    chave da forma <span style="color: #000000;">kwarg</span><span
    style="color: #666600;">=</span><span
    style="color: #000000;">valor.</span>Um kwarg refere ao nome do
    argumento usado na definição da função. Pegue a função definida
    abaixo com argumentos padrão e posicionado


        def show_args(arg, def_arg=1):
            return "arg={}, def_arg={}".format(arg, def_arg)

    Para ilustrar uma chamada de função com argumentos chave, a seguinte
    função pode ser chamada em qualquer das seguintes maneiras:

        show_args(arg="test", def_arg=3)


        show_args("test")

        show_args(arg="test")

        show_args("test", 3)

    Em uma chamada de função, argumentos chave não devem vir antes  de
    argumentos não chaves, assim, a seguinte maneira irá falhar:

        show_args(def_arg=4)

    Uma função não pode fornecer valores duplicados para um argumento,
    então a seguinte declaração é ilegal:


        show_args("test", arg="testing")

    No exemplo acima, o argumento arg é um argumento posicional, então o
    valor test é atribuído a ele. Tentar atribuir na chave arg novamente
    é uma tentativa de múltiplas atribuições, e isso é ilegal.

    Todos os argumentos chaves passados devem corresponder a um dos
    argumentos aceitos pela função, e a ordem das chaves incluindo
    argumentos não opcionais não é importante, então o seguinte código
    no qual a ordem dos argumentos está trocada é legal:

    
        show_args(def_arg="testing", arg="test")

-   **Lista aleatória de argumentos**: Python também suporta definir
    funções que recebem uma série aleatória de argumentos que são
    passados para a função em uma tupla. Um exemplo disso no tutorial
    python é dado abaixo:

    
        def write_multiple_items(file, separator, *args): 
            file.write(separator.join(args))

    O número aleatório de argumentos devem vir depois dos argumentos
    normais; nesse caso, depois dos argumentos <span
    style="color: #000000;">file</span> e <span
    style="color: #000000;">separator</span>. A seguir temos um exemplo
    de chamada de função para a função definida acima:

    
        f = open("test.txt", "wb")
        write_multiple_items(f, " ", "one", "two", "three", "four", "five")

    <p>
    Os argumentos <span style="color: #000000;">one two three four
    five</span> são todos agrupados juntos em uma tupla que podem ser
    acessados através do argumento <span
    style="color: #000000;">args</span>.

### Desempacotando Argumentos de Função

Algumas vezes, nós podemos ter argumentos para uma chamada de função
tanto em uma tupla, uma lista ou um dicionário. Esses argumentos pode
ser desempacotados nas funções pelas chamadas de função usando os
operadores <span style="color: #000000;">\*</span> ou <span
style="color: #000000;">\*\*</span>. Considere a seguinte função que
recebe 2 argumentos posicionais e mostra os valores

````shell
>>> def print_args(a, b):
        print a
        print b
````

Se nós tivermos os valores que nós queremos fornecer para a função em
uma lista, então nos poderíamos desempacotar esses valores diretamente
na função, como mostrado abaixo:

````shell
>>> args = [1, 2]
>>> print_args(*args)
1
2
````

Da mesma forma, quando nós temos palavras-chaves, nós podemos usar <span
style="color: #000000;">dicts</span> para armazenar, mapeando <span
style="color: #000000;">kwarg para valor</span> e o operador <span
style="color: #000000;">\*\*</span> para desempacotar os argumentos
chaves para as funções, como mostrado abaixo:

````shell
>>> def parrot(voltage, state=’a stiff’, action=’voom’):
        print "-- This parrot wouldn’t", action,
        print "if you put", voltage, "volts through it.",
        print "E’s", state, "!"

>>> d = {"voltage": "four million", "state": "bleedin’ demised", "action": "VOOM"}
>>> parrot(**d)
>>> This parrot wouldn’t VOOM if you put four million volts through it. E’s bleedin’ demised
````

### 

### Definindo funções com <span style="color: #666600;">\*</span> e <span style="color: #666600;">\*\*</span>

Algumas vezes, ao definir uma função, nós podemos não saber de antemão o
número de argumentos a esperar. Isso leva a definição de funções com a
seguinte assinatura:

````python
show_args(arg, *args, **kwargs)
````

O argumento <span style="color: #000000;">\*args</span> representa uma
sequência de tamanho desconhecido de argumentos posicionais, enquanto
<span style="color: #000000;">\*\*kwargs</span> representa um dicionário
de mapeamento nome-valor que pode conter qualquer quantidade de
nome-valor mapeada. O <span style="color: #000000;">\*args</span> deve
vir antes do <span style="color: #000000;">\*\*kwargs</span> na
definição da função. O seguinte código ilustra isso:

````shell
>>> def show_args(arg, *args, **kwargs):
        print arg
        for item in args:
            print args
        for key, value in kwargs:
            print key, value

>>> args = [1, 2, 3, 4]
>>> kwargs = dict(name='testing', age=24, year=2014)
>>> show_args("hey", *args, **kwargs)
hey
1
2
3
4
age 24
name testing
year 2014
````

O argumento normal deve ser fornecido para a função, mas o <span
style="color: #000000;">\*args</span> e <span
style="color: #000000;">\*\*kwargs</span> são opcionais, como
demonstrado abaixo:

````shell
>>> show_args("hey", *args, **kwargs)
hey
````

Na chamada da função o argumento normal é fornecido normalmente enquanto
os argumentos opcionais são desempacotados na chamada.

 

Funções Anônimas
----------------

Python também tem suporte para ***funções anônimas***. Essas função são
criadas usando a palavra chave <span
style="color: #000088;">lambda.</span>Expressões lambda em python são da
seguinte forma:

````python
lambda_expr ::=  "lambda" [parameter_list]: expression
````

Expressões lambda retornam objetos de função depois da avaliação e tem
os mesmo atributos das funções nomeadas. Expressões lamda são
normalmente apenas usadas para funções muito simples em python, como
demonstrado abaixo:

````shell
>>> square = lambda x: x**2
>>> for i in range(10):
    square(i)
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
>>>
````

A expressão lambda acima é equivalente a seguinte função nomeada:

````shell
>>> def square(x):
    return x**2
````

### 

Funções aninhadas e Closures
----------------------------

Definições de funções dentro de uma função cria funções aninhadas, assim
como mostrado abaixo:

````shell
>>> def outer():
        outer_var = "outer variable"
        def inner():
            return outer_var
        return inner
>>>
````

Nesse tipo de definição de função, a função <span
style="color: #000000;">inner</span> está apenas no escopo dentro da
função <span style="color: #000000;">outer</span>, por isso é na maioria
das vezes mais útil quando a função inner está sendo retornada
(movendo-a para o escopo da outer) ou quando está sendo passada em uma
outra função. Em funções aninhadas, tais como no exemplo acima, uma nova
instância da função aninhada é criada em cada chamada da função outer.
Isso porque durante a execução da função outer, a definição da nova
função inner é executada, mas o corpo não é executado.

Uma função aninhada tem acesso ao ambiente em que foi criada. Isso é um
resultado direto da semântica da definição de função python. Um
resultado é que a variável definida na função outer pode ser
referenciada na função inner mesmo depois da função outer já ter
finalizado sua execução.

````python
def outer():
    outer_var = "outer variable"
    def inner():
        return outer_var
    return inner
````

````shell
>>> x = outer()
>>> x
<function inner at 0x0273BCF0>
>>> x()
'outer variable'
````

Quando funções aninhadas referenciam variáveis de funções externas nós
dizemos que a função aninhada está fechada (closure) sobre a variável
referenciada. Nós podemos usar um dos atributos especiais de objetos
função, <span style="color: #000000;">\_\_closure\_\_</span> para
acessar as variáveis fechadas, como demonstrado abaixo:

````shell
>>> cl = x.__closure__
>>> cl
(<cell at 0x029E4470: str object at 0x02A0FD90>,)

>>> cl[0].cell_contents
'outer variable'
````

Closures em python tem um comportamento peculiar. No python 2.x e
abaixo, variáveis que apontam para tipos imutáveis tais como string e
números não podem ser recuperados dentro de um closure. O exemplo abaixo
ilustra isso:

````python
def counter():
    count = 0
    def c():
        count += 1
        return count
    return c
````

````shell
>>> c = counter()
>>> c()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in c
UnboundLocalError: local variable 'count' referenced before assignment
````

Uma solução bastante instável para isso é fazer uso de um tipo mutável
para capturar o closure, como mostrado abaixo:

````python
def counter():
    count = [0]
    def c():
        count[0] += 1
        return count[0]
    return c
````

````shell
>>> c = counter()
>>> c()
1
>>> c()
2
>>> c()
3
````

Python 3 introduziu a palavra chave <span
style="color: #000088;">nonlocal</span> que pode ser usada para resolver
esse problema de escopo de closure, como mostrado abaixo. No tutorial
sobre **namespaces**, nós descrevemos essas peculiaridades em mais
detalhes.

````python
def counter():
    count = 0
    def c():
        nonlocal count
        count += 1
        return count
     return c
````

Closures podem ser usados para manter estados (**não é para isso que
classes servem**) e para algum simples casos, fornecendo uma solução
mais sucinta e legível que classes. Nós usamos um exemplo de registro
(logging) copiado do
[tech\_pro](http://tech.pro/tutorial/1512/python-decorators) para
ilustrar isso. Imagine uma API de registro extremamente trivial usando
classes baseadas em orientação a objetos que pode fazer logon em
diferentes níveis:

````python
class Log:
    def __init__(self, level):
        self._level = level

    def __call__(self, message):
        print("{}: {}".format(self._level, message))

log_info = Log("info")
log_warning = Log("warning")
log_error = Log("error")
````

Essa mesma funcionalidade pode ser implementada com closures, como
demonstrado abaixo:

````python
def make_log(level):
    def _(message):
        print("{}: {}".format(level, message))
    return _

log_info = make_log("info")
log_warning = make_log("warning")
log_error = make_log("error")
````

A versão baseada em closure pode ser visto como a maneira mais sucinta e
legível, apesar de que ambas versões implementam a mesma funcionalidade.
Closures também desempenham um papel importante em uma grande função
Python: **funções decoradoras** *(function decorators)*. Essa é uma
funcionalidade amplamente usada que está explicada no próximo tutorial.

###  Leitura Complementar

-   [Closures em Python](http://tech.pro/tutorial/1512/python-decorators)
-   [Definindo funções](https://docs.python.org/2/tutorial/controlflow.html#defining-functions)

[Clique aqui para voltar para a tabela de conteúdo.]({filename}/pages/pythonista-intermediario.md)

N.T: Pessoal, tive uma certa dificuldade ao traduzir este capítulo da
série. Então gostaria de contar com o feedback de vocês nos comentários
para saber se conseguiram entender o que foi proposto :D

 
