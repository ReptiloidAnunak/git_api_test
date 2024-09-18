# **GitAPI test APP**

### **Тестируемый функционал**

1. Создание нового публичного репозитория.
2. Проверка списка репозиториев для подтверждения создания
3. Удаление репозитория

Логи всех ошибок фиксируются в файле `errors_logs/errors_logs.json`

## Запуск

1. Запустите команду установки виртуального окружения `python3 -m venv .venv`
2. Актвируйте виртуальное окружение 
На Linux/Mac: `source .venv/bin/activate`
На Windows (Command Prompt): `.venv\Scripts\activate`
На Windows (PowerShell): `.venv\Scripts\Activate.ps1`

3. Установите необходимые библиотеки
`pip install -r requirements.txt`
4. Запустите код `python test_api.py`