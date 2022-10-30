## Lancement avec Docker

Pour lancer le projet avec docker, il faut avoir <a href="https://www.docker.com/products/docker-desktop">Docker</a> d'installer sur son PC et effectuer les commandes suivantes :<br/>

```bash
docker build -t python-trello .
```

Have Your own .env with your Trello token and key.
replace [KEY] and [TOKEN] with yours.

```.dotenv
KEY=[KEY]
TOKEN=[TOKEN]
```

```bash
docker run -t -i python-trello
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

```bash
pip install -r requirement.txt
```

Have Your own .env with your Trello token and key.
replace [KEY] and [TOKEN] with yours.

```.dotenv
KEY=[KEY]
TOKEN=[TOKEN]
HOST=[HOST]
EMAIL=[EMAIL]
PASSWORD=[PASSWORD]
```

## Start

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

```bash
python -m main
```
