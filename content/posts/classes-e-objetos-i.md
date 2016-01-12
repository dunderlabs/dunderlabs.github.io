title: Classes e Objetos I
date: 2015-03-16 11:58
author: Patrick Mazulo
slug: classes-e-objetos-i
email: pmazulo@gmail.com
about_author: My name is Patrick and I'm a web developer who fell in love with Python

![Créditos para a imagem]({filename}/images/python-model.png)
Créditos para a imagem: http://blog.invisivel.net/2012/04/10/pythons-object-model-explained/

Em Python, tudo é um objeto. Classes fornecem o mecanismo para criar novos tipos de objetos. Neste tutorial, nós vamos deixar um pouco de lado o básico de classes e programação orientada a objetos e focaremos em tópicos que proveem um melhor entendimento deste paradigma de programação em Python. É assumido que nós estamos lidando com um novo estilo de classes. Existem classes Python que herdam da super classe *object*.
Definindo Classes
-----------------

A declaração <span style="color: #000088;">class</span> é usada para definir novas classes. Esta declaração define um conjunto de atributos, variáveis e métodos, que estão associados e compartilhados por uma coleção de instâncias de tal classe. Uma simples definição de classe é dada abaixo:
````python
class Account(object):
    num_of_accounts = 0

    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance 
        Account.num_of_accounts += 1

    def del_account(self):
        Account.num_of_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt 

    def withdraw(self, amt):
        self.balance = self.balance - amt 

    def inquiry(self):
        return self.balance
````

Definições de classe introduzem os seguintes novos objetos:

1.  Objeto de classe
2.  Objeto de Instância
3.  Objeto de método

Objetos de Classe
-----------------

Quando uma definição de classe é encontrada durante a execução de um programa, um novo namespace é criado, e este serve como o namespace em que todas as variáveis de classe e definições de métodos se ligam. Note que este namespace não cria um novo escopo local que pode ser usado por métodos de classe, daí a necessidade por nomes completos ao acessar variáveis em métodos. A classe <span style="color: #660066;">Account</span> da seção anterior ilustra isto; métodos que tentam acessar a variável <span style="color: #000000;">num\_of\_accounts</span> devem usar o nome completo, <span style="color: #660066;">Account</span>.<span style="color: #000000;">num\_of\_accounts</span>, senão resulta em um erro como mostrado abaixo, quando o nome completo não é usado no método \_\_init\_\_:

````python
class Account(object):
    num_of_accounts = 0

    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance 
        num_of_accounts += 1

    def del_account(self):
        Account.num_of_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt 

    def withdraw(self, amt):
        self.balance = self.balance - amt 

    def inquiry(self):
        return self.balance
````
````shell
>>> acct = Account('obi', 10)
Traceback (most recent call last):
  File "python", line 1, in <module>
  File "python", line 9, in __init__
UnboundLocalError: local variable 'num_of_accounts' referenced before assignment
````

No fim da execução de uma definição de classe, um objeto de classe é criado. O escopo que estava em vigor imediatamente antes que a definição de classe fosse criada é reintegrada, e o objeto classe é ligado aqui ao nome de classe dado no cabeçalho da definição de classe.

Agora vejamos uma curiosidade aqui. Alguém pode perguntar: ***se a classe criada é um objeto, então qual é a classe da classe objeto?***. De acordo com a filosofia de Python em que *tudo é um objeto*, o objeto de classe, de fato, tem uma classe da qual é criada, e no novo tipo de classes de Python, esta é a classe <span style="color: #000000;">type</span>.

````shell
>>> type(Account)
<class 'type'>
````

Então, só pra confundir você um pouco mais, o tipo de um type (o tipo de Account), é type. A classe type é uma ***metaclass***, uma classe criada para criar outras classes. Discutiremos sobre elas em um próximo tutorial.

![Créditos para a imagem]({filename}/images/types_map.png)
Créditos para a imagem: http://blog.invisivel.net/2012/04/10/pythons-object-model-explained/

Objetos de classe suportam referência de atributo e instanciação.
Atributos são referenciados usando a sintaxe padrão de objetos, um ponto
seguido pelo nome do atributo: obj.name. Nomes de atributos válidos são
todos os nomes de variáveis e métodos presentes no namespace da classe,
quando o objeto de classe foi criado. Por exemplo:

````shell
>>> Account.num_of_accounts
>>> 0
>>> Account.deposit
>>> <unbound method Account.deposit>
````

Instanciação de classe usa notação de função. Instanciação envolve
chamar o objeto de classe como uma função normal, sem parâmetros, como
mostrado abaixo para a classe Account:

````shell
>>> Account()
````

Depois da instanciação de um objeto de classe, um objeto de instância é
retornado, e o <span style="color: #000000;">\_\_init\_\_</span> que foi
definido na classe, é chamado com a instância como o primeiro argumento.
Isto executa qualquer inicialização definida pelo programador, como
inicializar os valores das variáveis de instância. No caso da classe
Account, o nome da conta e o balanço são setados, e o número de objetos
de instâncias é incrementado por mais 1.

Objetos de Instância
--------------------

Se imaginarmos os objetos de classe como cortadores de biscoitos, então
os objetos de instância são os biscoitos que são os resultados de
instanciar objetos de classe. Atributos, dados e métodos: referência são
as únicas operações que são válidas em objetos de instância.

Método de objetos
-----------------

Métodos de objeto são similares a objetos de função. Se <span
style="color: #000000;">x</span> é uma instância da classe <span
style="color: #660066;">Account</span>, <span
style="color: #000000;">x.deposit</span> é um exemplo de um método de
objeto. Métodos têm um argumento extra incluído em sua definição, o
argumento <span style="color: #000088;">self</span>. Este argumento
<span style="color: #000088;">self</span> se refere a uma instância da
classe. *Porque nós temos que passar uma instância como argumento para
um método?* Isso é melhor ilustrado por uma chamada de método:

````shell
>>> x = Account()
>>> x.inquiry()
10
````

O que exatamente acontece quando um método de instância é chamado? Você
pode ter notado que x.inquiry() acima é chamado sem um argumento, embora
a definição do método <span style="color: #000000;">inquiry()</span>
requeira o argumento <span style="color: #000088;">self</span>. O que
aconteceu com este argumento?

O que tornam os métodos tão especiais é que o objeto no qual um método
está sendo chamado é passado como primeiro argumento da função. Em nosso
exemplo, a chamada para <span style="color: #000000;">x.inquiry()</span>
é exatamente equivalente a <span
style="color: #660066;">Account</span>.<span
style="color: #000000;">f(x)</span>. Geralmente, chamar um método com
uma lista de *n* argumentos é equivalente a chamar a função
correspondente com uma lista de argumentos que é criada ao inserir o
objeto do método antes do primeiro argumento.

O tutorial do Python diz:

> Quando um atributo de instância é referenciado de que não é um
> atributo de dados, sua classe é pesquisada. Se o nome indica um
> atributo de classe válido que seja um objeto de função, um método de
> objeto é criado ao embalar (ponteiros) o objeto de instância e o
> objeto de função, ficando juntos em um objeto abstrato: este é o
> método de objeto. Quando o método de objeto é chamado com uma lista de
> argumentos, uma nova lista de argumento é construída a partir do
> objeto de instância e da list de argumentos, e o objeto de função é
> chamado com esta nova lista de argumentos.

O acima citado se aplica para todos os método de objetos de instância,
incluindo o método <span style="color: #000000;">\_\_init\_\_</span>. O
argumento self não é, na verdade, uma palavra chave, e qualquer nome de
argumento pode ser usado como demonstrado na definição abaixo para a
classe Account:

````python
class Account(object):
    num_of_accounts = 0

    def __init__(obj, name, balance):
        obj.name = name 
        obj.balance = balance 
        Account.num_of_accounts += 1

    def del_account(obj):
        Account.num_of_accounts -= 1

    def deposit(obj, amt):
        obj.balance = obj.balance + amt 

    def withdraw(obj, amt):
        obj.balance = obj.balance - amt 

    def inquiry(obj):
        return obj.balance
````

````shell
>>> Account.num_of_accounts
>>> 0
>>> x = Account('obi', 0)
>>> x.deposit(10)
>>> Account.inquiry(x)
>>> 10
````

Métodos de classe e estáticos
-----------------------------

Todos os métodos definidos em uma classe por padrão operam em
instancias. No entanto, podemos definir métodos de classe ou estáticos
ao decorar tais métodos com os decoradores correspondentes <span
style="color: #006666;">@staticmethods</span> ou <span
style="color: #006666;">@classmethods</span>.

### Métodos Estáticos

Métodos estáticos são métodos funções normais que existem no namespace
de uma classe. Referenciar um método estático de uma classe mostra que
em vez de um método type não ligado, uma *função* type é retornada como
mostrado abaixo:

````python
class Account(object):
    num_of_accounts = 0

    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance 
        Account.num_of_accounts += 1

    def del_account(self):
        Account.num_of_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt 

    def withdraw(self, amt):
        self.balance = self.balance - amt 

    def inquiry(self):
        return "Name={}, balance={}".format(self.name, self.balance) 

    @staticmethod
    def type():
        return "Current Account"
````

````shell
>>> Account.deposit
<unbound method Account.deposit>
>>> Account.type
<function type at 0x106893668>
````

Para definir um método estático, o decorador <span
style="color: #006666;">@staticmethod</span> é usado, e tal método não
requer o argumento <span style="color: #000088;">self</span>. Métodos
estáticos fornecem um mecanismo para melhor organização, como o código
relacionado a uma classe são colocados nessa classe e podem ser
sobrescritos em uma sub-classe como necessário.

### Métodos de classe

Métodos de classe, como o nome implica, operam nas classes em si em vez
de instâncias. Métodos de classe são criados usando o decorador <span
style="color: #006666;">@classmethod</span> com a classe passada como o
primeiro argumento para o método em vez da instância.

````python
import json

class Account(object):
    num_of_accounts = 0

    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance 
        Account.num_of_accounts += 1

    def del_account(self):
        Account.num_of_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt 

    def withdraw(self, amt):
        self.balance = self.balance - amt 

    def inquiry(self):
        return "Name={}, balance={}".format(self.name, self.balance) 

    @classmethod 
    def from_json(cls, params_json):
                params = json.loads(params_json)
        return cls(params.get("name"), params.get("balance"))

    @staticmethod
    def type():
        return "Current Account"
````

Um exemplo motivador do uso de métodos de classe é como uma *fábrica*
para criação de objeto. Imagine que dados para a classe <span
style="color: #660066;">Account</span> venham em diferentes formatos,
tais como tuplas, JSON, strings e etc. Nós não podemos definir múltiplos
métodos <span style="color: #000000;">\_\_init\_\_</span>, sendo que uma
classe Python pode ter apenas um método <span
style="color: #000000;">\_\_init\_\_</span>, desse modo métodos de
classe vêm a calhar nessas situações. Na classe <span
style="color: #660066;">Account</span> definida acima no exemplo, nós
queremos inicializar uma conta a partir de um objeto JSON, então nós
definimos um método de classe, <span
style="color: #000000;">from\_json</span> que recebe um objeto JSON e
manipula a extração de parâmetros e criação do objeto Account usando os
parâmetros extraídos. Um outro exemplo de um método de classe em ação é
o <span style="color: #000000;">dict.fromkeys</span>, método que é usado
para criar objetos dict de uma sequência de chaves e valores fornecidas.

#### Métodos especiais Python

Algumas vezes podemos querer customizar classes que definimos. Isto pode
ser alterar a maneira que objetos de classe são criados e inicializados,
ou fornecer comportamento polimórfico para certas operações.
Comportamento polimórfico habilita as classes que criamos a definir sua
própria implementação para certas operações Python, tais como a operação
+. Python fornece métodos *especiais* que habilitam isso. Esses métodos
estão normalmente na forma <span
style="color: #000000;">\_\_\*\_\_</span> onde <span
style="color: #000000;">\*</span> se refere ao nome do método. Exemplo
de tais métodos são <span style="color: #000000;">\_\_init\_\_</span> e
<span style="color: #000000;">\_\_new\_\_</span> para customizar criação
e inicialização de objeto, <span
style="color: #000000;">\_\_getitem\_\_</span>, <span
style="color: #000000;">\_\_get\_\_</span>, <span
style="color: #000000;">\_\_add\_\_</span> e <span
style="color: #000000;">\_\_sub\_\_</span> para emular tipos padrões do
Python, <span style="color: #000000;">\_\_getattribute\_\_</span>, <span
style="color: #000000;">\_\_getattr\_\_</span> e etc. para customizar
acesso de atributos. Esses são apenas alguns dos métodos especiais.
Discutiremos alguns métodos especiais abaixo para prover um
entendimento, mas a [documentação
Python](https://docs.python.org/3/reference/datamodel.html#special-method-names)
fornece uma lista compreensiva desses métodos.

### Métodos Especiais para Criação de Objetos

Novas instâncias de classes são criadas em um processo de 2 passos:
usando o método <span style="color: #000000;">\_\_new\_\_</span> para
criar uma nova instância e o método <span
style="color: #000000;">\_\_init\_\_</span> para inicializar o novo
objeto criado. Programadores já estão familiarizados com a definição do
método <span style="color: #000000;">\_\_init\_\_</span>; o método <span
style="color: #000000;">\_\_new\_\_</span> é raramente definido pelo
programador pra cada classe, mas é possível que algum queira customizar
a criação de instâncias de classe.

### Métodos Especiais para Acesso de Atributos

Nós podemos customizar o acesso de atributos para instâncias de classe
ao implementar os seguintes métodos listados:

````python
class Account(object):
    num_of_accounts = 0

    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance 
        Account.num_of_accounts += 1

    def del_account(self):
        Account.num_of_accounts -= 1

    def __getattr__(self, name):
        return "Hey I dont see any attribute called {}".format(name)

    def deposit(self, amt):
        self.balance = self.balance + amt 

    def withdraw(self, amt):
        self.balance = self.balance - amt 

    def inquiry(self):
        return "Name={}, balance={}".format(self.name, self.balance) 

    @classmethod 
    def from_dict(cls, params):
        params_dict = json.loads(params)
        return cls(params_dict.get("name"), params_dict.get("balance"))

    @staticmethod
    def type():
        return "Current Account"

x = Account('obi', 0)
````

1.   <span style="color: #000000;">\_\_getattr\_\_</span>(<span
    style="color: #000088;">self</span>, <span
    style="color: #000000;">name</span>): Este método é apenas chamado
    quando um atributo, *name*, que está referenciado não é nem um
    atributo de instância ou nem é encontrado na árvore da classe para
    o objeto. Este método deve retornar algum valor para o atributo, ou
    lança uma exceção <span
    style="color: #660066;">AttributeError</span>. Por exemplo, se *x* é
    uma instância da classe *Account* definida acima, tentar acessar um
    atributo que não existe resultará em uma chamada para este método.


        >>> acct = Account("obi", 10)
        >>> acct.number
        Hey I dont see any attribute called number

    <p>
    Note que se o código <span
    style="color: #000000;">\_\_getattr\_\_</span> referencia atributos
    de instância, e esses atributos não existem, um loop infinito pode
    ocorrer porque o método <span
    style="color: #000000;">\_\_getattr\_\_</span> é chamado
    sucessivamente sem um fim

2.  <span style="color: #000000;">\_\_setattr\_\_</span>(<span
    style="color: #000088;">self</span>, <span
    style="color: #000000;">name</span>, <span
    style="color: #000000;">value</span>): Este método é chamado sempre
    que uma atribuição de atributos é tentada. <span
    style="color: #000000;">\_\_setattr\_\_</span> deve inserir o valor
    sendo atribuído no dicionário do atributo de instância em vez de
    usar self.name=value, que resulta em uma chamada recursiva e,
    consequentemente, para um loop infinito.
3.  <span style="color: #000000;">\_\_delattr\_\_</span>(<span
    style="color: #000088;">self</span>, <span
    style="color: #000000;">name</span>): Este é chamado sempre que del
    obj é chamado.
4.  <span style="color: #000000;">\_\_getattribute\_\_</span>(<span
    style="color: #000088;">self</span>, <span
    style="color: #000000;">name</span>): Este método é sempre chamado
    para implementar acessos de atributos para instâncias de classe.

 

Métodos Especiais para Emulação de Tipos
----------------------------------------

Python define certa sintaxe especial para usar com certos tipos; por
exemplo, os elementos em listas e tuplas podem ser acessados usando a
notação de índice <span style="color: #000000;">\[\]</span>, valores
numéricos podem ser somados com o operador <span
style="color: #000000;">+</span>, e assim por diante. Podemos criar
nossas próprias classes que fazem uso desta sintaxe especial ao
implementar certos métodos especiais que o interpretador Python chama
sempre que ele encontra tais sintaxes. Ilustramos isso com um exemplo
muito simples abaixo, que emula o básico de uma lista Python:

````python
class CustomList(object):

    def __init__(self, container=None):
        # the class is just a wrapper around another list to 
        # illustrate special methods
        if container is None:
            self.container = []
        else:
            self.container = container

    def __len__(self):
        # called when a user calls len(CustomList instance)
        return len(self.container)

    def __getitem__(self, index):
        # called when a user uses square brackets for indexing 
        return self.container[index]

    def __setitem__(self, index, value):
        # called when a user performs an index assignment
        if index <= len(self.container):
            self.container[index] = value
        else:
            raise IndexError()

    def __contains__(self, value):
        # called when the user uses the 'in' keyword
        return value in self.container

    def append(self, value):
        self.container.append(value)

    def __repr__(self):
        return str(self.container)

    def __add__(self, otherList):
        # provides support for the use of the + operator 
        return CustomList(self.container + otherList.container)
````

No exemplo acima, o CustomList é um wrapper fino em torno de uma lista
real. Nós implementamos alguns métodos customizados para fins de
ilustração:

1.  <span style="color: #000000;">\_\_len\_\_</span>(<span
    style="color: #000088;">self</span>): Este é chamado quando a
    função len() é chamada em uma instância de CustomList, como mostrado
    abaixo:

        >>> myList = CustomList() 
        >>> myList.append(1)    
        >>> myList.append(2)
        >>> myList.append(3)
        >>> myList.append(4)
        >>> len(myList)
        4

2.  <span style="color: #000000;">\_\_getitem\_\_</span>(<span
    style="color: #000088;">self</span>, <span
    style="color: #000000;">value</span>): fornece suporte para o uso de
    colchetes para indexação em uma instância da classe CustomList:


        >>> myList = CustomList()
        >>> myList.append(1)    
        >>> myList.append(2)
        >>> myList.append(3)
        >>> myList.append(4)
        >>> myList[3]
        4


3.  <span style="color: #000000;">\_\_setitem\_\_</span>(<span
    style="color: #000088;">self</span>, <span
    style="color: #000000;">key</span>, <span
    style="color: #000000;">value</span>): Chamado para implementar a
    atribuição de valor para self\[key\] em uma instância da classe
    CustomList:

        >>> myList = CustomList()
        >>> myList.append(1)    
        >>> myList.append(2)
        >>> myList.append(3)
        >>> myList.append(4)
        >>> myList[3] = 100
        4
        >>> myList[3]
        100

4.  <span style="color: #000000;">\_\_contains\_\_</span>(<span
    style="color: #000088;">self</span>, <span
    style="color: #000000;">key</span>): Chamado para implementar
    operadores de teste de membros. Deve retornar *true* se item está em
    self, e *false* se não estiver:

        >>> myList = CustomList()
        >>> myList.append(1)    
        >>> myList.append(2)
        >>> myList.append(3)
        >>> myList.append(4)
        >>> 4 in myList
        True

5.  <span style="color: #000000;">\_\_repr\_\_</span>(<span
    style="color: #000088;">self</span>): Chamado para computar a
    representação do objeto para *self* quando print é chamado com o
    objeto como argumento:

        >>> myList = CustomList()
        >>> myList.append(1)    
        >>> myList.append(2)
        >>> myList.append(3)
        >>> myList.append(4)
        >>> print(myList)
        [1, 2, 3, 4]

6.  <span style="color: #000000;">\_\_add\_\_</span>(<span
    style="color: #000088;">self</span>, <span
    style="color: #000000;">otherList</span>): Chamado para computar a
    adição de duas instâncias de CustomList quando o operador + é usado
    para somar duas instâncias juntas:

        >>> myList = CustomList()
        >>> otherList = CustomList()
        >>> otherList.append(100)
        >>> myList.append(1)    
        >>> myList.append(2)
        >>> myList.append(3)
        >>> myList.append(4)
        >>> myList + otherList + otherList
        [1, 2, 3, 4, 100, 100]

Acima temos um exemplo de como podemos customizar comportamento de
classe ao definir certos métodos especiais de classe. Para uma listagem
de todos os métodos, veja a [documentação
Python](https://docs.python.org/3/reference/datamodel.html#basic-customization).
No tutorial seguinte, nós colocaremos em prática o que discutimos aqui
sobre métodos especiais e explicaremos **descriptors**, uma
funcionalidade muito importante, que tem uso generalizado em programação
orientada a objetos em Python.

NT.: Pessoal, tive uma certa dificuldade ao traduzir este artigo, pela
forma meio complicada que o autor o escreveu. Então desde já me desculpo
se alguma parte ficou meio -no sense-, e peço que coloquem nos
comentários qualquer possível melhoria que eu editarei o post :)

Leitura Complementar
--------------------

-   [Python Data Model](https://docs.python.org/3/reference/datamodel.html#)

[Clique aqui para voltar para a tabela de conteúdo.]({filename}/pages/pythonista-intermediario.md)

 

 

 
