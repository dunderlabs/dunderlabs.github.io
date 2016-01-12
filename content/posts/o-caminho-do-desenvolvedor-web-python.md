title: O caminho do desenvolvedor web Python
date: 2015-03-17 14:13
author: Patrick Mazulo
category: web
tags: python, web, web development
slug: o-caminho-do-desenvolvedor-web-python
email: pmazulo@gmail.com
about_author: My name is Patrick and I'm a web developer who fell in love with Python

![Créditos da imagem]({filename}/images/posts/dev_way2.png)

Créditos da imagem: http://brianmcdonnell.github.io/pycon_ie_2013/#/

Do começo do ano passado para cá, acabei ficando bem ativo no
grupo Python Brasil do Facebook, sempre compartilhando coisas legais que
eu encontrava pela internet, e/ou respondendo perguntas que eu poderia
ajudar. Nesse meio tempo, uma das perguntas mais recorrentes que eu
tenho visto tem sido esta: **O que eu devo fazer/estudar para
desenvolver para web com Python?**

Numa das últimas vezes que eu vi uma dessas, eu acabei comentando (com
textão hahaha) a minha opinião acerca deste assunto, sobre qual seria
uma boa via para seguir. Mas pelo fato de, como falei anteriormente,
esta pergunta ser recorrente ~~e porque o comentário ficou enorme,~~ e o
Facebook ter um fluxo alto de threads fazendo com que perguntas fiquem
lá atrás rapidamente, eu resolvi transformar em um post.

Aqui eu colocarei minha opinião, claro. E como tal é passível de
críticas. Logicamente que você pode não concordar com alguma parte, ou
por completo, ou quem sabe achar tudo bacana e querer testar. Mas, os
comentários estão ali pra isso :p deixe sua opinião sobre como foi pra
você caminhar por este percurso, ou o que achou das dicas ;)

Sem mais delongas, vamos lá!

Em algumas muitas vezes, esta pergunta sobre ser um desenvolvedor web
Python sempre vem acompanhada com alguma outra, como web e jogos, ou web
e desktop. Sobre isso, eu tenho o seguinte a falar:

Primeiramente, eu lhe dou a dica de ver suas prioridades e objetivos.
Por exemplo, qual seu objetivo para aprender games com Python? Diversão?
Realmente se especializar e tentar fazer dele algo rentável e trabalhar
realmente neste ramo? Cada uma dessas áreas, jogos, web, destops e etc
requerem uma GRANDE quantidade de tempo, esforço e dedicação. Mas nada
lhe impede de estudá-las em simultâneo, porém, lhe dou a seguinte dica:
veja qual sua prioridade. Quer trabalhar e ganhar dinheiro com web? Pois
foque a maior parte do tempo em estudar isso, e uma pequena parcela do
tempo estudando jogos, para diversão. E assim vice-versa.

Mas, levando em consideração o intuito de ser desenvolvedor web Python,
vamos falar agora sobre isso.

Antes de tudo, tenha certeza de realmente conhecer Python, e não só
saber as coisas superficiais: "while, for, funções, objetos e etc". Mas
sim saber como cada uma dessas coisas funcionam. O que é uma função?
Como ela funciona? E objetos? O que acontece em um for? O que são
realmente classes? E metaclass?  
Para isso, você pode contar com uma série de livros que podem lhe
ajudar. Entre eles tem o [Dive into Python
3](http://www.diveintopython3.net/), (disponíve online), onde você vai
aprender muita coisa bacana sobre Python. Conheço muitos bons devs
Python que começaram lendo esse livro. Temos também o [Python 3
Cookbook](http://shop.oreilly.com/product/0636920027072.do) (compra
online), onde você vai poder aprofundar tudo que aprendeu no livro
anterior. Aqui no blog também temos materiais sobre Python, incluindo
uma série que estamos traduzindo que falam sobre o funcionamento de
algumas coisas da linguagem. [Dá uma conferida lá
também](http://indacode.com/pythonista-intermediario/). Além desses,
existem diversos outros livros e materiais que você pode usar, como o
curso [Python para Zombies](http://pycursos.com/python-para-zumbis/),
ministrado pelo professor Fernando Massanori (eu fiz esse curso, e achei
super bacana!). Existem ótimos blogs que contam com ótimos materiais,
como o [Python Club](http://pythonclub.com.br/) e o [Programe em
Python](http://programeempython.blog.br/), dentre vários outros (sério,
são muitos).

Claro que você não precisa ser um Guido Van Hossum, o modaFuckingFoda em
Python. Mas ter real conhecimento sobre a linguagem vai lhe ajudar
muito. Esse é o diferencial de um bom programador para um cara que só
programa. Beleza, mas para que vai servir isso?

Mas sempre vem a(s) pergunta(s): Mas pra que estudar Python antes? Eu
não posso já começar a estudar o framework e aprender durante esse
estudo? Sim, pode. porém tendo esse conhecimento prévio da linguagem,
vai ficar muito mais fácil entender o funcionamento dos frameworks web.
Falo isso por experiência própria. Se parar pra pensar, os frameworks
com os quais você vai trabalhar são feitos em que linguagem? Python.
Então, como você vai poder usar todo o potencial do framework se não
souber bem a linguagem em que ele foi feita? É como querer construir um
carro sem conhecer as ferramentas necessárias para tal. Pode até
funcionar, mas o nível de código macarrônico/gambiarra pode ser muito
grande.

Finalizando essa parte do Python, eu aconselho que você estude também
sobre conceitos web. O que é HTTP? E HTTPS? o que é uma request? E
response? O que é um server e client? Como eles interagem? Saber dessas
coisas é mais do que essencial, porque afinal você vai estar lidando com
web, né?

![Créditos da imagem]({filename}/images/dev_way3.jpg)
Créditos da imagem: http://pt.slideshare.net/ricobl/python-e-django-na-globocom

Bom, agora chega a hora de escolher qual framework. E essa é a parte
complicada da história, causa de infinitas flamewars na comunidade.
Existem diversos frameworks web Python, mas alguns acabam se destacando
entre os outros. Entre eles podemos citar: Django, Web2Py, Flask e
Bottle. Cada um tendo suas particularidades, prós e contras. Vamos falar
um pouco sobre alguns.

1.  [Flask](http://flask.pocoo.org/docs/0.10/): é um leve framework web
    criado pelo austríaco [Armin
    Ronacher](https://github.com/mitsuhiko "Perfil GitHub"), baseado no
    kit WSGI e Jinja2 na engine de templates. Flask é bem simples de
    iniciar, uma vez que em um único arquivo você pode criar um "Hello
    World" (que em outros frameworks poderiam levar mais código). Não
    mostrarei exemplos de código aqui, mas você pode ver estes 2
    tutoriais que mostram exemplos práticos de criação de webapps com
    Flask
    ([aqui](https://stormpath.com/blog/build-a-flask-app-in-30-minutes/)
    e
    [aqui](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/),
    e neste [link](http://mitsuhiko.pocoo.org/flask-pycon-2011.pdf) você
    pode ler um slide do criador sobre o porque de ter criado Flask).
2.  [Django](https://docs.djangoproject.com): nasceu no outono de 2003,
    quando 2 programadores (Adrian Holovaty e Simon Willison) web do
    jornal Lawrence Journal-World começaram a usar Python para construir
    aplicações web. Ele foi lançado publicamente em 2005. Em junho de
    2008 foi formada a DSF (Django Software Foundation), que seria
    responsável por manter o Django dali em diante. Ele é amplamente
    usado no desenvolvimento web, e muito conhecido por suas "baterias
    inclusas", que são funcionalidades comuns no desenvolvimento web (
    authentication, URL routing, a sistema de template, um ORM e etc).
    Possui uma ótima documentação e comunidade, tanto quanto materiais
    de aprendizado. Dentre eles destaco o curso do Allisson de Azevedo,
    [Django para iniciantes](https://www.youtube.com/playlist?list=PLfkVgm8720kzm6fmTekjtKyFcppyD4Ubd),
    e o livro online [Tango with Django](www.tangowithdjango.com/book17/), bem como a própria
    documentação do framework.
3.  [Web2Py](http://www.web2py.com/init/default/documentation): criado
    por uma comunidade de profissionais e professores do curso de
    Ciência da Computação na DePaul University, em Chicago, tendo como
    desenvolvedor lider Massimo DiPierro. Web2py foi originalmente
    projetado como uma ferramenta de ensino, com ênfase no fácil uso
    e desenvolvimento. Seu design foi inspirado no Ruby on Rails (e no
    Django), que é focado no rápido desenvolvimento e permite o design
    MVC (model-view-controller). Ele é menos verboso e sua sintaxe muito
    clara, o que torna a construção de webapps muito fácil; e também vem
    com algumas baterias inclusas, para algumas funcionalidades.
    [Aqui](https://www.youtube.com/watch?v=6h73Tkco4pY) você vai
    encontrar um vídeo do Bruno Rocha falando sobre o desenvolvimento
    com web2py. E
    [aqui](http://pycursos.com/desenvolvimento-agil-para-web-com-web2py/)
    você vai encontrar um curso (pago) pela PyCursos, da incrível
    Júlia Rizza. Super recomendo!

Agora eu irei focar em um deles, que no caso será o que eu estou
atualmente estudando.

O 1ª framework que usei e tive contato foi o Django. Para aprender
Django, como falei antes e mostrei 1/3 da ponta do iceberg nos links,
nós temos **MUITOS** materiais sobre Django. Diversos livros e vídeo
aulas podem ser encontrados. No youtube você vai encontrar MUITAS aulas
sobre Django. Em pt-br tem alguns hangouts dos episódios do Mutirão
Python que falam sobre desenvolvimento web com Django; e você encontrará
muitos bons cursos em inglês (como
[este](https://www.youtube.com/playlist?list=PLEsfXFp6DpzT5veidCTZ1mQriBX0Mu2LF) e
[este](https://www.youtube.com/playlist?list=PLEsfXFp6DpzRgedo9IzmcpXYoSeDg29Tx)).

Sobre livros eu recomendo:

-   Pro Django (inglês). Estou lendo ele atualmente, e é realmente muito
    bom! Ele inicia explicando conceitos do funcionamento da
    linguagem Python. Conceitos esses que são usados dentro
    do framework. Após assistir as aulas do Allisson, você poderia
    partir para esse livro aqui. E ao finalizar este, poderia passar
    para este outro chamado;
-   Lightweight Django (inglês), que cobre a versão mais nova, 1.7.
    Porém esse é um pouco mais avançado.
-   [Tango with Django](www.tangowithdjango.com/book17/) (inglês bem
    simples): um livro online onde você estuda Django construindo
    uma aplicação.

Em acompanhamento aos estudos, crie um projeto e vá implementando de
acordo com o conhecimento que vai adquirindo. Pode ser qualquer coisa,
um sistema de cadastro de usuários, agenda de contatos, QUALQUER coisa.
Mas o importante é praticar todo santo dia. Ao finalizar essa timeline,
creio que você já estará em ótimas condições de conhecimento sobre web.
E a partir daí, já vai saber lidar com futuros desafios que encontrar
pela frente.

Bom, após tudo isso cabe a você agora testar cada dica e ver com qual
framework você se identificou mais. Lembre-se que esse caminho não é
curto, na verdade podemos dizer que ele nunca acaba, porque você sempre
vai estar estudando sobre alguma coisa relacionada a web. Então dê-se o
tempo necessário até que você pegue no gancho, e comece e realmente
sentir as coisas fluindo. Pode ser bem complicado no começo, mas posso
lhe dizer que com o tempo só tende a melhorar :) Bons estudos!
