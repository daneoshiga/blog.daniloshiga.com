Title: Um Djangonauta no Flask
Date: 
Author: daniloshiga
Tags: python, web, flask
Slug: um-djangonauta-no-flask 
status: draft

Quando saí do desenvolvimento com PHP fui diretamente para o Django, o ORM e
admin foram suficientes para que convencer de que seria o framework ideal para
mim, e venho usando ele em diversos projetos desde então.

Porém me deparei com uma demanda de "criar uma página de contatos que envia um
email", e só, cheguei a começar a fazer o setup do projeto com o Django, mas a
cada momento parecia mais que estava usando um canhão para matar uma formiga.

Então resolvi fazer o projeto em Flask, havia feito apenas o tutorial alguns
anos atrás mas parecia ser a opção correta para um projeto pequeno, um
microframework para uma pequena demanda.

Uma hora depois, 2 arquivos python (routes.py e forms.py), um template e alguns
statics o problema estava resolvido.

Além do flask, precisei instalar mais dois pacotes, Flask-Mail, Flask-WTF, o
que foi bem tranquilo, já que ambos os pacotes tem uma boa documentação e são
simples de usar, de certo modo, mais simples que o do Django.

Um lado negativo que vejo é que para conseguir desenvolver essa pequena
aplicação tive que manter 3 documentações diferentes abertas.
