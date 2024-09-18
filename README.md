# **GitAPI test APP**
https://github.com
### **Тестируемый функционал**

1. Создание нового публичного репозитория.
2. Проверка списка репозиториев для подтверждения создания
3. Удаление репозитория

Логи всех ошибок фиксируются в файле `errors_logs/errors_logs.json`

## Запуск

В файле 

**Стандартный запуск**
<br>
1. Запустите команду установки виртуального окружения `python3 -m venv .venv`<br>
2. Актвируйте виртуальное окружение 
Linux/Mac: `source .venv/bin/activate`<br>
Windows (Command Prompt): `.venv\Scripts\activate`<br>
Windows (PowerShell): `.venv\Scripts\Activate.ps1`<br>
<br>
3. Установите необходимые библиотеки
`pip install -r requirements.txt`<br>
4. Запустите код `python test_api.py`
<br><br>

**Запуск с помощью Docker**

Если на вашем компьютере не установлен Docker, скачайте его по инструкции на [официальном сайте](https://www.docker.com/get-started/)

1. Убедитесь, что вы находитесь в корневой директории, где расположен [Dockerfile](Dockerfile)<br>Запустите команду сбора докер-контейнера `docker build -t git_api_test .`
2. Запустите докер-контейнер<br>`docker run --restart unless-stopped -d --name git_api_container git_api_test && docker logs -f git_api_container`
3. Дождитесь выполнения кода<br>
<br>
Чтобы посмотреть все логи ошибок в файле `errors_logs/errors_logs.json`, выполните следующие команды:
-  Зайдите внутрь контейнера: `docker exec -it git_api_container /bin/bash`
- Получите содержимое файла с логами ошибок: `cat errors_logs/errors_logs.json`
