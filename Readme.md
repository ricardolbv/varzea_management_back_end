## Repositorio desenvolvido com Python - Django

### O objetivo do projeto é criar uma api REST.

#### Contribuição:

##### \* Apontar o ambiente virtual: "virtualenv -p python3 ."

##### \* Startar o ambiente virtual: ".\Scripts\activate"

##### \* Instalar os requisitos do projeto com "pip install -r requirements.txt"

##### \* Comando para inicializar o projeto: "python manage.py runserver"

#### \* Comando para rodar migration (Atualizar tabela do banco): "python manage.py makemigrations" "python manage.py migrate"

#### \* Comando para criar superuser migration (Usuario de acesso a api): "python manage.py createsuperuser"

#### \* Super usuario: varzeaadmin - Acessar em: (porta local)/admin

#### \* IMPORTANTE: No sqlserver para dar permissão de admin:

##### exec master ..sp_addsrvrolemember

##### root,

##### sysadmin
