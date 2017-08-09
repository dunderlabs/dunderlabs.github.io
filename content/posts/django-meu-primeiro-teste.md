title: Seu primeiro teste automatizado com Django
date: 2017-08-08 11:32
author: Patrick Mazulo
email: pmazulo@gmail.com
slug: seu-primeiro-teste-automatizado-com-django
category: django
tags: django, django-serie
summary: Agora que nosso projeto já está configurado e funcionando, vamos começar a programar! E que maneira melhor do que já começar programando ao escrever seu primeiro teste automatizado com Django?
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/django_test.svg

![Django test]({filename}/images/posts/django_test.svg)

Créditos da imagem: <https://docs.djangoproject.com/en/1.11/topics/testing/tools>

Posts anteriores da série:

- [Django Boilerplate: A estrutura de projeto Django que tenho usado]({filename}/posts/django-boilerplate-a-estrutura-de-projeto-django-que-tenho-usado.md)
- [Django startproject: Iniciando o seu projeto]({filename}/posts/django-iniciando-seu-projeto.md)
- [Configurando seu projeto Django]({filename}/posts/configurando-o-projeto.md)

Fala pessoal, tudo beleza? Agora que nosso projeto já está configurado e funcionando, vamos começar a programar! E que maneira melhor do que já começar programando ao escrever seu primeiro teste automatizado com Django? Se você for novo em programação web, ou só ainda não tinha se preocupado com isso, pode se perguntar: qual a vantagem de escrever testes?

Essa resposta pode ser tão longa que mereceria só um post pra ela, mas podemos resumir de maneira sucinta com uma única frase: vai te poupar **muito** tempo em testar manualmente as funcionalidades do teu sistema, além de salvar sua vida.

Escrever testes além de uma boa prática de programação (que inclusive está sendo cada vez mais requerida nas vagas para dev Python que tenho visto), é uma questão de segurança. Ao você ter testes que garantem a confiabilidade de uma feature do seu software, você tem mais **flexibilidade** e principalmente **segurança** em evoluir. Adicionar/remover features se tornam tarefas menos dolorosas, porque os seus testes vão garantir que essa alteração vai (ou não) impactar em outras áreas do sistema.

Seguindo essa boa prática, o Django vai nos fornecer uma [suíte de teste](https://docs.djangoproject.com/en/1.11/topics/testing/overview/) simplesmente sensacional! Essa suíte de teste usa a [unittest](https://docs.python.org/3/library/unittest.html#module-unittest), lib default do Python. Mas como ela funciona? Vamos ver como exemplo um trecho retirado da documentação oficial do Django. Digamos que nós temos um model `Animal`, que poderia ser mais ou menos assim:

```python
class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=20)

    def speak(self):
        return 'The {} says "{}"'.format(name, sound)
```

Agora como eu poderia testar esse model. Bom, o teste consistiria em poder garantir que um `Animal` criado com um dado som, ao ser chamado seu método `.speak()`, ele fale com o seu devido som. Vamos testar:

```python
from django.test import TestCase
from .models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
```

O que está acontecendo? Vamos por partes. Eu tenho uma classe `AnimalTestCase`, que vai herdar de [`TestCase`](https://docs.djangoproject.com/en/1.11/topics/testing/tools/#django.test.TestCase), que por sua vez é responsável por realizar testes que façam uso do banco de dados. O primeiro método que temos é o `setUp`, onde serão criados no banco 2 animais: um leão e um gato. Esse será o primeiro método que vai ser rodado antes de cada teste. Após termos nosso `setUp`, vamos ter o primeiro teste.

O método `test_animals_can_speak` vai verificar se os animais que foram criados antes, estão "falando" corretamente. De que maneira é feito isso? Vamos recuperar os 2 que foram criados anteriormente. Tendo-os salvos em variáveis, vamos usar o método [`.assertEqual`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual), que vai verificar se o primeiro argumento passado é igual ao segundo. Vamos olhar essa parte mais de perto:

```python
self.assertEqual(lion.speak(), 'The lion says "roar"')
self.assertEqual(cat.speak(), 'The cat says "meow"')
```

Lembram que o nosso model `Animal` tem um método `.speak()` que vai retornar um texto usando o `name` e `sound` para formatar o texto. Sabendo disso, eu faço a chamada desse método como primeiro argumento, e no segundo usarei o que eu estou esperando que seja a saída correta. Farei isso tanto para o *lion* quando para o *cat*.

Uma vez que você tem o teste escrito, tá na hora de... **testar!** Para isso, o Django vai nos disponibilizar um comando chamado `test`. Simples assim: `python manage.py test`. Ao executar esse comando, o Django vai procurar por qualquer arquivo nomeado `test*.py` dentro do diretório do projeto. Supondo que tivéssemos realmente um projeto Django para esse model `Animal`, e se fôssemos rodar os testes dele, teríamos como execução e output do terminal algo mais ou menos como isso:

```shell
$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).

----------------------------------------------------------------------
Ran 1 tests in 0.017s

OK
Destroying test database for alias 'default'...
```

Como mencionado anteriormente, estaremos fazendo uso do banco de dados para criar instâncias dos nossos models e salvá-los. Mas para isso, não faria o menor sentido usar o banco que você vai estar usando para desenvolvimento. Para isso, o Django vai criar um banco de teste. Depois de criar, agora sim os testes serão executados em ordem. Ao finalizar, o mesmo banco criado será destruído.

Temos já uma noção básica do que são testes, para quê servem, como criar e executá-los. Agora vamos fazer o primeiro teste para a nossa aplicação. Se você acessar `backend/core/` do nosso projeto, vai ver que já existe um arquivo chamado `tests.py` vazio, e será nele que criaremos os nossos testes. Neste momento você deve estar se perguntando:

> _"Beleza, mas o que nós vamos testar? Não temos sequer 1 model!"_

O que é verdade, mas temos algo que já usamos inclusive nos capítulos anteriores dessa série: uma view. Se você acessar o arquivo `backend/core/views.py` vai encontrar o seguinte código:

```python
from django.views import generic


class IndexView(generic.TemplateView):

    template_name = 'core/index.html'

```

Estamos usando [class-based views](https://docs.djangoproject.com/en/1.11/topics/class-based-views/intro/), o que inicialmente pode não fazer muito sentido. Mas calma, ainda vamos abordar com mais carinho essa parte. Por agora, o que a CBV (class-based view) [generic.TemplateView](https://docs.djangoproject.com/en/1.11/ref/class-based-views/base/#templateview) que nada mais faz do que basicamente renderizar um template fornecido. No caso, estamos fornecendo o path de um no atributo `template_name`. Uma coisa importante para sabermos e que veremos na prática, é que os testes consistem também em cobrir todas as camadas básicas da nossa aplicação: models, forms e views. No caso desse teste que faremos agora, vamos para a view.

Sem mais delongas, vamos codar. Dentro daquele arquivo `tests.py` você vai codar o seguinte conteúdo:

```python
from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexViewTest(TestCase):

    def setUp(self):

        self.url = reverse('core:index')

    def test_response_200(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
```

Como fizemos antes, estaremos usando a classe `TestCase` e criaremos uma `IndexViewTest` que herdará da primeira. Essa suite de testes será responsável por cobrir as funcionalidades da nossa view index. No método `setUp` salvarei a URL que estaremos acessando sempre nos testes, e para isso usaremos a função [`reverse`](https://docs.djangoproject.com/en/1.11/ref/urlresolvers/#reverse) que tratará de transformar esse namespace `'core:index'` em uma URL válida. 

Feito isso, criaremos o teste `test_response_200` que irá nos garantir que ao acessar a nossa página inicial, teremos um [status_code 200](https://httpstatusdogs.com/200-ok). Para tal, usaremos o [`self.client`](https://docs.djangoproject.com/en/1.11/topics/testing/tools/#django.test.Client), que nada mais é do que uma instância da classe [`Client`](https://docs.djangoproject.com/en/1.11/_modules/django/test/client/#Client) do Django que vai agir como se fosse um navegador, para que você possa interagir com as suas views, seja com `GET`, `POST` ou qualquer outra ação HTTP. Entendida essa parte, vamos seguir adiante. Iremos salvar o resultado desse GET na variável `response`, e a seguir usaremos novamente o `self.assertEqual` para confirmar que o `response.status_code` é igual a 200.

Pronto, criado nosso teste, vamos... **testar!**

> Obs.: Como estamos usando uma estrutura diferente de projeto, para rodar nossos testes usaremos um comando um pouco diferente do normal.
> Ao invés de usar `python manage.py test`, vamos usar `python manage.py test backend`. Uma vez que o diretório `backend` será o local onde estará nossas apps, nossos testes consequentemente estarão lá também. Ao passar dessa maneira, informamos que o Django tem que procurar os testes ali dentro, e o resto pode deixar que ele se vira. Adicionalmente, passaremos a flag `v` para termos um output um pouco mais verboso, e assim entendermos o que está acontecendo.


```shell
$ python manage.py test backend -v 2
Creating test database for alias 'default' ('test_turbo_send_mail')...
Operations to perform:
  Synchronize unmigrated apps: compressor, messages, sitemaps, staticfiles
  Apply all migrations: admin, auth, contenttypes, sessions, sites
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
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
System check identified no issues (0 silenced).
test_response_200 (core.tests.IndexViewTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.245s

OK
Destroying test database for alias 'default' ('test_turbo_send_mail')...
```

Com essa saída podemos ver o que está acontecendo: O Django está criando o banco de dados para o teste, roda as migrações (como não temos models e, portanto, não geramos migrações, só teremos as do Django) e por fim executa o teste. Estando correto, teremos um `ok` como o que está lá. Agora eu vou fazer uma pequena alteração no código para que ele falhe, apenas para podermos ver qual seria a saída. Então vou mudar o segundo argumento do `self.assertEqual` de 200 para 300, e rodar novamente os testes.

```shell
$ python manage.py test backend -v 2
[mais...]
test_response_200 (core.tests.IndexViewTest) ... FAIL

======================================================================
FAIL: test_response_200 (core.tests.IndexViewTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mazulo/dev/github/dunderlabs/turbo_send_mail_project/backend/core/tests.py", line 14, in test_response_200
    self.assertEqual(response.status_code, 300)
AssertionError: 200 != 300

----------------------------------------------------------------------
Ran 1 test in 0.141s

FAILED (failures=1)
Destroying test database for alias 'default' ('test_turbo_send_mail')...
```

Cada teste que falhar, vai nos trazer um traceback com as informações necessárias para que saibamos qual arquivo, teste e em qual linha ele falhou. Ao lermos, sabemos que no `AssertionError: 200 != 300`. Ou seja, o nosso `response.status_code` é 200, mas estamos comparando com 300. Pronto, feito isso, voltamos o nosso código para 200 e assim funcione bem.

Agora pare um pouco, e vislumbre: você escreveu seu primeiro teste! :D Mas não vamos parar aí, antes de finalizarmos esse post, vamos escrever mais um, e vai ser o seguinte:

```python
def test_template_used(self):
    response = self.client.get(self.url)

    self.assertTemplateUsed(response, 'core/index.html')
```

Adicione mais esse teste no arquivo `tests.py`. O nome do método é bem intuitivo: `test_template_used` será onde iremos verificar se naquele response está sendo renderizado o nosso template fornecido na nossa view. Feito isso, vamos rodar mais uma vez e ver o resultado:

```shell
$ python manage.py test backend     
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.260s

OK
Destroying test database for alias 'default'...
```

Dessa vez retirei a flag de verbosidade, porque uma vez que sabemos aqueles detalhes, podemos nos atentar para um output mais limpo. E como podemos ver, nossos 2 testes passaram com sucesso!

![](https://media.giphy.com/media/yoJC2GnSClbPOkV0eA/giphy.gif)

Agora uma rápida otimizada: para não termos que digitar sempre isso tudo `python manage.py test backend`, podemo colocar isso dentro do nosso arquivo `Makefile` e usar uma chamada menor. Ao final do arquivo, você adicionaria:

```makefile
test:
	python manage.py test backend
```

Após isso, você poderá chamar somente `make test` e terá os testes sendo executados. Pronto? Quase. Lembram que estamos utilizando o git? Fizemos algumas alterações no nosso projeto, então está na hora de commitar! Ao verificar o status do seu repositório local, verá que temos alterações em 2 arquivos:

```shell
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   Makefile
	modified:   backend/core/tests.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Exatamente os dois que modificamos no decorrer do post. Se você quiser saber o que está de diferente, basta executar `git diff`. Com ele, você vai ter um output muito parecido com esse:

```shell
diff --git a/Makefile b/Makefile
index 8e8bcd0..0255049 100644
--- a/Makefile
+++ b/Makefile
@@ -26,3 +26,6 @@ install-dev-requirements:
 
 setup-frontend:
        bower install --allow-root
+
+test:
+       python manage.py test backend
diff --git a/backend/core/tests.py b/backend/core/tests.py
index e69de29..5ae4aae 100644
--- a/backend/core/tests.py
+++ b/backend/core/tests.py
@@ -0,0 +1,19 @@
+from django.test import TestCase
+from django.core.urlresolvers import reverse
+
+
+class IndexViewTest(TestCase):
+
+    def setUp(self):
+
+        self.url = reverse('core:index')
+
+    def test_response_200(self):
+        response = self.client.get(self.url)
+
+        self.assertEqual(response.status_code, 200)
+
+    def test_template_used(self):
+        response = self.client.get(self.url)
+
+        self.assertTemplateUsed(response, 'core/index.html')
```

Nele você vai saber quais arquivos foram alterados, e quais as alterações. O `+` indica que houveram adições de conteúdo no arquivo, e o `-` a remoção. No nosso caso, só vamos ter adição. Feito isso, vamos adicionar essa mudança e commitar. Mas, faremos por partes. Uma coisa muito importante quando se trata de versionamento de código e commits, é ter tudo muito bem organizado. Um commit é como se fosse um _checkpoint_ do seu código. Você vai estar incorporando de fato uma alteração no seu repositório, e dando a ela um significado (mensagem do commit). Vimos um pouco disso no post passado.

Beleza, vamos começar adicionando o nosso `tests.py`:

```shell
$ git add backend/core/tests.py 
```
Depois disso, `git commit` que vai nos levar para aquela tela para que possamos escrever a mensagem do commit:
```shell

Add IndexViewTest
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#       modified:   backend/core/tests.py
#
# Changes not staged for commit:
#       modified:   Makefile
#
```

O mesmo para o `Makefile`.

```shell
$ git add Makefile 
```

e por fim `git commit` novamente:

```shell
Add test command to makefile
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#       modified:   Makefile
#
```

E pra fechar com chave de ouro, vamos enviar nossas alterações para o GitHub:

```shell
$ git push github master
Counting objects: 8, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 972 bytes | 0 bytes/s, done.
Total 8 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 3 local objects.
To github.com:dunderlabs/turbo_send_mail.git
   de47897..7ebcfa5  master -> master
```

Agora sim, podemos dormir em paz :) Ainda há **muita coisa** dentro desse tema chamado testes, mas vamos vendo aos poucos e com calma. Dessa maneira, conforme nossa aplicação for crescendo, vamos nos acostumando cada vez mais. Por hoje, vamos ficar por aqui. No próximo post vamos começar a dar uma olhada no models do Django. Então fica ligado :D

Dúvidas e/ou críticas, só visitar os comentários mais abaixo. Valeu pessoal, e até a próxima!
