# DevToolsPy - Git Repository Management Tools

Eine umfassende Sammlung von Python-basierten Entwicklerwerkzeugen zur effizienten Verwaltung und Automatisierung von Git-Repositories.

## Beschreibung

DevToolsPy bietet eine Suite von Kommandozeilen-Tools, die die tägliche Arbeit mit mehreren Git-Repositories vereinfachen. Von der Massenaktualisierung über Statusüberwachung bis hin zur automatisierten Repository-Verwaltung - diese Tools sparen Zeit und reduzieren manuelle Fehler.

## Setup-Anweisungen

### Windows

1. Systemvoraussetzungen:
   - Python 3.8 oder höher
   - Git installiert und im PATH verfügbar

2. Installation:
   ```cmd
   git clone https://github.com/stho32/DevToolsPy.git
   cd DevToolsPy
   pip install -r requirements.txt
   ```

3. Windows-Integration:
   - Öffnen Sie die Systemeinstellungen (Windows + R, "sysdm.cpl")
   - Klicken Sie auf "Erweitert" > "Umgebungsvariablen"
   - Fügen Sie den absoluten Pfad zum `windows`-Verzeichnis zur PATH-Variable hinzu
   - Öffnen Sie eine neue Kommandozeile für die Änderungen

### Linux

1. Systemvoraussetzungen:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git
   ```

2. Installation:
   ```bash
   git clone https://github.com/stho32/DevToolsPy.git
   cd DevToolsPy
   pip3 install -r requirements.txt
   ```

3. Skripte ausführbar machen:
   ```bash
   chmod +x source/*.py
   ```

## Verfügbare Tools

### Repository Management
- **git-status.py**: Zeigt eine übersichtliche Tabelle mit dem Status aller lokalen Repositories
- **git-pull.py**: Aktualisiert alle lokalen Repositories automatisch mit den neuesten Änderungen
- **git-push.py**: Pusht Änderungen in allen Repositories mit ausstehenden Commits
- **git-clone.py**: Klont Repositories von GitHub mit Filteroptionen
  - Verwendung: `git-clone.py <username> <prefix>`

### Wartung & Analyse
- **git-clear-projects.py**: Bereinigt nicht mehr benötigte Repositories
  - Interaktiver Modus zur sicheren Bestätigung von Löschungen
- **git-too-old.py**: Identifiziert inaktive Repositories (>2 Jahre ohne Updates)
  - Verwendung: `git-too-old.py <github-username>`
- **git-random-work.py**: Wählt zufällige Repositories für Code-Reviews oder Tests
- **analyze-project.py**: Analysiert Projektstruktur und generiert README-Updates
- **quality.py**: Führt Qualitätsprüfungen in Repositories durch

## Abhängigkeiten

Hauptabhängigkeiten:
- requests>=2.31.0
- prettytable>=3.9.0
- python-dateutil>=2.8.2
- pytz>=2023.3

Vollständige Liste in `requirements.txt`

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz veröffentlicht. Dies erlaubt:
- Kommerzielle Nutzung
- Modifikation
- Distribution
- Private Nutzung

Siehe `LICENSE` für den vollständigen Lizenztext.

---
Zuletzt aktualisiert: 2025-01-01
