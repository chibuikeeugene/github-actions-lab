FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt

RUN useradd --create-home --uid 10001 appuser

COPY --chown=appuser:appuser calculator.py app.py ./

USER appuser

EXPOSE 8000

CMD [ "python", "-m", "uvicorn", "app:app", "--host","0.0.0.0", "--port", "8000" ]
