# Padronização das branches

Adotamos o padrão [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow),

## Tipos

As 3 branches principais do projeto são:

- `main`: É a branch que contém o código estável e validado que está em produção.

- `hml`: Esta branch contém o código que será validado antes de ir para produção, ela é utilizada para testes funcionais e validação.

- `dev`: Branch dedicada ao desenvolvimento, ela deve receber todas as novas funcionalidades e correções ao longo da sprint. Serve como base para gerar versões que serão enviadas para a homologação.

Além dessas branches principais, os membros da equipe deverão criar branches para desenvolvimento de funcionalidades e correções. Estas branches devem ser criadas baseadas na branch `dev`, podem ser dos seguintes tipos:

- `feat`: Para desenvolvimento de novas funcionalidades.
- `hotfix`: Para correção urgente.
- `fix`: Para correções menores.
- `docs`: Para alterações na documentação.

## Fluxo
O fluxo de desenvolvimento é:

```shell
dev -> feature/fix etc -> dev -> hml -> main 
```

O desenvolvedor deve criar uma branch baseada em `dev` e trabalhar nela. Ao concluir seu trabalho, deverá abrir um *PR* para `dev`.

Em caso de hotfix:

```shell
main -> hotfix -> main

# Nas outras branches principais

hml <- main
dev <- main
```

A branch de `hotfix` deve ser baseada na `main`, logo após sua conclusão, deve-se abrir um *PR* para `main` e após o *merge* é preciso mesclar estas mudanças em `dev` e `hml`.

O **Scrum Master** será o responsável por mesclar as branches e aprovar os *PR*.

## Formato

As branches de desenvolvimento devem seguir o seguinte padrão:

```shell
tipo/task-id-descrição
```

**Exemplo:** `feat/pr-20-nova-funcionalidade`
