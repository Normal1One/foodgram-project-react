![example workflow](https://github.com/Normal1One/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)
### Foodgram
The project is a website + API Foodgram project

### Commands for launching a project
```
git clone https://github.com/Normal1One/foodgram-project-react.git
```
```
docker-compose up -d --build
```

### Template for the .env file

```
key="value"
```

### Instructions for filling the database with data
Perform migrations, collect statics, create a superuser and fill the database with data
```
docker-compose exec backend python manage.py makemigrations api
```
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
### Author
Nikita Lavrov
