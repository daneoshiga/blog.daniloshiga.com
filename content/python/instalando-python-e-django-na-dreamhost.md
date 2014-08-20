Title: Instalando Python e Django na Dreamhost
Date:
Author: daniloshiga
Tags: python, custom, infra
Slug: instalando-python-e-django-na-dreamhost

Os shared-hosts já foram a melhor opção de hospedagem barata e funcional que se
tinha, porém a cada dia opções de VPS e de [IaaS][] mais baratas aparecem, e os
shared-hosts e suas limitações são deixados para trás.

Um dos pontos negativos é a versão

    wget http://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz --no-check-certificate
    tar xzvf Python-2.7.8.tgz
    cd Python-2.7.8
    ./configure --enable-shared --prefix=$HOME/opt/python-2.7.8
    make && make install

    mkdir opt/python-2.7.8/local
    wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz --no-check-certificate
    tar -xzf virtualenv-1.9.1.tar.gz
    cd virtualenv-1.9.1
    python virtualenv.py /home/example/opt/python-2.7.8/local/
    easy_install virtualenv
    source ~/opt/python-2.7.8/local/bin/activate
    easy_install virtualenv

    wget http://www.doughellmann.com/downloads/virtualenvwrapper-2.6.1.tar.gz --no-check-certificate
    tar -xzf virtualenvwrapper-2.6.1.tar.gz
    cd virtualenvwrapper-2.6.1
    python setup.py install
    cp virtualenvwrapper.sh ~/opt/python-2.7.8/
    mdkir ~/.virtualenvs

.profile

    export PATH=$HOME/opt/python-2.7.8/local/bin:$HOME/opt/python-2.7.8/bin:$PATH
    export PYTHONPATH=$HOME/opt/python-2.7.8/local/lib/python2.7/site-packages:$PYTHONPATH
    export LD_LIBRARY_PATH=$HOME/opt/python-2.7.8/lib/
    export WORKON_HOME=$HOME/.virtualenvs
    source $HOME/opt/python-2.7.8/virtualenvwrapper.sh

passenger_wsgi.py

    import sys, os

    # Switch to the virtualenv if we're not already there
    INTERP = os.path.expanduser("~/.virtualenvs/example/bin/python")
    if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

    PROJECT_ROOT = '/home/example/example'

    sys.path.insert(0, PROJECT_ROOT + '/example/')
    sys.path.insert(0,
    '/home/example/.virtualenvs/example/lib/python2.7/site-packages')
    os.environ['DJANGO_SETTINGS_MODULE'] = "example.settings.dreamhost"
    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()

[IaaS]: http://en.wikipedia.org/wiki/Infrastructure_as_a_service#Infrastructure_as_a_service_.28IaaS.29
