title: Série Django - Settings
date: 2016-01-17 21:34
author: Patrick Mazulo
email: pmazulo@gmail.com
slug: serie-django-settings
category: django
tags: python, django, django settings, web development
summary: Iniciando nossa série de posts sobre Django, vamos falar sobre o arquivo settings.py, sua função e suas variáveis de configuração
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/django-settings.jpg

![Créditos da imagem]({filename}/images/posts/django-settings.jpg)	

Créditos da imagem: <https://www.coderedcorp.com/blog/django-settings-for-multiple-environments/>

Estaremos iniciando uma nova série no blog. Mas vamos tentar fazer de uma maneira diferente. Ao invés de criarmos uma aplicação, vamos falar sobre o Django em si, seus componentes, como funcionam, como se interrelacionam e etc. O post de hoje na realidade é uma "transcrição" de um hangout que aconteceu há um tempo atrás, de um grupo de estudo no Telegram chamado "Django Group - Initial Steps". Caso tenha interesse, [neste link](http://pastebin.com/nwYyG7Ar) vc terá informações sobre como se juntar ao grupo.

Neste [hangout](https://youtu.be/m7PujnjPboU) em questão falamos sobre o módulo `settings.py`. Então, vamos discutir um pouco sobre ele aqui neste post.

O `settings.py` nada mais é do que um arquivo de configuração do Django que contém todas as configurações da sua instalação do framework. Esse arquivo nada mais é do que também um módulo Python com váriaveis de nível de módulo.

Agora vamos percorrer suas linhas e entender o que cada uma faz.

Ao início do arquivo, você terá uma string de múltiplas linhas, com informações relevantes, incluindo links da documentação para você depois ter mais informações sobre este arquivo.
Agora vamos trazer atenção para estas linhas:

````python
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
````

O que está acontecendo? E para que serve esta variável `BASE_DIR`?

O módulo `os` do Python nos fornece uma maneira portável de usar funcionalidades do sistema operacional. No caso estaremos usando para manipular caminhos de diretórios (paths).

BASE_DIR é a variável que vai ter o caminho para o nosso projeto Django, e será usada mais a frente. Serve como uma maneira facilitada para que não tenhamos que trabalhar com caminho absoluto (absolute paths). Imagine que você salve o caminho para o seu projeto com o caminho absoluto como  `BASE_DIR = '/home/<user>/dev/django_projects/my_project'`, e por algum motivo tenha que mudar seu projeto para outra máquina. Quanta dor de cabeça seria para mudar todos os arquivos onde você precise desse caminho? Pois bem, o settings, ao iniciar o projeto, já vem com uma abordagem bem bacana para facilitar e nos livrar desse imenso trabalho.

Mas para entender melhor vamos pedaço por pedaço.

`__file__` é um atributo do módulo atual que representa o nome do arquivo. Faça um teste: salve um arquivo .py apenas com um `print(__file__)` e execute-o para ver o que será printado na tela.
Este vai ser o ponto de partida para descobrirmos o restante do caminho para o projeto.
Agora vamos realizar as chamadas dos métodos de dentro para fora, para podermos ver como vamos conseguir realizar tal façanha.

A chamada mais interna é esta: 
````python
os.path.abspath(__file__)
````
O `abspath` vai nos retornar uma versão absoluta e normalizada do caminho deste arquivo (arquivo este disponibilizado pelo `__file__`, lembra?). Digamos que na minha máquina eu tenha um projeto django chamado "django\_project\_1\_9". O `abspath` retornaria o seguinte caminho:

````shell
/home/mazulo/dev/web/django_projects/django_project_1_9/django_project_1_9/settings.py
````
Perceba que ao final do arquivo nós temos o próprio arquivo `settings.py`. Pois bem, o resultado desta chamada vai ser imediatamente jogado para a chamada mais externa, que no caso é o:

````python
os.path.dirname(os.path.abspath(__file__))
````
O `dirname` vai retorna o nome do diretório pai do caminho passado ao diretório. Vai ser o primeiro elemento do par retornado ao passar este path para a função `os.path.split()`. O resultado será:

````shell
/home/mazulo/dev/web/django_projects/django_project_1_9/django_project_1_9
````
Note que ele apenas retirou o nome do arquivo `settings.py`. Este é o diretório onde está o arquivo `settings.py`, ainda não é a raiz do nosso projeto, nosso atual objetivo. O resultado dessa chamada será então jogado como parâmetro para a última função encadeada:

````python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
````
Usamos novamente o `dirname` para pegar o diretório pai. Uma vez o último diretório era onde está armazenado o settings, acima dele teremos a raiz do nosso projeto, onde também está o arquivo `manage.py`. E é exatamente isso que será retornado e atribuído para a variável `BASE_DIR`:

````shell
/home/mazulo/dev/web/django_projects/django_project_1_9
````

Pronto, aí está o caminho para a raiz do nosso projeto sendo setada de maneira dinâmica. Agora, independente de quantas vezes trocarmos nosso projeto de pasta/máquina, este caminho estará funcionando perfeitamente.

Seguindo em frente teremos o `DEBUG`. 

````python
DEBUG = True
````

Sua função basicamente é mostrar informações detalhadas em uma página sobre o erro ocorrido. Lembra daquela página amarela?

![Exemplo da página de erro]({filename}/images/posts/django_page_error.png)

Mas não somente na documentação, como em qualquer post você vai encontrar o seguinte conseglho: **NUNCA** faça deploy de um sistema com o modo `DEBUG` ligado. **NUNCA**. O motivo é que nessa tela de erro, junto com o traceback do erro, são mostradas muitos metadados sobre o seu ambiente, assim como o que está definido no seu settings. Então, fica dado o recado: **NUNCA** *faça deploy de um sistema com o modo `DEBUG` ligado.*

Logo após a declaração do `BASE_DIR`, teremos o `ALLOWED_HOSTS`:

````python
ALLOWED_HOSTS = []
````

O `ALLOWED_HOSTS` é uma lista de strings representando o host/nome de domínio que o projeto Django pode servir. Serve como uma medida de segurança para impedir que um invasor possa realizar certos tipos de ataque (evenenamento de cache, disparo de e-mails de redefinição de senha contendo links para hosts maliciosos e etc).

Seguindo em frente teremos uma das mais conhecidas variáveis deste módulo, e primeiramente modificadas ao início de um projeto: `INSTALLED_APPS`

````python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
````

`INSTALLED_APPS` é uma lista de strings designando todas as aplicações que estão habilitadas nesta instalação do Django. Cada string deve ser um caminho Python (com pontos, algo como 'module.class') para:

- Uma classe de configuração de aplicação, ou
- Um pacote contendo uma aplicação (o caso daquele 'myapp')

Logo após teremos o `MIDDLEWARE_CLASSES`:

````python
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
````


O `MIDDLEWARE_CLASSES` é uma lista de classes Middleware que serão usadas no seu projeto Django. Middleware na realidade é um framework do Django, que tem um conjunto de classes que servem como "gatilhos" para processar e modificar request/response. Cada componente é responsável por fazer alguma coisa em específico. Por exemplo, é por causa do `'django.contrib.auth.middleware.AuthenticationMiddleware'` que você consegue ter acesso ao usuário da requisição (`request.user`, para ver o código do Django responsável por isso, [clique aqui](https://github.com/django/django/blob/master/django/contrib/auth/middleware.py#L22)), e também ao dicionário session (`request.session`), tendo a classe `'django.contrib.sessions.middleware.SessionMiddleware'` como responsável por isso. A ordem em que está configurado realmente importa, porque um middleware pode depender de outro. Por exemplo os que citamos aqui: a classe `AuthenticationMiddleware` armazena o usuário na sessão, então ele deve rodar depois do `SessionMiddleware`. Tudo beleza? Próximo, então.

`TEMPLATES` é uma lista de configuraçẽs para todas as engines de templates a serem usadas pelo Django. Cada item da lista é um dicionário contendo as opções para uma única engine. Neste dicionário teremos as seguintes chaves para sua configuração:

````python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
````

`BACKEND`: o backend/engine que será usado para renderizar os templates. Por padrão é usado o `DjangoTemplates`, mas você pode trocar e usar o `Jinja2` no lugar, que também já vem por padrão. Você também pode usar alguma outra engine de terceiros, basta indicar o caminho completo: `'mypackage.whatever.Backend'`.

`DIRS`: Diretórios onde a engine vai procurar por arquivos de templates, em ordem de pesquisa.

`APP_DIRS`: Valor booleano que vai indicar se a engine deve procurar por arquivos de templates dentro das aplicações instaladas no projeto.

`OPTIONS`: Um dicionário que servirá como parâmetros extras para passar ao backend do template. Esses parâmetros podem variar dependendo do backend. Por padrão virá apenas com apenas uma chave-valor, chamado `context_processors`.

`context_processors` é uma lista de objetos chamáveis que são usados para popular o contexto no objeto `RequestContext`. Esses chamáveis recebem um objeto request como argumento e retornam um dicionário de item para serem incorporados no contexto.

Vamos aos `WSGI_APPLICATION`:

````python
WSGI_APPLICATION = 'django_project_1_9.wsgi.application'
````

É o caminho Python completo para o objeto WSGI da aplicação que os servidores built-in (`runserver`, por exemplo) do Django vão usar. Ao executar o `django-admin.py startproject`, o comando vai criar um arquivo `wsgi.py` simples com um `application` chamável e apontar essa configuração para essa `application`.

Agora chegamos em outro também muito importante, o `DATABASES`:

````python
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
````

Nada mais é do que um dicionário de dicionários (dicionário aninhado) onde cada dicionário contém as configurações para uso de um banco de dados, possibilitando assim o uso de múltiplos banco num mesmo projeto. A configuração mais simples para esta variável encontra-se no `default` gerado pelo `django-admin.py` (snippet acima).

Seguindo em frente teremos o `AUTH_PASSWORD_VALIDATORS`:

````python
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
````

É uma lisa de validadores que são usados para checar a força da senha do usuário. O Django já disponibiliza alguns por padrão, mas nada o impede de criar os seus próprios e usar nesta configuração.


Internacionalização:

````python
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
````

Vamos por partes:

- `LANGUAGE_CODE`: Uma string que representa o código do idioma para esta instalação. Esse código tem de estar de acordo com o [formato padrão de ID de linguagem](https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code). Essa variável tem dois propósitos:
	
	- Se o locale middleware não está em uso, ele vai decidir qual tradução vai ser servida para todos os usuários
	- Se o locale middleware está ativado, ele fornece um idioma como fallback no caso do idioma escolhido pelo usuário não puder ser determinado, ou não for suportado pelo website.

- `TIME_ZONE`: Uma string representando a time zone para essa instalação. Essa não necessariamente vai ser a time zone do server. Um servidor pode servir múltiplos projetos Django, cada um com sua configuração de time zone separada. Ao usar `USE_TZ` como `False`, essa será a time zone na qual Django vai armazenar todos os horários (datetimes). Já quando o `USE_TZ` está setado como `True`, esse vai ser a time zone padrão que o Django vai usar para mostrar horários em templates, e interpretar datas/horários submetidos em forms.

- `USE_TZ`: Um boolean que indica se datas/horários serão reconhecidos pela timezone, ou não. Se for `True`, então o Django vai usar esse reconhecimento de datetimes internamente. Caso contrário, Django vai usar datetimes no tempo local.

- `USE_I18N`: Um boolean indicando se o sistema de tradução do Django deve ser habilitado.

- `USE_L10N`: Indica se os dados devem ser formatados levando em consideração sua localização. Se for `True`, Django vai mostrar números e datas usando o formato local atual.

E por fim, ao final do `settings.py` padrão gerado pelo `django-admin.py`, teremos o `STATIC_URL`:

````python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
````

Vai ser a URL usada para se referir aos arquivos estáticos localizados no `STATIC_ROOT`.

Exemplo: "/static/" (como no snippet acima), ou "http://static.server.com/"

Digamos que seus arquivos estáticos estão dentro do seu projeto Django, que seu `STATIC_URL` é "static", e que seu site se chama "http://meusite.com". No seu projeto você tem uma pasta "staticfiles" onde há um diretório para imagens chamado "img/". Ao acessar pela web a URL de alguma imagem do seu site, o caminho seria algo como: `http://meusite.com/static/img/imagem.jpg`. Sacou? :)


Bom pessoal, por enquanto é isso. Ainda tem **MUITA** coisa, que se eu fosse cobrir tornaria este post gigantescamente maior do que ficou hahaha. Caso tenha curiosidade, não esqueça de visitar a documentação.
E se você curtiu esse post, compartilhe com os amigos devs! :D

PS.: Há um python packate muito bacana chamado [simple-settings](https://github.com/drgarcia1986/simple-settings), desenvolvido pelo [@drgarcia1986](https://twitter.com/drgarcia1986), com o intuito de facilitar a maneira como você gerencia os settings dos projetos. Vale a pena dar uma olhada.

Valeu pessoal, e até a próxima!


Referências:

- [Documentação Django - settings](https://docs.djangoproject.com/en/1.9/topics/settings/)
- [Django Book](http://www.djangobook.com/en/2.0/chapter17.html)
- [Image how middleware works](https://docs.djangoproject.com/en/1.9/_images/middleware.svg)
- [Understanding django middlewares](http://agiliq.com/blog/2015/07/understanding-django-middlewares/)
- [What is a context in django](http://stackoverflow.com/questions/20957388/what-is-a-context-in-django)
- [Django tips: Template context processors](http://www.b-list.org/weblog/2006/jun/14/django-tips-template-context-processors/)
