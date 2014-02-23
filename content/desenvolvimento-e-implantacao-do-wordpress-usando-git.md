Title: Desenvolvimento e Implantação do Wordpress usando Git
Date: 2012-04-11 14:14
Author: daniloshiga
Category: git
Tags: git, implantação, wordpress
Slug: desenvolvimento-e-implantacao-do-wordpress-usando-git

Nesse post vou detalhar a estrutura de desenvolvimento e implantação do
wordpress usando git que estou usando para este blog, onde consigo
enviar mudanças feitas no ambiente de teste para produção usando um
simples "git push prod".

Eu irei detalhar apenas os passos que dei para criar esse ambiente, sem
me aprofundar nos conceitos do git.

Meu objetivo é usar ao máximo as funcionalidades do git para fazer a
implantação do blog, para isso, vou usar um repositório do wordpress
mantido no github, originalmente o código do wordpress é mantido em um
repositório svn, mas felizmente exite um clone no [github][], que é
atualizado de 30 em 30 minutos.

Clonando o repositório do wordpress, selecionando a versão que será
usada e criando um branch de desenvolvimento a partir dela:

    git clone https://github.com/markjaquith/WordPress.git blog.daniloshiga.com
    git checkout origin/3.3-branch
    git checkout -b dev

Adicionando o tema "roots" como um "submódulo falso" (ou seja, sem o uso
dos "submodules") do git.

    cd wp-content/themes
     git clone https://github.com/retlehs/roots.git
     git add roots/

Fiz desse modo para facilitar a implantação, de modo que tanto o
wordpress quanto o tema fiquem no mesmo repositório, sem haver a
necessidade de executar comandos para ativação e uso dos submódulos.

quando ativado, o tema roots gera um .htacess na base da instalação do
wordpress, talvez seja interessante adicionar o .htaccess no .gitignore
para evitar sobrepor o arquivo que será gerado na ativação do tema em
produção com o usado durante o desenvolvimento.

É necessário criar um repositório onde será feita a implantação, o uso
do comando "git init --bare" faz com que o repositório seja criado na
pasta atual, e não criada uma outra pasta .git com ele.

    mkdir blog.git && cd blog.git
    git init --bare

O ponto central da implantação será o uso de um "hook", no caso o
post-receive, que é um script que irá executar quando novos dados forem
recebidos no repositório.

o script é o blog.git/hooks/post-receive

    #!/bin/sh
    LIVE="[caminho para pasta do wordpress em produção]"
    read oldrev newrev refname
     if [ $refname = "refs/heads/dev" ]; then
     echo "===== DEPLOYING TO LIVE SITE ====="
     GIT_WORK_TREE=$LIVE git checkout -f dev
     echo "===== DONE ====="
     fi

Detalhando: ele limita o envio de dados para produção para apenas quando
for um push do branch "dev" dando um checkout no repositório na pasta de
produção, a vantagem de executar um checkout assim é que o repositório
em si não fica nessa pasta, não sendo necessário adicionar alguma regra
no servidor para bloquear o acesso ao repositório.

Feito isso, basta adicionar o repositório

    git remote add prod ssh://[usuario]@[host]/[caminho_repositório]/blog.git
    git push prod +dev:refs/heads/dev

Para a implantação, farei uso do post-receive hook, ou seja, irei
permitir que, ao executar o git push para um repositório remoto (mantido
no servidor de produção) os arquivos sejam colocados na pasta pública
utilizando um checkout.

### Vantagens dessa técnica:

Facilidade na implantação de novidades, e também na reversão das
mudanças caso necessário.

A pasta .git não fica na pasta pública, não sendo necessário assim
retirar o acesso a ela através do .htaccess.

O uso do submódulo falso simplifica a implantação, evitando a
necessidade de usar os comandos "git submodule init" e "git submodule
update" para conseguir obter os submódulos, adicionando-os diretamente
dentro do repositório faz com que um único checkout já os traga também.

### Desvantagens:

As alterações que forem realizadas em desenvolvimento relacionadas a
ativação e configuração de temas e plugins vão precisar ser reaplicadas
no servidor de produção, já que cada ambiente está usando um banco
separado, tornando o controle das alterações complicado nesse sentido.

### Referências:

<http://www.saintsjd.com/2011/03/automated-deployment-of-wordpress-using-git/>
(parte da solução, só que usa git pull)  
<http://webxl.net/2011/03/10/managing-wordpress-with-git/> (solução
usando checkout)  

[http://clintberry.com/2011/speed-up-your-wordpress-development-cycle-with-git/  
][]<http://debuggable.com/posts/git-fake-submodules:4b563ee4-f3cc-4061-967e-0e48cbdd56cb>

  [github]: https://github.com/markjaquith/WordPress
  [http://clintberry.com/2011/speed-up-your-wordpress-development-cycle-with-git/  
 ]: http://clintberry.com/2011/speed-up-your-wordpress-development-cycle-with-git/
