title: Funções Python II: decorators
date: 2015-02-18 12:38
author: Patrick Mazulo
slug: funcoes-python-ii-decorators
category: python
tags: python, python function, decorators, translations
summary: 4º post da série Pythonista Intermediário. Vamos continuar falando sobre funções em Python, mas dentro do conceito de `decorators`.
email: pmazulo@gmail.com
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/DecoratorsVisuallyExplained.png

![Créditos da imagem]({filename}/images/posts/DecoratorsVisuallyExplained.png)

Créditos da imagem: <https://www.freshbooks.com/developers/blog/logging-actions-with-python-decorators-part-i-decorating-logged-functions>

Decoradores de função (*Function Decorators*) habilitam a adição de nova
funcionalidade para a função sem alterar a funcionalidade original dela.
Antes de ler esse post, é importante que você tenha lido e entendido o a
[primeira parte](http://indacode.com/funcoes-python/ "Funções Python")
sobre funções python. O pensamento principal que devemos tirar a partir
desse tutorial, é que funções Python são objetos de primeira classe; um
resultado disso é que:

1.  Funções Python podem ser passadas como argumentos para outras
    funções
2.  Funções Python podem ser retornadas de outras chamadas de funções.
3.  Funções Python podem ser definidas dentro de outras funções
    resultando em closures.

As propriedades de funções Python listadas acima fornecem a função
necessária para explicar decoradores de função (que a partir daqui,
passaremos a nos referir no original, *function decorators*).
Simplificando, *function decorators* são **containers (*wrappers*) que
deixam você executar código antes** **das funções que elas decoraram sem
modificar a função em si**. A estrutura desse tutorial segue uma
excelente resposta encontrada no [stack
overflow](http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python/1594484#1594484) explicando
sobre *python decorators*.

Function Decorators
-------------------

*Function decorators* não são exclusivos ao Python, então para
explica-los, ignoremos a sintaxe de *function decorator *em Python por
enquanto, e ao invés disso vamos focar na essência de *function
decorators*. Para entender o que decorators fazem, nós implementamos uma
função bem simples que é decorada (*decorated*, termo em inglês) com uma
outra função simples que registra as chamadas para as funções decoradas.
A *decoração da função* é conseguida através da composição de funções,
como mostrado abaixo (seguem as explicações nos comentários):

````python
import datetime

# o decorator esperar uma outra função como argumento

def logger(func_to_decorate):

    # um container (wrapper) é definido na hora
    def func_wrapper():

        # adicione qualquer funcionalidade de execução na função original
        print("Calling function: {} at {}".format(func_to_decorate.__name__, datetime.datetime.now()))

        # execute a função original
        func_to_decorate()

        # adicione qualquer funcionalidade de execução na função original
        print("Finished calling : {}".format(func_to_decorate.__name__))
    # retorne a função wrapper definida no momento. O corpo da
    # função wrapper não foi executado ainda, mas um closure
    # na função func_to_decorate foi criado    
    return func_wrapper

def print_full_name():
    print("My name is John Doe")

````

````shell
>>>decorated_func = logger(print_full_name)
>>>decorated_func
# o valor retornado, decorated_func, é uma referência para a func_wrapper
<function func_wrapper at 0x101ed2578>
>>>decorated_func()
# decorated_func chamada
Calling function: print_full_name at 2015-01-24 13:48:05.261413
# a funcionalidade original é preservada
My name is John Doe
Finished calling : print_full_name
````

No simples exemplo definido acima, o decorator adiciona uma nova
funcionalidade, mostrando alguma informação antes e depois da chamada
original da função, para a função original sem altera-la. O decorator
<span style="color: #000000;">logger</span> recebe uma função para ser
decorada, <span style="color: #000000;">print\_full\_name</span> e
retorna uma função, <span style="color: #000000;">func\_wrapper</span>
que chama a função decorada, <span
style="color: #000000;">print\_full\_name</span>, quando é executada. A
função retornada, <span style="color: #000000;">func\_wrapper</span>
está fechada sobre a referência da função decorada (*closure*), <span
style="color: #000000;">print\_full\_name</span> e portanto pode invocar
a função decorada quando está executando. No exemplo acima, chamando
<span style="color: #000000;">decorated\_func</span> resulta em <span
style="color: #000000;">print\_full\_name</span> sendo executada além de
algum outro código implementando uma nova funcionalidade. Essa
habilidade de adicionar nova funcionalidade para uma função sem
modificar a função original é a essência de *function decorators*. Uma
vez que esse conceito é entendido, o conceito de *decorators* está
entendido.

 

Python decorators
-----------------

Agora que nós felizmente entendemos a essência de *function decorators*,
nós podemos seguir em frente para desconstruir construções Python que
permitem-nos definir decorators mais facilmente. A seção anterior
descreve a essência de decorators, mas ter que usar decorators através
de composições de funções como descrito é muito custoso. Python introduz
o símbolo <span style="color: #666600;">@</span> para decoração de
funções. Decorar uma função usando a sintaxe de decorator Python é
conseguida como mostrada abaixo:

````python
@decorator
def a_stand_alone_function():
    pass
````

Chamando <span style="color: #000000;">stand\_alone\_function</span>
agora é o equivalente a chamar a função <span
style="color: #000000;">decorated\_func</span> da seção anterior, mas
não precisamos mais definir a função intermediária <span
style="color: #000000;">decorated\_func</span>.

Note que decorators podem ser aplicados não apenas em funções Python,
mas também em classes Python e métodos de classe, mas discutiremos sobre
decorators de classes e métodos em um próximo tutorial.

É importante entender o que o símbolo <span
style="color: #666600;">@</span> faz em respeito aos decorators em
Python. A linha <span style="color: #006666;">@decorator</span> não
define um decorator, em vez disso pode-se pensar dele como um açúcar
sintático (*syntatic sugar*) para **decorar uma função**. Eu gosto de
definir **decorar uma função** como o processo de aplicar um decorator
existente a uma função. O ***decorator*** é a função real, <span
style="color: #000000;">decorator</span> que adiciona a nova
funcionalidade para a função original. De acordo com a PEP 318, o
seguinte trecho de decorator

````python
@dec2
@dec1
def func(arg1, arg2, ...):
    pass
````

é equivalente a:

````python
def func(arg1, arg2, ...):
    pass

func = dec2(dec1(func))
````

sem o argumento intermediário <span style="color: #000000;">func</span>.
No exemplo acima, <span style="color: #006666;">@dec1</span> e <span
style="color: #006666;">@dec2</span> são os invocadores dos decorators.
Agora pare, pense cuidadosamente e garanta que você entendeu isso. <span
style="color: #000000;">dec1</span> e <span
style="color: #000000;">dec2</span> são referências de objeto de função,
e esses são os decorators reais. Esses valores podem ainda ser
substituídos por qualquer ***chamada de função ou um valor que quando
avaliado retorna uma função que recebe uma outra função.*** *O que é de
suma importância é que o nome de referência* seguindo o símbolo <span
style="color: #666600;">@</span> é uma referência para um objeto função
(para esse tutorial, nós assumimos que esta referência deve ser um
objeto função, mas na realidade ela deve ser um objeto **chamável**
(**callable)**) que recebe uma função como argumento. Entender esse fato
profundo ajudará em entender decorators Python e tópicos sobre
decorators mais envolventes, tais como decorators que recebem
argumentos.

 

Argumentos de funções para funções decoradas
--------------------------------------------

Argumentos podem ser passados para funções que estão sendo decoradas ao
simplesmente passar essa função dentro da função que envolve ela, **isto
é a função interna retornada quando o decorator é invocado**, a função
decorada. Nós ilustramos isso com um exemplo abaixo:

````python
import datetime

# decorator espera uma outra função como argumento
def logger(func_to_decorate):

    # Uma função wrapper é definida na hora
    def func_wrapper(*args, **kwargs):

        # adicione qualquer funcionalidade de execução na função original
        print("Calling function: {} at {}".format(func_to_decorate.__name__, datetime.datetime.now()))

        # executa a função original
        func_to_decorate(*args, **kwargs)

        # adicione qualquer funcionalidade de execução na função original
        print("Finished calling : {}".format(func_to_decorate.__name__))

    # retorne a função wrapper definida no momento. O corpo da
    # função wrapper não foi executado ainda, mas um closure
    # na função func_to_decorate foi criado 
    return func_wrapper

@logger
def print_full_name(first_name, last_name):
    print("My name is {} {}".format(first_name, last_name))
````

````shell
print_full_name("John", "Doe")

Calling function: print_full_name at 2015-01-24 14:36:36.691557
My name is John Doe
Finished calling : print_full_name
````

Note como nós usamos <span style="color: #666600;">\*</span><span
style="color: #000000;">args</span> e <span
style="color: #666600;">\*\*</span><span
style="color: #000000;">kwargs</span> na definição da função wrapper
interna; isso é pelo simples motivo que nós não podemos saber de antemão
quais argumentos estão sendo passados para uma função que está sendo
decorada.

 Função decorator com argumentos de função
------------------------------------------

Nós também podemos passar argumentos para a função decorator atual, mas
isso é mais complexo do que o caso de passar funções para funções
decoradas. Nós ilustramos isso com um grande exemplo abaixo:

````python
# Essa função recebe argumentos e retorna uma função
# a função retornada é nosso decorator real
def decorator_maker_with_arguments(decorator_arg1):

    # isso é nosso decorator real que aceita uma função

    def decorator(func_to_decorate):
        # a função wrapper recebe argumentos para a função decoradora
        def wrapped(function_arg1, function_arg2) :
            # adicione qualquer funcionalidade de execução na função original
            print("Calling function: {} at {} with decorator arguments: {} and function arguments:{} {}".  
               format(func_to_decorate.__name__, datetime.datetime.now(), decorator_arg1, function_arg1, function_arg2))

            func_to_decorate(function_arg1, function_arg2)

            # adicione qualquer funcionalidade de execução na função original
            print("Finished calling : {}".format(func_to_decorate.__name__))

        return wrapped

    return decorator

@decorator_maker_with_arguments("Apollo 11 Landing")
def print_name(function_arg1, function_arg2):
   print ("My full name is -- {} {} --".format(function_arg1, function_arg2))
````

````shell
>>> print_name("Tranquility base ", "To Houston")

Calling function: print_name at 2015-01-24 15:03:23.696982 with decorator arguments: Apollo 11 Landing and function arguments:Tranquility base  To Houston
My full name is -- Tranquility base  To Houston --
Finished calling : print_name
````

Como mencionado anteriormente, a chave para entender o que está
acontecendo com isso é notar que nós podemos substituir o valor de
referência seguindo a @ em uma decoração de função com qualquer valor
que ***resulta em um objeto de função que recebe uma outra função como
argumento***. No exemplo acima, o valor retornado pela chamada de
função, <span
style="color: #000000;">decorator\_make\_with\_arguments</span>(<span
style="color: #008800;">"Apollo 11 landing"</span>), é o decorator. A
chamada resulta em uma função, decorator que aceita uma função como
argumento. Assim a decoração '@decorator\_maker\_with\_arguments("Apollo
11 landing")' é equivalente a <span
style="color: #006666;">@decorator</span> mas com o decorador, <span
style="color: #000000;">decorator</span>, fechado sobre o
argumento <span style="color: #008800;">Apollo 11 landing</span> pela
chamada da função <span
style="color: #000000;">decorator\_maker\_with\_arguments</span>. Note
que os argumentos fornecidos para um decorator não pode ser
dinamicamente mudado em tempo de execução como eles são executados na
importação do script.

 

Functools.wrap
--------------

Usar decorators envolve trocar de uma função para uma outra. Um
resultado disso é que meta informações, tais como docstrings são
perdidas quando usar um decorator com tal função. Isso é ilustrado
abaixo:

````python
import datetime

# decorator espera uma outra função como argumento
def logger(func_to_decorate):

    # uma função wrapper é definida na hora
    def func_wrapper():

        # adicione qualquer funcionalidade de execução na função original
        print("Calling function: {} at {}".format(func_to_decorate.__name__, datetime.datetime.now()))

        # execute a função original
        func_to_decorate()

        # adicione qualquer funcionalidade de execução na função original
        print("Finished calling : {}".format(func_to_decorate.__name__))

    # retorne a função wrapper definida no momento. O corpo da
    # função wrapper não foi executado ainda, mas um closure
    # na função func_to_decorate foi criado 
    return func_wrapper

@logger
def print_full_name():
    """return john doe's full name"""
    print("My name is John Doe")
````

````shell
>>> print(print_full_name.__doc__)
None
>>> print(print_full_name.__name__)
func_wrapper
````

No exemplo acima uma tentativa de mostrar a string de documentação
retorna <span style="color: #000088;">None</span> porque o decorator
trocou a função <span style="color: #000000;">print\_full\_name</span>
com a função <span style="color: #000000;">func\_wrapper</span> que não
tem string de documentação. Até mesmo o nome da função agora referencia
o nome da função wrapper, em vez da função real. Isso, na maioria das
vezes, não o que nós queremos quando usamos decorators. Para contornar
isso, o módulo Python <span style="color: #000000;">functools</span>
fornece a função <span style="color: #000000;">wraps</span> que também
passa a ser um decorator. Esse decorator é aplicado a função wrapper e
recebe a função a ser decorada como argumento. O uso é ilustrado abaixo:

````python
import datetime
from functools import wraps 

# decorator espera uma outra função como argumento
def logger(func_to_decorate):

    @wraps(func_to_decorate)
    # uma função wrapper é definida na hora
    def func_wrapper(*args, **kwargs):

        # adicione qualquer funcionalidade de execução na função original
        print("Calling function: {} at {}".format(func_to_decorate.__name__, datetime.datetime.now()))

        # execute a função original
        func_to_decorate(*args, **kwargs)

        # adicione qualquer funcionalidade de execução na função original
        print("Finished calling : {}".format(func_to_decorate.__name__))

    # retorne a função wrapper definida no momento. O corpo da
    # função wrapper não foi executado ainda, mas um closure
    # na função func_to_decorate foi criado 
    return func_wrapper

@logger
def print_full_name(first_name, last_name):
    """return john doe's full name"""
    print("My name is {} {}".format(first_name, last_name))
````

````shell
>>> print(print_full_name.__doc__)
return john doe's full name
>>>print(print_full_name.__name__)
print_full_name
````

Aplicação de Decoradores
------------------------

Decorators tem uma ampla variedades de aplicações em Python, e todas
essas não podem ser cobertas nesse artigo. Alguns exemplos de aplicações
de decorators incluem:

1.  Memoização (*memoization*) que é o cache de valores para prevenir
    recomputar tais valores se a computação é muito custosa; Um
    decorator de memoização pode ser usado para decorar uma função que
    executa o cálculo real, e a funcionalidade adicionada é que, para um
    dado argumento se o resultado já foi computado anteriormente então o
    valor armazenado é retornado para o chamador.
2.  Em aplicações web, decorators podem ser usados para proteger
    endpoints que requer autenticação; um endpoint é protegido com um
    decorator que checa se um usuário está autenticado quando uma
    requisição é feita para o endpoint. Django, um popular framework
    web, faz uso de decorators para gerenciar cache e permissões
    de views.
3.  Decorators podem também fornecer uma maneira limpa para realização
    de tarefas domésticas, tais como chamadas de funções de logging,
    tempo de função e etc.

O uso de decorators é um campo de atuação muito largo, que é único para
diferentes situações. A [biblioteca de decorator
Python](https://wiki.python.org/moin/PythonDecoratorLibrary) fornecem
ricos casos de uso de decorators Python. Navegando por esta coleção
fornecerá visão prática para o uso de decorators Python.

Leitura complementar
--------------------

-   [PEP 318 - Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
-   [StackOverflow](http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python/1594484#1594484)

[Clique aqui para voltar para a tabela de conteúdo.]({filename}/pages/pythonista-intermediario.md)


