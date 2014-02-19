Title: Erro do dia: chmod *
Date: 2012-08-24 06:26
Author: daniloshiga
Category: erro
Tags: erro
Slug: erro-do-dia-chmod

Chmod é um comando delicado, e executá-lo as pressas sem muita atenção e
com sono pode gerar alguns problemas.

O comando "chmod 600" muda as permissões de um arquivo para que apenas o
dono dele tenha acesso, barranco qualquer tipo de acesso de outros
usuários, o problema é que executei esse comando assim:

`sudo chmod 600 *`

Fiz isso dentro da home, em um primeiro momento pode-se até pensar que
isso não geraria problemas mais graves, até aumentaria a segurança do
sistema, o problema é que diretórios precisam de permissão de execussão
para que você possa lista-los, logo, fiquei sem acesso a nenhuma das
pastas da minha home, assim como os programas que estava usando no
momento.

A solução para o problema foi, primeiro voltar a permissão dos arquivos
para algo mais comum:

`sudo chmod 644`

Depois mudar as dos diretórios, para isso, executei um find no home,
buscando apenas pelo primeiro nível de profundidade (apenas os arquivos
presentes no mesmo diretório), usando "-type d" para atingir apenas os
diretórios, e finalmente usando o -exec neles, com o chmod com as
permissões corretas (incluindo execução), usando o "+" no exec porque
não há problemas em passar várias pastas como parâmetro do chmod.

`sudo find . -maxdepth 1 -type d -exec chmod 755 {} +`

Resultado, tudo de volta ao normal, e um lembrete para se tomar cuidado
com o chmod.
