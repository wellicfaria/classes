# Arquitetura de Data Pipelines

## Informações Gerais

**Tópico**: Arquitetura de Data Pipelines  
**Tema**: Data Pipelines  

## Estrutura da Aula

### Introdução (3 min)

- O que é um Data Pipelines? 

Um Data Pipeline é uma série de processos de dados projetados para *transformar*, *transportar* e *armazenar* dados de uma fonte para um destino.

O processo em um Data Pipeline geralmente começa com a *extração* de dados de fontes diversas, como bancos de dados, sistemas de arquivos, feeds ao vivo ou serviços na nuvem. Após a extração, os dados são *transformados*. Esta transformação pode envolver `limpeza, agregação, enriquecimento, ou outras formas de manipulação para tornar os dados mais úteis e consistentes`. Por fim, os dados transformados são *carregados* em um sistema de armazenamento ou análise, como um Data warehouse ou Data Lake.  Assim temos o conceito de ETL (Extract, Transform, Load). 

### Teoria Básica (4 min)

- Data Pipelines no `Mundo Real`. 

Vamos supor que você esteja trabalhando com dados de atendimento ao cliente e queira analisar a satisfação do cliente com base em tickets de suporte.

Aqui está o fluxo de ETL para este cenário:

`Extração (Extract)`: Os dados são extraídos de duas fontes - um banco de dados de tickets de suporte e um sistema de feedback do cliente.

`Transformação (Transform)`: Os dados são limpos (removendo entradas duplicadas, corrigindo erros), combinados (unindo dados de tickets com feedbacks) e agregados (calculando a média de satisfação por produto ou serviço).

`Carregamento (Load)`: Os dados transformados são carregados em um data warehouse para análise e geração de relatórios.

```mermaid
graph TD;
    A[Database de Tickets] -->|Extrair| C[Transformação];
    B[Sistema de Feedback] -->|Extrair| C[Transformação];
    C -->|Limpeza de Dados| D[Transformação];
    C -->|Combinação de Dados| E[Transformação];
    C -->|Agregação| F[Transformação];
    D --> G|Data Warehouse|[Carregamento];
    E --> G;
    F --> G;
    G --> H[Análise de Satisfação do Cliente];
```


- Importância dos Data Pipelines na engenharia de dados.

### Demonstrações de Código (6-8 min)
- Apresentação de um exemplo simples de pipeline de dados usando Python.
- Demonstração inclui extração de dados, uma transformação básica e carregamento em um sistema de armazenamento.

## Anotações Detalhadas

### Data Pipelines
- O que são Data Pipelines.
- Por que são essenciais na engenharia de dados.

### Componentes de um Data Pipeline
- Coleta de dados: Como os dados são adquiridos.
- Processamento de dados: Métodos de transformação dos dados.
- Armazenamento de dados: Onde e como os dados são armazenados.

### Conceito de ETL
- Explicação do processo ETL (Extract, Transform, Load).

## Recursos Adicionais

- [Exemplo de Código - Arquitetura de Data Pipelines](https://www.notion.so/Exemplo-de-C-digo-Arquitetura-de-Data-Pipelines-a83bf2a8a56a448597227d152d5254b8?pvs=21)

