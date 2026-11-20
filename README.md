
# TaskFlow

Sistema profissional de gerenciamento de tarefas.

## Tecnologias

- Python 3.11
- Django 5.2
- Django REST Framework
- PostgreSQL
- django-cors-headers
- django-environ
- React
- TypeScript
- Docker
- Pytest

## Objetivo

Desenvolver uma aplicação Full Stack para gerenciamento
de tarefas, prioridades, prazos e acompanhamento de atividades.

## Funcionalidades

- Cadastro de usuários.
- Autenticação.
- Cadastro de tarefas.
- Gerenciamento de prioridades.
- Controle de status.
- Filtros e pesquisas.
- API REST.
- Dashboard.

## Estrutura inicial do backend

```text
backend/
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   └── __init__.py
└── tests/
    └── __init__.py
```

O backend está preparado com configurações por variáveis de ambiente,
PostgreSQL, Django REST Framework, CORS e estrutura para aplicativos e testes.
Nenhuma funcionalidade de tarefas ou usuários foi implementada nesta etapa.

## Instalação e execução

Na raiz do repositório, ative o ambiente virtual e instale o projeto com suas
dependências de desenvolvimento:

```bash
source .venv/bin/activate
python -m pip install -e ".[dev]"
cp .env.example .env
```

Edite `.env` e configure `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` e os parâmetros
do PostgreSQL (`DATABASE_URL` ou as variáveis `DB_*`). Em seguida, inicie o
servidor:

```bash
python backend/manage.py runserver
```

Os comandos do Django e do Pytest devem ser executados na raiz do repositório.

## Arquitetura prevista

Backend: Django REST Framework.

Frontend: React + TypeScript.

Banco de dados: PostgreSQL.

Infraestrutura: Docker.

## Status

Em desenvolvimento.
