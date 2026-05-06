# Etap budowania zależności
FROM python:3.12-alpine AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# Etap końcowy
FROM python:3.12-alpine

LABEL org.opencontainers.image.authors="Julia Stanczak"

WORKDIR /app

COPY --from=builder /install /usr/local
COPY app.py .

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -qO- http://localhost:8080/health || exit 1

CMD ["python", "app.py"]