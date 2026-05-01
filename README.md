# Site Monitor API

Backend-сервис для мониторинга сайтов.

Позволяет:
- добавлять сайты
- запускать проверку сайта
- получать результаты проверок
- хранить историю проверок

Стек:
- Python
- Django
- Django REST Framework
- PostgreSQL
- Playwright

## Возможности

- CRUD для сайтов
- запуск проверки сайта через API
- получение title и h1 страницы
- сохранение HTTP статуса
- обработка ошибок
- история проверок
- просмотр через Django Admin

## Установка

1. Клонировать репозиторий:

```bash
git clone <ссылка>
cd site-monitor-api
```

2. Создать виртуальное окружение:

```bash

python -m venv .venv
```

3. Активировать:

Windows:

```bash

.venv\Scripts\activate
```
4. Установить зависимости:

```bash
pip install -r requirements.txt
```

## 4. Настройка базы:

Программа писалась на основе - PostgreSQL

```markdown
## Настройка базы данных

Указать настройки подключения в `.env` или `settings.py`.

После этого выполнить миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Запуск

```markdown
## Запуск проекта

```bash
python manage.py runserver

```
Сервер будет доступен по адресу:
http://127.0.0.1:8000/

## 6. API endpoints

```markdown

## API

### Сайты

- GET /api/sites/ — список сайтов
- POST /api/sites/ — создать сайт
- GET /api/sites/{id}/ — получить сайт
- DELETE /api/sites/{id}/ — удалить сайт

### Проверка сайта

- POST /api/sites/{id}/check/ — запустить проверку

### Результаты

- GET /api/results/ — список результатов
```
## Скриншоты

### Django Admin
<img width="522" height="176" alt="image" src="https://github.com/user-attachments/assets/30415789-bb55-49d8-aa81-3ce2bd19bad4" />

### API
<img width="553" height="206" alt="image" src="https://github.com/user-attachments/assets/f20f699c-c08d-4043-96a4-5a977542cfb1" />
