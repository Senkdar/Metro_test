API-сервис для получения новостей за заданный период. Для наполнения базы каждые 10 минут парсятся новости с сайта http://mosday.ru/news/tags.php?metro.

## Запуск проекта

Cоздать файл .env с настройками:
```
DB_NAME=<ИМЯ БАЗЫ ДАННЫХ>
DB_USER=<ИМЯ ПОЛЬЗОВАТЕЛЯ>
DB_PASSWORD=<ПАРОЛЬ>
DB_HOST=<ХОСТ>
```
Запустить docker - compose
```
docker-compose up -d --build
```