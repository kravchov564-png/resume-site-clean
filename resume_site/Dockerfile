FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup --system app && adduser --system --ingroup app app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app . /app/

RUN mkdir -p /app/staticfiles && chown -R app:app /app/staticfiles

USER app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "resume_site.wsgi:application"]
