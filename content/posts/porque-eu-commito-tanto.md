title: Porque eu "commito" tanto
date: 2016-06-27 18:12
author: Patrick Mazulo
email: pmazulo@gmail.com
slug: porque-eu-commito-tanto
category: git
tags: git, good practices, translations
summary: Existem alguns flows no uso do git. Aqui você vai encontrar um que segue uma abordagem quase atômica, que pode resolver grandes problemas.
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/criando_ambiente_django.png

![Créditos da imagem]({filename}/images/posts/in-case-of-fire-1-git-commit-2-git-push-3-leave-building2.png)

Créditos da imagem: <https://hikaruzone.wordpress.com/2015/10/06/in-case-of-fire-1-git-commit-2-git-push-3-leave-building/>

## Porque eu faço muitos git commit
Recentemente me juntei a um novo projeto, e um dos meus colegas de equipe me perguntou: "Porque você 'commita' tanto?". Eu decidi escrever este post para explicar meus motivos para ele e para qualquer outra pessoa que possa se deparar com meu trabalho no futuro.

### Commits pequenos podem ser seu melhor amigo.
Assim como funções, commits pequenos focam em uma coisa: uma simples mudança. Isso força nossa mensagem do commit ser mais descritiva (desculpa caras, "fixed some stuff" não está sendo nada descritivo).
Vamos dar uma olhada neste exemplo:

````shell
git commit -am "Updated 'Contact us' to 'Need Help? Contact Us!'"
````

Neste caso, você pode simplesmente olhar as mudanças feitas no commit, mas porque olhar no código quando a descrição está ali na sua frente? Commits pequenos tornam extremamente fácil encontrar uma mudança específica que entrou, especialmente quando tiver uma lista delas para analisar. Também tornam simples de ver como o projeto foi construído, pedaço por pedaço.

#### 1. Simplificam a revisão do código.
Commits pequenos tornam revisões de código muito mais fáceis. Permitem que você revise as mudanças, umas de cada vez, e compartilhe da mentalidade do autor. Os commits contam uma história, como se o autor estivesse explicando as mudanças para uma pessoa.

#### 2. Ajudam você a compartilhar conhecimento.
Recentemente, eu aprendi que adicionar uma quebra de linha depois da declaração de um `return` em JavaScript é a mesma coisa que não retornar nada (se você ficou curioso, veja [esta resposta no Stack Overflow](http://stackoverflow.com/a/8528606) para a explicação). Eu removi a quebra de linha e comitei o resultado:

````shell
git commit -am "A return followed by a line break doesn't actually return anything"
````

Graças aos pequeno commits, fui capaz de compartilhar esse conhecimento com meus colegas de equipe, sabendo que estaria salvo para sempre. Se há uma coisa que eu aprendi como um programador, é que há uma razão para tudo. Algumas vezes, o raciocínio não está claro e o comentário do código não faz sentido (pode imaginar cada `return` de funções JavaScript tendo um comentário dizendo "Quebra de linha não vão retornar esse dado"). Pequenos commits ajudam a preencher esta lacuna.

#### 3. Podem ajudar a consertar seus erros.
Nenhum desenvolvedor é perfeito. Algumas vezes, nós vamos pelo caminho errado e percebemos que algo que tentamos apenas não funciona. Talvez tentamos pôr em negrito algum texto ao adicionaar uma classe CSS e ajustando algumas propriedades, mas os resultados não parecem bons. E agora?

Poderíamos manualmente desfazer a mudança, mas é fácil esquecer de algo (por exemplo, você pode remove a classe CSS do elemento HTML, mas esquecer de remover a definição no arquivo CSS). `git revert` é uma maneira extremamente fácil de desfazer uma mudança sem ter que lembrar do estado inicial.

De modo semelhante, cada um de nós já escreveu um bug, e também consertou um bug enquanto introduzia mais três. Normalmente, somos capazes de encontrar a raiz do problema através do uso de breakpoints e reanalisar a problemática da lógica. No entanto, existem vezes onde essa problemática simplesmente não pode ser descoberta, não importa quais passos de debug você faça.

`git bisect` está aqui para salvar o dia! Ele primeiro pede para que você forneça um "bom" commit (um que não tenha o bug em questão), e um "mau" commit (normalmente, é o último commit). Ele então executa uma busca binária, testando vários commits como "bom" ou "mau".

É extremamente importante que cada commit esteja "compilável" e todos os testes passem. Por outro lado, será impossível verificar se um commit é "bom" ou "mau". No caso em que um commit quebrado se infiltrar (vindo de um colega da equipe, claro, porque nós somos bons rapazes e moças), `git bisect skip` pode ser usado para saltar sobre ele (apenas cruze seus dedos para que este commit não seja a causa do bug). No fim, `git bisect skip` retornará o commit que introduziu o bug. O pedaço problemático de código deve estar completamente obvio, e uma correção para ele já deve estar sendo preparada.

#### 4. Me protegem nas apresentações.
Se eu ganhasse um centavo por cada vez que tive um 'brancão' sobre as coisas que fiz no trabalho no dia anterior durante uma apresentação, estaria milionário. Uma vez tentei fazer uma lista das coisas que eu fiz durante o dia, mas era tedioso — e redundante, já que meus pequenos commits compartilhavam da mesma informação. E claro, ninguém quer ser aquele cara que tem uma longa lista das coisas que ele trabalhou, mas ir folheando pelo histórico de commits é uma boa maneira de refrescar a memória.

#### 5. Me permitem selecionar as mudanças.
Considere este cenário: enquanto trabalha numa tarefa separada, Joe Bob adicionou algumas novas strings aos arquivos de tradução que acabou de receber. Ele também começou a incorporar essas traduções nas views dele, mas ele continua tendo testes falhando. Susan iniciou a tarefa dela e percebeu que precisa algumas dessas strings. Não faria sentido fazer um merge da branch do Joe Bob com a dela, sendo que ele ainda está trabalhando nesta branch. Susan poderia apenas redefinir essas traduções, mas ela tem medo do temido merge conflict. Sendo que Joe Bob usa pequenos commits, Susan pode selecionar o commit que Joe Bob introduziu as traduções ao executar o comando:

````shell
git cherry-pick some-hash
````

#### Resumindo.
Não tem problema em ir pelo caminho errado, e em seguida, reverter as alterações. Ninguém se importa com pequenos erros estúpidos — na verdade isso mostra que você se importa em melhorar o projeto e, por fim, você mesmo. Se você está contribuindo para um projeto open source, normalmente é melhor ter um commit por feature ou correção. Para ter o melhor dos dois mundos, você pode [dar um squash de todos os seus pequenos commits em um só](http://makandracards.com/makandra/527-squash-several-git-commits-into-a-single-commit) antes de você publicar suas mudanças. E para qualquer um que estiver curioso, eu já estive em projetos com bem mais de 20000 commits, e nunca tive problemas de lentidão com git.

**_E você, commita muito?_**


Dúvidas e/ou críticas, só visitar os comentários mais abaixo. Valeu pessoal, e até a próxima!

Referências:

- [Post original](http://spin.atomicobject.com/2015/11/11/all-the-commits/)
