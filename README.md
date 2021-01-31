# Desafio-Backend---Star-Wars

## Como rodar o projeto

após clonar o repositório , entre na pasta raiz do projeto e crie um ambiente virtual utilizando 
uma versão do python3.x . 

### Criando um Ambiente Virtual
Execute no seu terminal o seguinte comando: 
```
python3.x -m venv venv
```

### Iniciando o seu Ambiente Virtual

Ainda em seu terminal execute: 
```
venv/bin/activate ou source venv/vin/activate
```
Após executar um desses comandos seu terminal deve mostrar o nome "venv" dentro de parênteses,
isso significa que você está em seu ambiente virtual.

### Verficando se estou no ambiente virtual

Execute o seguinte comando : 
```
pip freeze 
```
se não aparecer nenhuma lista de dependência significa que estamos no seu ambiente virtal.

### Instalando Dependências do Projeto

Execute: 
```
pip install -r requeriments.txt
```
Verificando se as dependências foram instaladas.

```
pip freeze
```


### Inciando o Projeto Django

Ainda na sua linha de comando execute: 
```
python manage.py migrate 
```
*(isso irá criar toda a estrutura de banco de dados)* , após a execução do migrate execute:
```
 python manage.py createsuperuser 
```
O django irá retornar um pequeno questionário e você deverá informar um nome de usuário um email e uma senha.

*obs: createsuperuser irá criar um usuário administrador para o django.*

### Finalmente Rodando o Projeto

Execute: 
```
python manage.py runserver
```
Acesse: 
```
http://127.0.0.1:8000/
```

## Rodando Testes

Execute :
```
python manage.py test
```