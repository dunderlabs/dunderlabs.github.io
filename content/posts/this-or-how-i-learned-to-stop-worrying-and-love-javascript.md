title: this or: How I Learned to Stop Worrying and Love JavaScript
date: 2017-03-03 15:00
author: Nilton Cesar
slug: this-or-how-i-learned-to-stop-worrying-and-love-javascript
category: javascript
tags: javascript, lexical scope, dynamic scope, arrow function
summary: JavaScript é uma linguagem legal, flexível e apaixonante, porém tem seus cantos obscuros que faz muita gente penar pra entender. Um desses cantos é o valor this dentro das funções.
email: niltoncms@gmail.com

Vou tentar fazer uma rápida porém merecida explicação sobre o uso do `this` na execução de funções, tópico que tira a paciência de muita gente que tá começando na linguagem ou vem ~viciado de libs e frameworks.
Os exemplos aqui são executados no browser, mas podem ser executados no Node sem problema algum, mudando só o objeto `window` para `global`.


## O que é _isto_?

Bom, você deve tentar adivinhar pela tradução que `this` se refere a "isto". Não está totalmente errado, o ponto chave é o que é o "isto". Tente executar o `this` no console, só ele e nada mais, e você vai receber o objeto `window`. Esses são os objetos que, nos seus ambientes, guardam as referências pros outros objetos, funções, classes, etc, definidos pelo desenvolvedor. Ou seja, quando você define e atribui `var a = 7` fora de escopo de funções ou fora de objetos, na verdade é criada uma referência para essa variável em `window`, significando que dá pra acessar essa mesma variável tanto fazendo `a` como `window.a`.
Ok, mas e se eu definir uma função assim
```javascript
function outerScope() {
    console.log(this)
};
```
quando eu chamá-la eu vou rebecer a própria função? (??) Não.

Quando você chama `outerScope()` na verdade é a mesma coisa de estar chamando `window.outerScope()` e o `this` vai mostrar `window`. O que acontece é que o `this` se refere justamente ao contexto de invocação, ou seja, como e onde ela é *chamada*. No exemplo, quem está chamando a função `outerScope` implicitamente é o objeto `window`.


## `this` em métodos

Ainda no mesmo ambiente, suponha que você agora defina um objeto `o` assim:
```javascript
var o = {
    m: outerScope
};
```
A chave `m` tem como valor a função definida anteriormente, o que faz com que `m` seja um método do objeto `o`. Pra executar, basta `o.m()`.

TCHARAN! O que foi mostrado foi o próprio objeto `o`, porque agora ele é quem executa essa função que agora foi atribuída a ele.

Percebe como nesse caso, mesmo a função sendo definida fora do objeto, quando é atribuída e trazida pra dentro do objeto,e a partir daí não tem mais relação com o que acontece externamente com a função, o `this` muda? ;)

O mesmo comportamento acontece se tratando de eventos:
```javascript
var el = document.querySelector('#submit-form');

el.addEventListener(
    'click',
    function() { console.log(this); }
)
```
No código acima, atribuímos um elemento HTML à variável `el`, e depois definimos que o evento de click executa uma função que loga o `this`. Nesse caso, também o `this` se refere ao próprio elemento que disparou o evento, no caso `el`.
Até agora imagino que tá tudo de boa, eu acho.


## `function`s criam escopo, e não preservam o `this` do contexto

Voltemos ao exemplo do objeto, mas vamos criar mais um método:
```javascript
var o = {
    m: outerScope,

    n: function() {
        console.log(this);

        function inside() {
            console.log(this);
        };
        
        inside();
    }
};
```
Aqui, adicionamos mais um método à `o`, `n`, que loga o `this` duas vezes: uma diretamente no método e outra dentro de uma função que está _dentro_ desse método. Se você executar `o.n()`, sua reação pode ser das mais variadas: "whatta fuck" "Q" "BÉ ISSO, MAH" e por aí vai.

O primeiro `this` se refere ao objeto `o`, como anteriormente, porém sendo chamado dentro da função `inside` ele mostra `window`! Isso acontece porque, ao criar uma nova função com `function`, o `this` (e até `arguments`) não é trazido do contexto da função mais externa para o função interna, e então ele se refere ao próprio `window`.

![mindblowing](https://media.giphy.com/media/OK27wINdQS5YQ/giphy.gif "mindblowing")

Mas então, como diabos eu acessaria o `this` da função externa? Quando eu tiver definindo uma função construtora e seus metódos, como é que eu ia referenciar o `this`, que é o objeto criado?


### 1/2: arrow function

Se você é descolado(a) e quer usar as novas features da linguagem e dizer que tá por dentro, pode usar as queridinhas arrow functions. Mais do que uma forma curta de escrever funções anônimas (`() => console.log(this)`), as arrow functions fazem o contexto permanecer o mesmo para o `this`, ficando o código assim
```javascript
var o = {
    m: outerScope,

    n: function() {
        console.log(this);

        // Tenho que autoexecutá-la já que é uma função anônima
        (() => {
            console.log(this);
        })();
    }
};
```
e mostrando duas vezes o objeto `o`. Simples e elegante.


## 2/2: "that" pra quem te quer

Se você não quer usar arrow function, ou melhor, quando NÃO HAVIA ISSO NA LINGUAGEM, o que era feito era atribuir o valor de `this` a outra variável no escopo acima, geralmente com o nome "that" ou "self" e aí sim através dela estaria disponível no escopo mais interno. Ficaria assim:
```javascript
var o = {
    m: outerScope,

    n: function() {
        console.log(this);
    
        // TAH-DAH ;)
        var that = this;
        function inside() {
            console.log(that);
        };
        
        inside();
    }
};
```


## Conclusão

Acho que consegui cobrir os principais casos do `this` na invocação de funções. Se faltou alguma coisa (e faltou), comenta aí embaixo pra gente trocar uma ideia sobre :D
Pra um texto bem mais aprofundado e completo, recomendo demais a leitura do EXCELENTE [You Don't Know JS: _this_ & Object Prototypes](https://github.com/getify/You-Dont-Know-JS/tree/master/this%20%26%20object%20prototypes), especialmente os capitulos 1 e 2 tratam desse tema.

Durante muito tempo eu *só* usei jQuery nas minhas páginas, pelos motivos óbvios: mais rapidez no desenvolvimento, segurança ao fazer uma página que vai funcionar na maior quantidade de navegadores possível, biblioteca que faz de tudo um pouco, etc. E longe de mim condenar a lib, eu acho que o que merece atenção é a *atitude* dos desenvolvedores que a utilizam sem conhecer a linguagem em si, porque você acaba ficando viciado nela sem realmente entender como a liguagem funciona e não  sabe o que fazer quando você não tem ela à mão. Recomendo botar a mão na massa.