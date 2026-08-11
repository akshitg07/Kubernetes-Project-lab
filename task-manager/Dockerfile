FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    TASK_MANAGER_ENVIRONMENT=production \
    TASK_MANAGER_LOG_LEVEL=INFO \
    TASK_MANAGER_DATABASE_URL=sqlite:////data/task_manager.db

WORKDIR /app

RUN addgroup --system taskmanager \
    && adduser --system --ingroup taskmanager taskmanager \
    && mkdir -p /data \
    && chown -R taskmanager:taskmanager /data /app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY backend ./backend

USER taskmanager
WORKDIR /app/backend

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
