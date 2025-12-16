# syntax=docker/dockerfile:1

# Базовый образ с Python
FROM python:3.12-slim

# Устанавливаем системные пакеты (при необходимости сборки, можно убрать)
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копируем только зависимости
COPY requirements.txt .

# Ставим зависимости
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY . .

# Открываем порт, на котором слушает Uvicorn
EXPOSE 8000

# Команда запуска FastAPI через Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
