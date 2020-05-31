title: Inserindo informações em PDFs editáveis com Python
date: 2020-05-31 10:56
author: Patrick Mazulo
slug: inserindo-informacoes-em-pdfs-editaveis
category: python
tags: python, pdf
summary: É muito comum no mercado o uso de arquivos editáveis para gerar relatórios, como arquivos .xls. Mas e PDF? Precisei fazer isso no trabalho e quero mostrar como consegui.
email: pmazulo@gmail.com
about_author: My name is Patrick and I'm a web developer who fell in love with Python
image: /images/posts/python-pdf.jpg

![Python + PDF]({filename}/images/posts/python-pdf.jpg)

Créditos da imagem: <https://pdftables.com/blog/pdf-to-excel-with-python>

Fala pessoal, tudo beleza? Quase 3 anos depois, estou de volta ao blog. E dessa vez, para ficar!

![I am back](https://media.giphy.com/media/yj5UdA4elp8Wc/giphy.gif)

Há algum tempo que eu estava pensando em algum assunto interessante para voltar a escrever aqui. Algo pequeno porém conciso. Daí, em um dia normal do trabalho, passei muita dor de cabeça pra resolver um problema. Era um projeto que um colega me propôs onde iríamos melhorar um processo para os nossos usários internos. Atualmente, pra finalizar esse processo, nossos usuários faziam o seguinte:
- Baixavam um template de PDF
- Buscavam no sistema as informações necessárias para preenchê-lo
- Preenchiam manualmente
- Exportavam o template como um novo PDF (para que fosse read-only)
- Checavam novamente se todas as informações estava corretas

Acho que já deu pra visualizar onde o gargalo e consumo de tempo estão, né? Pois é. Para resolver isso, a proposta seria: inserir essas informações no template de PDF automáticamente com os dados que já tínhamos no banco de dados... Na primeira vez que ele me falou isso, minha reação imediata foi:

![Como???](https://media.giphy.com/media/QjIz1AqkGTszK/giphy.gif)

É bem comum manipulações com certos tipos de arquivo, como `.csv` ou mesmo arquivos `.xlsx`. Apesar de eu saber que não é impossível fazer o mesmo com PDF, pelo pouco que eu sabia do arquivo, seria bem trabalhoso (spoiler: nem foi tanto assim). Certo, se é isso que precisamos fazer, vamos nessa. Comecei a pesquisar sobre maneiras de manipular arquivos PDF. Uma amiga do trabalho também me enviou dois links ([PDF for Python](https://medium.com/@umerfarooq_26378/python-for-pdf-ef0fac2808b0) e [PDF processing with Python](https://towardsdatascience.com/pdf-preprocessing-with-python-19829752af9f)) que ajudaram bastante. Neles temos listados algumas libs Python já existentes para lidar com esse tipo de arquivo. Tem algumas que parece ser bem famosas nesse quesito. Uma entre elas me chamou atenção. E essa foi a [`pdfrw`](https://github.com/pmaupin/pdfrw), por ter o seguinte na descrição: _The **fastest** pure Python PDF parser available_. A [PyPDF2](https://github.com/mstamy2/PyPDF2) também carrega essa alcunha no título, com exceção do *fastest*. Não fiz nenhum teste de benchmarch (ainda), então preferi acreditar na audácia do autor em colocar isso :P

Biblioteca escolhida, vem a segunda parte: como fazer para preencher um template de PDF com as informações que nós queremos? Bom, de volta a sala de pesquisa. Adentrando um pouco mais o Google, consegui encontrar um post de alguém que ensinava como fazer **exatamente** o que eu precisava: [_How to Populate Fillable PDF's with Python_](https://bostata.com/how-to-populate-fillable-pdfs-with-python/). Achei uma abordagem muito simples, além de ter me lembrado de algo que eu já não fazia há algum tempo: salvar e compartilhar um aprendizado (o autor do post antes de chegar nessa solução, também pesquisou bastante e se baseou em outros posts). Beleza, vamos colocar os dedos no código!

Mas antes de qualquer código, precisamos preparar nosso template de PDF. Assim como no post mencionado anteriormente, vamos pegar um do [Square](https://squareup.com/us/en/invoices/invoice-templates), onde podemos baixar um PDf de [cobrança gratuitamente](https://d1g145x70srn7h.cloudfront.net/invoices/templates/red/invoice-template-en-us.pdf?color=red&format=pdf). Primeiro, vamos abrir esse arquivo para ver o que temos. Estou usando KDE, então estou utilizando o Okular para arquivos PDF. Ao abrir o arquivo, essa é a imagem que tenho: ![PDF aberto usando Okular](https://i.imgur.com/d2icDUe.png).

Você vai notar que tem um botão _Show Forms_ e ao clicar nele caixas escuras vão aparecer no PDF onde existem campos preenchíveis (você pode checar [aqui](https://i.imgur.com/1vdbroU.png)). Cada campo desse pode ter um valor inserido. É realmente como se fosse um formulário. Certo, agora o próximo passo é editar o _nome_ de cada um desses campos pra algo mais próximo do nome de uma variável, afinal seria um pouco estranho ficar referenciando `Business Name` ao invés de `business_name` (vamos ver como isso vai ajudar mais na frente). Para isso, vamos precisar de algum programa para editar esse form, e infelizmente o Okular não tem essa funcionalidade. Pesquisando um pouco encontrei algumas opções e para fins de praticidade acabei ficando com o [Master PDF Editor Free](https://aur.archlinux.org/packages/masterpdfeditor-free/). É a versão free de um software pago. Também encontrei uma ferramenta web que nos traz a mesma funcionalidade, [PDF Escape](https://www.pdfescape.com/). Só fica um pouco escondida (você tem que dar [_unlock_](https://i.imgur.com/mTcFDRy.png) no field, depois [_Object Properties_](https://i.imgur.com/8LAUe1o.png) que vai abrir um [_modal_](https://i.imgur.com/NsxzsfE.png) onde você vai poder mudar o `Name` do field). Finalizando toda a troca dos nomes por um snake-case, teremos o seguinte:

![PDF com nomes em snake-case](https://i.imgur.com/dnzC6hm.png)


Agora vamos pegar cada um desses nomes e salvar em um dicionário sendo as chaves e criar alguns valores fictícios. Aqui vou deixar ele assim:

```python
data_dict = {
   'business_email_address': 'contato@dunderlabs.com',
   'business_name_1': 'Dunderlabs',
   'business_name_2': 'Dunderlabs',
   'business_phone_number': '(34) 2222-2222',
   'customer_email': 'mazulo@dunderlabs.com',
   'customer_name': 'Patrick Mazulo',
   'due_date': '30/05/2020',
   'invoice_number': '5786878',
   'item_1_amount': 'R$8000',
   'item_1_price': 'R$200/hr',
   'item_1_quantity': '40 hours',
   'item_1': 'Criação de blog',
   'note_contents': 'Muito obrigado por realizar essa compra!',
   'send_date': '29/05/2020',
   'subtotal': 'R$8000',
   'total': 'R$8000',
}
```

Um arquivo de PDF internamente parece ter algumas peculiaridades interessantes em relação a como é construído e interpretado. Vale a pena dar uma lida maior sobre o tipo de arquivo se bater uma curiosidade maior (a especificação do arquivo tem mais de 1000 páginas!). Agora, vamos começar a brincar com o PDF usando pdfrw. Primeiramente, precisamos instalar a lib usando nosso clássico `pip install pdfrw`. Agora vou abrir um terminal do ipython para que possamos ver o que temos:

```ipython
In [1]: from pdfrw import PdfReader                                                    

In [2]: import os                                                                      

In [3]: from pathlib import Path                                                       

In [4]: path = 'Documents/Dunderlabs/Posts/pdf_template.pdf'                           

In [5]: pdf = PdfReader(os.path.join(Path.home(), path))                               

In [6]: pdf.keys()                                                                     
Out[6]: ['/Root', '/Info', '/ID', '/Size']

In [7]: pdf.Info                                                                       
Out[7]: 
{'/CreationDate': '(D:20160817230153Z)',
 '/Creator': '(Word)',
 '/Keywords': '()',
 '/ModDate': "(D:20160902175952-07'00')",
 '/Producer': '(Adobe Mac PDF Plug-in)',
 '/Title': '(Microsoft Word - [For PDF] Invoice Template - Purple.dotx)'}

In [8]: len(pdf.pages)                                                                 
Out[8]: 1
```

Como podemos ver, o `PdfReader` lê o arquivo PDF e entrega pra gente um objeto de fácil interação. Pelo que pudemos ver, essa instância também tem métodos que você normalmente encontra em um dicionário, como `.keys()`. Se você der um `dir(pdf)` vai conseguir ver todos os métodos que esse objeto nos dá, entre eles `.values()`, `.update()` (métodos de `dict`) além de métodos da específicos da classe `PdfReader`. Se você der um print em `pdf.Root` ele irá mostrar todo o conteúdo do PDF parseado na estrutura `key:value` que a lib cria. O código que vamos usar para escrever as nossas informações no template, vai percorrer a estrutura da página do template (no nosso caso, só temos 1 página) usando essas "notações" para chegar nos campos editáveis. Para concluir nosso objetivo, vamos ter o seguinte código:

```python
import os
from pathlib import Path

import pdfrw


TEMPLATE_PATH = 'Documents/Dunderlabs/Posts/pdf_template.pdf'
OUTPUT_PATH = 'Documents/Dunderlabs/Posts/invoice.pdf'

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_pdf(input_pdf, output_pdf, data_dict):
    template_pdf = pdfrw.PdfReader(os.path.join(Path.home(), input_pdf))  # [1]

    annotations = template_pdf.pages[0][ANNOT_KEY]  # [2]

    for annotation in annotations:  # [3]
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:  # [4]
                key = annotation[ANNOT_FIELD_KEY][1:-1] # [5]
                if key in data_dict.keys():  # [6]
                    update = {
                        'V': data_dict[key],  # [7]
                    }
                    annotation.update(pdfrw.PdfDict(**update))  # [8]
        annotation.update(pdfrw.PdfDict(Ff=1))  # [9]

    template_pdf.Root.AcroForm.update(  # [10]
        pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true'))
    )
    pdfrw.PdfWriter().write(os.path.join(Path.home(), output_pdf), template_pdf)  # [11]
```

Agora vamos comentar as partes mais importantes:

- `[1]` nós estamos lendo o nosso template usando o `PdfReader`, assim como mostrei já antes.
- `[2]` como nosso arquivo possui apenas uma página, podemos usar `.pages[0][ANNOT_KEY]` para pegar as _annotations_ do arquivo diretamente. Caso você tenha mais de 1 página, isso ficará dentro de um outro loop.
- `[3]` vamos agora percorrer todas as _annotations_ que pegamos na página.
- `[4]` verificamos se essa annotation possui algo dentro da chave `'/T'`. É lá onde teremos os nosso campos editáveis.
- `[5]` aqui nós vamos usar slice para pegar a key de `annotation[ANNOT_FIELD_KEY][1:-1]` da maneira como salvamos no nosso dicionário. Lembra da imagem que as keys dos campos editáveis são salvas da seguinte maneira: `[business_name]`? Com o slice `[1:-1]` só será retornado o texto dentro dos `[]`.
- `[6]` vamos nos assegurar que a key que pegamos está dentro do nosso dicionário de dados. Isso vai ser necessário no nosso caso porque por questões de praticidade, não editei todos os fields do template, somente aqueles que salvei em `data_dict`.
- `[7]` atualizamos o valor da chave `V` com o que temos no nosso `data_dict`. Isso sobrescreverá o valor vazio que está no template com o nosso valor.
- `[8]` atualizo o dict da annotation com o dict `update` contendo os novos valores.
- `[9]` ao final de cada loop, essa linha vai servir para fazer com que esse campo do form não seja mais editável quando você abri-lo. Agradecimentos a resposta nessa [issue](https://github.com/pmaupin/pdfrw/issues/186#issuecomment-585020314)
- `[10]` isso vai fazer com que quando salvarmos o arquivo, o PDF abra e não apareça mais como sendo um template sem valores nos seus campos. Sem isso, ao abrir o PDF depois de salvo, ainda mostrava os fields e só mostrava os valores ao clicar. Nessa [issue](https://github.com/pmaupin/pdfrw/issues/84#issuecomment-463493521) encontrei isso como solução.
- `[11]` ao final de tudo, uso o `PdfWriter` para escrever o template modificado em um novo PDF.

Agora temos por completo o código que vai preencher o formulário em um PDF. As aplicações disso são várias, como por exemplo: uma view Django que gera um PDF preenchido com as informações que estejam no banco de dados. Isso vai diminuir a possibilidade de erro humano, além de acelerar um processo que pode ser facilmente feito pelo sistema. Agora nossos usuários podem focar em somente checar as informações (o que é muito mais rápido) e seguir com o processo.

O código completo você pode encontrar aqui nesse [gist](https://gist.github.com/mazulo/30b8778166897e2722d5ec4bd81f9f2e)

Notas finais:

- Caso você não queira passar por toda aquela dor de cabeça em achar um jeito de editar os nomes dos campos, fiz esse [script](https://gist.github.com/mazulo/1ffa79d611d096771dd602ef680a9ac7) que vai mostrar pra você o nome deles. Com isso, você pode ir testando eles e usá-los como keys no seu dicionário de dados.
- Tive alguns problemas na edição usando _Master PDF Editr_ e _PDF Escape_ online. O script não estava conseguindo atualizar os dados em alguns dos campos. Então caso queira testar esse código com um template que funcione por completo, estou deixando nesse [link](https://bostata.com/download/post/fillable_pdf/invoice_template.pdf) o PDF que o autor do post usou como exemplo. Esse foi editado usando o Adobe Acrobat PDF. Infelizmente não temos opções muito poderosas assim para linux (não que eu conheça, ainda estou pesquisando para futuramente atualizar o post mas caso você conheça, deixa lá nos comentários :)
- Apesar de ser consideravelmente simples usar [pdfrw](https://github.com/pmaupin/pdfrw), a lib não tem atualizações desde 2018 e a última interação do criador em PRs foi em junho de 2019. As outras libs listadas naqueles 2 artigos também não estão em um estado muito diferente :/

Dúvidas e/ou críticas, só visitar os comentários mais abaixo. Valeu pessoal, e até a próxima!
