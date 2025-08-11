1) Sostituire la stringa "my_app" in tutti i file di progetto con il nome del progetto. Se non presente creare una cartella "logs"
allo stesso livello della cartella "configurations"
2)  "pip install -e .[dev]" Per installare il progetto come package
3) "tox run -e lint" per far partire la parte di linting della pipeline
4) "tox run -f test" per far partire la pipeline di test
5)  Il processo completo per la generazione della documentazione è:
    - eliminazione cartella docs
    - ricreazione cartella vuota docs ed esecuzione del comando "sphinx-quickstart docs"
    - sostituzione del contenuto del nuovo file conf.py con il vecchio contenuto nel file docs_info/conf.py
    - Esecuzione del comando "tox run -e docs" per la generazione dei file html
    - Aggiunta della stringa modules all'interno del toctree nel file index.rst (Non servono apici va aggiunta semplicemente la parola modules per l'importazione dei file di documentazione)
    - Nuova Esecuzione del comando "tox run -e docs" per la generazione finale della documentazione