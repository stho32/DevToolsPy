#!/bin/python3
import os
import subprocess

def ensure_gitignore():
    """Stellt sicher, dass .gitignore existiert und .aider* enthält"""
    gitignore_path = '.gitignore'
    aider_ignore = '.aider*'
    
    # Prüfe ob .gitignore existiert
    if not os.path.exists(gitignore_path):
        # Erstelle neue .gitignore
        with open(gitignore_path, 'w', encoding='utf-8') as f:
            f.write(f"{aider_ignore}\n")
        print("Neue .gitignore erstellt mit .aider* Eintrag")
        return
    
    # Prüfe ob .aider* bereits in .gitignore ist
    with open(gitignore_path, 'r', encoding='utf-8') as f:
        content = f.read()
        if aider_ignore not in content:
            # Füge .aider* zur bestehenden .gitignore hinzu
            with open(gitignore_path, 'a', encoding='utf-8') as f:
                if not content.endswith('\n'):
                    f.write('\n')  # Stelle sicher, dass wir in einer neuen Zeile beginnen
                f.write(f"{aider_ignore}\n")
            print(".aider* zur bestehenden .gitignore hinzugefügt")

def git_commit_and_push():
    """Führt git commit und push durch"""
    try:
        # Änderungen stagen
        subprocess.run(['git', 'add', '.'], check=True)
        # Commit durchführen
        subprocess.run(['git', 'commit', '-m', 'Dokumentation aktualisiert'], check=True)
        # Push durchführen
        subprocess.run(['git', 'push'], check=True)
        print("Änderungen wurden erfolgreich committed und gepusht.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Git-Vorgang: {e}")
        return False

def suggest_repo_names():
    """Verwendet Aider um neue Repository-Namen vorzuschlagen"""
    try:
        aider_command = [
            'aider',
            '--message',
            'Basierend auf dem Inhalt der README.md, schlage bitte 3-5 alternative Namen für dieses Repository vor. '
            'Die Namen sollten prägnant, modern und beschreibend sein. Formatiere die Vorschläge als nummerierte Liste. '
            'Berücksichtige dabei: 1. Aktuelle Namenskonventionen für GitHub-Repos 2. Suchmaschinenoptimierung '
            '3. Verständlichkeit für neue Nutzer.',
            '--no-git',
            '--no-suggest-shell-commands',
            'README.md'
        ]
        subprocess.run(aider_command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Generieren von Repository-Namen: {e}")
        return False

# Dateiendungen, nach denen gesucht werden soll
extensions = ['.py', '.ps1', '.js', '.html', '.md', '.cs']
files_to_process = []

# Stelle sicher, dass wir im Root-Verzeichnis sind
if os.path.exists('source'):
    os.chdir('source')
    os.chdir('..')

# .gitignore überprüfen und aktualisieren
ensure_gitignore()

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
    '--no-suggest-shell-commands',  # Keine Shell-Befehle vorschlagen
    'README.md'  # Zu bearbeitende Datei
] + files_to_process  # Alle gefundenen Dateien als Kontext

try:
    # Aider ausführen
    subprocess.run(aider_command, check=True)
    print("README.md wurde erfolgreich mit Aider aktualisiert.")

    # Frage nach Git-Commit und Push
    answer = input("\nMöchten Sie die Änderungen committen und pushen? (j/N): ").lower()
    if answer == 'j':
        git_commit_and_push()

    # Frage nach Repository-Namen-Vorschlägen
    answer = input("\nMöchten Sie Vorschläge für alternative Repository-Namen erhalten? (j/N): ").lower()
    if answer == 'j':
        suggest_repo_names()

except subprocess.CalledProcessError as e:
    print(f"Fehler beim Ausführen von Aider: {e}")
