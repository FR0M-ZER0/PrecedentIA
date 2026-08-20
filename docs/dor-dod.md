# ⚖️ Backlog de User Stories - Sistema de Apoio Jurídico

Este documento detalha as **User Stories** (Histórias de Usuário) atualizadas, incluindo seus respectivos critérios de prontidão (**DoR**) e de conclusão (**DoD**).

---

## 📋 Definições de Qualidade

### **Definition of Ready (DoR)**
*A história só será iniciada se atender aos seguintes pontos:*
- [ ] Regras de negócio detalhadas.
- [ ] Dados, tipos e validações definidos.
- [ ] Mensagens de sistema (erro/sucesso/aviso) mapeadas.
- [ ] Esboço da interface (UX/UI) criado.

### **Definition of Done (DoD)**
*A história só será considerada entregue se:*
- [ ] Código revisado (**Code Review**).
- [ ] **Pull Request** aprovado por 2 membros na branch principal.
- [ ] **Testes de regressão** executados sem falhas.
- [ ] Manuais de usuário/instalação atualizados (conforme exigido pela US).

---

## 🚀 User Stories (Backlog)

### US01 - Extração Automatizada
> **Título:** Como Juiz, desejo submeter o arquivo de uma petição inicial para extrair os pontos principais do processo de forma automatizada.
- **Requisitos:** RF02, RNF01, RNF02, RNF03, RNF04, RNF06, RNF08
- **Entrega Obrigatória:** Código + Manual de Usuário + Manual de Instalação.

### US02 - Categorização de Precedentes
> **Título:** Como Juiz, desejo visualizar precedentes jurídicos categorizados pelo seu nível de aplicabilidade ao caso, para agilizar a fundamentação da minha decisão.
- **Requisitos:** RF03, RNF02, RNF04, RNF05, RNF08

### US03 - Síntese Explicativa
> **Título:** Como Juiz, desejo ler uma síntese explicativa que compare a petição aos precedentes listados, para compreender a justificativa da recomendação da ferramenta antes de tomar minha decisão.
- **Requisitos:** RF04, RNF02, RNF03, RNF04, RNF08

### US04 - Área Confidencial
> **Título:** Como Juiz, desejo acessar uma área de trabalho confidencial e individualizada, para garantir o sigilo absoluto das informações processuais que estou analisando.
- **Requisitos:** RF01, RNF03, RNF06

### US05 - Histórico na Tela Inicial
> **Título:** Como Juiz, desejo visualizar minhas análises mais recentes logo na tela de boas-vindas, para retomar meu trabalho rapidamente de onde parei.
- **Requisitos:** RF05, RNF09

### US06 - Emissão de Documento Formal
> **Título:** Como Juiz, desejo emitir um documento formal com o resultado da análise e os precedentes selecionados, para anexá-lo como material de apoio aos autos do processo judicial.
- **Requisitos:** RF06, RNF02, RNF03, RNF06
- **Entrega Obrigatória:** Código + Manual de Usuário + Manual de Instalação.

### US07 - Busca e Ranqueamento para Advogados
> **Título:** Como Advogado, desejo inserir a descrição e os documentos de um caso para que o sistema identifique a matéria e busque precedentes aplicáveis ranqueados por relevância e hierarquia.
- **Requisitos:** RF07, RNF02, RNF03, RNF04, RNF05
- **Entrega Obrigatória:** Código + Manual de Usuário + Manual de Instalação.

### US08 - Sugestão de Petição Inicial
> **Título:** Como Advogado, desejo que o sistema gere uma sugestão de petição inicial estruturada (fatos, fundamentos, pedidos e citações), para reduzir meu tempo de elaboração.
- **Requisitos:** RF08, RNF02, RNF03, RNF04

### US09 - Minuta de Decisão de 2ª Instância
> **Título:** Como Julgador (2ª Instância), desejo que o sistema gere uma minuta de decisão (com relatório, fundamentação e dispositivo) baseada nos precedentes do tribunal, sinalizando eventuais ausências de teses fortes.
- **Requisitos:** RF11, RNF02, RNF03, RNF04

### US10 - Classificação de Autos Completos
> **Título:** Como Julgador (2ª Instância), desejo submeter os autos completos (PDF) para que o sistema classifique as peças processuais e extraia o contexto da inicial.
- **Requisitos:** RF10, RNF02, RNF03, RNF06, RNF08

### US11 - Edição Assistida
> **Título:** Como Advogado, desejo um ambiente de edição assistida para a minuta gerada, permitindo refinar a tese central e trocar os precedentes sugeridos.
- **Requisitos:** RF09, RNF09, RNF10

---

## 📊 Matriz de Rastreabilidade

| ID | Título Resumido | RF | RNF |
|:---:|:--- |:---:|:--- |
| **US01** | Extração de Petição | RF02 | RNF01, 02, 03, 04, 06, 08 |
| **US02** | Visualização de Precedentes | RF03 | RNF02, 04, 05, 08 |
| **US03** | Síntese e Justificativa | RF04 | RNF02, 03, 04, 08 |
| **US04** | Sigilo e Confidencialidade | RF01 | RNF03, 06 |
| **US05** | Boas-vindas e Recentes | RF05 | RNF09 |
| **US06** | Exportação de Relatório | RF06 | RNF02, 03, 06, 10 |
| **US07** | Precedentes para Advogados | RF07 | RNF02, 03, 04, 05 |
| **US08** | Sugestão de Petição Inicial | RF08 | RNF02, 03, 04 |
| **US09** | Minuta de Decisão Judicial | RF11 | RNF02, 03, 04 |
| **US10** | Classificação de Autos Completos | RF10 | RNF02, 03, 06, 08 |
| **US11** | Edição Assistida | RF09 | RNF09, 10 |