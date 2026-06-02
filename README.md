# PI1-SI-2026-Time01
Integrantes:
Cauã Queiroz Guerra,
João Victor Teles Carneiro,
Maria Teodora Santana de Martin,
Murilo Boschiero,
Ronald Leandro Feliciano Silva,
Warley Mendes de Souza
# Sistema de Controle de Solicitações Corporativas
Descrição do Projeto:

O projeto foi desenvolvido na disciplina de Projeto Integrador 1 do curso de Sistemas de Informação da PUC-Campinas.
O sistema tem como objetivo organizar e gerenciar solicitações corporativas de forma centralizada, substituindo métodos informais como mensagens, anotações e e-mails dispersos.
A aplicação foi desenvolvida em Python com integração ao MySQL, permitindo cadastro, controle e acompanhamento das solicitações.

## Objetivos do Sistema
Registrar solicitações;
Cadastrar solicitantes;
Organizar solicitações por categorias;
Definir prioridades;
Controlar status das solicitações;
Permitir consultas, edições e exclusões;
Gerar relatórios básicos.

# 1.	PRIMEIRA REUNIÃO – ORGANIZAÇÃO INICIAL DO PROJETO

### 1.1 Objetivo da Reunião
A primeira reunião do Projeto Integrador I teve como objetivo definir a estrutura inicial do trabalho e organizar os recursos necessários para o desenvolvimento do sistema. Nessa etapa, foram discutidos os requisitos propostos pela disciplina, as tecnologias que seriam utilizadas e as ferramentas de apoio ao gerenciamento das atividades.
A reunião foi fundamental para alinhar a equipe quanto às responsabilidades de cada integrante e estabelecer uma metodologia de trabalho que pudesse ser utilizada durante todo o desenvolvimento do projeto.

### 1.2 Criação do Repositório GitHub
Como parte das atividades iniciais, foi criado um repositório na plataforma GitHub para armazenar os arquivos do projeto e centralizar o desenvolvimento da aplicação.
O repositório passou a servir como ambiente principal para compartilhamento do código-fonte entre os integrantes da equipe, além de permitir o registro das alterações realizadas ao longo do projeto por meio do controle de versões.
A utilização do GitHub contribuiu para manter a organização dos arquivos e facilitar o acompanhamento da evolução do sistema.

### 1.3 Configuração do README
Após a criação do repositório, foi elaborado o arquivo README.md contendo as informações iniciais do projeto.
Nesse documento foram registrados os dados de identificação da equipe, os integrantes participantes e uma descrição resumida da proposta do sistema. Também foram informadas as tecnologias previstas para o desenvolvimento da aplicação.
O README foi utilizado como documentação inicial do projeto e como referência para consulta rápida das principais informações relacionadas ao trabalho.

### 1.4 Tecnologias Utilizadas
As tecnologias adotadas foram definidas de acordo com os requisitos estabelecidos pela disciplina.
Python
Python foi escolhido como linguagem principal para o desenvolvimento da aplicação devido à sua simplicidade, legibilidade e ampla utilização em projetos acadêmicos.
MySQL
O MySQL foi definido como sistema gerenciador de banco de dados responsável pelo armazenamento e gerenciamento das informações utilizadas pelo sistema.
GitHub
O GitHub foi utilizado para hospedagem do projeto, controle de versões e gerenciamento das atividades da equipe.
Interface em Terminal
A aplicação foi planejada para funcionar por meio de uma interface baseada em terminal (CLI – Command Line Interface), conforme especificado nos requisitos da disciplina.

### 1.5 Levantamento dos Requisitos Funcionais
Durante a reunião foram analisados os requisitos funcionais que deveriam ser implementados no sistema. Esses requisitos representam as principais funcionalidades previstas para a aplicação.
RF01 – Cadastro de Solicitante
Permitir o cadastro e a consulta de solicitantes, armazenando as informações necessárias para identificação dos usuários do sistema.
RF02 – Abertura de Solicitação
Permitir o registro de solicitações vinculadas a um solicitante, contendo informações relevantes para seu acompanhamento.
RF03 – Prioridade Automática
Implementar uma regra responsável por definir automaticamente a prioridade das solicitações de acordo com critérios previamente estabelecidos.
RF04 – Acompanhamento e Consultas
Permitir a consulta das solicitações cadastradas e o acompanhamento de seu status ao longo do fluxo de atendimento.
Os requisitos levantados serviram como base para o planejamento das atividades de desenvolvimento.

### 1.6 Criação das Issues dos Requisitos Funcionais
Após a definição dos requisitos funcionais, foram criadas Issues no GitHub para representar cada funcionalidade prevista para o sistema.
Cada requisito recebeu uma Issue específica, permitindo que as tarefas fossem organizadas e acompanhadas de forma individual durante o desenvolvimento do projeto.
As Issues criadas foram:
•	RF01 – Cadastro de Solicitante; 
•	RF02 – Abertura de Solicitação; 
•	RF03 – Prioridade Automática; 
•	RF04 – Acompanhamento e Consultas. 
A utilização das Issues permitiu transformar os requisitos em tarefas organizadas, facilitando o planejamento das atividades e o acompanhamento do progresso da equipe.

### 1.7 Organização das Demais Atividades
Além das Issues relacionadas aos requisitos funcionais, também foram cadastradas Issues destinadas a atividades complementares necessárias para o desenvolvimento do projeto.
Essas atividades incluíram tarefas relacionadas à documentação, estruturação do banco de dados, definição de funcionalidades auxiliares e organização do ambiente de desenvolvimento.
A adoção dessa estratégia contribuiu para que todas as atividades do projeto fossem registradas e acompanhadas em um único ambiente.

### 1.8 Criação do GitHub Project
Com o objetivo de melhorar a organização das tarefas, foi criado um GitHub Project utilizando a metodologia Kanban.
O quadro foi estruturado para representar as diferentes etapas do fluxo de trabalho da equipe, permitindo acompanhar o andamento das atividades desde seu planejamento até sua conclusão.
As colunas definidas para o projeto foram:
•	Backlog; 
•	Ready; 
•	In Progress; 
•	In Review; 
•	Done. 
Essa organização proporcionou uma visão mais clara das atividades previstas e facilitou o gerenciamento das tarefas ao longo do desenvolvimento.

### 1.9 Resultados da Reunião
Ao final da primeira reunião, foram concluídas as atividades necessárias para iniciar o desenvolvimento do projeto.
Entre os principais resultados alcançados destacam-se:
•	Criação do repositório no GitHub; 
•	Elaboração do arquivo README; 
•	Definição das tecnologias a serem utilizadas; 
•	Levantamento dos requisitos funcionais; 
•	Criação das Issues correspondentes aos requisitos do sistema; 
•	Organização das tarefas no GitHub Project. 
Com essas definições, o projeto passou a contar com uma estrutura organizada para apoiar as próximas etapas de desenvolvimento.

# 2.	SEGUNDA REUNIÃO – LEVANTAMENTO DAS INFORMAÇÕES NECESSÁRIAS

### 2.1 Objetivo da Reunião
A segunda reunião do Projeto Integrador I teve como objetivo detalhar os requisitos funcionais definidos anteriormente, identificando quais informações seriam necessárias para o funcionamento adequado de cada funcionalidade do sistema.
Nessa etapa, a equipe concentrou seus esforços em compreender quais dados deveriam ser coletados, armazenados e utilizados pela aplicação, estabelecendo uma base para as próximas fases do projeto.

### 2.2 RF01 – Cadastro de Solicitante
Para atender ao requisito de cadastro de solicitantes, foram discutidas as informações necessárias para identificar e manter os dados básicos dos usuários que utilizariam o sistema.
Após análise, foram definidos os seguintes dados:
•	Nome;
•	E-mail;
•	Telefone.
Essas informações foram consideradas suficientes para permitir a identificação dos solicitantes e possibilitar futuras associações com as solicitações registradas no sistema.

### 2.3 RF02 – Abertura de Solicitação
Durante a análise do processo de abertura de solicitações, foram identificados os dados necessários para registrar adequadamente cada solicitação.
As informações levantadas foram:
•	Solicitante responsável;
•	Categoria da solicitação;
•	Descrição da solicitação;
•	Data de abertura;
•	Status da solicitação.
A definição desses dados teve como objetivo garantir que cada solicitação pudesse ser registrada e acompanhada de maneira organizada durante seu ciclo de atendimento.

### 2.4 RF03 – Prioridade Automática
Para o requisito relacionado à definição de prioridade, foi discutida a necessidade de padronizar a classificação das solicitações.
A equipe definiu que a prioridade não seria informada diretamente pelo usuário, mas calculada automaticamente pelo sistema com base em critérios previamente estabelecidos.
Foram definidos três níveis de prioridade:
•	Baixa;
•	Média;
•	Alta.
Essa abordagem foi considerada adequada por proporcionar maior consistência na classificação das solicitações e reduzir possíveis divergências de interpretação por parte dos usuários.

### 2.5 RF04 – Consultas e Estatísticas
Também foram discutidas as informações que deveriam estar disponíveis para consulta durante a utilização do sistema.
Entre as funcionalidades previstas destacam-se:
•	Consulta de solicitações cadastradas;
•	Consulta por status;
•	Consulta por prioridade;
•	Consulta por categoria;
•	Visualização de informações estatísticas relacionadas aos registros realizados.
Esses recursos foram considerados importantes para facilitar o acompanhamento das solicitações e fornecer uma visão geral dos dados armazenados pela aplicação.

### 2.6 Consolidação dos Dados Necessários
Após o levantamento das informações relacionadas a cada requisito funcional, foi realizada uma consolidação dos dados identificados durante a reunião.
Nessa etapa, a equipe organizou os elementos que seriam necessários para representar os solicitantes, as solicitações e suas respectivas classificações dentro do sistema.
Foram agrupadas as informações de identificação dos usuários, os dados relacionados às solicitações e os elementos utilizados para classificação, acompanhamento e consulta dos registros.
Essa consolidação permitiu visualizar de forma mais clara quais informações deveriam ser armazenadas pela aplicação, servindo como referência para as próximas etapas de análise e estruturação dos dados do projeto.

### 2.7 Resultados Obtidos
Ao final da reunião, foram identificadas e organizadas as principais informações necessárias para o funcionamento das funcionalidades previstas no sistema.
Os dados levantados forneceram uma visão mais detalhada dos requisitos funcionais e serviram como base para as etapas seguintes do projeto, contribuindo para o planejamento da estrutura que seria utilizada para armazenamento e gerenciamento das informações.
Com isso, a equipe passou a ter uma compreensão mais clara dos dados envolvidos no processo e dos elementos necessários para o desenvolvimento da aplicação.

4.	TERCEIRA REUNIÃO – ESTRUTURAÇÃO DOS DADOS E PLANEJAMENTO DO FLUXO

4.1 Objetivo da Reunião
A terceira reunião teve como objetivo organizar as informações levantadas anteriormente e transformá-las em estruturas de dados mais definidas para utilização no sistema.
Durante essa etapa, a equipe analisou quais campos seriam necessários para armazenar as informações de cada funcionalidade, definiu os relacionamentos entre os dados e iniciou o planejamento da estrutura que seria utilizada para armazenamento das informações.
Essas definições serviriam como base para a modelagem do banco de dados e para o desenvolvimento das funcionalidades previstas nos requisitos do projeto.

4.2 Estrutura dos Dados de Solicitante
A partir do requisito funcional relacionado ao cadastro de solicitantes, foram definidos os dados necessários para identificação e contato dos usuários.
Os campos planejados foram:
| Campo	| Tipo de Dado	| Descrição	| Chave |
|-------|---------------|-----------|------|
Código |	Inteiro	| Identificador do solicitante |	Sim
| Nome |	Texto |	Nome do solicitante	| Não |
| E-mail	| Texto |	Endereço eletrônico do solicitante |	Não |
| Telefone |	Texto	| Número para contato	| Não |


A definição desses campos buscou garantir que cada solicitante pudesse ser identificado de forma única dentro do sistema e associado às solicitações registradas.

Observa-se que os campos definidos durante a etapa de planejamento foram posteriormente utilizados na estrutura de armazenamento dos solicitantes.

4.3 Estrutura dos Dados de Categoria
Durante a reunião também foi definida uma estrutura destinada à classificação das solicitações por categoria.
Os campos planejados foram:
| Campo	| Tipo de Dado |	Descrição	| Chave |
|-------|--------------|------------|-------|
| ID	 | Inteiro |	Identificador da categoria	| Sim |
| Categoria |	Texto	| Nome da categoria |	Não |

Além da estrutura básica, a equipe definiu algumas categorias iniciais que seriam disponibilizadas aos usuários para facilitar o registro das solicitações.
As categorias planejadas foram:
•	Suporte Técnico;
•	Financeiro;
•	Recursos Humanos;
•	Infraestrutura;
•	Outros.

A definição prévia dessas categorias contribuiu para padronizar os registros e facilitar futuras consultas e análises.

4.4 Estrutura dos Dados de Solicitação
A principal estrutura do sistema foi definida para armazenar as solicitações abertas pelos usuários.
Os campos identificados como necessários foram:
Campo	Tipo de Dado	Descrição	Chave
ID	Inteiro	Identificador da solicitação	Sim
Solicitante	Inteiro	Referência ao solicitante responsável	Não
Categoria	Inteiro	Categoria da solicitação	Não
Descrição	Texto	Detalhamento da solicitação	Não
Data de Abertura	Data e Hora	Momento do registro da solicitação	Não
Status	Texto	Situação atual da solicitação	Não
Prioridade	Texto	Nível de prioridade atribuído à solicitação	Não
Essa estrutura foi planejada para concentrar as principais informações manipuladas pelo sistema, permitindo registrar, acompanhar e consultar as solicitações cadastradas.

A estrutura definida contempla as informações necessárias para o funcionamento dos requisitos relacionados ao registro e acompanhamento das solicitações.

4.5 Relacionamento entre os Dados
Após a definição das estruturas, foram analisados os relacionamentos existentes entre os dados.
Foi estabelecido que um solicitante poderia possuir várias solicitações associadas, enquanto cada solicitação estaria vinculada a apenas um solicitante.
Também foi definido que cada solicitação deveria pertencer a uma categoria específica, sendo possível que uma mesma categoria fosse utilizada em diversas solicitações.
A definição desses relacionamentos foi considerada importante para garantir a integridade das informações e evitar inconsistências durante o armazenamento dos dados.

Essas restrições garantem que as solicitações cadastradas estejam sempre associadas a um solicitante e a uma categoria válida.

4.6 Planejamento Inicial da Estrutura do Sistema
Além da organização dos dados, a equipe iniciou o planejamento da estrutura geral da aplicação, identificando os módulos necessários para atender aos requisitos funcionais.
Foram definidos os seguintes componentes principais:
•	Cadastro de solicitantes;
•	Registro de solicitações;
•	Consultas e filtros;
•	Estatísticas;
•	Controle de prioridade automática.
Essa organização permitiu visualizar de forma mais clara como os dados seriam utilizados pelas funcionalidades previstas para o sistema.

4.7 Resultados Obtidos
Ao final da reunião, a equipe concluiu a definição das principais estruturas de dados necessárias para o sistema, bem como os relacionamentos existentes entre elas.
Também foram definidas as categorias iniciais que seriam utilizadas na classificação das solicitações e estabelecida a base para a modelagem do banco de dados.
As decisões tomadas nesta etapa forneceram os elementos necessários para dar continuidade ao desenvolvimento do sistema e à implementação das funcionalidades previstas nos requisitos funcionais.













