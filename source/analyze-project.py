#!/bin/python3
import os
import subprocess

# Dateiendungen, nach denen gesucht werden soll
extensions = ['.py', '.ps1', '.js', '.html', '.md', '.cs']
files_to_process = []

# Verzeichnis rekursiv durchsuchen
for root, dirs, files in os.walk('.'):
    # .git Verzeichnis überspringen
    if '.git' in dirs:
        dirs.remove('.git')
    
    for file in files:
        if any(file.endswith(ext) for ext in extensions):
            files_to_process.append(os.path.join(root, file))

# Aider-Befehl vorbereiten
aider_command = [
    'aider',
    '--message',  # Einzelne Nachricht senden
    'Bitte analysiere den Code und aktualisiere die README.md. Die README sollte folgendes enthalten: 1. Einen aussagekräftigen Projekttitel und eine kurze Beschreibung 2. Detaillierte Setup-Anweisungen für Windows und Linux 3. Eine Übersicht aller verfügbaren Tools mit Beschreibungen ihrer Funktionen 4. Informationen zu Abhängigkeiten 5. Lizenzinformationen',
    '--no-git',  # Kein Git-Commit
    'README.md'  # Zu bearbeitende Datei
] + files_to_process  # Alle gefundenen Dateien als Kontext

try:
    # Aider ausführen
    subprocess.run(aider_command, check=True)
    print("README.md wurde erfolgreich mit Aider aktualisiert.")
except subprocess.CalledProcessError as e:
    print(f"Fehler beim Ausführen von Aider: {e}")
