@echo off
REM Запуск FastAPI через uvicorn
uvicorn api:app --reload --host 127.0.0.1 --port 8000
