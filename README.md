# API для Yatube

API для социальной сети блогеров. Учебный проект.

## Функционал 

- Для аутентификации используются JWT-токены.
- У неаутентифицированных пользователей доступ к API только на чтение. Исключение — эндпоинт /follow/: доступ к нему должен предоставляться только аутентифицированным пользователям.
- Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.


## Технологии
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) Django 2.2.19

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) Python 3.7
 

## Запуск проекта в dev-режиме

1.  Клонировать репозиторий и перейти в него в командной строке
2.  Cоздать виртуальное окружение:
```
	python -m venv venv
```
3.  Активируйте виртуальное окружение
```
	source venv/Scripts/activate
```
4.  Установите зависимости из файла requirements.txt
```
	pip install -r requirements.txt
```
5. В папке с файлом manage.py выполните команду:
```
	python manage.py runserver
```  
## Примеры запросов

- GET-Response: http://127.0.0.1:8000/api/v1/posts/ 

        Request:
        [ 
            { 
                'id': 1, 
                'author': 'author', 
                'image':'' 'text': 
                'text', 'pub_date': 
                'pub_date', 
                'group': null 
            }, 
        ]

- POST-Response: http://127.0.0.1:8000/api/v1/posts/ :

        {
           "text": "string",
           "image": "string",
           "group": 0
        }

        Request:

        {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2023-01-12T14:15:22Z",
        "image": "string",
        "group": 0
        }


## Автор

Студент курса "Python-разработчик" от Яндекс-Практикума: Лазаренков Евгений


![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
[Ссылка на мой github](https://github.com/lazarenkov-e)