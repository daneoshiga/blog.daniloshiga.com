Title: Escrita na HD, noatime, nodiratime
Date: 2013-11-19 12:45
Author: daniloshiga
Category: linux
Tags: mount, performance
Slug: escrita-na-hd-noatime-nodiratime

Um grande gargalo de performance é sempre a escrita em disco, existe uma
mudança no /etc/fstab que pode melhorar um pouco a performance do
sistema.

No caso, é necessário adicionar o "noatime" e "nodiratime" nas options
de montagem, no meu caso, adicionei tanto no / como no /home

 

> UUID=3fbf7e07-a761-4780-8e08-b7a5a9b9322d / ext4
> noatime,nodiratime,errors=remount-ro 0 1
>
> UUID=55960f8a-716a-475f-9b52-180d1df7aaa7 /home ext4
> noatime,nodiratime,defaults 0 2

De acordo com o manual do mount, esse é o significado dessas
configurações:

 

> **noatime**
>
> Do not update inode access times on this filesystem (e.g., for faster
> access on the news spool to speed up news servers).

 

> **nodiratime**  
>  Do not update directory inode access times on this filesystem.

Resumindo, você perde a informação de "quando foi a última vez que o
arquivo/pasta foram acessados", que eu não sei exatamente quais partes
do sistema utilizam, mas não tem me feito falta nos últimos meses.

Não fiz nenhum benchmark, porém a lógica está a favor de alguma melhora
de performance durante a leitura na HD (ou seja, ler um arquivo não
envolve mais realizar uma escrita). O que provavelmente só vai ser
notável em um processo de leitura de muitos arquivos.
