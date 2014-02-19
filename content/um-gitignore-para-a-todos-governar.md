Title: Um gitignore para a todos governar
Date: 2012-04-18 16:24
Author: daniloshiga
Category: git
Tags: configuração
Slug: um-gitignore-para-a-todos-governar

Existem certos arquivos que você nunca vai querer no seu repositório,
como por exemplo os arquivos .swp gerados pelo vim.

Uma opção seria adicionar esses arquivos em arquivos.gitignore de todos
os projetos, mas existe uma opção melhor, criar um gitignore global, que
assim como as configurações globais do git, se aplique a todos os seus
repositórios.

Isso pode ser conseguido com um comando:

    git config --global core.excludesfile ~/.gitignore

Pronto, agora só é necessário adicionar as regras dos arquivos que você
não quer em nenhum repositório no arquivo \~/.gitignore
