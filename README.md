# Cornershop Test

## System requirements
Install Docker (Latest stable version)

## Init Project
```shell
$ git clone https://git@github.com:pablotoro19/Backend-Test-Toro.git
$ cd Backend-Test-Toro/
```

## Create Docker image and data base (postgresql)
```shell
$ make images
$ make migrate
```

## In settings.py add configurations
```python

TOKEN_SLACK = 'token_slack'
ADMIN_ID = 'default=1'
LIMIT_TIME = 'default=11'
```

## Load data
```shell
$ make load-data
```

## Run project
```shell
$ make up
```

## Login
ADMIN cornershop:cornershop <br />
USER nora:lavendedora

## Menu
http://localhost:8000/menu/886313e1-3b8a-5372-9b90-0c9aee199e5d

## Test
```shell
$ make test
$ make coverage_report
```

![Alt text](cornershop-test.jpg?raw=true "Component Model")
