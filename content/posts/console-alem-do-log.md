title: console dos browsers além do .log
date: 2017-03-18 19:52
author: Nilton Cesar
slug: console-alem-do-log
category: javascript
tags: javascript, console, browser, log, debug
summary: Entenda alguns dos métodos do objeto console
image: /images/posts/console-alem-do-log/post-cover.png
email: niltoncms@gmail.com

![Console e seus métodos]({filename}/images/posts/console-alem-do-log/post-cover.png)

E aí, meus queridos devs, tudo joia com vocês? ;D

Vou falar de uma das ferramentas mais poderosas pra quem trabalha com JavaScript e no entanto pouco utilizada: o `console`. A [especificação](https://console.spec.whatwg.org) ainda não é consistente entre os maiores browsers do mercado. Todos os exemplos aqui foram testados no Chrome 57.

Bem, calma. `console` na verdade é um objeto JavaScript que tem uma série de métodos, incluindo o mais famoso (e acho que mais usado), `.log`. Quem nunca usou um `console.log('enter the function')` ou até `console.log('dados recebidos:', data)` pra verificar o que ia acontecendo no código? É bastante útil durante o desenvolvimento porque te dá um feedback rápido do que tá acontecendo direto ali, sem precisar de muito esforço pra entender o que tá acontecendo. Disclaimer: _não estou dizendo dizendo que isso deve substituir suas rotinas de testes, ou deixar de debugar quando necessário, ou até mesmo deixar de lado seu TDD ou BDD_. **Nada disso**.


## Mostrando informações

Bom, quem nunca precisou mostrar aqueles dados que pegou via AJAX, ou marcar onde aparece aquele erro? Há formas mais eficientes de mostrar essas informações:

### `console.log()`

Clássico. Mostra as informações da forma que elas vêm.

![Clássico console.log]({filename}/images/posts/console-alem-do-log/log.png)

### `console.warn()`

Mostra as informações como uma mensagem de alerta, destacando as chamadas de função.

![Mensagem de alerta]({filename}/images/posts/console-alem-do-log/warn.png)

### `console.error()`

Mostra como uma mensagem de erro,  destacando as chamadas de função.

![Mensagem de erro]({filename}/images/posts/console-alem-do-log/error.png)

### `console.info()`

Mostra as informações de uma maneira com um ícone descritivo de informação, útil para identificar que tipo de mensagem é essa.

![Mensagem de informação]({filename}/images/posts/console-alem-do-log/info.png)

### `console.table()`

Esse é muito útil para visualização de dados (arrays e propriedades enumeráveis de objetos) pois os mostra em formato tabular.

![Todos os dados tabulados]({filename}/images/posts/console-alem-do-log/table-all-columns.png)

Ainda é posível filtrar as colunas pelo nome!

![Dados tabulados filtrados]({filename}/images/posts/console-alem-do-log/table-filter-column.png)

Nota: os "erros" aqui **não** param a execução do código.

## Contando o tempo de execução

Legal também é medir quanto tempo leva pra executar um trecho de código, colocando ele entre `.time()` e `.timeEnd()`. É interessante também passar como argumento um rótulo para aquele contador, pra poder identificá-los quando houver múltiplos contadores.

!['Tempo de execução da função']({filename}/images/posts/console-alem-do-log/time.png)

## Verificando as execuções

Usando [como exemplo um comentário do post anterior](entendendo-ordenacao-de-arrays-em-javascript-sort-of.html#comment-3200924458) muito bem indicado pelo [Hector Cardoso](https://disqus.com/by/disqus_Bu8QAZBLDU/)

```javascript
function sortByReleaseYear(objOriginal) {
    let objTmp = Object.assign([], objOriginal);

    objTmp.sort((a, b) => a.releaseYear - b.releaseYear);

    return objTmp;
};
```

![Execução das funções]({filename}/images/posts/console-alem-do-log/trace.png)

essa função retorna um array ordenado pelo ano de lançamento dos álbuns.
É possível verificar o _stack trace_, ou seja, a "pilha" de execuções até a função que está sendo chamada. Colocando antes do `return` o método `console.trace()`, e executando  `sortByReleaseYear(beatlesTopFour)`, é possível ver toda a execução que houve até aquele ponto onde o `.trace()` está sendo chamado.

## Juntando tudo

Juntando muito do que vimos até aqui podemos analisar a execução do nosso código com muita riqueza de detalhes:

```javascript
console.info('original array', beatlesTopFour);
console.info('ordered array');
console.time('sort by release year');
console.table(sortByReleaseYear(beatlesTopFour));
console.timeEnd('sort by release year');
```

![Alguns métodos aplicados]({filename}/images/posts/console-alem-do-log/all-together.png)

***

Ainda tem muito a ser explorado, como o `.dir()` que é útil para visualizar hierarquicamente grandes quantidades de dados (como na capa do post), trabalhar com grupos através dos métodos `group`, `groupCollapsed` e `groupEnd`, fazer marcações em Timeline, inicar um Profiler... muita coisa legal na [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Console) pra gente brincar ;D

Queria deixar duas referências sensacionais, ambas do [Fernando Daciuk](https://twitter.com/fdaciuk): uma é sobre [como debugar JavaScript no browser](http://blog.da2k.com.br/2015/01/10/debugar-javascript-no-browser) e a outra é sobre [como usar o `.time()` para medir suas instruções](http://blog.da2k.com.br/2015/01/08/javascript-medindo-o-tempo-de-suas-instrucoes/) que falei aqui :)

**Atenção**: esses métodos devem ser usados para fornecer feedback ao desenvolvedor, ou seja, se você estiver construindo uma API é interessante em alguns casos você o use. Caso o seu código vá pra produção e não interesse ao usuário essas mensagens, você deve removê-los do código. Recomendo utilizar o ESLint, que entre outras regras de avaliação do seu código, já tem uma [regra específica](http://eslint.org/docs/rules/no-console) que retira todas as chamadas de `console` ;)

Se faltou alguma coisa e vocês quiserem adicionar mais informações, ou deixar dúvidas, ou trocar alguma ideia sobre isso, o comentário é livre. Sinta-se à vontade, e vamos trocar uma ideia :DD