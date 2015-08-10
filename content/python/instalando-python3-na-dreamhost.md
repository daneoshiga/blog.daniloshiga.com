Title: Instalando Python 3 na Dreamhost
Date: 2015-08-09
Author: daniloshiga
Tags: python, custom, infra
Slug: instalando-python3-na-dreamhost
status: draft

Quase um ano depois de [instalar manualmente o python 2.7 e django na
dreamhost]({filename}instalando-python-e-django-na-dreamhost.md), senti que era
hora de tentar fazer o mesmo para o python 3.4.

Hoje, o python padrão das instancias compartilhadas da Dreamhost já é o 2.7,
tornando o post anterior desnecessário, mas já é hora de fazer o máximo de uso
possível do python 3.

Usei como base meu post anterior e este aqui [Deploying Django with virtualenv
on Dreamhost][], que é bem direto e mais simples do que o que eu havia feito no
passado, e pude seguir praticamente linha a linha para conseguir rodar uma
aplicação com python 3 na dreamhost.

Primeiro, é necessário fazer download e extrair o código fonte do python:

```bash
wget http://python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz
tar xvfJ Python-3.4.3.tar.xz 
cd Python-3.4.3
```

Depois disso, compilar e instalar o python (essa etapa vai demorar bastante,
uma opção é fazer tudo dentro de uma screen):

```bash
./configure --prefix=$HOME/python34
make
make install
```

Depois de um bom tempo, as últimas linhas da instalação são especialmente
interessantes:

```
Collecting setuptools
Collecting pip
Installing collected packages: pip, setuptools


Successfully installed pip-6.0.8 setuptools-12.0.5
```

Ou seja, já temos o pip a nossa disposição, podemos checar que estamos usando a
versão instalada no home do usuário.

```bash
$ which python3
/home/foo/python34/bin/python3
$ which pip3
/home/foo/python34/bin/pip3
$ which pyvenv-3.4
/home/foo/python34/bin/pyvenv-3.4
```


[Deploying Django with virtualenv on Dreamhost]: http://brobin.me/blog/2015/3/22/deploying-django-with-virtualenv-on-dreamhost
