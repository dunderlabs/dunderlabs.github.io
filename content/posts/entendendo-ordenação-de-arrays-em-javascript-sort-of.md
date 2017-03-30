title: Entendendo ordenação de arrays em JavaScript, sort of.
date: 2017-03-10 15:15
author: Nilton Cesar
slug: entendendo-ordenacao-de-arrays-em-javascript-sort-of
category: javascript
tags: javascript, array, sort, number, ordering
summary: Ordenar valores em JavaScript pode parecer estranho mas é uma funcionalidade bastante poderosa.
image: /images/posts/entendendo-ordenacao-de-arrays-em-javascript-sort-of/post-cover.png
email: niltoncms@gmail.com

E aí, meus queridos devs, tudo ok com vocês? :D
Depois de uma conversinha com [Patrick Mazulo](https://twitter.com/ericleribertson) sobre JavaScript, ele me veio com o seguinte cenário na ordenação de valores de um array:

```javascript
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].sort()
```

Parece bem simples e direto, porém o resultado é:

> 1, 10, 2, 3, 4, 5, 6, 7, 8, 9

![WHAT](http://i.giphy.com/EsmlrgWNx5v0Y.gif 'ÉOQ')

Eu tive exatamente a mesma reação na primeira vez que  vi isso.


Na verdade, o que acontece ali é que o método `.sort()` ordena em ordem crescente através do caracteres da tabela Unicode quando convertidos para string. Então nesse caso, "10" vem antes do "2" porque "1", que é o primeiro caractere de "10", vem antes do "2".

De acordo com a implementação da [tabela Unicode](http://unicode.org/charts/), [é possível perceber, pelo menos no nosso subset](http://unicode.org/charts/PDF/U0000.pdf), que a ordem é: alguns símbolos, números, letras maiúsculas, letras minúsculas, mais alguns outros símbolos. O que quer dizer que deverão também obedecer a essa ordem, ou seja, "a" antes do "b", "ab" depois do "a" e antes de "b", "a0" entre "a" e "ab", "Ab" antes de "a", e por aí vai.


## "mas como eu ordeno números pelo valor"?

Mas voltando ao nosso problema inicial, o objetivo era ordenar os números pelo seu valor, não pelo ~código Unicode, certo?

Bom, pra isso o JavaScript aceita um parâmetro opcional no método `sort`: uma função que determina como seriam as regras da ordenação. Essa função recebe dois argumentos, por convenção chamados de **a** e **b**, que representam dois itens do array que estão sendo comparados.

![hm](https://media.giphy.com/media/sBl8Fowq0ErFC/giphy.gif)

A vantagem disso é que, na função, você tem controle de qual critério da ordenação utilizar, de acordo com algumas regras.

Funciona assim: são comparados `a` e `b`, e caso:

- a comparação seja menor que zero, `a` é posicionado antes de `b`

- a comparação seja maior que zero, `a` é posicionado depois de `b`

- a comparação seja igual a zero, `a` e `b` permancem com as posições inalteradas


"Bom, mas como comparar? Não entendi como essas regras se aplicam"


### explicação curta (pois deadline chegando)

O que você pode fazer é diminuir os dois valores entre si, e o resultado vai decidir se `a` ou `b` avança, recua, ou ambos permanecem nas posições atuais.

```javascript
var arr = [5, 3, 1, 4, 2];

console.log('Array original:', arr);

arr.sort(function(a, b) {
    return a - b;
});

console.log('Array ordenado:', arr);
```

O código acima define um array, o ordena, e o mostra modificado. A parte-chave desse código é o `a - b` que faz o array ser ordenado de forma **crescente**. O contrário, `b - a` o ordena de forma **decrescente**.

![wow](http://i.giphy.com/vLq5FWMjfN47S.gif)


### aprofundando a explicação (para nerds)

O que acontece é que o `sort()` pega o array original, compara dois valores e os **muda de posição de acordo com essa comparação**, logo em seguida ele pega novamente dois valores e os compara pra **rearranjá-los de novo**, e faz isso até que todo o array esteja ordenado.

Pegando o primeiro exemplo, onde usamos `a - b`, a ordenação acontece da seguinte forma: se o primeiro elemento comparado, no caso `a`, for maior que `b`, a subtração `a - b` resulta em um valor maior que zero, então `a` é posicionado depois de `b` (de acordo com as regras). Essa mesma lógica aplicada repetidamente no array, que está sendo modificado, faz que com que os valores maiores sejam posicionados mais ao fim do array, ou seja, faz a ordenação em ordem crescente!

A mesma lógica se aplica para ordenação decrescente, `b - a`, só que agora com os valores trocados de lugar faz com que a ordenação seja ao contrário da anterior :). Se você ficou confuso ou quer ver isso passo-a-passo, você pode visualizar os valores de `a` e `b` mudando:

```javascript
arr.sort(function(a, b) {
    console.log(a, b, a - b)
    return a - b;
});
```

![mindblowing](https://media.tenor.co/images/c7eac59fb909510e714e85de277ca81a/raw)

Não encontrei na [especificação](http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf), mas você pode observar que a lógica por trás disso é semelhante a alguns algoritmos de ordenação conhecidos, como o BubbleSort. [Aparentemente, cada engine implementa esse algoritmo de uma maneira](https://blog.rodneyrehm.de/archives/14-sorting-were-doing-it-wrong.html)


## Indo um pouco além

Já que `a` e `b` são, de fato, elementos do array, é possível acessá-los e expandir um pouco as possiblidades do uso do método `sort`.

Digamos que você tenha um array de objetos com o nome de um álbum e o ano de lançamento em cada um:

```javascript
var beatlesTopFour = [
    {
        album: 'Abbey Road',
        releaseYear: 1969
    },
    {
        album: 'Revolver',
        releaseYear: 1966
    },
    {
        album: 'The Beatles (White Album)',
        releaseYear: 1968
    },
    {
        album: 'Rubber Soul',
        releaseYear: 1965
    }
];
```

Pra ordenar esses objetos de acordo com o ano de lançamento, você pode comparar a propriedade `releaseYear` de cada objeto, sem ter que manipular mais nada :)

```javascript
beatlesTopFour.sort(function(a, b) {
    return a.releaseYear - b.releaseYear;
});
```

e TCHARAM: ordenados em ordem crescente pelo ano

![awesome](https://media.giphy.com/media/aLdiZJmmx4OVW/giphy.gif)


**Pro-tip**: fique atento com a utilização do método `sort` pois ele altera o array original. Se você está aplicando uma abordagem funcional, pode não ser interessante utilizá-lo em escopos mais externos.

Espero que esse artigo tenha sido útil, e não deixem de olhar o que tem na [MDN](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/sort), por exemplo, caso algo não tenha ficado claro. OU é só gritar aqui embaixo que a gente responde ;)

Sempre disponível praquele feedback maroto de vocês. Até logo!