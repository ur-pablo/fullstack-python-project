FROM python:3.10-slim

# Instala poetry
RUN pip install --upgrade pip && pip install poetry

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de configuración de Poetry primero para cachear dependencias
COPY pyproject.toml poetry.lock* /app/

# Instala dependencias
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copia el código
COPY app /app/app

# Ejecuta la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
