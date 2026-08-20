# 🎯 Requisitos Funcionais (RF)

### Frente Base: Análise e Consulta (1ª Instância)
* **RF01 - Autenticação e Sigilo:** O sistema deve permitir login seguro para garantir que o magistrado ou advogado acesse uma área de trabalho confidencial e individualizada (US04).
* **RF02 - Processamento de Petições:** O sistema deve receber arquivos de petição inicial, extrair os pontos principais do processo de forma automatizada e estruturar esses dados (US01).
* **RF03 - Busca e Classificação de Precedentes:** O sistema deve buscar precedentes jurídicos e categorizá-los pelo seu nível de aplicabilidade ao caso submetido (US02).
* **RF04 - Síntese Explicativa:** O sistema deve gerar um texto comparando a petição aos precedentes listados, justificando a recomendação da ferramenta (US03).
* **RF05 - Histórico de Análises:** O sistema deve exibir, na tela de boas-vindas, as análises mais recentes do usuário para permitir a retomada rápida do trabalho (US05).
* **RF06 - Exportação de Relatório:** O sistema deve emitir um documento formal com o resultado da análise e os precedentes selecionados para anexação como material de apoio aos autos (US06).

### Frente 1: Assistente ao Advogado
* **RF07 - Identificação e Ranqueamento:** A partir da descrição do caso e dos documentos inseridos, o sistema deve identificar a matéria e buscar precedentes aplicáveis, ranqueados por relevância e hierarquia (US07).
* **RF08 - Sugestão de Petição Inicial:** O sistema deve gerar uma sugestão de petição inicial estruturada, contendo fatos, fundamentos, pedidos e citações de precedentes (US08).
* **RF09 - Edição Assistida:** O sistema deve prover um ambiente de edição para a minuta gerada, permitindo ao advogado refinar a tese central e substituir precedentes sugeridos (US11).

### Frente 2: Assistente ao Julgador (2ª Instância)
* **RF10 - Classificação de Autos Completos:** O sistema deve receber autos processuais completos em PDF, classificar as peças internas e extrair especificamente o contexto da petição inicial (US10).
* **RF11 - Minuta de Decisão Judicial:** O sistema deve gerar uma minuta de decisão de 2ª instância (relatório, fundamentação e dispositivo) baseada nos precedentes, sinalizando de forma clara a ausência de teses fortes (US09).

---

# ⚙️ Requisitos Não Funcionais (RNF)

* **RNF01 - API em FastAPI:** O back-end principal da aplicação deve ser construído em Python utilizando o framework FastAPI.
* **RNF02 - Motor de Inteligência Artificial (OpenAI):** O processamento de linguagem natural, extração de contexto e geração de minutas/sínteses devem ser realizados via integração com a **API da OpenAI** (utilizando modelos como GPT-4o ou equivalentes).
* **RNF03 - Anonimização e Conformidade (LGPD):** O sistema deve executar uma rotina prévia de ofuscação/anonimização de dados pessoais sensíveis do processo antes de enviar qualquer *payload* de texto para a API da OpenAI.
* **RNF04 - Banco Vetorial e Cache:** A arquitetura deve utilizar o **Qdrant** para armazenamento de *embeddings* e realização das buscas semânticas, em conjunto com o **Redis** para gerenciamento rápido de cache.
* **RNF05 - Ingestão de Dados (Scraping):** O sistema deve possuir scripts automatizados para raspagem e atualização periódica da base de precedentes a partir do portal Pangea ou bases similares.
* **RNF06 - Contêinerização (Docker):** O ambiente de execução do back-end, bancos de dados e serviços auxiliares deve ser totalmente isolado em contêineres Docker.
* **RNF07 - Microsserviços e Versionamento:** O código-fonte deve estar organizado de forma modular utilizando *Git Submodules*, separando responsabilidades (API, Scraper, Mobile, etc.).
* **RNF08 - Pipelines CI/CD:** O projeto deve contar com integração e entrega contínuas para automação de testes e deploys.
* **RNF09 - Usabilidade e Interface (UX/UI):** O aplicativo mobile deve focar na clareza e facilidade de leitura para magistrados e advogados.
* **RNF10 - Documentação Técnica:** O repositório deve manter atualizados o Manual de Instalação, o Manual do Usuário e a documentação das rotas da API.

---

# 📊 Matriz de Rastreabilidade

| ID | User Story | Requisitos funcionais | Requisitos não funcionais |
|:---:|:---|:---|:---|
| **US01** | Extração automatizada da petição | RF02 | RNF01, RNF02, RNF03, RNF04, RNF06, RNF08 |
| **US02** | Precedentes categorizados por aplicabilidade | RF03 | RNF02, RNF04, RNF05, RNF08 |
| **US03** | Síntese comparativa e justificativa | RF04 | RNF02, RNF03, RNF04, RNF08 |
| **US04** | Área de trabalho confidencial | RF01 | RNF03, RNF06 |
| **US05** | Análises recentes na tela de boas-vindas | RF05 | RNF09 |
| **US06** | Documento formal da análise | RF06 | RNF02, RNF03, RNF06, RNF10 |
| **US07** | Busca de precedentes para o advogado | RF07 | RNF02, RNF03, RNF04, RNF05 |
| **US08** | Sugestão estruturada de petição inicial | RF08 | RNF02, RNF03, RNF04 |
| **US09** | Minuta de decisão de 2ª instância | RF11 | RNF02, RNF03, RNF04 |
| **US10** | Classificação dos autos completos | RF10 | RNF02, RNF03, RNF06, RNF08 |
| **US11** | Edição assistida da minuta | RF09 | RNF09, RNF10 |