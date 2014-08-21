Title: Introdução aos Testes no Django
Date: 2014-07-11
Author: daniloshiga
Tags: python, django, testes
Slug: introducao-a-testes-no-django

Estou iniciando no processo de gerar testes para meu código no django, vou ir
colocando as minhas impressões sobre o assunto.

Em primeiro lugar, pelo menos na versão 1.5, é de senso comum que o código de
testes apresentado para o Django está longe do ideal, o que vejo é que a
maioria dos projetos não faz uso do "tests.py" padrão gerado no comando
"createapp", logo existem muitas versões diferentes de estruturas e testrunners
na internet.

Decidi me basear no que pode ser encontrado no [Two Scoops of Django][].

Um detalhe importante é verificar qual versão do Django está sendo usada,
porque da 1.5 para a 1.6 houve uma troca no "[test runner][]" para usar um que
encontra com mais facilidade os testes dentro dos módulos.

Nesse caso, é interessante criar um settings/test.py específico para testes. De
modo que seja usado um banco de dados sqlite na memória, que torna o processo
bem mais rápido. o settings pra versão [1.5][] e [1.6][] podem ser encontrados no
github do projeto base do Two Scoops of Django.

A partir daí, é apenas começar a escrever os testes :), o que preciso começar a
fazer e aprender conforme faço.

  [Two Scoops of Django]: http://twoscoopspress.com/products/two-scoops-of-django-1-5
  [test runner]: https://docs.djangoproject.com/en/dev/releases/1.6/#discovery-of-tests-in-any-test-module
  [1.5]: https://github.com/twoscoops/django-twoscoops-project/blob/10789b5ea39ac9a1517727f962780241fef3ed43/project_name/project_name/settings/test.py
  [1.6]: https://github.com/twoscoops/django-twoscoops-project/blob/develop/project_name/project_name/settings/test.py
