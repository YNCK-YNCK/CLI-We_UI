
# Interaktives CLI Web Interface

Eine dynamische Webseite mit einem interaktiven Command Line Interface (CLI), das einige grundlegende Linux-Befehle simuliert. Nutzer können durch ein simuliertes Dateisystem navigieren, Verzeichnisse auflisten, Dateiinhalte anzeigen und vieles mehr. Dient nur als Proof of Concept für diesen Webdesign-Ansatz. 

## Beschreibung

Dieses Projekt bietet eine einfache Webseite, die ein interaktives CLI simuliert. Es ermöglicht Benutzern, Befehle wie `cd`, `ls`, `nano` usw. auszuführen, um durch ein simuliertes Dateisystem zu navigieren. Das Projekt verwendet Flask als Backend-Server und jQuery für die Frontend-Interaktion.

## Installation

Bevor Sie beginnen, stellen Sie sicher, dass Python und pip auf Ihrem System installiert sind.

1. Klonen Sie das Repository auf Ihren lokalen Computer.

   ```bash
   git clone [...]
   cd interaktives-cli-web-interface
   ```

2. Installieren Sie die notwendigen Python-Pakete.

   ```bash
   pip install flask
   ```

3. Starten Sie den Flask-Server.

   ```bash
   backend_CLI.py
   ```

4. Öffnen Sie Ihren Web-Browser und gehen Sie zu `http://127.0.0.1:5000`, um die Anwendung zu verwenden.

## Verwendung

- Verwenden Sie die Eingabezeile, um Befehle einzugeben.
- Unterstützte Befehle:
  - `cd <directory>`: Wechseln Sie in ein Verzeichnis. Verwenden Sie `cd ..`, um in das vorherige Verzeichnis zu wechseln.
  - `ls`: Listet den Inhalt des aktuellen Verzeichnisses auf.
  - `nano <filename>`: Zeigt den Inhalt einer Datei an.
  - `clear`: Löscht die Ausgabe im Terminal.
  - `help`: Zeigt eine Liste der verfügbaren Befehle an.
  - `exit`: Beendet den Dateiansichtsmodus (falls aktiv).

## Funktionen

- Simulation eines Dateisystems mit Verzeichnissen und Dateien.
- Unterstützung grundlegender Linux-Befehle wie `cd`, `ls` und `nano`.
- Interaktives CLI im Webbrowser.
- Möglichkeit, Dateiinhalte anzuzeigen und durch das Dateisystem zu navigieren.

## Beiträge

Beiträge sind willkommen! Bitte erstellen Sie einen Pull Request oder öffnen Sie ein Issue, um Ihre Vorschläge oder Fehlerberichte einzureichen.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
```
