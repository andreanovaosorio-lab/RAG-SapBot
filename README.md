# ReglaBot - Sistema RAG sobre el Reglamento Estudiantil

ReglaBot es un asistente conversacional especializado en el archivo `pdf/reglamento_estudiantil.pdf`. El sistema carga el PDF, crea fragmentos de texto, genera embeddings, guarda la informacion en ChromaDB y responde preguntas desde una interfaz web creada con Flask.

## 1. Preparar el PDF

La carpeta `pdf` ya esta creada. Para copiar automaticamente el reglamento desde la carpeta original, ejecuta:

```powershell
python copiar_pdf.py
```

Al final debe quedar este archivo:

```text
pdf/reglamento_estudiantil.pdf
```

## 2. Crear el entorno virtual

Abre esta carpeta en Visual Studio Code:

```powershell
cd "C:\Users\Andrea Nova\OneDrive\Escritorio\Proyecto Agente SAP"
python -m venv .venv
```

Activa el entorno:

```powershell
.\.venv\Scripts\activate
```

## 3. Instalar dependencias

```powershell
python -m pip install --upgrade pip
pip install -r requirements-rag.txt
```

## 4. Configurar la llave API

Copia el archivo de ejemplo:

```powershell
copy .env.example .env
```

Abre `.env` y reemplaza:

```text
GOOGLE_API_KEY=pega_aqui_tu_api_key
```

por tu llave real de Google Gemini.

## 5. Crear la base vectorial

Este paso carga el PDF, crea chunks, genera embeddings y guarda todo en la carpeta `chromadb`.

```powershell
python ingest.py
```

## 6. Ejecutar la interfaz Flask

```powershell
python app.py
```

Luego abre:

```text
http://127.0.0.1:5000
```

## Como responde ReglaBot

- Tiene nombre y rol definido: ReglaBot, asistente academico especializado en el Reglamento Estudiantil.
- Responde solo con informacion del contexto recuperado.
- Si no encuentra la respuesta en el documento, responde: `No encuentro esa informacion en el reglamento estudiantil consultado.`
- Al final de cada respuesta cita las paginas consultadas.

## Estructura

```text
Proyecto Agente SAP/
├── app.py
├── config.py
├── ingest.py
├── copiar_pdf.py
├── rag_engine.py
├── requirements-rag.txt
├── .env.example
├── README.md
├── pdf/
│   └── reglamento_estudiantil.pdf
├── chromadb/
├── templates/
│   └── index.html
└── static/
    └── styles.css
```
