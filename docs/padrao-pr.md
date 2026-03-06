# Padronização dos PRs

## Título

O título da *PR* deve ser curto e conciso. Ele deve ser prefixado com o ID da task e deve iniciar com um verbo no **imperativo** (Exemplo: *adiciona* e não *adicionado*/*adicionei*).

**Exemplo:** `[pr-20]: Adiciona nova funcionalidade`

## Formato

O *Pull Request* deve estar formatado no seguinte padrão:

### Descrição

Deve conter uma breve descrição das mudanças introduzidar por este *PR*.

**Exemplo:** Este pull request adiciona a autenticação do usuário no sistema.

### Motivação

Deve conter a razão pela mudança e qual problema ele resolve.

**Exemplo:** Anteriormente, o sistema estava aberto para qualquer usuário, o que permitia o acesso ao qualquer dado, até mesmo os privados.

### Mudanças

Aqui deve ter uma lista das mudanças feitas no código.

**Exemplo:** 
- Adicionado funcionalidade de token de refresh e de acesso
- Adicionado middleware para proteger rotas
- Adicionado endpoint para sign-in e sign-out

### Testando

Aqui deve haver os passos necessários para testar a mudança.

**Exemplo:**
1. Faça uma requisição para `/customer/123`
2. Verifique se a API retorna um erro `401`
3. Agora faça uma requsição para `/sign-in/` com os dados do usuário padrão
4. Tente acessar novamente `/customer/123` e verifique se os dados são retornados corretamente

### Link da task

Por fim, será necessário colocar o link da task ao qual o *PR* faz referência

**Exemplo:** https://tasks.com/pr-20
