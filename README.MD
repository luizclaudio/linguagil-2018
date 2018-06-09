### Conteúdo apresentado no minicurso *"Aplicações Web Python na Nuvem"*, no evento *"LinguÁgil 2018"*, em 08/06/2018. ###

Os programas, arquivos de configuração e orientações contidos neste repositório têm o objetivo de permitir testar de forma simples como executar uma aplicação Web [Python 3](https://www.python.org/), tanto localmente quanto na Nuvem. Neste segundo caso, executar em plataformas como serviço, em provedores de máquinas virtuais e em provedores de infraestrutura para containers Docker.

A aplicação-exemplo, utilizada em todos os casos, se baseia sempre que possível nos princípios da metodologia "[The Twelve-Factor App](https://12factor.net/)". A aplicação implementa uma API REST que pode salvar e recuperar dados em um banco de dados MongoDB, também hospedado na Nuvem. São usadas as bibliotecas (libs) Python [Flask](http://flask.pocoo.org/), [PyMongo](https://api.mongodb.com/python/current/) e [Gunicorn](http://gunicorn.org/) e o utilitário [Pipenv](https://github.com/pypa/pipenv). As referências a seguir dão mais detalhes sobre esses recursos:

- [Flask by Example (Real Python)](https://realpython.com/flask-by-example-part-1-project-setup/)

- [PyMongo Tutorial : Insert, Read, Update, Delete in MongoDB](
https://codehandbook.org/pymongo-tutorial-crud-operation-mongodb/)

- [Pipenv & Virtual Environments (The Hitchhiker's Guide to Python)](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


**IMPORTANTE**: Como as versões dos softwares e dos sites dos provedores mudam, as orientações dadas aqui poderão não se aplicar mais, depois de um tempo.

1. **Baixando e configurando o conteúdo deste repositório**
    - ```git clone https://github.com/luizclaudio/linguagil-2018.git```
    - Trocar o valor da variável *"COLECAO"* no arquivo *".env"* para um nome de sua escolha.
    - Verificar se o utilitário *"pipenv"* está instalado: ```pipenv --version```
    - Instalar, se necessário o utilitário o *"pipenv"*: ```pip install pipenv```
    - ```pipenv install```

2. **Executando Localmente**

    - ```pipenv run gunicorn -b 0.0.0.0:8000 application:app```

    - **A seguir, são mostrados exemplos usando os utilitários [HTTPie](https://httpie.org/) e [Curl](https://curl.haxx.se/)**

        **Listar todos os documentos**

        - ```http -v GET http://127.0.0.1:8000/api/documentos/``` ; ou

        - ```curl  http://127.0.0.1:8000/api/documentos/```

        **Criar um novo documento**

        - ```http -v POST http://127.0.0.1:8000/api/documentos/ nome="Maria José" idade:=23 notificar:=false``` ; ou

        - ```curl -v -H "Content-Type: application/json" -X POST -d '{"nome":"Maria José", "idade":23, "notificar":false}'  http://127.0.0.1:8000/api/documentos/```

        **Recuperar um documento por id**

        - ```http -v GET http://127.0.0.1:8000/api/documentos/<doc_id>``` ; ou

        - ```curl  http://127.0.0.1:8000/api/documentos/<doc_id>```

        **Recuperar um documento por chave e valor**

        - ```http -v GET http://127.0.0.1:8000/api/documentos/?nome=Maria+Jos%C3%A9``` ; ou

        - ```curl  http://127.0.0.1:8000/api/documentos/?nome=Maria+Jos%C3%A9```

        **Atualizar um documento**

         - ```http -v PUT http://127.0.0.1:8000/api/documentos/<doc_id> idade=44```; ou

         - ```curl -v -H "Content-Type: application/json" -X PUT -d '{"idade": 44}'  http://127.0.0.1:8000/api/documentos/<doc_id>```

        **Excluir um documento**

        - ```http -v DELETE http://127.0.0.1:8000/api/documentos/<doc_id>``` ; ou

        - ```curl -v -X DELETE http://127.0.0.1:8000/api/documentos/<doc_id>```

        **Excluir toda a coleção**
         - ```http -v DELETE http://127.0.0.1:8000/api/documentos/``` ; ou

         - ```curl -v -X DELETE http://127.0.0.1:8000/api/documentos/```


3. **Executando no Heroku (PaaS)**

    - Referência:

        [Getting Started on Heroku with Python (Heroku Dev Center)](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

    - Cadastrar-se no Heroku
    - Baixar o CLI
    - ```heroku login```
    - ```heroku create linguagil-2018```
    - ```git push heroku master```
    - Se comando anterior falhar:
        - ```git remote add heroku https://git.heroku.com/linguagil-2018.git```
    - ```heroku config:set SERVIDOR=ds245210.mlab.com:45210 USUARIO=user_la2018 SENHA=passw0rd BANCO=la2018 COLECAO=<nome_colecao>```
    - ```heroku open```
    - Se comando anterior falhar:
        - ```heroku ps:scale web=1```


4. **Executando em uma VM na Google Computing Platform (GCP)**

    - Cadastrar-se na GCP (se tiver Gmail, não precisa)
    - Ir para [https://console.cloud.google.com/](https://console.cloud.google.com/)
    - Cadastrar um projeto;
    - Ir para [https://console.cloud.google.com/compute/](https://console.cloud.google.com/compute/)
    - Criar uma VM:
        - Mudar imagem para Ubuntu 16.04
        - Liberar porta 8000 em "... detalhes da rede"
    - Abrir o console pelo navegador;
    - ```sudo passwd```
    - ```sudo apt-get update```
    - ```sudo apt-get install python3-pip```
    - ```pip3 install pipenv```
    - ```git clone https://github.com/luizclaudio/linguagil-2018.git```
    - ```cd linguagil-2018```
    - ```pipenv install```
    - ```pipenv run gunicorn -b 0.0.0.0:8000 application:app```


5. **Executando em um container na Amazon Web Services (AWS)**

    **Preparação do Container**

    - Instalar o [Docker](https://www.docker.com/);
    - ```docker build . -t la2018```
    - ```docker run -it --rm -p 8000:8000 -e SERVIDOR=ds245210.mlab.com:45210 -e USUARIO=user_la2018 -e SENHA=passw0rd -e BANCO=la2018 -e COLECAO=<nome colecao> la2018```
    - Cadastrar-se em [http://hub.docker.com](http://hub.docker.com)
    - ```docker login```
    - ```docker tag la2018 <usuario docker hub>/la2018```
    - ```docker push <usuario docker hub>/la2018```

    **Utilização do Container**

    - Referência:

        - [Take Containers From Development To Amazon ECS](https://docs.bitnami.com/aws/how-to/ecs-rds-tutorial/#step-23-set-up-amazon-ecs)

    - Cadastrar-se na AWS
    - Ir para [https://console.aws.amazon.com/](https://console.aws.amazon.com/)
    - Escolher a opção *Elastic Container Service (ECS)*
    - Criar um Cluster
        - Cluster name: la2018
        - Key pair: YOUR_KEY_PAIR
        - VPC: YOUR_DB_VPC
        - Subnets: Selecionar todas
    - Criar Task Definition
        - Task Definition Name: la2018
        - Container name: la2018
        - Image: YOUR_DOCKER_HUB_USER/linguagil-2018
        - Memory Limits: Soft limit - 300
        - Port mappings: host port - 80, container port - 8000, protocol - tcp
        - **Setar variáveis de ambiente.**
    - Criar Service
        - Task Definition: la2018
        - Cluster: la2018
        - Service name: la2018
        - Number of tasks: 1
        - Minimum healthy percent: 0
        - Maximum percent: 200
    - Observar a tab Events.
    - Procurar a tab *ECS Instances* no Cluster.
    - **Conferir as configurações do Security Group.**
    - **Ver o caminho para a VM onde está o container.**
