# Zadanie 1 — Docker

Autor: Julia Stanczak

## Opis aplikacji

Aplikacja webowa napisana w Pythonie z użyciem Flask. Pozwala wybrać kraj i miasto z listy, a następnie pobiera aktualną pogodę z API Open-Meteo.

Po uruchomieniu kontenera aplikacja zapisuje w logach:
- datę uruchomienia,
- imię i nazwisko autora,
- port TCP, na którym nasłuchuje aplikacja.

## Pliki projektu

- app.py
- requirements.txt
- Dockerfile
- zadanie1.md

## Budowanie obrazu

```bash
docker build -t pogoda-app .