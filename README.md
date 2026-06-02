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

# 3.	TERCEIRA REUNIÃO – ESTRUTURAÇÃO DOS DADOS E PLANEJAMENTO DO FLUXO

### 3.1 Objetivo da Reunião
A terceira reunião teve como objetivo organizar as informações levantadas anteriormente e transformá-las em estruturas de dados mais definidas para utilização no sistema.
Durante essa etapa, a equipe analisou quais campos seriam necessários para armazenar as informações de cada funcionalidade, definiu os relacionamentos entre os dados e iniciou o planejamento da estrutura que seria utilizada para armazenamento das informações.
Essas definições serviriam como base para a modelagem do banco de dados e para o desenvolvimento das funcionalidades previstas nos requisitos do projeto.

### 3.2 Estrutura dos Dados de Solicitante
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

### 3.3 Estrutura dos Dados de Categoria
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

### 3.4 Estrutura dos Dados de Solicitação
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

### 3.5 Relacionamento entre os Dados
Após a definição das estruturas, foram analisados os relacionamentos existentes entre os dados.
Foi estabelecido que um solicitante poderia possuir várias solicitações associadas, enquanto cada solicitação estaria vinculada a apenas um solicitante.
Também foi definido que cada solicitação deveria pertencer a uma categoria específica, sendo possível que uma mesma categoria fosse utilizada em diversas solicitações.
A definição desses relacionamentos foi considerada importante para garantir a integridade das informações e evitar inconsistências durante o armazenamento dos dados.

Essas restrições garantem que as solicitações cadastradas estejam sempre associadas a um solicitante e a uma categoria válida.

### 3.6 Planejamento Inicial da Estrutura do Sistema
Além da organização dos dados, a equipe iniciou o planejamento da estrutura geral da aplicação, identificando os módulos necessários para atender aos requisitos funcionais.
Foram definidos os seguintes componentes principais:
•	Cadastro de solicitantes;
•	Registro de solicitações;
•	Consultas e filtros;
•	Estatísticas;
•	Controle de prioridade automática.
Essa organização permitiu visualizar de forma mais clara como os dados seriam utilizados pelas funcionalidades previstas para o sistema.

### 3.7 Resultados Obtidos
Ao final da reunião, a equipe concluiu a definição das principais estruturas de dados necessárias para o sistema, bem como os relacionamentos existentes entre elas.
Também foram definidas as categorias iniciais que seriam utilizadas na classificação das solicitações e estabelecida a base para a modelagem do banco de dados.
As decisões tomadas nesta etapa forneceram os elementos necessários para dar continuidade ao desenvolvimento do sistema e à implementação das funcionalidades previstas nos requisitos funcionais.


# 4.	QUARTA REUNIÃO – DEFINIÇÃO DO FLUXO DE UTILIZAÇÃO DO SISTEMA

### 4.1 Objetivo da Reunião
A quarta reunião teve como objetivo definir o fluxo de utilização da aplicação em modo texto, estabelecendo a forma como os usuários acessariam as funcionalidades disponíveis no sistema.
Como o projeto foi desenvolvido utilizando uma interface baseada em terminal (CLI – Command Line Interface), tornou-se necessário planejar a organização dos menus e a navegação entre as funcionalidades, garantindo uma utilização simples e intuitiva.
As definições realizadas nesta etapa serviram como referência para a implementação da interface textual e para a integração dos requisitos funcionais ao fluxo de utilização do sistema.

### 4.2 Estrutura do Menu Inicial
Foi definido que o sistema seria iniciado por meio de um menu inicial responsável por direcionar o usuário para os diferentes módulos da aplicação.
Essa organização permite que o usuário tenha acesso rápido às principais funcionalidades do sistema, centralizando toda a navegação em um único ponto de entrada.

### 4.3 Relação entre o Menu e os Requisitos Funcionais
Após a definição da estrutura principal de navegação, foi realizado o mapeamento entre as opções disponíveis no sistema e os requisitos funcionais definidos nas reuniões anteriores.
| Opção |	Funcionalidade |	Requisito Relacionado |
|-------|----------------|------------------------|
| 1	| Cadastro de Solicitantes |	RF01 |
| 2	| Solicitações |	RF02 e RF03 |
| 3	| Consultas	| RF04 |
| 4	| Estatísticas |	RF04 |
| 0	| Encerramento do Sistema	| - |

Esse mapeamento permitiu verificar que todos os requisitos funcionais previstos para o projeto poderiam ser acessados por meio da estrutura de navegação definida pela equipe.

### 4.4 Fluxo de Cadastro de Solicitantes
Para o gerenciamento dos solicitantes foi definido um módulo específico contendo as operações relacionadas ao cadastro e manutenção dos registros.
O fluxo planejado consiste em:
1.	Acesso ao menu principal;
2.	Seleção da opção de cadastro;
3.	Escolha da operação desejada;
4.	Inserção ou alteração dos dados;
5.	Validação das informações;
6.	Confirmação da operação;
7.	Retorno ao menu anterior.
Esse módulo está diretamente relacionado ao requisito funcional RF01.

### 4.5 Fluxo de Abertura de Solicitações
Para o registro das solicitações foi definido um fluxo capaz de associar cada solicitação a um solicitante previamente cadastrado.
O processo definido foi:
1.	Acesso ao módulo de solicitações;
2.	Seleção da opção de nova solicitação;
3.	Identificação do solicitante;
4.	Escolha da categoria;
5.	Registro da descrição;
6.	Definição dos critérios utilizados para cálculo da prioridade;
7.	Cálculo automático da prioridade;
8.	Armazenamento da solicitação;
9.	Retorno ao menu anterior.
Essa funcionalidade contempla os requisitos RF02 – Abertura de Solicitação e RF03 – Prioridade Automática.

### 4.6 Fluxo de Consultas
Também foi definido um módulo destinado à consulta e acompanhamento das solicitações registradas no sistema.
As funcionalidades previstas incluem:
•	Consulta geral das solicitações;
•	Consultas utilizando filtros;
•	Atualização das informações registradas;
•	Acompanhamento do status das solicitações.
O fluxo definido consiste em:
1.	Acesso ao módulo de consultas;
2.	Seleção do tipo de consulta desejada;
3.	Aplicação dos filtros necessários;
4.	Visualização dos resultados;
5.	Retorno ao menu anterior.

### 4.7 Fluxo de Estatísticas
Durante a reunião também foi definida uma funcionalidade destinada à geração de informações estatísticas relacionadas aos dados armazenados pela aplicação.
O fluxo planejado consiste em:
1.	Acesso ao módulo de estatísticas;
2.	Processamento das informações registradas;
3.	Geração dos indicadores;
4.	Exibição dos resultados;
5.	Retorno ao menu principal.

Essa funcionalidade também está vinculada ao requisito funcional RF04, permitindo a análise dos dados cadastrados no sistema.

### 4.8 Resultados Obtidos
Ao final da quarta reunião, a equipe concluiu a definição da estrutura de navegação da aplicação e dos fluxos de utilização das principais funcionalidades do sistema.
Também foi realizado o mapeamento entre os módulos disponíveis e os requisitos funcionais previamente definidos, garantindo que todas as funcionalidades previstas pudessem ser acessadas de forma organizada por meio da interface textual.
As definições estabelecidas nesta etapa serviram como base para a implementação dos menus e para o desenvolvimento das operações que compõem o sistema.


# 5.	QUINTA REUNIÃO – INÍCIO DO DESENVOLVIMENTO DO SISTEMA

### 5.1 Objetivo da Reunião
A quinta reunião teve como objetivo iniciar efetivamente o desenvolvimento do sistema, colocando em prática as definições realizadas nas etapas anteriores.
Diferentemente das reuniões anteriores, que tiveram foco no planejamento e na modelagem da solução, esta etapa marcou o início da implementação do banco de dados e da estrutura principal da aplicação em Python.
As atividades foram divididas em duas frentes principais: desenvolvimento da estrutura de armazenamento dos dados e implementação da interface inicial da aplicação.

### 5.2 Criação da Estrutura Inicial do Banco de Dados
Com base nas definições realizadas durante as etapas de modelagem, foi iniciada a construção do script SQL responsável pela criação do banco de dados do projeto.
A primeira etapa consistiu na criação da estrutura principal do banco de dados.

<img width="442" height="150" alt="image" src="https://github.com/user-attachments/assets/5e72671a-c76a-4114-bc73-f0c166ad36da" />

 
Essa configuração garante um ambiente adequado para armazenamento das informações manipuladas pela aplicação.

### 5.3 Implementação da Tabela de Solicitantes
Após a criação do banco de dados, foi implementada a estrutura destinada ao armazenamento dos solicitantes cadastrados no sistema.

<img width="615" height="235" alt="image" src="https://github.com/user-attachments/assets/79f8f85b-8ec7-4a40-80b1-d2c32eb2110d" />

 
Durante essa implementação foram utilizados conceitos relacionados à definição de chaves primárias, restrições de unicidade e seleção adequada dos tipos de dados.
A utilização de identificadores automáticos facilita o gerenciamento dos registros e reduz a possibilidade de duplicidade.

### 5.4 Implementação da Tabela de Categorias
Também foi criada a estrutura responsável pelo armazenamento das categorias utilizadas para classificação das solicitações.

<img width="570" height="140" alt="image" src="https://github.com/user-attachments/assets/7cf622a3-b20a-4074-ab67-eead5be64e7e" />

 
Além da criação da tabela, foram definidos registros iniciais para utilização no sistema.

<img width="463" height="154" alt="image" src="https://github.com/user-attachments/assets/a5282be7-78e6-4f52-8aee-e419ea90b46e" />

 
Essas categorias permitem padronizar a classificação das solicitações cadastradas pelos usuários.

### 5.5 Implementação da Tabela de Solicitações
Em seguida, foi iniciada a implementação da principal estrutura do sistema, responsável pelo armazenamento das solicitações registradas.

<img width="808" height="221" alt="image" src="https://github.com/user-attachments/assets/beedb876-8902-4a84-a020-da00bcb5b417" />

 
Essa estrutura concentra as informações necessárias para o registro, acompanhamento e gerenciamento das solicitações realizadas pelos usuários.

### 5.6 Implementação dos Relacionamentos
Para garantir a integridade das informações armazenadas, foram implementados os relacionamentos entre as tabelas do sistema por meio de chaves estrangeiras.

<img width="694" height="196" alt="image" src="https://github.com/user-attachments/assets/858abad8-d420-4fb3-a668-59178e315484" />

 
Essas restrições garantem que toda solicitação esteja vinculada a um solicitante e a uma categoria válidos, evitando inconsistências nos dados armazenados.

### 5.7 Implementação das Regras de Integridade dos Dados
Além dos relacionamentos, também foram implementadas regras de validação para garantir que determinados campos recebessem apenas valores previamente definidos.

<img width="886" height="56" alt="image" src="https://github.com/user-attachments/assets/7add4e51-cbe0-4641-bbc5-c7c79c3809fd" />

 
Essas restrições contribuem para a integridade dos dados cadastrados, impedindo o armazenamento de valores inválidos para os campos de status e prioridade.
A adoção dessas validações aumenta a confiabilidade das informações registradas pelo sistema.

### 5.8 Início da Estrutura da Aplicação em Python
Paralelamente ao desenvolvimento do banco de dados, foi iniciada a implementação da estrutura principal da aplicação em Python.
O primeiro componente desenvolvido foi o menu inicial, responsável por centralizar o acesso às funcionalidades disponíveis.

<img width="788" height="412" alt="image" src="https://github.com/user-attachments/assets/f0755332-20d1-4f10-ab40-97435c716746" />

 
Esse menu representa o ponto inicial de interação entre o usuário e o sistema, permitindo o acesso organizado às funcionalidades previstas nos requisitos funcionais.

### 5.9 Organização do Projeto
Durante a implementação também foram realizadas atualizações no repositório GitHub da equipe.
As alterações desenvolvidas foram registradas por meio de commits e associadas às Issues previamente criadas, permitindo acompanhar o progresso do projeto de forma organizada.
O GitHub Project continuou sendo utilizado para monitorar o andamento das atividades e registrar a evolução das tarefas previstas.

### 5.10 Resultados Obtidos
Ao final da quinta reunião, a equipe havia realizado os primeiros avanços concretos no desenvolvimento da solução proposta.
Entre os principais resultados alcançados destacam-se:
•	Criação da estrutura inicial do banco de dados;
•	Implementação das tabelas principais do sistema;
•	Definição dos relacionamentos entre as entidades;
•	Inserção das categorias iniciais;
•	Implementação das regras de integridade dos dados;
•	Desenvolvimento da estrutura inicial da aplicação em Python;
•	Criação do menu principal da aplicação;
•	Atualização do repositório GitHub e das ferramentas de gerenciamento.
Essa etapa marcou a transição entre o planejamento realizado nas reuniões anteriores e o início efetivo da implementação do sistema.

 # 6.	SEXTA REUNIÃO – ACOMPANHAMENTO DA EVOLUÇÃO E PLANEJAMENTO DAS PRÓXIMAS ETAPAS

### 6.1 Objetivo da Reunião
A sexta reunião teve como objetivo analisar o estágio atual do projeto, consolidar os resultados obtidos até o momento e definir as próximas etapas necessárias para continuidade do desenvolvimento.
Diferentemente da reunião anterior, que teve foco na implementação inicial do sistema, esta etapa foi dedicada à avaliação do progresso alcançado pela equipe, à verificação da organização dos artefatos produzidos e ao planejamento das atividades futuras.
Também foram identificados os requisitos que já possuíam uma estrutura definida e aqueles que ainda dependeriam de implementação nas próximas fases do projeto.

### 6.2 Apresentação do Andamento do Projeto
Durante a reunião foi realizada uma análise geral dos artefatos produzidos desde o início do desenvolvimento.
Foi constatado que o projeto já possuía uma estrutura inicial de banco de dados e uma versão preliminar da aplicação em Python, permitindo visualizar a organização geral da solução proposta.
Entre os principais elementos desenvolvidos até o momento destacam-se:
•	Estrutura do banco de dados;
•	Definição das tabelas principais;
•	Relacionamentos entre entidades;
•	Cadastro das categorias iniciais;
•	Estrutura final da aplicação em Python;
•	Menu principal da aplicação;
•	Organização do projeto no GitHub.
Esses elementos representavam a base necessária para o desenvolvimento das funcionalidades previstas nos requisitos do sistema.

### 6.3 Estruturas Já Implementadas
Durante a análise do projeto foi verificado que as principais estruturas de armazenamento de dados já haviam sido definidas, essas já citadas anteriormente.
A existência dessas estruturas demonstrava que o projeto já possuía uma base consistente para armazenamento das informações necessárias ao funcionamento da aplicação.

### 6.4 Estrutura da Aplicação
Também foi apresentado o estágio atual da aplicação desenvolvida em Python.

### 6.5 Verificação da Organização do Repositório
Outro aspecto analisado durante a reunião foi a organização do projeto no GitHub.
Foram verificadas as seguintes atividades:
•	Existência do repositório oficial do projeto;
•	Atualização do arquivo README;
•	Presença das Issues relacionadas aos requisitos funcionais;
•	Organização do GitHub Project;
•	Armazenamento dos arquivos produzidos;
•	Registro das alterações realizadas por meio de commits.
A utilização dessas ferramentas permitiu manter o desenvolvimento organizado e facilitar o acompanhamento da evolução do projeto.

### 6.6 Identificação das Funcionalidades Pendentes
Após a análise das estruturas já desenvolvidas, a equipe realizou um levantamento das funcionalidades que ainda precisariam ser implementadas.
Entre as principais pendências identificadas estavam:
•	Cadastro completo de solicitantes;
•	Consulta de solicitantes cadastrados;
•	Atualização de dados dos solicitantes;
•	Exclusão de registros;
•	Cadastro completo de solicitações;
•	Atualização de status das solicitações;
•	Implementação das consultas específicas;
•	Implementação das estatísticas previstas nos requisitos.

A identificação dessas pendências permitiu organizar melhor as próximas etapas do desenvolvimento.

### 6.7 Situação Atual dos Requisitos
Com base na análise do projeto realizada durante a reunião, foi elaborado um panorama geral da situação dos requisitos funcionais.
| Requisito |	Situação |
|-----------|----------|
| RF01 – Cadastro de Solicitante	| Estrutura definida |
| RF02 – Abertura de Solicitação |	Estrutura definida |
| RF03 – Prioridade Automática	| Regras definidas |
| RF04 – Acompanhamento e Consultas	| Estrutura planejada |

Essa visão permitiu identificar de forma clara quais requisitos já possuíam uma base estabelecida e quais ainda dependeriam de implementação nas próximas etapas do projeto.

### 6.8 Definição da Próxima Etapa de Desenvolvimento
Seguindo o planejamento do projeto, a equipe definiu que a próxima etapa prioritária seria a implementação das operações de CRUD (Create, Read, Update e Delete).
Essa decisão foi tomada porque essas operações representam a base funcional necessária para manipulação dos dados armazenados no sistema.
A implementação dessas funcionalidades permitiria:
•	Cadastrar novos registros;
•	Consultar informações existentes;
•	Atualizar dados cadastrados;
•	Excluir registros quando necessário.

### 6.9 Atualização do Planejamento
Ao final da reunião, o planejamento do projeto foi atualizado para refletir o estágio atual do desenvolvimento.
As Issues existentes foram revisadas, o quadro Kanban foi atualizado e as atividades futuras foram registradas para acompanhamento.
Essa atualização permitiu manter uma visão clara do progresso do projeto e das próximas entregas previstas.

### 6.10 Resultados Obtidos
Ao término da sexta reunião, a equipe possuía uma visão consolidada sobre o estágio atual do projeto.
Foi possível verificar que a estrutura inicial da aplicação e do banco de dados já havia sido construída, que o ambiente de desenvolvimento se encontrava organizado e que os próximos passos estavam claramente definidos.
A principal decisão tomada durante a reunião foi estabelecer a implementação das operações de CRUD como prioridade para a próxima fase do desenvolvimento, dando continuidade à construção das funcionalidades previstas nos requisitos do sistema.







































































