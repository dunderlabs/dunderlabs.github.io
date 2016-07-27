title: Eu deveria usar PYTHONOPTIMIZE?
date: 2016-07-26 22:09
author: Patrick Mazulo
email: pmazulo@gmail.com
slug: eu-deveria-usar-pythonoptimize
category: python
tags: python, optimization, translations
summary: Existem alguns flows no uso do git. Aqui você vai encontrar um que segue uma abordagem quase atômica, que pode resolver grandes problemas.
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/pythonoptimize.jpg

![Créditos da imagem]({filename}/images/posts/pythonoptimize.jpg)

Créditos da imagem: <http://blog.ziade.org/2015/11/25/should-i-use-pythonoptimize/>

## Eu deveria usar PYTHONOPTIMIZE?

Ontem, eu estava revisando alguns códigos para os nossos projetos e em um PR eu vi algo ligeiramente similar a isso:

````python
try:
    assert hasattr(SomeObject, 'some_attribute')
    SomeObject.some_attribute()
except AssertionError:
    SomeObject.do_something_else()
````

Não me levou a crer que seria uma boa ideia depender do `assert` porque quando Python é executado usando a flag **PYTHONOPTIMIZE**, que você pode ativar com o variável de ambiente de mesmo nome ou com `-O` ou `-OO`, todas as declarações de `assert` são retiradas do código.

Para minha surpresa, muitas pessoas estão ignorando `-O` e `-OO` dizendo que ninguém usa essas flags em produção, e que o código que contém asserts é bom.

**PYTHONOPTIMIZE** tem três valores possíveis: **0**, **1** (-O) or **2** (-OO). **0** é o default, onde nada acontece.

Quando o valor é **1**, é isso o que acontece:

- asserts são removidos
- os arquivos bytecode gerados estão usando a extensão **.pyo** ao invés de **.pyc**
- **sys.flags.optimize** é setado para 1
- **__debug__** é setado para False

E para **2**:

- tudo que o **1** faz
- docstrings são removidas

A meu conhecimento, uma razão antiga para rodar com a flag **-O** era produzir um código bytecode mais eficiente, mas como falei isso não é mais verdade.

Um outro comportamento que mudou está relacionado ao **pdb**: você não poderia rodar um debugging passo-a-passo quando **PYTHONOPTIMIZE** estiver ativado.

Por último, a questão **.pyo** vs **.pyc** deve sumir um dia, de acordo com a [PEP 488](https://www.python.org/dev/peps/pep-0488).

Então o que faz isso nos deixar? Há alguma boa razão para usar essas flags?

Algumas aplicações aproveitam a flag **__debug__** para oferecer dois modos de execução. Um com mais informações de debug, ou um comportamento diferente quando um erro é encontrado.

Esse é o caso para o pyglet, de acordo com a [documentação dele](http://pyglet.readthedocs.org/en/latest/programming_guide/debug.html#error-checking).

Algumas empresas também estão usando o modo **-O** para ligeiramente reduzir o consumo de memória ao rodar aplicações. Esse parece ser o caso no YouTube.

E é inteiramente possível que o próprio Python, no futuro, adicione algumas novas otimizações por trás dessa flag.

Então, sim, mesmo que você não use essas opções de flags, é uma boa prática assegurar que seu código python está testado com todos os possíveis valores para **PYTHONOPTIMIZE**.

É fácil demais, apenas rode seus testes com **-O** e **-OO** e sem, e assegure que seu código não depende de docstrings ou assertions.

Se você tem dependências em algum deles, tenha certeza que seu código trata elegamentemente o modo otimizado, ou lança um erro no início explicando porque você não está compatível com ele.

Agradecimentos a Brett Cannon, Michael Foord e outros pelo feedback no Twitter sobre este assunto.


Dúvidas e/ou críticas, só visitar os comentários mais abaixo. Valeu pessoal, e até a próxima!

Referências:

- [Post original](http://blog.ziade.org/2015/11/25/should-i-use-pythonoptimize/)
