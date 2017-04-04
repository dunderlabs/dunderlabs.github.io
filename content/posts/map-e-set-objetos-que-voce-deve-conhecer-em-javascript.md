title: Map e Set: objetos que você deve conhecer em JavaScript
date: 2017-04-04 02:15
author: Nilton Cesar
slug: map-e-set-objetos-que-voce-deve-conhecer-em-javascript
category: javascript
tags: javascript, es6, map, set, object, array
summary: Map e Set podem parecer tipos totalmente novos, mas eles são velhos conhecidos da linguagem só que com superpoderes.
image: /images/posts/map-e-set-objetos-que-voce-deve-conhecer-em-javascript/post-cover.png
email: niltoncms@gmail.com

![Dentro de um objeto Map]({filename}/images/posts/map-e-set-objetos-que-voce-deve-conhecer-em-javascript/post-cover.png)


Olá, dev amados!!!
Gostaria de abordar aqui alguns objetos desconhecidos pela maioria dos desenvolvedores JavaScript, mas que podem ser bastante úteis.

> Mas porquê usá-los?!

Você não é obrigado a usá-los. Na verdade, os objetos mencionados são parecidos com objetos já conhecidos como `Object` e `Array`, porém de certa forma *melhorados*. Cabe somente a você, desenvolvedor, decidir quando/se será sábio usá-los e onde.

## Map

`Map` é muito semelhante a `Object`: uma coleção de pares chave-valor, sendo possível adicionar novos pares, acessar, modificar e deletá-los. Porém, com duas fundamentais diferenças:

1. qualquer objeto pode ser uma chave
2. um `Map` guarda a ordem dos pares

Ok, talvez a primeira não seja tão interessante pois geralmente as chaves são usadas como referências para os valores, por isso são nomes ou números. Embora seja interessante pensar que é possível guardar, por exemplo, um `Array` como chave para algum outro valor *because reasons*.

Mas a segunda diferença, **pra mim**, é a mais importante (leia-se aplicável, prática): ele guarda a ordem dos pares, ou seja, assim é possível por exemplo realizar um loop num `Map` e confiar que a ordem da iteração será igual ao objeto internamente! O que não acontece com `Object`, onde geralmente você percorreria cada propriedade do próprio objeto e armazenaria num novo `Array`, ou algo do tipo dependendo do que deseja.

A forma de manipulação muda bastante também. Por exemplo, não é possível adicionar ou definir novos pares com a notação `.key = value`/`[key] = value`, e pegar novos valores só chamando `.key`/`[key]`, ao invés disso deve-se usar os métodos `.set` e `.get`

Aqui criamos um objeto `Map` através do construtor `new`, setamos duas propriedades e mostramos o objeto recém-criado:

![Novo Map criado]({filename}/images/posts/map-e-set-objetos-que-voce-deve-conhecer-em-javascript/new-map.png)

Por ter a ordem de inserção preservada, poderíamos percorrê-lo por alguma das estruturas `for`, mas os objeto `Map` já tem o método `forEach`, com funcionamento quase igual aos objetos `Array`: recebe uma função (*callback*) que recebe dois argumentos, o primeiro sendo o valor da propriedade e o segundo o nome da propriedade (ordem inversa ao callback de `Array`s):

![Método de iteração forEach em um objeto Map]({filename}/images/posts/map-e-set-objetos-que-voce-deve-conhecer-em-javascript/new-map.png)

Outras diferençãs legais são o método `has` e a propriedade `size`! Quem já teve que contar quantas propriedades um `Object` tem, sabe como é penoso ter que fazer um loop no objeto, filtrar as propriedades usando `.hasOwnProperty()` e adicionar à um contador, ou usar `Object.keys(obj).length` pra quem usa ES6. Com o `Map` você só tem que acessar a propriedade `size` e TAH-DAH, é retornado o tamanho dele ;)

```javascript
let obj = {
	a: 1,
	b: 2
};

let objSize = 0;

// ES5 approach
for(prop in obj) {
	if(obj.hasOwnProperty(prop))
		objSize++;
};

console.log(objSize);

// ES6 way
console.log(Object.keys(obj).length);

// Getting Map's size
console.log(map.size);
```

### Quando utilizá-los?
Na MDN tem uma [excelente lista](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Map#Objetos_e_mapas_comparados) de como identificar quando utilizar `Map` ao invés de `Object`:
> - As keys são desconhecidas até o tempo de execução, você precisa procurá-las dinamicamente?
> - Todos os valores sempre serão do mesmo tipo, e podem ser usados de forma intercambiável?
> - Você precisa de keys que não são strings?
> - Os pares key-value são adicionados ou removidos frequentemente?
> - Você tem uma quantidade de pares key-value arbitrária (de troca fácil) ?
A coleção é iterada?

[Alguns](https://jsperf.com/map-vs-object-as-hashes/2) [testes](https://jsperf.com/es6-map-vs-object-properties/2) de performance apresentam diferenças entre as diversas formas de percorrer `Map`s e `Object`s. Então, be wise ao usá-los.

## Set

Outro objeto bastante interessante é o `Set`, muito parecido com o nosso velho conhecido `Array`. Se `Map` está para `Object`, `Set` está para `Array` :D

A principal diferença conceitual entre objetos do tipo `Set` e arrays é que `Set` não aceita valores repetidos, ou seja, guarda **somente somente valores únicos**. Isso pode oferecer mais segurança no código.

`Set` tem métodos de manipulação parecidos com `Map`: `add()` para adicionar novos itens, `delete()` para retirar o item (através do item, não do índice), `has()` pra verificar se o item existe, `forEach()` pra percorrê-lo, e [muitos outros](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Set). A propriedade `size` também está presente retornando o tamanho.

É possível também facilmente criar um `Set` a partir de um Array passando ele dentro do construtor com `new`:

![Set sendo criado a partir de um Array]({filename}/images/posts/map-e-set-objetos-que-voce-deve-conhecer-em-javascript/new-set.png)

O interessante desse exemplo é como ele trata os valores repetidos: ele simplesmente pula as repetições e as desconsidera ;)

---

O interessante desses dois tipos de objetos é que eles são como `Object` e `Array` porém ~ tunados ~ permitindo que se faça muita coisa facilmente, sem precisar brigar com a linguagem pra conseguir resolver o seu problema :D

Só fique atento com a compatibilidade! Eles vieram junto com o ES6, e caso você não esteja usando algum polyfill como o [Babel](https://babeljs.io/learn-es2015/#ecmascript-2015-features-map-set-weak-map-weak-set) `babel-polyfill` tem que verificar se os ambientes onde esse código vai rodar os suportam.

Recomendo também conhecer os objetos "irmãos" desses, o `WeakMap` e o `WeakSet`, que são chamados *fracos* porque seus objetos internos podem ser coletados caso o *garbage collector* da *engine* decida que suas referências devem ser removidas. Talvez por isso eles não tenham tanto valor prático se você não estiver construindo uma grande aplicação ou digamos uma biblioteca, ou algo que exija bastante otimização de performance.

Você já conhecia esses objetos? Já o utlizou alguma vez? Se não, acredita que irá usar num próximo projeto? A melhor parte de escrever, além de aprender bastante pra poder explicar, é o feedback e o contato com a comunidade. Adoraria ouvir algo de vocês <3

Brigado pela leitura :*