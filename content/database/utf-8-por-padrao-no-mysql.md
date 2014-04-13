Title: UTF-8 por padrão no MySQL
Date: 2012-09-13 00:29
Author: daniloshiga
Tags: mysql, charset
Slug: utf-8-por-padrao-no-mysql

Para que o mysql use UTF-8 por padrão, é necessário adicionar duas
linhas no /etc/mysql/my.cnf (no caso do ubuntu)

    [mysqld] 
    character-set-server=utf8 
    collation-server=utf8_general_ci

Depois disso e de reiniciar o mysql (sudo restart mysql), é possível
verificar se deu certo com a query:

    show variables like "%character%";show variables like "%collation%";

Se tiver dado certo, a coluna Value estará apenas com valores
relacionados ao UTF-8
