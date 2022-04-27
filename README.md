![example workflow](https://github.com/Normal1One/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)
### Foodgram
Проект является сайтом + API проекта Foodgram

### Команды для запуска проекта
```
git clone https://github.com/Normal1One/foodgram-project-react.git
```
```
docker-compose up -d --build
```

### Шаблон наполнения .env файла

```
ключ=значение
```

### Инструкция для заполнения базы данными
Выполните миграции, соберите статику, создайте суперпользователя и заполните базу данными
```
docker-compose exec backend python manage.py migrate
```
```
docker-compose exec backend python manage.py collectstatic --no-input
```
```
docker-compose exec backend python manage.py createsuperuser
```
```
docker-compose exec backend python manage.py loadjson --path 'api/data/ingredients.json'
```
### Автор
Никита Лавров

### Адрес сервера
http://84.201.138.102/

Email администратора: admin@gmail.com
Password администратора: admin
