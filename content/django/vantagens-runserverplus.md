Title: Vantagens ao usar o runserver_plus
Date: 2015-01-07
Author: daniloshiga
Tags: python, django, django-extensions
Slug: vantagens-ao-usar-runserverplus

O runserver_plus é um utilitário que pode te dar um pouco mais de produtividade
quando desenvolvendo usando Django, faz parte do pacote django-extensions que
tem vários outros comandos úteis para o desenvolvimento (como o shell_plus) e
faz uso do [Werkzeug][], é simples instalá-lo via pip.


```bash
pip install django-extensions
pip install Werkzeug
```

E adicioná-lo nas INSTALLED_APPS do django:

```python
INSTALLED_APPS += (
        'django_extensions',
) 
```
A partir daí` as telas d` erro do Django ficaram assim:

![Traceback do runserver_plus](/images/django/vantagens-ao-usar-runserverplus/runserverplus-traceback.png)

A mais útil é um terminal python direto no traceback na tela, onde é possível
fazer o debug do que causou a Exception, inspecionar as variáveis e o ambiente
naquele momento e encontrar o problema.

![Terminal integrado](/images/django/vantagens-ao-usar-runserverplus/runserverplus-interactive.png)

Outra opção é ver o código fonte do arquivo onde aconteceu a Exception, talvez
seu arquivo de view já esteja aberto no editor, mas como é possível visualizar
isso do traceback inteiro, você pode ter mais informações do fonte do próprio
Django

![Código Fonte](/images/django/vantagens-ao-usar-runserverplus/runserverplus-viewsource.png)

E também é possível ver os comandos SQL gerados durante uma requisição passando
o parametro "`--print-sql`" para o runserver_plus, que pode ser muito útil para
visualizar o que o ORM do django está gerando, e encontrar locais onde o acesso
ao banco pode estar gerando problemas.

![Código Fonte](/images/django/vantagens-ao-usar-runserverplus/runserverplus-printsql.png)

Essas são algumas vantagens que que o runserver_plus pode oferecer, são
pequenos ganhos que ajudam na produtividade com Django.

[Werkzeug]: http://werkzeug.pocoo.org/ 
