Title: Problemas com pip freeze > requirements.txt
Date: 2014-11-16
Author: daniloshiga
Tags: python, virtualenv
Slug: problemas-com-pip-freeze-requirements

Em muitos tutoriais é comum encontrar o comando `pip freeze > requirements.txt`
como exemplo de como guardar os requisitos de um projeto.

usar o requirements é uma boa prática e deve ser sempre seguida, porém o
problema é quando ela é mal executada, podendo gerar mais problemas do que
ajudar dependendo da situação.

Por exemplo, tenho um [projeto][] que usa o [Markdoc][] para gerar uma wiki
simples a partir de arquivos markdown, e tinha feito, a um bom tempo, o arquivo
de requirements usando o pip freeze... gerando um arquivo assim:

    CherryPy==3.2.2
    Jinja2==2.6
    Markdoc==0.6.6
    Markdown==2.2.1
    PyYAML==3.10
    Pygments==1.5
    WebOb==1.2.3
    argparse==1.2.1
    wsgiref==0.1.2

Onde todas as dependências do Markdoc foram parar no requirements, no momento
tudo pareceu estar bem, porém, 2 anos depois, tentando regerar o virtualenv, me
deparo com o erro a seguir:

    :::bash
    $ pip install -r requirements.txt
    Downloading/unpacking CherryPy==3.2.2 (from -r requirements.txt (line 1))
      Could not find a version that satisfies the requirement CherryPy==3.2.2 (from
      -r requirements.txt (line 1)) (from versions: 3.2.6, 3.4.0, 2.1.1, 2.2.0beta,
      3.2.3, 3.2.4, 3.2.4, 3.2.5, 3.2.5, 3.2.6, 3.2.6, 3.3.0, 3.3.0, 3.4.0, 3.4.0,
      3.5.0, 3.5.0, 3.6.0, 3.6.0)
        Some externally hosted files were ignored (use --allow-external to allow).
        Cleaning up...
        No distributions matching the version for CherryPy==3.2.2 (from -r
        requirements.txt (line 1))
        Storing debug log for failure in ~/.pip/pip.log

Ou seja, a versão do CherryPy na época da criação do projeto não está mais
disponível no [PyPI][], porém não é do CherryPy que eu preciso, e sim do
Markdoc, então, ignorei o requirements e instalei o Markdoc diretamente.

    :::bash 
    $ pip install Markdoc

E a instalação ocorreu normalmente, olhando o pip freeze, é possível notar que
várias dependências do Markdoc foram atualizadas, mas o Markdoc em si continua
na mesma versão:

    CherryPy==3.6.0
    Jinja2==2.7.3
    Markdoc==0.6.6
    Markdown==2.5.1
    MarkupSafe==0.23
    PyYAML==3.11
    Pygments==2.0.1
    WebOb==1.4
    argparse==1.2.1
    wsgiref==0.1.2

Então, atualizei o requirements para ter apenas o Markdoc, o que vai evitar
qualquer problema desse tipo no futuro.

Como o projeto é muito simples foi fácil encontrar o problema e corrigir, mas
se houvessem várias dependências ou dependências compartilhadas poderia ter
sido bem mais complicado de se resolver.

[projeto]: https://github.com/daneoshiga/wikishiga
[Markdoc]: http://markdoc.org/
[PyPI]: https://pypi.python.org/pypi/CherryPy
