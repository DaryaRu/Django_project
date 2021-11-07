# Online shop project

## Features

* [x] products
* [x] products categories
* [x] products filtering
* [x] user authorization and authentication
* [x] user cart
* [x] user orders
* [x] admin panel

## Used technologies

* [DRF](https://www.django-rest-framework.org/)
* [Docker](https://dker.ru/docs/)

## Quick start

### Run project

```bash
cd Django_project
docker-compose up --build -d
```

## Project structure

```
root
|
| - config
| - shop
    |
    | - admin
    | - migrations
    | - models
    | - serializers
    | - viewsets
| Dockerfile
| docker-compose.yaml
| manage.py
| README.MD
| requirements.txt
```