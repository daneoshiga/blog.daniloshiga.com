Title: Instalando Python e Django na Dreamhost
Date: 
Author: daniloshiga
Tags: python, custom, infra
Slug: instalando-python-e-django-na-dreamhost

wget http://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz --no-check-certificate
tar xzvf Python-2.7.8.tgz
cd Python-2.7.8
./configure --enable-shared --prefix=$HOME/opt/python-2.7.8
make && make install

mkdir opt/python-2.7.8/local
wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz --no-check-certificate
tar -xzf virtualenv-1.9.1.tar.gz
cd virtualenv-1.9.1
python virtualenv.py /home/premiumgrafica/opt/python-2.7.8/local/
easy_install virtualenv
source ~/opt/python-2.7.8/local/bin/activate
easy_install virtualenv

wget http://www.doughellmann.com/downloads/virtualenvwrapper-2.6.1.tar.gz --no-check-certificate
tar -xzf virtualenvwrapper-2.6.1.tar.gz
cd virtualenvwrapper-2.6.1
python setup.py install
cp virtualenvwrapper.sh ~/opt/python-2.7.8/
mdkir ~/.virtualenvs
mkdir ~/.virtualenvs

.profile
export PATH=$HOME/opt/python-2.7.8/local/bin:$HOME/opt/python-2.7.8/bin:$PATH
export PYTHONPATH=$HOME/opt/python-2.7.8/local/lib/python2.7/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$HOME/opt/python-2.7.8/lib/
export WORKON_HOME=$HOME/.virtualenvs
source $HOME/opt/python-2.7.8/virtualenvwrapper.sh
