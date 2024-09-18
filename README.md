# **GitAPI test APP**
https://github.com
### **Тестируемый функционал**

1. Создание нового публичного репозитория.
2. Проверка списка репозиториев для подтверждения создания
3. Удаление репозитория

Логи всех ошибок фиксируются в файле `errors_logs/errors_logs.json`

## Запуск

**Стандартный запуск**
<br>
1. Запустите команду установки виртуального окружения `python3 -m venv .venv`<br>
2. Актвируйте виртуальное окружение 
Linux/Mac: `source .venv/bin/activate`<br>
Windows (Command Prompt): `.venv\Scripts\activate`<br>
Windows (PowerShell): `.venv\Scripts\Activate.ps1`<br>
<br>
3. Установите необходимые библиотеки
`pip install -r requirements.txt`
4. Запустите код `python test_api.py`
<br>

**Запуск с помощью Docker**

1. Запустите команду сбора докер-контейнера `docker build -t git_api_test .`
2. Запустите докер-контейнер<br>`docker run -d --name my_git_api_container git_api_test && docker logs -f my_git_api_container`