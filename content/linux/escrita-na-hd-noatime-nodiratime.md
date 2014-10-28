Title: Escrita na HD, noatime, nodiratime
Date: 2013-11-19 12:45
Author: daniloshiga
Tags: mount, performance
Slug: escrita-na-hd-noatime-nodiratime

Um grande gargalo de performance é sempre a escrita em disco, existe uma
mudança no /etc/fstab que pode melhorar um pouco a performance do
sistema.

No caso, é necessário adicionar o "noatime" ou "nodiratime" nas options
de montagem, no meu caso, adicionei tanto no / como no /home

 

    UUID=3fbf7e07-a761-4780-8e08-b7a5a9b9322d / ext4 noatime,errors=remount-ro 0 1
    UUID=55960f8a-716a-475f-9b52-180d1df7aaa7 /home ext4 noatime,defaults 0 2

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

EDIT
====

Como apontado pelo [Douglas][] nos comentários, o noatime já implica o
nodiratime, então se for feito o uso do primeiro, não é necessário usar o
segundo, pesquisei um pouco e encontrei [o motivo][], onde, se o noatime
estiver sendo usado, o código nem mesmo checa pelo nodiratime:

    void touch_atime(struct vfsmount *mnt, struct dentry *dentry)
    {
            /* ... */
            if (inode->i_flags & S_NOATIME)
                    return;
            if (IS_NOATIME(inode))
                    return;
            if ((inode->i_sb->s_flags & MS_NODIRATIME) && S_ISDIR(inode->i_mode))
                    return;

Editei o post para refletir essa informação, e obrigado [Douglas][] pela correção.

[Douglas]: http://localhost:9000/2013/11/escrita-na-hd-noatime-nodiratime/#comment-1651688435
[o motivo]: http://lwn.net/Articles/245002/
