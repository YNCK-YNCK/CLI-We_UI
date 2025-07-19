from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='.')

# Simuliertes Dateisystem
file_system = {
    'root': {
        'type': 'directory',
        'contents': {
            'documents': {
                'type': 'directory',
                'contents': {
                    'file1.txt': {'type': 'file', 'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'},
                    'file2.txt': {'type': 'file', 'content': 'Inhalt von file2'}
                }
            },
            'pictures': {
                'type': 'directory',
                'contents': {
                    'photo1.jpg': {'type': 'file', 'content': 'Bildinhalt'}
                }
            }
        }
    }
}

current_directory = file_system['root']
previous_directory_stack = []
in_file_view_mode = False  # Zustand: Ob im Dateiansichtsmodus

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command')
    global current_directory, previous_directory_stack, in_file_view_mode

    if in_file_view_mode and command.lower() == 'exit':
        in_file_view_mode = False
        response = "Verlassen des Dateiansichtsmodus."
    elif command.startswith('cd '):
        directory = command.split(' ')[1]
        if directory == '..':
            if previous_directory_stack:
                current_directory = previous_directory_stack.pop()
                response = f"Verzeichnis gewechselt zum vorherigen Verzeichnis"
            else:
                response = "Sie befinden sich bereits im Stammverzeichnis."
        else:
            if directory in current_directory['contents']:
                previous_directory_stack.append(current_directory)
                current_directory = current_directory['contents'][directory]
                response = f"Verzeichnis gewechselt zu {directory}"
            else:
                response = f"Verzeichnis nicht gefunden: {directory}"
    elif command == 'ls':
        contents = list(current_directory['contents'].keys())
        response = "\n".join(contents)
    elif command.startswith('nano '):
        filename = command.split(' ')[1]
        if filename in current_directory['contents'] and current_directory['contents'][filename]['type'] == 'file':
            in_file_view_mode = True
            response = current_directory['contents'][filename]['content']
        else:
            response = f"Datei nicht gefunden: {filename}"
    elif command == 'clear':
        response = "CLEAR_CONSOLE"  # Spezielle Antwort zum Leeren des CLI
    elif command == 'help':
        response = """Verfügbare Befehle:
        - cd <directory>: Wechsel in ein Verzeichnis. Verwenden Sie 'cd ..', um in das vorherige Verzeichnis zu wechseln.
        - ls: Liste den Inhalt des aktuellen Verzeichnisses auf.
        - nano <filename>: Zeige den Inhalt einer Datei an.
        - clear: Löscht die Ausgabe im Terminal.
        - help: Zeigt diese Hilfemeldung an.
        - exit: Beendet den Dateiansichtsmodus (falls aktiv)."""
    elif command.lower() == 'exit':
        response = "Befehl 'exit' kann nur im Dateiansichtsmodus verwendet werden."
    else:
        response = "Unbekannter Befehl"

    return jsonify({'output': response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
