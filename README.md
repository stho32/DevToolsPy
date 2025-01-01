# DevToolsPy

Eine Sammlung nützlicher Python-Skripte für die Git-Verwaltung und Entwicklung.

## Setup

### Windows

1. Repository klonen
2. Python 3 installieren (falls noch nicht vorhanden)
3. Abhängigkeiten installieren: `pip install -r requirements.txt`
4. Windows-Integration einrichten:
   - Navigieren Sie zum `windows`-Verzeichnis im Repository
   - Fügen Sie den absoluten Pfad zu diesem `windows`-Verzeichnis zu Ihrer PATH-Umgebungsvariable hinzu
   - Nach dem Hinzufügen zum PATH können Sie die Befehle direkt in der Kommandozeile verwenden, z.B. `git-status` statt `python source/git-status.py`

### Linux

```bash
wget -q -O - https://raw.githubusercontent.com/stho32/DevToolsPy/main/setup.sh | bash
```

## Verfügbare Tools

### git-pull
Führt `git pull` im aktuellen Verzeichnis aus.

### git-pull-all
Durchsucht alle Unterverzeichnisse und führt `git pull` in jedem Git-Repository aus.
Perfekt um mehrere Projekt-Repositories gleichzeitig zu aktualisieren.

### git-clear-projects
Überprüft Git-Repositories im aktuellen Verzeichnis und zeigt deren Status an.
Mit dem Parameter `--do-it` werden "saubere" Repositories, die nicht mit "devtools" oder "project" beginnen, gelöscht.

### git-clone
Hilft beim Klonen von Repositories.

### git-push
Führt `git push` im aktuellen Repository aus.

### git-status
Zeigt den Git-Status des aktuellen Repositories an.

### git-too-old
Listet GitHub-Repositories eines bestimmten Benutzers auf, die älter als 2 Jahre sind (basierend auf dem letzten Push).
Verwendung: `git-too-old <github-username>`

### git-random-work
Tool für zufällige Git-Operationen (vermutlich für Testzwecke).

### quality
Skript für Qualitätsprüfungen.

## Windows-Integration
Im `windows`-Verzeichnis finden Sie .bat-Dateien für alle Skripte. Diese ermöglichen es Ihnen, die Skripte direkt von der Kommandozeile aus aufzurufen, ohne den Python-Interpreter explizit anzugeben. Stellen Sie sicher, dass Sie das `windows`-Verzeichnis zu Ihrer PATH-Umgebungsvariable hinzugefügt haben.

## Abhängigkeiten
Die Skripte benötigen verschiedene Python-Pakete, die in `requirements.txt` aufgeführt sind.

## Lizenz
Siehe LICENSE-Datei im Repository.

Zuletzt aktualisiert: 2025-01-01
