title: Configurando seu projeto Django
date: 2017-08-04 04:54
author: Patrick Mazulo
email: pmazulo@gmail.com
slug: django-configurando-seu-projeto
category: django
tags: django, django-serie
summary: Já temos nosso projeto, então agora vamos dar os tapas finais e começar a programar o nosso sistema de envio de e-mails!
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/criar-repositorio-github.png

![Criando repositório no GitHub]({filename}/images/posts/criar-repositorio-github.png)

Posts anteriores da série:

- [Django Boilerplate: A estrutura de projeto Django que tenho usado]({filename}/posts/django-boilerplate-a-estrutura-de-projeto-django-que-tenho-usado.md)
- [Django startproject: Iniciando o seu projeto]({filename}/posts/django-iniciando-seu-projeto.md)

Fala pessoa, tudo beleza? Vamos dar continuidade a nossa série de posts sobre Django. Nós já conhecemos a estrutura do template de projeto que usaremos, demos o `startproject` usando ele, então agora vamos começar a brincar com Django. Claro, nessa série nós não vamos ver só e somente Python/Django, mas pretendo abordar um pouquinho de cada coisa que envolve o desenvolvimento de software. Não vou me aprofundar muito, mas pretendo mostrar o pouquinho que já sei :)

Bom, antes de qualquer coisa, o que nós faremos será renomear algumas coisas no nosso projeto. Vocês vão ver que em alguns arquivos, como no `app.json`, você verá referências para "DjangoBoilerplate". Sua missão será renomear essas referências com o nome do nosso projeto "TurboSendMail". Você vai fazer isso em:

- `app.json` (atualizar "name")
- `README.md` (mudar informações gerais, nesse você está livre para colocar o que quiser)
- `bower.json` (atualizar "name" e "authors")
- `package.json` (atualizar "name", "description" e "repository", esse último com o link do seu repositório no github)

Feito isso, quero fazer uma pergunta: você já sabe o que é [Controle de Versão](https://git-scm.com/book/pt-br/v1/Primeiros-passos-Sobre-Controle-de-Vers%C3%A3o) dentro do contexto do mundo do software? Caso não, dá uma lida nesse post que linkei antes de nós podermos continuar. Pronto? Vamos continuar então.

Para essa série de posts, nós vamos utilizar o [Git](https://git-scm.com/) para o nosso versionamento. Se você ainda não havia mexido com ele antes, no mesmo site você vai encontrar uma seção para o livro [Pro Git v2](https://git-scm.com/book/pt-br/v2), com o primeiro capítulo traduzido para pt_BR. A [v1](https://git-scm.com/book/pt-br/v1) está <s>quase</s> completamente traduzida. Tirando ele, você vai poder encontrar muito material bacana sobre na web.

Conforme formos usando os comandos, vou dando rápidas explicações sobre os comandos. Então, let's go! O primeiro que vamos usar, vai ser como poderíamos esperar, o comando para iniciar. No git, ele vai ser o `git init`. Então uma vez dentro do diretório do seu projeto, você vai executar esse comando:

```shell
$ git init
Initialized empty Git repository in /home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/.git/
```

Como o comando vai mostrar pra você, o que ele vai fazer é criar um diretório `.git/` dentro do diretório do seu projeto. Ele vai ser usado pelo Git para gerenciar esse diretório (ou repositório) localmente e remotamente. Só isso? Quase. Uma prática mais do que comum também é você deixar salvo o seu código na ~nuvem~. Existem alguns serviços web para isso, porém os 3 mais conhecidos são:

- [GitHub](https://github.com)
- [BitBucket](https://bitbucket.org)
- [GitLab](https://gitlab.com)

Cada um vai ter sua vantagem e desvantagem, mas há a unanimidade em usar o GitHub (que já virou sinônimo de Open Source) para projetos. Além da sua facilidade no uso. Por esse e outros motivos, usaremos ele. Após você criar sua conta, poderá criar repositórios públicos, da maneira como mostra a imagem abaixo que seria a criação de um repositório para hospedar o nosso código.

![Criando repositório no GitHub]({filename}/images/posts/criar-repositorio-github.png)


Você pode, claro, mudar o nome do repositório e a descrição. Só **não marque** aquele checkbox com texto "Initialize this repository with a README". Após preencher nome e descrição (esse último opcional), basta clicar em "Criar repositório". Após isso, você verá uma dela semelhante a essa abaixo:

![Criando repositório no GitHub]({filename}/images/posts/add_remote_github.png)

Você verá que tem duas opções: uma criando um repositório com o `git init`, cria um arquivo e executa alguns outros comandos antes de enviar o código (que não é o nosso caso uma vez que já fizemos isso), e outra abordagem onde você adiciona o endereço para o seu repositório online. Vamos fazer um pouco de cada. Vamos lá.

Uma vez que já demos o *init* com o Git, vamos adicionar o nosso repositório remoto ao nosso local. Faremos isso usando o `git remote` usando a opção `add`.

```shell
$ git remote add github git@github.com:dunderlabs/turbo_send_mail.git
```

Você vê que eu estou passando para o comando `add` um nome `github` antes da URL, certo? Esse vai ser o "nome" do nosso repositório remoto. Porque isso? 2 motivos:

- Você não iria querer digitar aquela URL toda vez que quiser enviar seu código para o GitHub
- Você pode ter mais de um endereço. Por exemplo, ter o seu código no GitHub e no GitLab. Seriam 2 URLs, com 2 nomes diferentes

Para você saber quais *remote*'s você está usando, basta executar o seguinte comando:

```shell
$ git remote -v
github  git@github.com:dunderlabs/turbo_send_mail.git (fetch)
github  git@github.com:dunderlabs/turbo_send_mail.git (push)
```

Certo, agora vamos dar uma olhada em como nosso repositório local está, e pra isso usaremos o comando `git status`. Você verá uma saída parecida com essa, mostrando os arquivos que não estão sendo rastreados ou que foram alterados.

```shell
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    .bowerrc
    .gitignore
    Makefile
    Procfile
    README.md
    app.json
    backend/
    bin/
    bower.json
    example.env
    frontend/
    manage.py
    package.json
    requirements.txt
    requirements/
    runtime.txt
    settings/
```

Beleza, agora vamos adicionar todos esses arquivos e diretórios para serem rastreados. Uma vez feito isso, o Git vai ter um registro de cada alteração feita dentro desse nosso repositório.

```shell
$ git add .
```

Após adicionar, e você executar mais uma vez o `git status`, vai notar que a mensagem está diferente. Ele está reconhecendo todos, e aguardando para que possamos escrever nossa mensagem de commit, registrando assim essa alteração.

```shell
$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

    new file:   .bowerrc
    new file:   .gitignore
    new file:   Makefile
    new file:   Procfile
    new file:   README.md
    new file:   app.json
    new file:   backend/core/__init__.py
    new file:   backend/core/admin.py
    new file:   backend/core/apps.py
    new file:   backend/core/forms.py
    new file:   backend/core/migrations/__init__.py
[mais...]
```

Ao você executar `git commit`, você provavelmente vai ser jogado no editor de texto [Nano](https://en.wikipedia.org/wiki/GNU_nano), ou no [Vim](https://www.vim.org/). Estando em algum desses, você vai poder escrever sua mensagem de commit. A minha vai ser: "Start project".

```shell
Start project
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
#
# Initial commit
#
# Changes to be committed:
#       new file:   .bowerrc
#       new file:   .gitignore
#       new file:   Makefile
#       new file:   Procfile
#       new file:   README.md
#       new file:   app.json
#       new file:   backend/core/__init__.py
[mais...]
```

Agora só resta uma coisa: enviar o nosso código para o nosso repositório remoto, lá no GitHub. Para isso, vamos usar o `git push`. Seguido desse comando, você vai informar para qual repositório remoto você quer enviar, e qual branch local.

```shell
$ git push github master
Counting objects: 47, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (37/37), done.
Writing objects: 100% (47/47), 7.98 KiB | 0 bytes/s, done.
Total 47 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), done.
To github.com:dunderlabs/turbo_send_mail.git
 * [new branch]      master -> master
```

Tudo maravilha. Agora vamos configurar o nosso `.env`. Lembra que temos um arquivo `example.env` no nosso boilerplate? Vamos usar ele agora. O conteúdo dele vai ser esse debaixo:

```shell
# Rename to .env
DATABASE_URL='postgres://user:password@localhost:5432/database_name'
DEBUG=True

SECRET_KEY=put-an-awesome-secret-key-here

STATIC_URL=
MEDIA_URL=

# Email settings
DEFAULT_FROM_EMAIL=
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=
SENDGRID_PASSWORD=
SENDGRID_USERNAME=
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

Eu sugiro usar o banco de dados postgres também para o desenvolvimento, mas caso você não o tenha instalado e por algum motivo não possa instalar agora, não precisa. Se você não usar, o [python-decouple](https://pypi.python.org/pypi/python-decouple) vai usar outros valores. No caso do banco de dados, ao invés de usar um Postgres, usará o SQLite. Mas, vou seguir como se fôssemos utilizar a primeira opção. Para isso, vou primeiro criar o banco na minha máquina:

```shell
createdb turbo_send_mail
```

Após criar, basta mudar as credenciais em `DATABASE_URL` do nosso arquivo. Mas antes disso, vamos fazer uma cópia dele e renomear para .env
```shell
cp example.env .env
```

Agora abrindo o esse novo arquivo, vamos substituir alguns valores. Ao final, ele deverá ficar parecido com isso:


```shell
# Rename to .env
DATABASE_URL=postgres://mazulo@localhost:5432/turbo_send_mail
DEBUG=True

SECRET_KEY=&cb%k3i$$r2ku69te*2+ikhuwr7ve07kb(nasfvbnkag3&8k%4
ALLOWED_HOSTS=127.0.0.1

STATIC_URL=/static/
MEDIA_URL=/media/

# Email settings
DEFAULT_FROM_EMAIL=
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=
SENDGRID_PASSWORD=
SENDGRID_USERNAME=
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

Veja que substituí o anterior `postgres://user:password@localhost:5432/database_name` por `postgres://mazulo@localhost:5432/turbo_send_mail`. No meu caso, eu não coloquei a senha, porque configurei o meu postgres para localmente não precisar de autenticação. Aquela SECRET_KEY eu gerei usando um trecho de código desse [gist](https://gist.github.com/ndarville/3452907). Você não precisa se preocupar com os dados de email, por enquanto. Veremos isso depois.

Pronto, temos nosso banco criado e as credenciais salvas no nosso `.env`. Agora lembra daquela mensagem que vimos no post anterior ao rodar o `runserver` sobre migrações não aplicadas? Então, agora que temos nosso banco, vamos aplicá-las. Sobre elas, vamos falar mais para frente :)

```shell
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, sites
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
  Applying sites.0001_initial... OK
  Applying sites.0002_alter_domain_unique... OK
```

Para termos certeza que está tudo OK, você pode acessar o seu banco localmente, e ver as tabelas que foram criadas. A seguir, você vai ver respectivamente os comandos utilizados para: acessar o shell do postgres, listar os bancos, conectar em um deles e mostrar as tabelas desse banco.

```shell
$ psql postgres
psql (9.6.3)
Type "help" for help.

postgres=# \l
                                     List of databases
      Name       |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------------+----------+----------+-------------+-------------+-----------------------
 turbo_send_mail | mazulo   | UTF8     | en_US.UTF-8 | en_US.UTF-8 |

postgres=# \c turbo_send_mail
You are now connected to database "turbo_send_mail" as user "mazulo".

turbo_send_mail=# \dt
 public | auth_group                 | table | mazulo
 public | auth_group_permissions     | table | mazulo
 public | auth_permission            | table | mazulo
 public | auth_user                  | table | mazulo
 public | auth_user_groups           | table | mazulo
 public | auth_user_user_permissions | table | mazulo
 public | django_admin_log           | table | mazulo
 public | django_content_type        | table | mazulo
 public | django_migrations          | table | mazulo
 public | django_session             | table | mazulo
 public | django_site                | table | mazulo
```

Finalizada toda essa parte, se rodarmos novamente o `runserver`, não veremos novamente aquela mensagem. Ficará assim:

```shell
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
August 04, 2017 - 07:15:05
Django version 1.11.3, using settings 'settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Tá começando a ficar muito bacana. Eu falei que nesse post já teríamos programação, mas o post acabou ficando um pouco extenso demais, então vou pausar aqui. No próximo vou falar um pouco sobre tests, e a partir dele vamos ter bastante Python/Django. Vou tentar lançar ele amanhã, então fica ligado aqui :D

Dúvidas e/ou críticas, só visitar os comentários mais abaixo. Valeu pessoal, e até a próxima!
