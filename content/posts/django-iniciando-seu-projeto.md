title: Django startproject: Iniciando o seu projeto
date: 2017-07-27 19:21
author: Patrick Mazulo
email: pmazulo@gmail.com
slug: django-iniciando-seu-projeto
category: django
tags: django, django-serie
summary: Uma vez que temos a escolha da nossa estrutura, vamos iniciar um projeto Django novo usando esse boilerplate
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/django-startproject.png

![Créditos da imagem]({filename}/images/posts/django-startproject.png)

Posts anteriores da série:

- [Django Boilerplate: A estrutura de projeto Django que tenho usado]({filename}/posts/django-boilerplate-a-estrutura-de-projeto-django-que-tenho-usado.md)

Fala pessoal, tudo beleza? Como prometido, vamos dar prosseguimento nesta série de posts. Agora que já temos o nosso boilerplate, vamos poder iniciar nosso projeto. Antes de tudo, você precisa ter configurado o seu ambiente de desenvolvimento. Se você não tiver feito isso ainda e/ou não souber muito sobre esse tema, aqui na casa temos [outro post]({filename}/posts/criando-ambiente-django.md) onde você vai poder tirar suas dúvidas sobre o assunto :)

Sem mais delongas, vou criar o meu ambiente virtual para o projeto usando o virtualenvwrapper. O output vai ser algo muito parecido com:

```shell
$ mkvirtualenv turbo_send_mail
Using base prefix '/usr'
New python executable in /home/mazulo/.virtualenvs/turbo_send_mail/bin/python
Installing setuptools, pip, wheel...done.
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/turbo_send_mail/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/turbo_send_mail/bin/postdeactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/turbo_send_mail/bin/preactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/turbo_send_mail/bin/postactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/turbo_send_mail/bin/get_env_details
Error: deactivate must be sourced. Run 'source deactivate'
instead of 'deactivate'.
```

Feito isso, vamos instalar o Django para que possamos utilizar o `django-admin`. Basta um comando do `pip`:

```shell
$ pip install django
Collecting django
  Downloading Django-1.11.3-py2.py3-none-any.whl (6.9MB)
    100% |████████████████████████████████| 7.0MB 131kB/s 
Collecting pytz (from django)
  Using cached pytz-2017.2-py2.py3-none-any.whl
Installing collected packages: pytz, django
Successfully installed django-1.11.3 pytz-2017.2
```

Agora vamos usar alguns recursos do `django-admin` que podem passar despercebidos. Dentre eles:

- `--template`
    - Aqui você pode especificar um diretório ou uma URL de um template de projeto customizado. No caso de URL, vamos usar a do GitHub que nos dá o nosso projeto comprimido num `.zip`.
- `--verbosity`
    - Especifica a quantidade de informação que aquele comando vai jogar na tela conforme ele é executado. Os níveis são:
        - 0 significa sem output
        - 1 significa output normal (default)
        - 2 significa output verboso
        - 3 significa output muito verboso

Vou usar o 3 que é pra termos o máximo de informação de como esse processo ocorre. Ah, como comentei no post anterior, o nosso projeto vai ser um simples sistema que envia e-mails para contatos que eu salvar, como em uma agenda. O nome deste [inovador](https://media.giphy.com/media/aBDQ0bQ4b4sx2/giphy.gif) projeto será: *turbo_send_mail_project*. Nome escolhido, vamos enfim dar o start:


```shell
$ django-admin startproject turbo_send_mail_project --template=https://github.com/dunderlabs/django-boilerplate/archive/master.zip --verbosity 3
Rendering project template files with extensions: .py
Rendering project template files with filenames: 
Downloading https://github.com/dunderlabs/django-boilerplate/archive/master.zip
Extracting /tmp/django_project_template_6nafk1qd_download/django-boilerplate-master.zip
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/runtime.txt
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/requirements.txt
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/package.json
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/manage.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/example.env
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/bower.json
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/app.json
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/README.md
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/Procfile
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/Makefile
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/.gitignore
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/.bowerrc
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/settings/static.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/settings/security.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/settings/mail.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/settings/base.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/settings/__init__.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/requirements/test.txt
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/requirements/test.in
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/requirements/production.txt
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/requirements/production.in
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/requirements/heroku.txt
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/requirements/heroku.in
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/requirements/dev.txt
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/requirements/dev.in
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/frontend/templates/base.html
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/frontend/templates/core/index.html
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/frontend/styles/main.scss
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/bin/post_compile
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/wsgi.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/urls.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/views.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/utils.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/urls.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/tests.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/models.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/forms.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/apps.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/admin.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/__init__.py
Creating /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/migrations/__init__.py
Cleaning up temporary files.
```

Como você pode ver, ele faz o download do nosso projeto zipado em `/tmp/django_project_template_<hash>_download/`, um diretório que ele criou para extrair os arquivos do `.zip` e depois criar o nosso projeto usando esses arquivos dentro do diretório onde eu rodei o comando. Após isso, ele vai limpar os arquivos extraídos naquele diretório temporário criado anteriormente, deixando só o `master.zip`. Ao acessar o diretório do projeto que o `startproject` criou, você vai notar que a estrutura vai ser extamente a mesma mostrada no post anterior:

```shell
$ tree -d -L 4               
.
├── backend
│   └── core
│       └── migrations
├── bin
├── frontend
│   ├── styles
│   └── templates
│       └── core
├── requirements
└── settings
```

Finalizada essa parte, os próximos passos serão: atualizar os pacotes nos requirements, instalar eles e por fim instalar as dependências do front. Vou em cada um dos passos.

Para o `make pip-compile` você vai ter uma saída parecida com essa para cada um dos arquivos `requirements/*.in`:

```shell
$ make pip-compile 
# Update requirements/*.txt with latest packages from requirements/*.in
>>> Installing/upgrading pip-tools...
pip install -qU pip-tools
>>> Upgrading local packages...
pip-compile -U requirements/dev.in
#
# This file is autogenerated by pip-compile
# To update, run:
#
#    pip-compile --output-file requirements/dev.txt requirements/dev.in
#
click==6.7                # via python-dotenv
dj-database-url==0.4.2
django-appconf==1.0.2     # via django-compressor
django-compressor==2.1.1
django==1.11.3
[mais...]
```

Após essa atualização, só nos resta instalar usando o comando `make install-dev-requirements`, que vai nos dar um output semelhante a esse:

```shell
$ make install-dev-requirements 
# Install requirements for a local development environment
>>> Installing dev requirements...
pip install -qU pip-tools
pip-sync requirements/*.txt
Collecting dj-database-url==0.4.2
  Using cached dj_database_url-0.4.2-py2.py3-none-any.whl
Collecting django-appconf==1.0.2
  Using cached django_appconf-1.0.2-py2.py3-none-any.whl
Collecting django-compressor==2.1.1
[mais...]
```

Agora só ficou faltando as dependências do front. Mas antes de rodar o comando, certifique-se que você tem o [bower](https://bower.io/) instalado. Caso contrário, na página oficial você vai encontrar um guia de como instalar, de acordo com o seu sistema operacional. Feito isso, execute o comando `make setup-frontend`, que vai gerar um output como esse:

```shell
$ make setup-frontend 
bower install --allow-root
bower semantic#^2.2.4           cached https://github.com/Semantic-Org/Semantic-UI.git#2.2.10
bower semantic#^2.2.4         validate 2.2.10 against https://github.com/Semantic-Org/Semantic-UI.git#^2.2.4
bower susy#^2.2.12              cached https://github.com/ericam/susy.git#2.2.12
bower susy#^2.2.12            validate 2.2.12 against https://github.com/ericam/susy.git#^2.2.12
bower jquery#^3.1.0             cached https://github.com/jquery/jquery-dist.git#3.2.1
bower jquery#^3.1.0           validate 3.2.1 against https://github.com/jquery/jquery-dist.git#^3.1.0
[mais...]
susy#2.2.12 frontend/bower_components/susy

jquery#3.2.1 frontend/bower_components/jquery

semantic#2.2.11 frontend/bower_components/semantic
└── jquery#3.2.1
```

**Agora estamos prontos!** Para testar nossa aplicação, vamos rodar o famoso `runserver`. Ao executar esse comando, você verá uma saída como a debaixo, mas já avisando: não se preocupe com a mensagem que vai estar em vermelhos sobre *15 unapplied migrations* por enquanto. A saída vai ser algo assim:

```shell
$ python manage.py runserver 8001
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions, sites.
Run 'python manage.py migrate' to apply them.

July 27, 2017 - 21:23:45
Django version 1.11.3, using settings 'settings'
Starting development server at http://127.0.0.1:8001/
Quit the server with CONTROL-C.
```

Ao acessar [http://localhost:8001/](http://localhost:8001/) você verá uma página quase em branco. "Quase" porque se você abrir o arquivo `frontend/styles/main.scss` vai ver que o `body` vai estar com `background: #eee;`. O que significa que o carregamento dos arquivos estáticos, bem como o compilador e "compressor" de arquivos (ou seja, o django-compreesor) está funcionando muito bem. Bom, sobre eles eu vou falar em outro post, porque esse acaba por aqui ;)

No próximo post vamos começar a programar de verdade, com uns leves toques de testes automatizados. Fiquem ligados!

Dúvidas e/ou críticas, só visitar os comentários mais abaixo. Valeu pessoal, e até a próxima!


<br>
Referências:

- Documentação sobre o [django-admin](https://docs.djangoproject.com/en/1.11/ref/django-admin/)
