# Базовый образ с Python
FROM python:3.12-slim

# Не задаём maintainer — уже не используется официально

# Устанавливаем системные пакеты (компилятор и т.п. на будущее)
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем только requirements и ставим зависимости
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY . .

# Открываем порт (Timeweb.Cloud по умолчанию слушает 8080, но укажем явно 8000)
EXPOSE 8000

# Команда запуска FastAPI через Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
