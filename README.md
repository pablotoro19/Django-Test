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

## Test
```shell
$ make test
$ make coverage_report
```

## Components model
![Alt text](/cornershop-test.jpg?raw=true "Components Model")



# API
Examples with data loaded previously(Load data) and fake data


## Menu

**Create Menu:** https://localhost/menu/user/{user_id}

* method: POST

* Request

https://localhost/menu/user/1

```json
{
	"menu_date": "2020-01-09"
}
```
* Response
```json
{
    "id": 2,
    "uuid": "51a9bd1d-1896-4174-902e-265da2fcdb33",
    "menu_date": "2020-01-09"
}
```

**List Menu:** https://localhost/menu

* method: GET

* Request

https://localhost/menu

* Response
```json
[
    {
        "id": 1,
        "uuid": "68be4876-843f-4765-a1c7-8ec2453b2fb5",
        "menu_date": "2020-01-08"
    },
    {
        "id": 2,
        "uuid": "51a9bd1d-1896-4174-902e-265da2fcdb33",
        "menu_date": "2020-01-09"
    }
]
```

**Get Menu:** https://localhost/menu/{uuid}

* method: GET

* Request

https://localhost/menu/68be4876-843f-4765-a1c7-8ec2453b2fb5

* Response
```json
{
    "id": 1,
    "uuid": "68be4876-843f-4765-a1c7-8ec2453b2fb5",
    "menu_date": "2020-01-08",
    "options": [
        {
            "menu": 1,
            "option": 1,
            "description": "Pure con vienesas y ensalada"
        },
        {
            "menu": 1,
            "option": 2,
            "description": "Arroz con pollo y ensalada"
        },
        {
            "menu": 1,
            "option": 3,
            "description": "Hamburguesa y papas"
        },
        {
            "menu": 1,
            "option": 4,
            "description": "Lentejas y ensalada de tomate"
        }
    ]
}
```


## Option

**Create Option:** https://localhost/menu/option/user/{user_id}

* method: POST

* Request

https://localhost/menu/option/user/1

```json
{
	"menu": 2,
	"option" : 1,
	"description": "Pollo con papas fritas y Ensalada"
}
```
* Response
```json
{
    "menu": 2,
    "option": 1,
    "description": "Pollo con papas fritas y Ensalada"
}
```

**Update Option:** https://localhost/menu/option/user/{user_id}

* method: PUT

* Request

https://localhost/menu/option/user/1

```json
{
	"menu": 1,
	"option" : 1,
	"description": "Pastel de choclo y ensalada"
}
```
* Response
```json
{
    "menu": 1,
    "option": 1,
    "description": "Pastel de choclo y ensalada"
}
```


## User

**Create User:** https://localhost/user

* method: POST

* Request

https://localhost/user

```json
{
	"name": "Juan",
	"username": "juanito",
	"email": "juanito@menu.com",
	"country_code": "CL"
}
```
* Response
```json
{
    "id": 4,
    "name": "Juan",
    "username": "juanito",
    "email": "juanito@menu.com",
    "country_code": "CL"
}
```

**Get User:** https://localhost/user/{user_id}

* method: GET

* Request

https://localhost/user/4

* Response
```json
{
    "id": 4,
    "name": "Juan",
    "username": "juanito",
    "email": "juanito@menu.com",
    "country_code": "CL"
}
```


## Order

**Create Order:** https://localhost/order/user/{user_id}

* method: POST

* Request

https://localhost/order/user/4

```json
{
	"menu": 1,
	"menu_option": 1,
	"quantity": 2,
	"customizations": "Ensalada solo con limon"
}
```
* Response
```json
{
    "message": "Order created successfully",
    "order": "Arroz con pollo y ensalada",
    "customizations": "Ensalada solo con limon",
    "order_date": "2020-01-08"
}
```

**Get Orders:** https://localhost/order/user/{user_id}

* method: GET

* Request

https://localhost/order/user/4

* Response
```json
[
    {
        "customizations": "Ensalada solo con limon",
        "option": "Arroz con pollo y ensalada",
        "menu_option": 2,
        "quantity": 2,
        "order_date": "2020-01-08",
        "user_name": "Juan",
        "user_id": 4
    }
]
```
