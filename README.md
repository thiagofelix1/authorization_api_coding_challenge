# authorization_api_coding_challenge
<p>Projeto realizado para o coding challenge do programa dev experts do Itaú em parceria com a Let's Code.</p>
<p>Se baseia em uma Aplicação de autenticação para um serviço 
onde os usuários possam ver informações sobre determinados filmes, dar uma nota e realizar comentários.</p>
<p>A <a href="https://github.com/thiagofelix1/movie_api_coding_challenge">API de notas e comentários </a>
trabalha em conjunto com este projeto, sendo este responsável por todo controle de usuários e os endpoints são consumidos 
pela API de notas e comentários.</p>
<p>Todos os endpoints da API de autenticação necessitam de um token para serem acessadas de forma a receber 
só requisições da API de notas e comentários, o token já está presente nas duas aplicações e pode ser visto em: 
authorization_api_coding_challenge/application/permissions.py </p>

## 🛠️ Abrir e rodar o projeto
<p>Para executar os comandos de inicialização da Api de Autenticação é recomendado ter o 
<a href="https://www.python.org/downloads/">Python3</a> ou superior instalado, além disso vamos usar uma virtual environment para isolar
as dependências do nosso projeto</p>
<h3>Criando e ativando uma virtual environment</h3>
<p> A instalação de uma virtualenv pode ser feita utilizando o pip </p>

```
pip install virtualenv
```
<p>Para criar uma virtualenv é bastante simples, sugiro cria-lá na mesma hierarquia deste projeto, por exemplo:</p>
<p>pasta/authorization_api_coding_challenge</p>
<p>pasta/venv</p>
<p>Vamos criar e ativar a virtualenv no Linux:</p>

```
virtualenv venv
source venv/bin/activate
```
<p> Agora vamos criar e ativar a virtualenv no Windows:</p>

```
python venv venv
venv/Scripts/activate

```
<h3>Instalando dependências e iniciando o serviço</h3>
<p>Com a virtualenv ativa, podemos instalar todas as depedências do nosso projeto, as mesmas se encontram no arquivo requirements.txt, entre
no diretório raiz deste projeto e rode o comando abaixo</p>

```
pip install -r requirements.txt
```

<p> Após instalar as dependências podemos iniciar os comandos de inicialização do nosso projeto, antes de ir pros comandos vamos falar um pouco
mais do uso do <a href="https://www.djangoproject.com/"> Django </a> e do <a href="https://www.django-rest-framework.org/"> Django Rest Framework </a> que foram os frameworks utilizados para desenvolver a api</p>
<p>O Django é um poderoso framework para desenvolvimento web em python que fornece inúmeros benefíicos como desenvolvimento rápido e 
segurança, já o Django Rest Framework é um kit de ferramentas poderoso e flexível para construir APIs REST utilizado em grandes empresas 
como Mozilla, Red Hat e Heroku.</p>
<p> Agora vamos iniciar as configurações do nosso projeto. Primeiro vamos rodas as migrações no nosso banco de dados, para fim de simplificação foi
utilizado o sqlite3, porém o django fornece suporte a vários databases como é descrito na 
<a href="https://docs.djangoproject.com/en/4.0/ref/databases/"> documentação </a>, sendo extremamente fácil realizar o apontamento para um banco de 
dados mais complexo.</p>
<p>No diretório raiz do projeto podemos executar o seguinte comando:</p>

```
python manage.py migrate
```
<p> Este comando criará um arquivo .sqlite3 na raiz do projeto e irá rodar as migrações, após executado você vai ver algo como: </p>

```
Operations to perform:
  Apply all migrations: admin, application, auth, authtoken, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying application.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying authtoken.0003_tokenproxy... OK
  Applying sessions.0001_initial... OK
```

<p>Em seguida, podemos criar um superuser para verificar as informações sendo cadastradas no site de administração do django presente em 
http://127.0.0.1:8000/admin/ , por ser um superusuario ele já vai ser criado com o perfil de moderator(Moderador) e com 1000 pontos</p>

<p>Após rodas as migrações você pode iniciar o serviço utilizando: </p>

```
python3 manage.py createsuperuser
```
<p>O terminal exibirá algumas informações para vocẽ preencher, algo como: </p>

```
Email address: thiagofelixdasilva099@gmail.com
Nickname: thiagofelix
First name: thiago
Last name: felix
Password: 
Password (again):
Superuser created successfully.
```
<p>Após isso você pode usar o username e password para entrar no site de administração.</p>

```
python3 manage.py runserver
```
<p> Você verá que o serviço vai rodar no localhost na porta 8080, algo como http://127.0.0.1:8080/</p>
<p> A documentação da API, os endpoints de acesso e suas descrições assim como os parâmetros de autenticação e envio das informações 
podem ser vistos na documenta da API, presente em http://127.0.0.1:8000/documentation</p>
