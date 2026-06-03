\# Zadanie 2 - GitHub Actions



Autor: Julia Stanczak



\## Opis



Projekt wykorzystuje GitHub Actions do automatycznego budowania obrazu kontenera na podstawie aplikacji przygotowanej w zadaniu 1.



Pipeline wykonuje:



1\. Pobranie kodu z repozytorium.

2\. Konfigurację Buildx i QEMU.

3\. Logowanie do DockerHub.

4\. Logowanie do GitHub Container Registry (ghcr.io).

5\. Budowę obrazu do skanowania.

6\. Test bezpieczeństwa CVE przy użyciu Trivy.

7\. Budowę obrazu wieloplatformowego:

&#x20;  - linux/amd64

&#x20;  - linux/arm64

8\. Wysłanie obrazu do GitHub Container Registry.

9\. Zapis i odczyt cache z DockerHub.



\## Wykorzystane technologie



\- Docker

\- Docker Buildx

\- GitHub Actions

\- Trivy

\- GitHub Container Registry (GHCR)

\- DockerHub



\## Tagowanie obrazów



Obraz publikowany jest z tagami:



```text

latest

```



oraz



```text

SHA\_COMMITU

```



Przykład:



```text

ghcr.io/stanczakjulka/pogoda-app:latest

ghcr.io/stanczakjulka/pogoda-app:a1b2c3d

```



Dzięki temu możliwe jest:

\- używanie najnowszej wersji aplikacji,

\- identyfikacja konkretnej wersji kodu.



\## Cache



Cache przechowywany jest w publicznym repozytorium DockerHub:



```text

stanczakjulka/pogoda-app-cache

```



Wykorzystywany jest:



```text

cache-from

cache-to

mode=max

```



co przyspiesza kolejne budowania obrazu.



\## Test CVE



Do analizy bezpieczeństwa wykorzystano narzędzie Trivy.



Pipeline zostanie przerwany, jeśli wykryte zostaną podatności:



```text

HIGH

CRITICAL

```



Dzięki temu do GHCR publikowane są wyłącznie obrazy spełniające wymagania bezpieczeństwa.



\## Uruchomienie workflow



Workflow uruchamia się:



\- automatycznie po wysłaniu zmian do gałęzi main,

\- ręcznie z poziomu GitHub Actions.



\## Pliki projektu



```text

app.py

requirements.txt

Dockerfile

README.md

.github/workflows/docker.yml

```

