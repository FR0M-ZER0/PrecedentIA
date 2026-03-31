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
- **Requisitos:** RF02, RNF01, RNF04, RNF08, RNF11, RNF13
- **Entrega Obrigatória:** Código + Manual de Usuário + Manual de Instalação.

### US02 - Categorização de Precedentes
> **Título:** Como Juiz, desejo visualizar precedentes jurídicos categorizados pelo seu nível de aplicabilidade ao caso, para agilizar a fundamentação da minha decisão.
- **Requisitos:** RF02, RNF04, RNF05, RNF12, RNF13

### US03 - Síntese Explicativa
> **Título:** Como Juiz, desejo ler uma síntese explicativa que compare a petição aos precedentes listados, para compreender a justificativa da recomendação da ferramenta antes de tomar minha decisão.
- **Requisitos:** RF03, RNF01, RNF13

### US04 - Área Confidencial
> **Título:** Como Juiz, desejo acessar uma área de trabalho confidencial e individualizada, para garantir o sigilo absoluto das informações processuais que estou analisando.
- **Requisitos:** RF01, RNF10

### US05 - Organização de Relatórios
> **Título:** Como Juiz, desejo organizar os relatórios de casos que já analisei em pastas personalizadas, para consultar rapidamente estudos anteriores em processos futuros.
- **Requisitos:** RF04, RNF06, RNF07

### US06 - Histórico na Tela Inicial
> **Título:** Como Juiz, desejo visualizar minhas análises mais recentes logo na tela de boas-vindas, para retomar meu trabalho rapidamente de onde parei.
- **Requisitos:** RF05, RNF09
- **Entrega Obrigatória:** Código + Manual de Usuário + Manual de Instalação.

### US07 - Emissão de Documento Formal
> **Título:** Como Juiz, desejo emitir um documento formal com o resultado da análise e os precedentes selecionados, para anexá-lo como material de apoio aos autos do processo judicial.
- **Requisitos:** RF06, RNF02, RNF03
- **Entrega Obrigatória:** Código + Manual de Usuário + Manual de Instalação.

---

## 📊 Matriz de Rastreabilidade

| ID | Título Resumido | RF | RNF |
|:---:|:--- |:---:|:--- |
| **US01** | Extração de Petição | RF02 | RNF01, 04, 08, 11, 13 |
| **US02** | Visualização de Precedentes | RF02 | RNF04, 05, 12, 13 |
| **US03** | Síntese e Justificativa | RF03 | RNF01, 13 |
| **US04** | Sigilo e Confidencialidade | RF01 | RNF10 |
| **US05** | Pastas Personalizadas | RF04 | RNF06, 07 |
| **US06** | Boas-vindas e Recentes | RF05 | RNF09 |
| **US07** | Exportação de Relatório | RF06 | RNF02, 03 |