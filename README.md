# Aplicação em Django

Criação de um site com o framework [Django](https://www.djangoproject.com/) versão 2.1.2 e utilizando um ambiente virtual com o [virtualenv](https://virtualenv.pypa.io/en/stable/)

## Usando o venv

Basicamente o virtualenv é uma ferramenta que permite criar ambientes python, onde consegue-se utilizar bibliotecas em um ambiente sem que haja conflitos que os arquivos do seu pc. E ele também permite que ao instalar um determinada versão de uma pacote ele não seja atualizado quando for dado um update no sistema de arquivo do seu sistema.

Para instalar o virtualenv deve-se utilizar o pip, com o seguinte comando:

```sh
    $ [sudo] pip install virtualenv
```

### Criando um novo ambiente

Nesse projeto já existe um ambiente criado é o ambiente no diretório **meuAmbiente**, mas se deseja criar um novo ambiente deve rodar esse comando:

```sh
    $ python3 -m venv nome_do_ambiente
```

### Acessando ambiente

Estando na raiz do projeto rode o seguinte comando:

```sh
    $ . meuAmbiente/bin/activate
```

### Pacotes usados no ambiente

django

## Django

Novo projeto:

```sh
    $ django-admin.py startproject meu_projeto
```

Rodando projeto:

```sh
    $ python manage.py runserver
```

Start squile3:

```sh
    $ ./manage.py migrate --run-syncdb
```

Criando um módulo no projeto:

```sh
    $ python manage.py startapp nome_novo_modulo
```
