# Rede Neural para Prever Sentimentos de Criptomoedas
Este código usa uma rede neural para prever o sentimento de menções de criptomoedas no Twitter. Ele utiliza dados de um arquivo CSV e solicitações de API para obter os preços do Bitcoin (BTC), Ethereum (ETH) e Litecoin (LTC).

# Uso de Dependências
* torch: PyTorch é uma biblioteca de aprendizado de máquina em Python que permite a criação de modelos de rede neural para tarefas como classificação, regressão, processamento de linguagem natural, visão computacional, entre outras. O PyTorch oferece várias ferramentas para criação e treinamento de modelos, incluindo tensores (arrays multidimensionais) que podem ser utilizados para realizar operações numéricas em GPU e CPU.

* pandas: Pandas é uma biblioteca de análise de dados em Python que oferece ferramentas para leitura, manipulação, agregação e visualização de dados tabulares.  O principal objeto de dados no Pandas é o DataFrame, que é uma tabela bidimensional com rótulos de colunas e linhas, permitindo a realização de operações matemáticas e estatísticas nas colunas e linhas dos dados.

* sklearn: é uma biblioteca de aprendizado de máquina em Python que oferece uma variedade de ferramentas para pré-processamento de dados, seleção de modelos, validação e avaliação de modelos, além de algoritmos para aprendizado supervisionado e não supervisionado.



# Certifique-se de que todas as dependências necessárias estejam instaladas.

Clone este repositório e navegue até o diretório contendo o código.
Execute o código usando um interpretador Python.

# Etapas

* O arquivo CSV com os dados de menção de criptomoedas é lido em um dataframe do Pandas.

* A coluna de saída do dataframe é convertida em valores binários (positivo=1, negativo=0).
* O dataframe é dividido em conjuntos de treinamento e teste usando a função train_test_split do sklearn.
* A rede neural é definida usando Pytorch. Ela possui três camadas totalmente conectadas e usa as funções de ativação ReLU e sigmoid.

* A função de perda de entropia cruzada binária e o otimizador Adam são definidos.
* O modelo é treinado por 100 épocas usando os dados de treinamento.
* O modelo é testado nos dados de teste para determinar sua precisão.
* Os preços de BTC, ETH e LTC são obtidos usando a API da Coinbase por meio de solicitações e json.
* Os preços são adicionados ao dataframe.
* O dataframe é dividido novamente em conjuntos de treinamento e teste.
* A rede neural é treinada e testada novamente usando o dataframe atualizado.

* Aviso Legal
Este código é apenas para fins educacionais e não deve ser usado para análise financeira ou decisões de investimento. A precisão do modelo não é garantida e não deve ser confiada.