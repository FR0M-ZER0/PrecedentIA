# ⚖️ Análise de Precedentes Jurídicos - Xertica

Este projeto é uma aplicação móvel integrada à nuvem que utiliza técnicas de Inteligência Artificial para analisar petições iniciais, gerar resumos e retornar os precedentes jurídicos mais adequados da base nacional (como o Pangea). O objetivo é reduzir o tempo de pesquisa e aumentar a precisão da tomada de decisão jurídica.

---

## 🎯 Requisitos Funcionais (O que o sistema faz)

* **RF01 - Autenticação e Perfil:** O sistema deve permitir que o juiz faça login (via e-mail/senha ou Google) e gerencie os dados de sua conta com segurança.
* **RF02 - Processamento de Petições:** O sistema deve receber arquivos de petições (PDF/DOCX), extrair seus dados principais e buscar no banco de dados os precedentes mais aplicáveis ao caso.
* **RF03 - Geração de Síntese (IA):** O sistema deve gerar um texto explicativo que relacione a petição enviada com os precedentes sugeridos, servindo apenas como material de apoio à decisão do juiz.
* **RF04 - Histórico e Pastas:** O sistema deve salvar as análises feitas pelo usuário, permitindo que ele dê nomes aos relatórios e os organize em pastas.
* **RF05 - Tela Inicial (Dashboard):** O sistema deve ter uma página inicial que exiba atalhos rápidos para as 5 últimas análises feitas pelo juiz.
* **RF06 - Exportação em PDF:** O sistema deve permitir que o juiz baixe a análise completa (resumo, precedentes e síntese) em um documento PDF.

---

## ⚙️ Requisitos Não Funcionais (Como o sistema deve ser construído)

* **RNF01 - API em FastAPI:** O back-end principal que atende o aplicativo deve ser construído em Python usando o framework FastAPI.
* **RNF02 - Manual de Instalação:** O repositório deve conter um guia passo a passo de como instalar e rodar o projeto.
* **RNF03 - Manual do Usuário:** O sistema deve ter um documento ensinando os juízes a usarem o aplicativo.
* **RNF04 - Banco Vetorial e Cache:** O sistema usará o Qdrant para armazenar os dados de inteligência artificial e o Redis para gerenciamento rápido de cache.
* **RNF05 - Docker:** Toda a aplicação (bancos, IA e API) deve rodar dentro de contêineres Docker para facilitar a execução em qualquer máquina.
* **RNF06 - Pipeline CI:** O código deve ter testes automáticos rodando a cada nova atualização.
* **RNF07 - Pipeline CD:** O sistema deve ter deploy automatizado na nuvem.
* **RNF08 - Separação de Pipelines:** A arquitetura deve separar a rotina pesada de coleta de dados da rotina rápida que responde ao celular do juiz.
* **RNF09 - Usabilidade (UX):** A interface deve ser fácil de usar, com design limpo e focado no trabalho do juiz.
* **RNF10 - Segurança e LGPD:** Os dados processados devem trafegar de forma segura, respeitando a lei de proteção de dados.
* **RNF11 - Configuração de Repositórios:** O código-fonte deve ser versionado no GitHub de forma organizada.
* **RNF12 - Ingestão Automática (Scraping):** O sistema deve ter um robô (usando Playwright) que atualiza a base de precedentes buscando dados do Pangea a cada 14 dias.
* **RNF13 - Motor de IA Local:** O sistema usará Sentence-Transformers para a busca inteligente de textos e o Ollama (modelo Qwen2.5) para gerar as sínteses explicativas.