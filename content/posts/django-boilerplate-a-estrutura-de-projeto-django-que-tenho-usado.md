title: Django Boilerplate: A estrutura de projeto Django que tenho usado
date: 2017-07-27 01:11
author: Patrick Mazulo
email: pmazulo@gmail.com
slug: django-boilerplate-a-estrutura-de-projeto-django-que-tenho-usado
category: django
tags: django, django-serie
summary: Depois de algum tempo utilizando Django e o seu famoso "startproject", você começa a se aventurar em novos caminhos testando novas estruturas. Aqui vou mostrar um pouco da atual estrutura que estou utilizando para os meus projetos
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/django-boilerplate.png

![Créditos da imagem]({filename}/images/posts/django-boilerplate.png)

# Django Boilerplate: A estrutura de projeto Django que tenho usado

Fala pessoal, tudo beleza? Finalmente eu <s>criei vergonha na cara</s> vou iniciar uma série de posts sobre Django. YAY!

Vou falar sobre alguns quesitos interessantes e que a galera lá do grupo [Django Brasil](https://t.me/djangobrasil) no Telegram pediram. Inclusive fica aí a deixa pra você participar do grupo, caso ainda não conheça :)

Antes de tudo, achei interessante começar falando sobre a estrutura de projeto. Nós já conhecemos o bom e velho `django-admin.py startproject myproject`, que vai nos gerar uma estrutura parecida com essa:

```shell
.
└── myproject
    ├── manage.py
    └── myproject
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

2 directories, 6 files
```

Depois de algum tempo, você começa a se aventurar em querer testar outras estruturas que possam melhorar a sua produtividade, modularidade, segurança e outros pontos do seu projeto. Um ótimo guia que você pode adquirir, é o livro [Two Scoops of Django](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11) que recentemente foi atualizado para a versão 1.11 (LTS) do Django. Outra maneira é pesquisar outras estruturas por aí. GitHub é uma ótima fonte, lá cê encontra **várias** opções. Daí uma ótima ideia é: ver cada um, estudar seu esqueleto, a abordagem pretendida, e se ela se encaixa bem nas suas necessidades/requisitos. Feito isso, você pode:

1. Adotar um desses boilerplates

2. Pegar o que viu de melhor nos pesquisados e fazer o seu

Há um tempo atrás, eu e 2 amigos trabalhávamos numa certa empresa. Num dado momento resolvemos mudar a maneira como iniciaríamos os novos projetos. Um desses caras havia feito uma estrutura diferente em um projeto pessoal. A partir daí, resolvemos ir lapidando até chegarmos no que tornou-se nossa estrutura "oficial". A estrutura final é aquela da imagem no início do post, e que repito aqui abaixo (save your scroll):


```shell
.
├── backend
│   └── core
│       └── migrations
├── bin
├── frontend
│   ├── bower_components
│   │   ├── jquery
│   │   ├── semantic
│   │   └── susy
│   ├── scripts
│   ├── styles
│   └── templates
│       └── core
├── requirements
└── settings
```

Como vocês podem ver, separamos tudo em módulos:

- backend
    - Irá conter tudo diretamente relacionado ao backend, e com isso teremos: os módulos das apps, bem como o arquivo `urls.py` principal e o `wsgi.py`.
- frontend
    - Tudo relacionado ao frontend estará neste diretório, ou seja, isso inclui os arquivos de template e os arquivos estáticos.
- requirements
    - Estaremos utilizando o [pip-tools](https://github.com/jazzband/pip-tools) que é uma ferramenta sensacional para ajudar a manter as versões dos seus pacotes sempre atualizadas e pinadas. Aqui você pode ler um [post sobre ele](http://jamescooke.info/a-successful-pip-tools-workflow-for-managing-python-package-requirements.html) (EN). Então dentro desse diretório você vai encontrar os arquivos `.ini` e `.txt` dos requirements do projeto.
- settings
    - Como o nome já sugere, será o módulo de configuração do projeto. Nele nós quebramos o que antes era um único `settings.py` em 4 arquivos diferentes (na verdade são 5, eu sei, mas não vamos contar com o `__init__.py`), cada um contendo partes específicas do settings, sendo eles:
        - `base.py`
        - `__init__.py`
        - `mail.py`
        - `security.py`
        - `static.py`

Dessa maneira, cobrimos as principais partes desse boilerplate. Agora um ponto importante a ressaltar é: esse projeto foi estruturado e criado para integrar o [bower](https://bower.io/), bem como facilitar o deploy de uma aplicação diretamente no [Heroku](https://www.heroku.com/). Sendo assim você vai encontrar também os sequintes arquivos:

- .bowerrc
    - É o arquivo de configuração do bower. Nele vamos encontrar, por exemplo, o diretório no qual o bower deve instalar as dependências
- Procfile
    - É o arquivo usado pelo ambiente do Heroku para declarar quais comandos vão ser executados pelos dynos da aplicação
- app.json
    - Arquivo também utilizado pelo Heroku para "descrever" as aplicações web que vão ser "deployadas" lá. Nesse arquivo você pode declarar variáveis de ambiente, bem como o buildpack dessa aplicação
- bower.json
    - Arquivo de dependências de frontend usadas pelo bower. Aqui você vai ter listado no formato JSON algumas informações, entre elas quais pacotes frontend o bower deve instalar
- package.json
    - Em resumo: é como se fosse o `bower.json` só que utilizado pelo npm, no caso, para instalar o bower
- runtime.txt
    - Usado pelo Heroku para especificar qual versão do Python vai ser usada na criação do seu ambiente lá

Pra facilitar nossa vida, você vai encontrar também um `Makefile` que vai conter atalhos para executar os comandos principais. Vão ser eles:

- `pip-compile`
    - Vai atualizar os `requirements/*.txt` com as versões mais atuais dos pacotes listados em ``requirements/*.in`
- `install-dev-requirements`
    - Instala os requirements
- `setup-frontend`
    - Instala as dependências frontend do projeto (não esqueça de rodar um `npm install` caso não tenha ainda o bower na sua máquina)

Depois disso tudo, podemos agora ter uma visão geral de como ficou nosso boilerplate:

```shell
$ tree -L 3
.
├── app.json
├── backend
│   ├── core
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── urls.py
│   └── wsgi.py
├── bin
│   └── post_compile
├── bower.json
├── example.env
├── frontend
│   ├── bower_components
│   │   ├── jquery
│   │   ├── semantic
│   │   └── susy
│   ├── scripts
│   ├── styles
│   │   └── main.scss
│   └── templates
│       ├── base.html
│       └── core
├── Makefile
├── manage.py
├── package.json
├── Procfile
├── README.md
├── requirements
│   ├── dev.in
│   ├── dev.txt
│   ├── heroku.in
│   ├── heroku.txt
│   ├── production.in
│   ├── production.txt
│   ├── test.in
│   └── test.txt
├── requirements.txt
├── runtime.txt
└── settings
    ├── base.py
    ├── __init__.py
    ├── mail.py
    ├── security.py
    └── static.py
```

Eu não vou entrar em mais detalhes (como o conteúdo dos arquivos do `settings`) porque veremos isso nos posts seguintes, como no próximo onde vou usar esse boilerplate para criar um novo projeto. Inclusive, já dando uma palhinha, essa série de posts vai ser feita em cima de um projeto bem simples: uma app Django que envia e-mails para contatos. Simples, não é? Mas dá pra fazermos um trabalho bacana e ir aprendendo juntos :)

E é isso, pessoas. O link para o projeto desse boilerplate tá aqui: [https://github.com/dunderlabs/django-boilerplate](https://github.com/dunderlabs/django-boilerplate)

Dúvidas e/ou críticas, só visitar os comentários mais abaixo. Valeu pessoal, e até a próxima!
