## PROBLEMA

A companhia de marketing Vough tem trabalhado cada vez mais para empresas de tecnologia que disponibilizam código aberto.

Com o aumento das demandas surgiu a necessidade de rankear seus atuais e potenciais clientes por um nível de prioridade, de modo a dar preferência a projetos de empresas maiores e mais influentes no meio open source.

## SOLUÇÃO

Para resolver este problema foi desenvolvido uma ferramenta para consultar as organizações no Github e criar um Ranking baseado na quantidade de pessoas e de repositórios que ela possui.

Utilizando o Python 3.9 + Django Rest Framework, API consulta a organização no Github, soma a quantidade de repositórios públicos com a quantidade de pessoas que participa dela criando assim sua pontuação. Após encontrada cria-se um registro no cache local para facilitar as requisições futuras.

##  Endpoints
| Métodos | Rotas | Descrição | Parâmetros
|    --   |   --  |     --    |     --     |
|   GET   | /api/orgs/ | Lista as organizações em cache |
|   GET   | /api/orgs/\<login> | Busca organização pelo login | login: str
|   DELETE   | /api/orgs/\<login> | Deleta organização salva no cache | login: str
|   GET   | /swagger/ | Documentação da API com Swagger |
|   GET   | /redoc/ | Documentação da API com Redoc |


#  Desenvolvimento
**Pré Requisitos**
- Python3.9
- [Pipenv](https://pypi.org/project/pipenv/)
- [Github Token](https://docs.github.com/pt/github/authenticating-to-github/creating-a-personal-access-token)

##  Instalação
Após clonar o projeto, com o *pipenv* instalado, execute o comando de instalação na pasta raiz
```
pipenv install
```

**Ativar ambiente de desenvolvimento**

```
pipenv shell
```

**Github Token**
Antes de executar a aplicação é preciso inserir o token do Github nas variáveis de ambiente do sistema
```
export GITHUB_TOKEN=<token>
```

**Executando**
```
python manage.py runserver
```

**Testes**
> Para executar os testes é necessário ter o GITHUB_TOKEN

```
python manage.py test
```

**Testes com o [K6](https://k6.io/)**
```
k6 run -e API_BASE='http://localhost:8000/' tests-open.js
```
