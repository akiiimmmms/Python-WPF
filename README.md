# FastAPI CRUD Server

Ein minimaler FastAPI-Server mit CRUD-Funktionalität (Create, Read, Update, Delete) unter Verwendung von SQLAlchemy und Pydantic.

## Features

- **FastAPI**: Schnelles, asynchrones Web-Framework.
- **SQLAlchemy**: ORM zur einfachen Anbindung von Datenbanken (z. B. SQLite).
- **Pydantic**: Datenvalidierung und Serialisierung.
- **Uvicorn**: Schneller ASGI-Webserver.

## Installation

Stellen Sie sicher, dass Python >= 3.10 installiert ist.

### Mit uv (empfohlen)
Erstellen Sie eine virtuelle Umgebung und installieren Sie die Abhängigkeiten:
```bash
uv venv
uv pip install -e .
```

### Mit pip
```bash
pip install -e .
```

### Mit Poetry
```bash
poetry install
```

## Server starten

Starten Sie den Entwicklungsserver:

### Mit uv (empfohlen)
Durch das in `pyproject.toml` definierte Skript:
```bash
uv run start-server
```

### Alternativ (Entwicklungsmodus mit Live-Reload)
Wenn Sie Änderungen im Code machen und der Server automatisch neu starten soll:
```bash
uv run uvicorn crud.__main__:app --reload
```

### Ohne uv
Aktivieren Sie Ihre virtuelle Umgebung und führen Sie aus:
```bash
uvicorn crud.__main__:app --reload
```

## API Dokumentation

Nach dem Start ist die interaktive API-Dokumentation (Swagger UI) unter folgender Adresse erreichbar:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpunkte

Alle Endpunkte werden unter `http://127.0.0.1:8000` bereitgestellt.

### Health‑Check
| Methode | Pfad      | Beschreibung                |
|---------|-----------|----------------------------|
| GET     | `/health` | Liefert `{ "status": "ok" }` |



### Baum‑Ressource (`/baum`)

| Methode | Pfad          | Beschreibung                     | Beispiel‑cURL |
|---------|---------------|----------------------------------|----------------|
| GET     | `/baum`       | Gibt eine Liste aller Bäume zurück | |
| GET     | `/baum/{id}`  | Gibt den Baum mit der angegebenen ID | |
| GET     | `/baum?query` | Gibt Bäume mit den angegebenen Parametern zurück |
| POST    | `/baum`       | Erstellt einen neuen Baum (Body = JSON) | |
| PUT     | `/baum/{id}`  | Aktualisiert den Baum mit der ID | |
| DELETE  | `/baum/{id}`  | Löscht den Baum mit der ID | |

> **Hinweis**: Der JSON‑Body muss dem Schema von `BaumModel` entsprechen:
> ```json
> {
>   "id": 1,
>   "name": "Eiche",
>   "ast": {
>     "id": 1,
>     "name": "Ast1",
>     "blatt": {
>       "id": 1,
>       "farbe": "Grün"
>     }
>   }
> }
> ```

## Lizenz

MIT Lizenz
