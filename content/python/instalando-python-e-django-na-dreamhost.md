Title: Instalando Python e Django na Dreamhost
Date: 2014-08-21
Author: daniloshiga
Tags: python, custom, infra
Slug: instalando-python-e-django-na-dreamhost

Os shared-hosts já foram a melhor opção de hospedagem barata e funcional que se
tinha, porém a cada dia opções de VPS e de [IaaS][] mais baratas aparecem, e os
shared-hosts e suas limitações são deixados para trás.

Um dos pontos negativos é a versão do python disponível, atualmente a dreamhost
oferece a versão 2.6.6, o que obviamente não é o ideal, a última versão de cada
ciclo (2.7 e 3.3) seria a melhor escolha.

No meu caso, instalei a versão 2.7 que é a que estou usando em um projeto, aqui
o passo a passo do que fiz, que poderia facilmente ser transformado em um bash
script [como já foi feito em alguns lugares][], mas como eu só precisava do
python, virtualenv e virtualenvwrapper, resolvi fazer manualmente.

Para instalar o python:

```bash
wget http://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz --no-check-certificate
tar xzvf Python-2.7.8.tgz
cd Python-2.7.8
./configure --enable-shared --prefix=$HOME/opt/python-2.7.8
make && make install
```


O mais importante ali é a definição de um "prefix" no .configure, que permite
instalar o python em uma pasta dentro do home do usuário.

Depois, o virtualenv:

```bash
mkdir opt/python-2.7.8/local
wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz --no-check-certificate
tar -xzf virtualenv-1.9.1.tar.gz
cd virtualenv-1.9.1
python virtualenv.py /home/user/opt/python-2.7.8/local/
easy_install virtualenv
source ~/opt/python-2.7.8/local/bin/activate
easy_install virtualenv
```

E finalmente o virtualenvwrapper:

```bash
wget http://www.doughellmann.com/downloads/virtualenvwrapper-2.6.1.tar.gz --no-check-certificate
tar -xzf virtualenvwrapper-2.6.1.tar.gz
cd virtualenvwrapper-2.6.1
python setup.py install
cp virtualenvwrapper.sh ~/opt/python-2.7.8/
mdkir ~/.virtualenvs
```

Para que tudo isso funcione, é necessário complementar e adicionar algumas
variáveis de ambiente e ativar o virtualenvwrapper, isso pode ser feito a
partir do .profile ou do .bashrc

.profile

```bash
export PATH=$HOME/opt/python-2.7.8/local/bin:$HOME/opt/python-2.7.8/bin:$PATH
export PYTHONPATH=$HOME/opt/python-2.7.8/local/lib/python2.7/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$HOME/opt/python-2.7.8/lib/
export WORKON_HOME=$HOME/.virtualenvs
source $HOME/opt/python-2.7.8/virtualenvwrapper.sh
```

Agora considerando um projeto usando Django, a dreamhost usa o [passenger][]
para executar aplicações em python, e um arquivo passenger_wsgi.py é necessário
na raiz da pasta para a qual o domínio está apontando para fazer o passenger
encontrar a aplicação.

Essa deve ser provavelmente a parte mais complicada do processo, porque existe
pouca ou nenhuma documentação de como é o modo correto de criar este arquivo.

Os pontos importantes dele são:

- Definir na variável INTERP o caminho para o executável do python a ser
  usável, de preferência sendo o do virtualenv criado para o projeto

- Adicionar no path todos os caminhos pertinentes ao projeto, através do
  sys.path.insert, que atualiza o path adicionando novos valores no começo do
  mesmo.

- Adicionar qualquer variável de ambiente necessária para o sistema no ambiente
  através do os.environ, no caso, estou setando o arquivo settings a ser usado
  pelo projeto.

- A criação da variável "application" que vai ser usada pelo passenger para
  rodar a aplicação.

passenger_wsgi.py

```python
import sys, os

# Switch to the virtualenv if we're not already there
INTERP = os.path.expanduser("~/.virtualenvs/python/bin/python")
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

PROJECT_ROOT = '/home/user/example'

sys.path.insert(0, PROJECT_ROOT + '/example/')
sys.path.insert(0, '/home/user/.virtualenvs/example/lib/python2.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = "example.settings.dreamhost"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
```

E por último, na dreamhost a pasta "public" deve ser usada para servir os
arquivos estáticos da aplicação, nesse caso, é necessário definir o STATIC_ROOT
e MEDIA_ROOT em pastas dentro do public, e os STATIC_URL e MEDIA_URL
considerando o caminho a partir da public.

settings/dreamhost.py
```python
STATIC_ROOT = os.path.join(HOME_DIR, 'example.daniloshiga.com', 'public', 'static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(HOME_DIR, 'example.daniloshiga.com', 'public', 'media')

MEDIA_URL = '/media/'
```


Do modo que está acima, essas pastas vão ficar em
/home/user/example/example.daniloshiga.com/public/static e /public/media, mas a
URL delas é apenas /static e /media.

Depois disso, para reiniciar o passenger toda vez que houver uma novidade no
projeto, é necessário alterar a data de modificação de um arquivo restart.txt
dentro da pasta tmp/ do domínio, por exemplo, através do comando:

```bash
touch ~/example.daniloshiga.com/tmp/restart.txt
```

Se isso não for suficiente, ainda é possível matar os processor do python que
estiverem rodando, usando o comando `pkil python`.

E é isso, foi um processo um pouco trabalhoso, mas tem a vantagem de dar mais
liberdade em um ambiente limitado, o que permite aproveitar algumas vantagens
de uma hospedagem como a [dreamhost][]

[IaaS]: http://en.wikipedia.org/wiki/Infrastructure_as_a_service#Infrastructure_as_a_service_.28IaaS.29
[como já foi feito em alguns lugares]: https://github.com/tmslnz/Dreamhost-Custom-Env
[dreamhost]: http://www.dreamhost.com/r.cgi?1117908
[passenger]: http://wiki.dreamhost.com/Passenger
