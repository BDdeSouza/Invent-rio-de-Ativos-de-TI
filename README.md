# Inventario-de-Ativos-de-TI
Exercício Laboratório de Banco de Dados

# Passo a Passo para rodar a API

Esse README fornece um guia passo a passo para configurar e executar a API.

## Clonar os Repositórios
```bash
git clone https://github.com/BDdeSouza/Inventario-de-Ativos-de-TI.git
```
OU
```bash
git clone git@github.com:BDdeSouza/Inventario-de-Ativos-de-TI.git
```

## Configuração de Ambiente

Aqui são as etapas necessárias para configurar e executar o ambiente de desenvolvimento.

### Pré-requisitos

- Ter os pacotes:
  - python 3.10.X e inferiores
  - python-venv
  - MongoDB
  
### Instalação e Configuração do Ambiente Virtual
#### Linux
```bash
python3 -m venv venv
. venv/bin/active
pip install r requirements.txt
```
#### Windows
```bash
python3 -m venv venv
. venv/Scripts/active
pip install r requirements.txt
```

### Configuração do .env seguindo o .env.template (MongoDB)
#### Exemplo:
```
MONGODB_URI=mongodb://localhost:27017
DB_NAME=Inventario
```

### rodar no terminal
````uvicorn main:app --reload````



## Documentação
### Após rodar a API siga a instrução abaixo:
###  Para acessar a documentação para fácil implementação: http://localhost:8000/docs

