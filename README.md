<h1 align ="center">Dashbord de Vendas Globais</h1>

## O Problema:
<div align="justify">
Na área de <i>Gestão Comercial</i> há vários tipos de estratégias e práticas que uma empresa pode utilizar para gerir as atividades ligadas à venda. Dentre elas está o acompanhamento do <b>histórico de vendas</b>, que consiste no registro de informações relacionadas às vendas efetuadas em determinado período. No entanto, não se trata apenas de uma mera organização de registros, mas sim uma estratégia comercial que permite, por exemplo, traçar um perfil dos clientes, quais produtos/serviços são mais populares, além de fornecer subsídios para traçar planejamentos futuros.
Dentro dessa ideia, a presente análise pretende estabelecer o panorama de uma empresa fictícia, através de <i>dados sintéticos</i>,  focando-se nas seguintes questões: <b>qual foi o montante total vendido durante o período</b>, <b>quais produtos mais/menos vendidos</b>, <b>o tamanho do mercado consumidor</b> e <b>o perfil de consumo</b>.
</div>
 
 ---------------------------------------------------------------------
 Exemplo  | Valor do exemplo
--------- | ------
Exemplo 1 | R$ 10
Exemplo 2 | R$ 8
Exemplo 3 | R$ 7
Exemplo 4 | R$ 8

 ---------------------------------------------------------------------
## Por que utilizar Python?
<div align="justify">
Para atingir o resultado final desse tipo de análise, um <b>Dashbord</b>, é preciso percorrer todo um caminho que vai desde a <i>extração dos dados</i>, passando por <i>carregamento</i>, <i>tratamento</i>, <i>análise exploratória</i> e <i>visualização dos dados</i>. A <b>linguagem Python</b> permite executar todos esses processos em um único ambiente, aproveitando as suas inúmeras bibliotecas dedicadas a cada uma dessas etapas. Além disso, pensando na integridade dos dados, a manipulação de dados com Python admite a possibilidade de preservar a fonte de dados em sua forma original, prevenindo assim possíveis problemas.
Por fim, caso haja a necessidade de uma análise mais complexa, como uma análise preditiva (o que não está no escopo desse projeto), a linguagem Python também comporta esse tipo de estudo, sendo fundamental nos casos de utilização de <i>Machine Learning</i>.
</div>

---------------------------------------------------------------------
## Método:
<div align="justify">
Em Ciência de Dados, um dos processos mais importantes diz respeito a <i>modelagem de dados</i>. Tal procedimento diz respeito a criação de uma estrutura lógica que represente a forma como os dados serão armazenados, relacionados e usados (<i>Data Science Academy</i>). E uma dessas formas de representação é chamada de <b>Modelagem Dimensional</b>, que se notabiliza por classificar os dados de acordo com os <i>“fatos”</i> e as suas <i>“dimensões”</i>. A(s) tabela(s) “fato” representa(m) as medidas quantitativas, como o número de vendas, enquanto a(s) tabela(s) “dimensão” apresentam o contexto dessas medidas, como a data, local, produto, entre outros.
Embora essa metodologia seja mais comumente utilizada quando a fonte de dados é um conjunto de tabelas, é possível utilizá-la em uma tabela simples. Identifica-se as colunas correspondentes aos fatos e as suas respectivas dimensões, e a partir daí a agregação dos dados é facilitada, além da posterior construção do Dashbord.
</div>

---------------------------------------------------------------------
## Tecnologias utilizadas:
    • Pandas;
    • Streamlit;
    • Plotly
---------------------------------------------------------------------
## Análise dos dados:
<div align="justify">
Nesta análise, foram considerados dados de <b>51.280</b> pedidos com informações como <b>valor total da venda</b>,<b>data do pedido</b>,<b>segmento</b>,<b>país</b>(e sua respectiva região),<b>categoria</b>,<b>subcategoria</b> e <b>prioridade</b>.
A coluna 'segmento' diz respeito a divisão dos tipos de clientes, que são <i>'Home Office'</i>,<i>'Corporativo'</i>, e <i>'Consumidor'</i>. Por sua vez, 'categoria' se refere aos tipos de produtos vendidos pela empresa, que estão catalogados como <i>'Suprimentos'</i>,<i>'Moveis'</i> e <i>'Tecnologia'</i>. Finalmente, 'subcategoria' faz a divisão por produtos em si.

Em relação aos <b>países</b>, os dados demonstram que o mercado consumidor da empresa é bastante vasto, com presença em todos os continentes, exceção feita à Antártida. <b>No total são 147 países</b> distribuídos em cinco continentes, o que representa <b>71%</b> de todos os países disponíveis.
</div>

### Países consumidores
<img src="https://github.com/MoreiraRomulo/Dashbord-de-Vendas-Globais/blob/main/mapa.png" alt="Mercado Consumidor">

