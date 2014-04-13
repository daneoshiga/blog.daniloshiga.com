Title: UserDir vs. VirtualHost
Date: 2012-04-14 10:28
Author: daniloshiga
Tags: apache
Slug: userdir-vs-virtualhost

Durante a preparação de um ambiente de teste me deparei com duas opções,
ativar o módulo UserDir do apache para acessar uma pasta do meu home
usando um endereço como "http://localhost/\~usuario" ou setar um
VirtualHost apontando para a pasta onde estava colocando o projeto.

### Usando UserDir:

    cd /etc/apache2/mods-enabled
    sudo ln -s ../mods-available/userdir.conf userdir.conf
    sudo ln -s ../mods-available/userdir.load userdir.load

Depois disso, reinicie o apache

    sudo /etc/init.d/apache2 restart

Por default, o userdir.conf aponta para a pasta "public\_html" mas você
pode alterar isso no userdir.conf (como eu já tinha uma pasta para os
projetos, foi isso que eu fiz, para não precisar alterar as coisas)

Uma observação, se for fazer uso de arquivos .htaccess, é interessante
alterar a configuração do AllowOverride, se estiver com preguiça (como
eu) permitir tudo pode resolver um erro 500. (que foi o erro que
encontrei quando ativei o tema roots do wordpress nesse cenário).

    AllowOverride All

### VirtualHost

No caso de uso de VirtualHosts, é necessário criar um arquivo com o nome
que você quiser dentro de /etc/apache2/sites-available/

    :::apache
    <VirtualHost *>
         ServerName projetos.local
         DocumentRoot /home/daniloshiga/projetos

         <Directory /home/daniloshiga/projetos>
             DirectoryIndex index.php
             AllowOverride All
             Order allow,deny
             Allow from all
         </Directory>
    </VirtualHost>

Com o arquivo criado, é necessário ativá-lo no apache (o que irá gerar
uma cópia dele na pasta sites-enabled):

    sudo a2ensite projetos.local

E adicionar uma linha ao arquivo /etc/hosts para que ao acessar o
endereço do virtual host, o linux saber que pra qual IP direcionar a
requisição (no caso, localhost):

    127.0.0.1 projeto.local

E finalmente, reiniciar o apache:

    sudo /etc/init.d/apache2 restart

é isso, no caso do VirtualHost também é possível criar um endereço
específico para cada site em desenvolvimento, mas talvez seja algo que
gere muito trabalho sem muitas vantagens, por enquanto estou utilizando
a solução do UserDir.

Fontes:

[How to Create Multiple Virtual Hosts in Ubuntu](http://codingpad.maryspad.com/2012/03/14/how-to-create-multiple-virtual-hosts-in-ubuntu/)
