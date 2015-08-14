Title: Instalando Python 3 na Dreamhost
Date: 2015-08-09
Author: daniloshiga
Tags: python, custom, infra
Slug: instalando-python3-na-dreamhost

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

Nesse ponto chegamos no momento mais específico da Dreamhost, que é o uso do
passenger para aplicações python.

Ele utiliza um arquivo passenger_wsgi.py na raiz do domínio que é usado para
definir o python que será usado pela aplicação e outras informações, ele
depende de uma variável "application" que é a aplicação wsgi que irá rodar.

```python
import sys, os
import logging
cwd = os.getcwd()
sys.path.append(cwd)

INTERP = os.path.expanduser("~/venv/bin/python")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,'$HOME/my_project/my_project')
sys.path.insert(0,'$HOME/venv/bin')
sys.path.insert(0,'$HOME/venv/lib/python3.4/site-packages/django')
sys.path.insert(0,'$HOME/venv/lib/python3.4/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "my_project.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

E pronto, bem mais simples que o caso do python 2.7 e pronto para trabalhar
numa versão mais "evoluída" do python, mesmo que a hospedagem em si ainda não
esteja.


[Deploying Django with virtualenv on Dreamhost]: http://brobin.me/blog/2015/3/22/deploying-django-with-virtualenv-on-dreamhost
