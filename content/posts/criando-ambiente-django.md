title: Criando seu ambiente isolado para desenvolvimento web com Django
date: 2016-01-25 23:29
author: Patrick Mazulo
email: pmazulo@gmail.com
slug: criando-seu-ambiente-para-desenvolvimento-web-com-django
category: django
tags: python, django, django environment, web development
summary: Está decidido, você vai estudar desenvolvimento web com Django. Mas como ter um ambiente preparado para começar? Quais ferramentas podem me ajudar nisso? Vamos responder essas e outras perguntas
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/criando_ambiente_django.png

![Créditos da imagem]({filename}/images/posts/criando_ambiente_django.png)

Créditos da imagem: <https://www.howtoforge.com/tutorial/how-to-install-django-1-9-on-ubuntu-15-04/>

O começo de qualquer nova atividade é sempre meio complicada. Você se vê perdido no meio de tantas possibilidades e maneiras diferentes de se fazer a mesma coisa. Se você não tiver um mínimo de mentoria, como alguém mais experiente que lhe mostre alguns macetes iniciais, ou que indique o tão famoso "caminho das pedras", essa nova estrada vai estar cheia de obstáculos que você ainda não conhece. Dentre os vários tipos de pessoas no mundo, existem aquelas que documentam essas experiências, para servir de guia para quem estará passando por ele também. E é isso que este post será. Simbora?

Que Python é uma maravilha e que deveria estar na lista das maravilhas deste mundo, todo mundo já sabe. E com ele foi criado um dos mais conhecidos frameworks web: Django. Mas qual a dessa história toda de ambiente de desenvolvimento? Para ilustrar melhor, vamos imaginar o seguinte cenário:

Digamos que você foi contratado para desenvolver um sistema web, e para ele você vai utilizar uma determinada versão do Django. Então você vai lá na sua máquina e instala:

````shell
$ pip install django==1.6
````

> Obs.: Ao não especificar a versão que será instalada, o pip irá instalar a versão mais recente e estável.

Porém nesse sistema você terá que utilizar algumas libs externas. Simples, só instalar usando o pip:

````shell
$ pip install gunicorn<=18.0 lxml<=3.2.4

````

> Obs.: Se você estiver utilizando o [zsh](http://www.zsh.org/) como seu shell padrão, terá que envolver cada uma das declarações de pacote com aspas simples, ficando assim: 
	
	$ pip install 'gunicorn<=18.0' 'lxml<=3.2.4'

Pronto, você acaba de instalar no seu SO esses 3 pacotes, e já pode começar a desenvolver. Mas agora digamos que você também vai trabalhar em outro projeto paralelo. E agora se vê diante de um problema ao olhar as versões que terá que usar:

````
django # 1.9
gunicorn # 19.4.5
lxml # 3.5
````

E agora, o que fazer? Vou ter que desinstalar as versões anteriores para instalar essas específicas deste novo projeto? E quando eu for para outro, terei que fazer isso novamente?

A resposta é: Sim, caso você não use a abordagem de trabalhar com ambientes virtuais isolados.

Ambiente virtual isolado é auto-explicativo. Você terá um ambiente isolado do seu sistema, onde nele você poderá ter todas as dependências instaladas para o seu projeto. Uma vez criado e instalado os pacotes, você pode iniciar seu projeto. Vai começar outro projeto com outras dependências? Beleza, só criar outro ambiente e ser feliz!

Mas como começar a usar essa abordagem? Aqui que a parada começa a ficar interessante ;-)

Lhes apresento o [virtualenv](https://virtualenv.readthedocs.org/en/latest/) e [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html)!
São duas ferramentas maravilhosas que vão possibilitar essa nova maneira de trabalhar. Mas o que é um ou outro? Vamo lá.

`virtualenv` é uma ferramenta para criar para criar ambientes Python isolados. Para instalar é super simples:

````shell
$ [sudo] pip install virtualenv

````

A instalação dele é feita globalmente, então dependendo do seu SO talvez seja necessário usar o `sudo` neste comando. Ao finalizar, já podemos criar nossa primeira env:

````shell
$ virtualenv minha_env
New python executable in /home/mazulo/dev/python/minha_env/bin/python
Installing setuptools, pip, wheel...done.
````

> Obs.: Ao executar dessa maneira, a env criada usará como python padrão o mesmo Python que é padrão no seu SO. No caso do Ubuntu, até a versão 14.04 (a que eu uso), o Python 2.7.6 é o padrão. Sendo assim o python do `minha_env` será o python 2.7.6. Caso você queira usar uma versão diferente, basta usar o parâmetro `-p` (ou `--python`) e indicar qual versão utilizar. Caso eu use a versão 3.x, ficaria dessa maneira:

````shell
$ virtualenv minha_env -p python3 
````

Isso criará no seu diretório atual uma pasta chamada `minha_env`. Dentro deste diretório teremos:

- **minha\_env/lib/** e **minha\_env/include/**, contendo arquivos da biblioteca de suporte para um virtualenv python. Pacotes de terceiros (instalados via pip, por exemplo) instalados neste ambiente ficarão em **minha\_env/lib/pythonX.X/site-packages/**.

- **minha_env/bin/** é onde os executáveis ficam, como o próprio python, por exemplo. Sendo assim, executar um arquivo com `#! /caminho/para/minha_env/bin/python` usará a versão do Python desta virtualenv.

- Os pacotes principais, `pip` e `setuptools` já estão instalados. Dessa maneira, você pode instalar novos pacotes dentro da própria env.

env criada, agora vamos ativá-la:

````shell
$ source minha_env/bin/activate
````

Esse comando ativará sua env. Um indicativo disso será o nome da sua env aparecer entre () antes do nome do seu usuário no seu bash.

````shell
(minha_env)user@machine:~$
````

Eu uso [zsh](http://www.zsh.org/) com o tema fox, e ao ativar a env ele fica da seguinte maneira:

````shell
$ (minha_env) ┌[mazulo☮cabuloso]-(~/dev/python)
└> # sim, o nome do meu PC é cabuloso hahaha
````

> Obs.: Daqui em diante, os exemplos do terminal serão um ctrl+c ctrl+v do meu terminal, que usa o tema citado acima.

A partir deste momento, você está totalmente isolado do seu sistema, e pode começar a instalar todas as dependências do seu projeto sem medo de ser feliz. 

Porém...

Como você percebeu, o `virtualenv` cria uma pasta no seu diretório atual, o que pode se tornar uma chatice, principalmente se você utilizar versionamento de código. 

- "Ah, mas é só colocar essa pasta no .gitignore"

Verdade, mas seria bem melhor não ter que fazer isso, né? Bom, uma maneira seria centralizar todas suas envs dentro de uma pasta, chamada `virtualenvs`, por exemplo. Ela ficaria na sua home (ou onde você achar melhor). Daí sempre na hora de criar uma nova env, você navegaria até este diretório, criaria sua env, ativaria ela e depois iria para o seu diretório de trabalho... Eita, meus dedos até cansaram de digitar todo esse percurso :-P

Com o tempo isso pode se tornar extremamente fatigante. Mas não perca as esperanças, pois está na hora do [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html) entrar em ação!

virtualenvwrapper é um conjunto de extensões para o virtualenv. Essas extensões incluem wrappers para criação e exclusão de ambientes virtuais, além de gerenciar seu workflow de desenvolvimento, tornando fácil trabalhar em mais de um projeto.

Suas features:

- Organizar todos os seus ambientes virtuais em um só lugar(!!!!)
- Wrappers para gerenciar seus ambientes (criar, deletar, copiar e etc)
- Usar um simples comando para trocar entre ambientes(!!!!!!!!!!!!!!)
- Autocomplete com tab para comandos que recebem um ambiente virtual como argumento
- Gatilhos configuráveis pelo usuário para todas as operações

dentre algumas outras.

Conseguem ver a maravilha que isso é?! Acho simplesmente sensacional! E para poder usufruir de tudo isso, vamos para o passo a passo.

Da mesma maneira que o `virtualenv`, a instalação do `virtualenvwrapper` será feita globalmente.

````shell
$ [sudo] pip install virtualenvwrapper
````

Agora nós vamos adicionar 3 linhas no arquivo de inicialização do seu shell 

- _.bashrc_ ou _.profile_ para o bash padrão
- _.zshrc_ para zsh shell

````
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
````

A primeira linha configura a localização de onde seus ambientes virtuais vão ficar. Na segunda teremos a localização dos seus diretórios de projetos em desenvolvimento (pode apagar essa, se quiser), e na terceira a localização do script instalado com esse pacote. Depois disso você terá que recarregar a inicialização deste arquivo

````shell
$ source ~/.zshrc # ou .bashrc, ou o arquivo que o seu shell usa
````

Pronto, agora você pode criar/ativar suas envs da maneira mais simples possível :)
Exemplo executado na minha máquina:

````shell
[mazulo☮cabuloso]-(~/dev/python)
└> mkvirtualenv nova_env -p /usr/bin/python3.4 
Running virtualenv with interpreter /usr/bin/python3.4
Using base prefix '/usr'
New python executable in /home/mazulo/.virtualenvs/nova_env/bin/python3.4
Also creating executable in /home/mazulo/.virtualenvs/nova_env/bin/python
Installing setuptools, pip, wheel...done.
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/nova_env/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/nova_env/bin/postdeactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/nova_env/bin/preactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/nova_env/bin/postactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/nova_env/bin/get_env_details
(nova_env) ┌[mazulo☮cabuloso]-(~/dev/python)
└> 
````

Estou criando uma outra env, chamada **nova_env**, agora utilizando o wrapper do `virtualenvwrapper` chamado `mkvirtualenv`. Ele vai criar essa env dentro do diretório que nós configuramos naquela 1ª das 3 linhas que adicionamos no arquivo de configuração do shell, e após isso já ativa ela pra nós!

Agora digamos que eu vá trabalhar em outro projeto. Vou criar a env para ele:

````shell
(nova_env) ┌[mazulo☮cabuloso]-(~/dev/python)
└> mkvirtualenv django_project -p /usr/bin/python3.4 
Running virtualenv with interpreter /usr/bin/python3.4
Using base prefix '/usr'
New python executable in /home/mazulo/.virtualenvs/django_project/bin/python3.4
Also creating executable in /home/mazulo/.virtualenvs/django_project/bin/python
Installing setuptools, pip, wheel...done.
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/django_project/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/django_project/bin/postdeactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/django_project/bin/preactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/django_project/bin/postactivate
virtualenvwrapper.user_scripts creating /home/mazulo/.virtualenvs/django_project/bin/get_env_details
(django_project) ┌[mazulo☮cabuloso]-(~/dev/python)
└> 
````

Perceba que eu ainda estava com a **nova\_env** ativada ao criar a env **django_project**. Mas sem problemas, o `virtualenvwrapper` cria a env, desativa a anterior e ativa a nova pra mim :)

E caso eu queira trocar de ambiente para voltar a trabalhar na nova_env? Simples:

````shell
(django_project) ┌[mazulo☮cabuloso]-(~/dev/python)
└> workon nova_env 
(nova_env)┌[mazulo☮cabuloso]-(~/dev/python)
└> 
````

Vou utilizar o `workon` para trocar de maneira rápida e fácil de ambiente. O bacana é que ele permite você usar autocomplete com o tab para a env que deseja ativar. Sem trocar de diretório para isso. Sensacional, diz aí!

Bom, basicamente era isso que eu gostaria de mostrar sobre o [virtualenv](https://virtualenv.readthedocs.org/en/latest/) e [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html), e como configurar um ambiente para começar a trabalhar com django.

- "Ah, mas você nem falou como instalar o django"

Super fácil, ora pois:

````shell
(django_project) ┌[mazulo☮cabuloso]-(~/dev/python)
└> pip install django
Collecting django
  Downloading Django-1.9.1-py2.py3-none-any.whl (6.6MB)
    100% |████████████████████████████████| 6.6MB 181kB/s 
Installing collected packages: django
Successfully installed django-1.9.1
````

Pronto, django instalado de maneira isolada no seu ambiente. Agora só começar a codar!


Dúvidas e/ou críticas, só visitar os comentários mais abaixo. Valeu pessoal, e até a próxima!

Referências:

- [Virtualenv](https://virtualenv.readthedocs.org/en/latest/index.html)
- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
