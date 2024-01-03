# Data Lake House de baixo custo

## Escopo do Teste MVP de Data Pipeline Utilizando Python, GCP e duckDB

##### Objetivo:

Desenvolver e validar um MVP de data pipeline para coletar, transformar e armazenar dados de API's. Os dados serão
processados utilizando Python, armazenados no Google BigQuery e visualizados através do Power BI.

### Etapas do Projeto:

#### Coleta de Dados:

* Acesso e autenticação na API da RedeMob utilizando Python.
* Seleção dos endpoints específicos da API para coleta de dados.
* Definição da frequência de coleta de dados.

##### Processamento e Transformação de Dados com Python:

* Desenvolvimento de scripts Python para a extração de dados da API.
* Utilização de bibliotecas Python para transformação e limpeza dos dados (ex: pandas, NumPy).
* Testes para validar a integridade e a qualidade dos dados processados.

##### Armazenamento de Dados no BigQuery:

* Configuração da pipeline de dados para carregar os dados transformados no BigQuery.
* Monitoramento do processo de carga de dados para identificação de potenciais falhas.

##### Integração com Power BI:

* Conexão do BigQuery ao Power BI.
* Desenvolvimento de dashboards e relatórios no Power BI para análise dos dados.
* Testes para assegurar a correta visualização e interpretação dos dados.

### Custos Estimados:

#### Custos de Desenvolvimento e Operação:

* Recursos computacionais para desenvolvimento e execução dos scripts Python.

#### Custos de Armazenamento e Processamento no BigQuery:

* Custos de armazenamento de dados no BigQuery.
* Custos de processamento no BigQuery para execução de consultas e análises.

#### Custos de Ferramentas e Licenças:

* Licença do Power BI.
* Possíveis custos de ferramentas adicionais para orquestração e monitoramento da pipeline (se necessário).

#### Considerações Adicionais:

* Segurança e Privacidade dos Dados: Implementação de medidas para proteger os dados durante a coleta, processamento e
  armazenamento.
* Documentação: Manutenção de documentação detalhada sobre os scripts Python e processos de pipeline.
* Testes e Validação: Realização de testes rigorosos para garantir a acurácia e a eficácia da pipeline.