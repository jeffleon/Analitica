# Analitica

### Pre-requisites 📋
We need to have installed

- **Docker**
- **Docker-compose**
- **Python**

### Installation 🔧
**1.** Clone the Repository
```
    git clone https://github.com/jeffleon/Analitica.git
```

**2.** Create a .env file with the variables describe below
```
   DEBUG=True
```
*True if its a development environment and False if its a deploy environment*
```
    FLASK_ENV=XXXX
```
*For this environment variable only you can choose development, testing, production*    
```
    FLASK_APP=analitica:app
```
*you need to specify a entry point for the app in this case is analitica:app please put as shown in the example above*
```
    SECRET_JWT=XXX
```
*With this vairable you can choose the string for encrypt the JWT with Bcrypt*

**3.** Run the python environment 

```
    source analitica_env/Scripts/activate
```

**4.** Run the re_boot.sh bash to run the Docker file 

```
    ./re_boot.sh
```

**5.** Run the boot.sh bash to run Docker compose file to create  the two containers mysql container and python-alpine container 

```
    ./boot.sh
```

### Aplication Structure 

```
    |- Analitica
        |- app/
            |- templates/
            |- static/
            |- main/
                |- templates/
                |- __init__.py
                |- errors.py
                |- forms.py
                |- routes.py
            |- auth/
                |- templates/
                |- __init__.py
                |- routes.py
            |- models.py
        |- migrations/
        |- tests/
        |- db/
        |- documentation/
        |- requirements.txt
        |- config.py
        |- analitica.py
        |- Dockerfile
        |- docker-compose.yaml
        |- boot.sh
        |- reboot.sh        
```

### Endpoints Allowed

```
    POST /auth/create_account
    GET /auth/decode 🔒
    POST /auth/login
    POST /auth/logout 🔒
    POST /auth/refresh 🔒
```
*if you need to see the documentation go to the endpoint*
```
    GET /apidocs/
```
## Build with 🛠️

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - 
Web framework used
* [Docker](https://www.docker.com) - Generate the Development environment
* [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/) - Used to generate JWT
* [Unittest](https://docs.python.org/3/library/unittest.html) - Used to do a Unit test
* [Swagger-Flasgger](https://github.com/flasgger/flasgger) - Documentation

## Deploy 📦

## Authors ✒️

* **Jefferson León** - *Initial Work* - [jeffLeon](https://github.com/jeffleon)
* **Jonathan Rodríguez** - *Initial Work* - [elchory96](https://github.com/elchory96)

