# MINISTÉRIO DA EDUCAÇÃO^

# SECRETARIA DE EDUCAÇÃO PROFISSIONAL E TECNOLÓGICA^

# INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DE SANTA CATARINA^

### CAMPUS FLORIANÓPOLIS – DEPARTAMENTO ACADÊMICO DE ELETROTÉCNICA

# _____________________________________________________________________

Curso de Especialização em Computação Científica Aplicada à Indústria
Unidade Curricular: Introdução à Inteligência Artificial Conexionista Semestre: 2016/
Professor: Cesar Alberto Penz
Professor: Marco Aurélio Moreira Saran

```
TRABALHO
MLP e Confiabilidade
```
1. Descrição do processo sob análise: Smart position sensor system
Considerando o esquema apresentado na figura 1, a ideia geral é estimar a posição y do anteparo através das tensões
de saída – v 1 e v 2 – de dois módulos fotovoltáicos. O deslocamento do anteparo na direção y causará diferentes
áreas de sombra nos módulos fotovoltáicos, o que afetará as tensões de saída.

```
Figura 1 - Smart position sensor system
```
```
O comportamento esperado para as tensões v 1 e v 2 é semelhante ao apresentado na figura 2.
```
```
Figura 2 – Tensões de saída das células versus posição do anteparo
```
```
Para a definição, treinamento e teste de redes neurais artificiais que possam representar a função y = f(v 1 ,v 2 ) será
gerada experimentalmente uma base de dados.
```

2. Atividades a serem desenvolvidas no trabalho
    a. Definição de parâmetro de desempenho desejado e, a partir da base de dados fornecida, definição de
       um conjunto de treinamento e um conjunto de teste.
          i. Apresentar de maneira gráfica os conjuntos de treinamento e teste.
ii. Definir as características de desempenho desejadas para a ferramenta a ser desenvolvida.
    b. Treinamento de, no mínimo, 5 redes neurais do tipo feed-forward backpropagation com diferentes
       topologias (quantidade de camadas, neurônios por camada, funções de ativação) utilizando todos os
       padrões do conjunto de treinamento. Importante: explorar a flexibilidade que existe na definição da
       topologia.
          i. Apresentar: topologias; histórico do erro durante o treinamento; histórico do gradiente
             durante o treinamento; comparação gráfica das saídas das redes com os valores esperados;
             análise do desempenho das redes.

```
ii. Escolher uma das topologias para uso; justificar a escolha.
```
```
iii. Utilizar a rede neural escolhida com todos os padrões do conjunto de teste; apresentar os
resultados de forma gráfica (saída esperada versus saída da rede), evidenciar os erros para
os dados de teste.
```
```
iv. Apresentar e identificar os parâmetros da rede escolhida (pesos, funções de ativação); fazer
uma representação gráfica da rede.
```
```
c. Para a topologia escolhida no item b deve ser realizado um estudo com foco na confiabilidade da rede
neural.
i. Treinar, no mínimo, 5 redes neurais a partir de subconjuntos de dados, escolhidos
aleatoriamente, do conjunto de treinamento. A quantidade de dados escolhidos deve ser de
8 0% do total de padrões; utilizar as redes neurais com todos os padrões da base de dados de
teste; apresentar os resultados de forma gráfica (saída esperada versus saída da rede),
evidenciar os erros para os dados de teste. Analisar o desempenho das redes neurais com
foco na representatividade dos dados escolhidos aleatoriamente.
```
```
ii. Treinar 3 redes neurais com conjuntos de treinamento escolhidos manualmente de modo a
evidenciar a importância da representatividade dos dados na descrição do processo. A
quantidade de dados escolhidos para os conjuntos de treinamento deve ser de 80% do total
de padrões da base de dados de treinamento. Analisar o desempenho das redes neurais com
foco na representatividade dos dados escolhidos.
```
```
iii. Criar um comitê com 15 redes neurais treinadas a partir de subconjuntos de dados,
escolhidos aleatoriamente, compostos por 8 0% dos padrões da base de dados de
treinamento. Analisar o desempenho do comitê frente ao desempenho das redes neurais
individuais utilizando todos os padrões da base de dados de teste.
```
3. Observações finais e encaminhamento do trabalho.
    a. Deverá ser gerado um relatório organizado com as atividades executadas (gráficos, tabelas,
       esquemas contribuem para a clareza do documento). Enviar por email em formato PDF.

```
b. O arquivo base do Scilab para desenvolvimento do trabalho disponibilizado no SIGAA. Todos os
arquivos do Scilab, gerados durante a execução trabalho, deverão ser encaminhados por email.
O arquivo contento a base de dados será disponibilizado.
```
```
c. Arquivos, no formato txt, contento os pesos da rede neural referente ao item b (iv) devem ser
encaminhados por email, sendo um arquivo para cada camada da rede. Considere a organização dos
pesos nos arquivos conforme a apresentação da variável W no scilab.
```
```
d. Avaliação do trabalho compreenderá todos os itens apresentados neste documento.
```
## e. Data de entrega: 30 / 10 /20 23 , horário limite 23 h 30 min.


