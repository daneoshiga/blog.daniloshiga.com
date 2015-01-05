Title: Vantagens ao usar o runserver_plus
Date: 2015-01-05
Author: daniloshiga
Tags: python, django, django-extensions
Slug: vantagens-ao-usar-runserverplus

O runserver_plus é um utilitário que pode te dar um pouco mais de produtividade
quando desenvolvendo usando Django.

![Traceback do runserver_plus](/images/vantagens-ao-usar-runserverplus/runserverplus-traceback.png)

Ele faz parte do pacote django-extensions, que tem vários outros comandos
úteis para o desenvolvimento (como o shell_plus).

Ele faz uso do Werkzeug WSGI, que renderiza uma tela de debug muito mais útil
que a padrão, com a possibilidade de interagir com o traceback.

A mais útil é um terminal python direto no traceback na tela, onde é possível
fazer o debug do que causou a Exception, inspecionar as variáveis e o ambiente
naquele momento e encontrar o problema.

Outra opção é ver o código fonte do arquivo onde aconteceu a Exception,
