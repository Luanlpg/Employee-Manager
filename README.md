# Employee-Manager

Aplicativo para gerenciar informações dos funcionários, como nome, e-mail e departamento.


## Instalação de requisitos (NECESSÁRIO:Python 3.6.0+ e pip(Atualizado))

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça um clone do projeto: `git clone https://github.com/Luanlpg/Employee-Manager.git`

- Acesse o repositório: `cd Employee-Manager/`

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Rodando o server da API

- Acesse o projeto django com: `cd manager`

- Rode as migrações do projeto: `python manage.py migrate`

- Crie um super user com: `python manage.py createsuperuser`

- Para rodar testes: `python manage.py test`

- Caso não queira adicionar funcionários manualmente utilize a fixture luizalabs.json
que já está pronta com o comando: `python manage.py loaddata luizalabs.json`

- Rode o servidor local com: `python manage.py runserver`

## Navegando pela API

- Faça login com o seu usuário em: `localhost:8000/admin`

- Acesse a root da API em: `localhost:8000/api/`

- Faça consulta e cadastro de funcionários em: `localhost:8000/api/employee/`
    - Após a adição de algum funcionário, será gerado um link de detalhes do mesmo,
    basta você clicar em "Employee List" na parte superior da tela.
    - Cada funcionário possui um link que direciona para a page de detalhes, lá também
    é possível editar(remover, alterar) o funcionário.
    - Para fazer a edição basta inserir um json com as alterações.

- também é possivel fazer requisições com o comando: `curl -H "Content-Type: application/javascript" http://localhost:8000/api/employee/`



## EXTRA

- Meses atrás havia feito outra API para o Luizalab que achei um pouco mais interessante,
o repositório é: `https://github.com/Luanlpg/Salas_lab.git`
